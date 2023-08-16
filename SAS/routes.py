from main import *

from fastapi_utils.session import FastAPISessionMaker
from fastapi_utils.tasks import repeat_every

# import httpx



@app.get("/")
async def root():
    return {"200": "200"} 