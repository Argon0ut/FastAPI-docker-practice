from typing import Annotated

from fastapi import APIRouter, Depends

from database import TaskORM
from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    #Depends() --> This is part of FastAPI's Dependency Injection system.
    #Annotated[] --> This is the newer, cleaner way (Python 3.10+) to combine type hinting and dependency injection.
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks