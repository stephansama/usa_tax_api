import fastapi

router = fastapi.APIRouter()


@router.get('/federal')
async def get_federal():
    pass
