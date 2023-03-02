from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ['http://localhost:3000', 'https://fastapi-1436a.web.app']

@app.get("/")
def root():
    return {"message": "Welcome to Fast API"}