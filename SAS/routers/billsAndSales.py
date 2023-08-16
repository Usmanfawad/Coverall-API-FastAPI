from fastapi import APIRouter

router = APIRouter(
    prefix="/billing",
    tags=["billing"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.get("/subscribe")
async def api_billing_subscribe():
    return

@router.get("/cancel")
async def api_billing_cancel():
    return

@router.get("/update")
async def api_billing_update():
    return