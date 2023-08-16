from fastapi import APIRouter

from . import billsAndSales, contentManagement, policyManagement, userManagement

router = APIRouter()

def include_api_routes():
    ''' Include to router all api rest routes with version prefix '''
    router.include_router(billsAndSales.router, prefix="/v1")
    router.include_router(contentManagement.router, prefix="/v1")
    router.include_router(policyManagement.router, prefix="/v1")
    router.include_router(userManagement.router, prefix="/v1")

include_api_routes()