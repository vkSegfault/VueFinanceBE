from fastapi import FastAPI, HTTPException, Path, Query, Depends
from fastapi.middleware.cors import CORSMiddleware
import json
import time
from models.asset import Bond, BondDTO, Stock, StockDTO, AssetType
from models.temp_db import bond_list, stock_list
from typing import Annotated
from contextlib import asynccontextmanager
from db import init_db, get_session
from sqlmodel import Session, select
import uuid


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# should be DB here
with open('jobs.json') as f:
    json_data = json.load(f)

data = json_data['jobs']

@app.get('/assets', status_code=200)
async def get_all_assets(
    type: str | None = None,
    description: bool = False,
    name: Annotated[str | None,
    Query(max_length=10)] = None,
    session: Session = Depends(get_session)
) -> list[Bond | Stock]:
    
    time.sleep(1)  # TO BE REMOVED

    bond_list = session.exec(select(Bond)).all()
    stock_list = session.exec(select(Stock)).all()
    assets = bond_list + stock_list

    if type == None:  # when we don't call type query param
        pass

    if type:
        match type:
            case 'STOCK':
                assets = [a for a in assets if a.type == AssetType.STOCK]
            case 'BOND':
                assets = [a for a in assets if a.type == AssetType.BOND]

    if description:
        assets = [a for a in assets if a.description != ""]

    if name:
        # this is partial search: querying for 'lok' will find all `lokata`
        assets = [a for a in assets if name.lower() in a.name.lower()]
    
    return assets


@app.get('/assets/bond/{id}')
async def get_one_bond(
    id: Annotated[uuid.UUID, Path(title='UUID of bond')],
    session: Session = Depends(get_session)
) -> Bond:
    time.sleep(1)  # TO BE REMOVED
    bond = session.get(Bond, id)
    if bond is None:
        raise HTTPException(status_code=404, detail="Bond not found")
    return bond


@app.get('/assets/stock/{id}')
async def get_one_stock(
    id: Annotated[uuid.UUID, Path(title='UUID of stock')],
    session: Session = Depends(get_session)
) -> Stock:
    time.sleep(1)  # TO BE REMOVED
    stock = session.get(Stock, id)
    if stock is None:
        raise HTTPException(status_code=404, detail="Stock not found")
    return stock


@app.get('/about')
async def about() -> str:
    return 'This is backend for Vue Finance'


@app.post('/assets/bond')
async def create_bond(
    bondDTO: BondDTO,
    session: Session = Depends(get_session)  # DI happens here
) -> Bond:
    uid = uuid.uuid4()
    new_bond = Bond( id=uid, name=bondDTO.name, description=bondDTO.description, type=AssetType.BOND, value=bondDTO.value, rate=bondDTO.rate, days=bondDTO.days, tax=bondDTO.tax )
    
    session.add(new_bond)
    session.commit()
    session.refresh(new_bond)

    return new_bond


@app.post('/assets/stock')
async def create_stock(
    stockDTO: StockDTO,
    session: Session = Depends(get_session)  # DI happens here
) -> Stock:
    uid = uuid.uuid4()
    new_stock = Stock( id=uid, name=stockDTO.name, description=stockDTO.description, type=AssetType.STOCK, stocksAmount=stockDTO.stocksAmount, stockPrice=stockDTO.stockPrice )
    
    session.add(new_stock)
    session.commit()
    session.refresh(new_stock)

    return new_stock


@app.put("/assets/bond/{id}", response_model=Bond)
async def update_bond(
    id: Annotated[uuid.UUID, Path(title='UUID of bond')],
    bondDTO: BondDTO,
    session: Session = Depends(get_session)  # DI happens here
) -> Bond:
    bond = session.get(Bond, id)
    if bond is None:
        raise HTTPException(status_code=404, detail="Bond not found")

    # https://fastapi.tiangolo.com/tutorial/sql-databases/#update-a-hero-with-heroupdate
    bond_data = bondDTO.model_dump(exclude_unset=True)
    bond.sqlmodel_update(bond_data)

    session.add(bond)
    session.commit()
    session.refresh(bond)
    
    return bond


@app.delete('/assets/bond/{id}')
async def delete(
    id: Annotated[uuid.UUID, Path(title='UUID of bond')],
    session: Session = Depends(get_session)  # DI happens here
) -> dict:
    bond = session.get(Bond, id)
    if not bond:
        raise HTTPException(status_code=404, detail="Bond not found")

    session.delete(bond)
    session.commit()

    return { 'Message in a bottle': 'Bond deleted' }

@app.delete('/assets/stock/{id}')
async def delete(
    id: Annotated[uuid.UUID, Path(title='UUID of stock')],
    session: Session = Depends(get_session)  # DI happens here
) -> dict:
    stock = session.get(Stock, id)
    if not stock:
        raise HTTPException(status_code=404, detail="Stock not found")

    session.delete(stock)
    session.commit()

    return { 'Message in a bottle': 'Stock deleted' }
