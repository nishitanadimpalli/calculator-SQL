from fastapi import FastAPI
from db import Base, engine
from models import *  # noqa
from routers.calculations import router as calc_router

# Ensure metadata matches DB (tables already created by SQL, but this is safe)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Calculator (Docker)")

@app.get("/")
def root():
    return {"status": "ok"}

app.include_router(calc_router)
