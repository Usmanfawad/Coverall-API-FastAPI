from fastapi import APIRouter

router = APIRouter(
    prefix="/policy",
    tags=["policy"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get("/create")
async def api_policy_create():
    return

@router.get("/update")
async def api_policy_update():
    return

@router.get("/delete")
async def api_policy_delete():
    return