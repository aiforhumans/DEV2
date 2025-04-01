from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="AI DEV Kit Backend")
app.include_router(router)
