from fastapi import FastAPI

from app.db import Base, engine
from app import models

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Event booking API is running"}