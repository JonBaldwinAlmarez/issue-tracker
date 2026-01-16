from fastapi import FastAPI
from app.routes.issues import router as issues_router


# Create an instance of the FastAPI application
app = FastAPI()

app.include_router(issues_router)
