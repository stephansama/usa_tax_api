from fastapi import APIRouter, Path

from database.schemas.year import Year

router = APIRouter()


@router.get('/year/{year_id}', response_model=Year)
async def get_year(
    year_id: int = Path(..., description="")
):
    pass
