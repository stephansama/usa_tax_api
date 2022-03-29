from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

from api import feds, states, years
from database.setup import engine
from database.models import state, year

state.Base.metadata.create_all(bind=engine)
year.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title=os.getenv('APP_NAME'),
    version=os.getenv('APP_VER'),
    description=os.getenv('APP_DESC'),
    license_info={"name": os.getenv('APP_LICENSE')},
    contact={
        "name": os.getenv('APP_CONTACT_NAME'),
        "email": os.getenv('APP_CONTACT_EMAIL')
    }
)


app.include_router(feds.router)
app.include_router(states.router)
app.include_router(years.router)
