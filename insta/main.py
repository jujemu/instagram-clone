from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .db import models
from .db.database import engine
from .routers import post, user


app = FastAPI()


app.include_router(user.router)
app.include_router(post.router)

models.Base.metadata.create_all(bind=engine)

app.mount('/images', StaticFiles(directory='images'), name='images')

@app.get('/')
def default():
    return 'Welcome'
