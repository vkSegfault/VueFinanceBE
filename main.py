from fastapi import FastAPI

app = FastAPI()

@app.get('/asset')
async def getAllAssets() -> dict[str, str]:
    return {'job no': '69'}

@app.get('/about')
async def about() -> str:
    return 'This is backend for Vue Finance'