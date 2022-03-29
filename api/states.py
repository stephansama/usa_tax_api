# Stephan Randle
# 03 / 24 / 2022
#
# State Router
#
#
from typing import Optional, List
from fastapi import APIRouter, Path, Query, Depends

from sqlalchemy.orm import Session

from .utils.states import find_state
from database import setup
from database.schemas.state import State 

router = APIRouter()


@router.get('/state/{state_id}', response_model=State)
async def get_state_info(
    state_id: int = Path(
        ..., description=""),
    db: Session = Depends(setup.get_db)
):
    """
    Get individual state tax object
    """
    return find_state(db, state_id)


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
