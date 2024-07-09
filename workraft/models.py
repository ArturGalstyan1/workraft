from beartype.typing import Literal, Optional
from pydantic import BaseModel


class DBConfig(BaseModel):
    host: str
    port: int
    user: str
    password: str
    database: str


class WorkerState(BaseModel):
    id: str
    status: Literal["idle", "working", "offline"]
    current_task: Optional[str] = None
