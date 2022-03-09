from fastapi import FastAPI
from const import *
from api import federal, state, year


federal.router

app = FastAPI(
    title=APPLICATION_NAME,
    version=APPLICATION_VER,
    description=APPLICATION_DESC,
    contact=APPLICATION_CONTACT,
    license_info=APPLICATION_LICENSE
)


app.include_router(federal.router)
# app.include_router(state.router)
# app.include_router(year.router)
