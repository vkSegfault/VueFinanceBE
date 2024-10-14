from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
import time
from models.asset import Bond, Stock
from models.temp_db import bond_list, stock_list


app = FastAPI()

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
async def getAllAssets() -> list[Bond | Stock]:
    time.sleep(1)  # TO BE REMOVED
    return bond_list + stock_list

@app.get('/assets/{id}')
async def getOneAsset(id: int) -> dict:
    asset = next((a for a in data if int(a['id']) == id), None)
    if asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    return asset

@app.get('/about')
async def about() -> str:
    return 'This is backend for Vue Finance'