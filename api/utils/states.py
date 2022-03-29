from sqlalchemy.orm import Session

from database.models.state import State

def find_state(db: Session, state_id: int):
    return db.query(State).filter(State.id == state_id).first()