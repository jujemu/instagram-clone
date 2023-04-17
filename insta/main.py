from fastapi import FastAPI

from .db import models
from .db.database import engine
from .routers import user


app = FastAPI()


app.include_router(user.router)


models.Base.metadata.create_all(bind=engine)


@app.get('/')
def default():
    return 'Welcome'