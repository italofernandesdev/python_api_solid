from fastapi import FastAPI
from app.api.user import userRoute

app = FastAPI()

app.include_router(userRoute)
