from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from app.controllers import sample_controller

app = FastAPI(
    title="Sample MVC FastAPI",
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/docs",
)


def custom_openapi():
    """Customize the OpenAPI schema."""
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version="1.0.0",
        description="Sample API demonstrating MVC with secure practices.",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

app.include_router(sample_controller.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Sample API"}
