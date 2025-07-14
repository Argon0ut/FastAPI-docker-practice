from typing import Optional, Annotated

from fastapi import FastAPI, Depends
from pydantic import BaseModel

from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from schemas import STaskAdd
from router import router as tasks_router



@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Database was cleared")
    await create_tables()
    print("Database is ready")

    yield
    print("turning off the lifespan")
app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
