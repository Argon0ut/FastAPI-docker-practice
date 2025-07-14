#this file is created after we created the asynchronoustextmanager lifespan function and in this
# file we will mainly write the scripts that will allow us freely work with database (maily CRUD commands for DB)
from sqlalchemy import select

from database import new_session, TaskORM
from schemas import STaskAdd, STask


class TaskRepository:
    @classmethod #You can call the method on the class, not on an instance
    async def add_one(cls, data: STaskAdd) -> int:# to work with new tasks we need specific data, and those data will have the type of STaskAdd now, access the current session which will allow us to work with the DB objects as a real models, that is to say: we will not only work with JSONs or dict, but with a solid Classes from database.py

        async with new_session() as session: #opening a context manager which will provide the object to the session
            task_dict = data.model_dump() #convert to dictionary

            task = TaskORM(**task_dict) #opening the task_dict so that its fields are automatically were declared in here(kwargs)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id  #the instance was added to the db via .add() and .flash() -> return the id -> commit the changes

    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskORM)
            result = await session.execute(query) #it is an iterator under the hood
            task_models = result.scalars().all() #alchemy objects that will be returned
            task_schemas = [STask.model_validate(task_model) for task_model in task_models]
            #adding this line to show the example value that will be returned to make it more convenient for frontend developer
            return task_schemas
