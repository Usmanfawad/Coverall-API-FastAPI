from SAS.main import *

from fastapi import APIRouter
from fastapi_utils.session import FastAPISessionMaker
from fastapi_utils.tasks import repeat_every

# import httpx

router = APIRouter()



@router.get("/")
async def api_users_signup():
    return {"200": "200"}