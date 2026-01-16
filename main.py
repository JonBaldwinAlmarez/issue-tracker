from fastapi import FastAPI
from app.routes.issues import router as issues_router
from app.middleware.timer import timer_middleware
from fastapi.middleware.cors import CORSMiddleware


# Create an instance of the FastAPI application
app = FastAPI()
app.middleware("http")(timer_middleware)  # Add the timer middleware to the app
app.include_router(issues_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
