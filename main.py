from fastapi import FastAPI
from api import federal, state, year
from dotenv import load_dotenv
import os

load_dotenv()


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


app.include_router(federal.router)
app.include_router(state.router)
app.include_router(year.router)
