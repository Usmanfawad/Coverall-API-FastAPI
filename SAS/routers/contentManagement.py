from fastapi import APIRouter

router = APIRouter(
    prefix="/content",
    tags=["content"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.get("/submit")
async def api_content_submit():
    return

@router.get("/update")
async def api_content_update():
    return

@router.get("/delete")
async def api_content_delete():
    return

@router.get("/approve")
async def api_content_approve():
    return

@router.get("/reject")
async def api_content_reject():
    return
