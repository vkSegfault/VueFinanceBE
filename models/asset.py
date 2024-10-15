from enum import Enum
from uuid import UUID
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship

# TODO - use SQLAlchemy instead SQLModel (SQLModel can't combine inheritance and table mappings)

# def asset() -> None:
#     pass

# if __name__ == "__asset__":
#     asset()

class AssetType(Enum):
    STOCK = 'STOCK'
    BOND = 'BOND'
    MORTGAGE = 'MORTGAGE'


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    # asset_id: UUID = Field(foreign_key="asset.id")
    bonds: list["Bond"] = Relationship(back_populates='user')
    stocks: list["Stock"] = Relationship(back_populates='user')


# SQLModel already inherits from BaseModel of pydantic
# class Asset(SQLModel, table=True):
#     id: UUID = Field(default=None, primary_key=True)
#     name: str = Field(index=True)
#     type: AssetType
#     description: Optional[str] = ""
#     create_date: datetime = datetime.now()
#     user_id: int | None = Field(default=None, foreign_key='user.id')
#     user: User | None = Relationship(back_populates='assets')

##################################################################################
### note that we stor both złote and grosze as int so 2,34 ZŁ is stored as 234 int
##################################################################################

class Stock(SQLModel, table=True):
    id: UUID = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    type: AssetType
    description: Optional[str] = ""
    create_date: datetime = datetime.now()
    user_id: int | None = Field(default=None, foreign_key='user.id')
    user: User | None = Relationship(back_populates='stocks')
    stocksAmount: int
    stockPrice: int


class Bond(SQLModel, table=True):
    id: UUID = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    type: AssetType
    description: Optional[str] = ""
    create_date: datetime = datetime.now()
    user_id: int | None = Field(default=None, foreign_key='user.id')
    user: User | None = Relationship(back_populates='bonds')
    value: int
    rate: int
    days: int
    tax: int


############# DTOs ################


class AssetDTO(BaseModel):
    name: str
    type: AssetType
    description: Optional[str] = ""


class StockDTO(AssetDTO):
    stocksAmount: int
    stockPrice: int


class BondDTO(AssetDTO):
    value: int
    rate: int
    days: int
    tax: int