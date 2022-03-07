from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    """Changed the description

    Returns:
        _type_: _description_
    """
    return {"message": "Hello World"}
