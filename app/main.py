from fastapi import FastAPI
from app.controllers import sample_controller

app = FastAPI(title="Sample MVC FastAPI")

app.include_router(sample_controller.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Sample API"}
