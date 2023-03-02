from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from schemas import SuccessMsg

from routers import route_todo

app = FastAPI()
app.include_router(route_todo.router)

@app.get("/", response_model=SuccessMsg)
def root():
    return {"message": "Welcome to Fast API"}