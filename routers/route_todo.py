from fastapi import APIRouter
from fastapi import Response, Request, HTTPException
from fastapi.encoders import jsonable_encoder
from typing import List
from schemas import Todo, TodoBody
from database import db_create_todo, db_get_todos, db_get_single_todo
from starlette.status import HTTP_201_CREATED

router = APIRouter()

@router.post("/api/todo", response_model=Todo)
async def create_todo(request: Request, response: Response, data: TodoBody):
    # 辞書型で受け取る
    todo = jsonable_encoder(data)
    # mongodbに飛ばす
    res = await db_create_todo(todo)
    # 作成時のレスポンスは基本201
    response.status_code = HTTP_201_CREATED

    if res:
        return res
    raise HTTPException(
        status_code=404, detail="Create task failed"
    )

@router.get("/api/todo", response_model=List[Todo])
async def get_todos():
    res = await db_get_todos()
    return res


@router.get("/api/todo/{id}", response_model=Todo)
async def get_single_todo(id : str):
    res = await db_get_single_todo(id)
    if res:
        return res
    raise HTTPException(
        status_code=404, detail=f"Task of ID: {id} does not exist"
    )
