import fastapi

router = fastapi.APIRouter()


@router.get('/year')
async def get_year():
    pass
