from pydantic import BaseModel

# 受け取り型
class TodoBody(BaseModel):
    title: str
    description: str

# 返還型
class Todo(BaseModel):
    id: str
    title: str
    description: str


class SuccessMsg(BaseModel):
    message : str