from fastapi import FastAPI, HTTPException
import json


app = FastAPI()

# should be DB here
with open('jobs.json') as f:
    json_data = json.load(f)

data = json_data['jobs']

@app.get('/assets', status_code=200)
async def getAllAssets() -> list[dict]:
    return data

@app.get('/assets/{id}')
async def getOneAsset(id: int) -> dict:
    asset = next((a for a in data if int(a['id']) == id), None)
    if asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    return asset

@app.get('/about')
async def about() -> str:
    return 'This is backend for Vue Finance'