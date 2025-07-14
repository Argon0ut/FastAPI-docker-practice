from typing import Optional

from pydantic import BaseModel


class STaskAdd(BaseModel): # example of the model creation in fastAPI similar to the Django's
    name: str
    description: Optional[str]=None

class STask(STaskAdd): # --> model for workning with DB
    id: int

class STaskId(BaseModel):
    ok: bool = True
    task_id: int