import fastapi

router = fastapi.APIRouter()


@router.get('/state')
async def get_state():
    pass


@router.get('/states')
async def get_states():
    pass
