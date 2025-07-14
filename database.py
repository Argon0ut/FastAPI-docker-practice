from typing import Optional

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

    #create_async_engine --> Engine that will send requests to the database

engine = create_async_engine(
    "sqlite+aiosqlite:///tasks.db"
    #DB name + driver(aiosqlite) :/// actual name of the db
)

    #async session maker --> session opener for working with db

new_session = async_sessionmaker(engine, expire_on_commit=False)
    #This line creates a function (factory) that will generate new asynchronous database sessions.


class Model(DeclarativeBase):
    pass

class TaskORM(Model):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True) #mandatory to always add at least one primary key field
    name: Mapped[str]
    description: Mapped[Optional[str]]

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)
    #an asyncronous function to create a DB.
    # it first goes to the engine, then goes to Model base and creates all the tables

async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)

