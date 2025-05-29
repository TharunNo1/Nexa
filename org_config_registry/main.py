from fastapi import FastAPI
from core.db import engine
from models.base import Base
from api.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Nexa Connector Registry")
app.include_router(router)
