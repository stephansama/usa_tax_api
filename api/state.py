from optparse import Option
from typing import Optional
from fastapi import APIRouter, Path, Query

router = APIRouter()


@router.get('/state/{state_id}')
async def get_state_info(
    state_id: int = Path(
        ..., description="")
):
    """
    Get individual state tax object
    """
    ...


@router.get('/states')
async def get_states_info(
    start: Optional[int] = Query(
        None, description="Starting position for states request"),
    end: Optional[int] = Query(
        None, description="Ending position for states request"),
    year: Optional[int] = Query(
        2022, description="Year for requested state tax information")
):
    """
    Get all states based on requested information
    """
    return {
        "year": year,
        "results": end - start if end else 0
    }
