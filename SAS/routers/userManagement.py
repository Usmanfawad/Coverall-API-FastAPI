from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.get("/signup")
async def api_users_signup():
    return

@router.get("/login")
async def api_users_login():
    return

@router.get("/logout")
async def api_users_logout():
    return

@router.get("/update")
async def api_users_update():
    return

@router.get("/delete")
async def api_users_delete():
    return
