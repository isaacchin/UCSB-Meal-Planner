from fastapi import FastAPI
from app.core.config import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.middleware.cors import CORSMiddleware

from app.models.user_model import User
from app.models.diningmenu_model import DiningMenu
from app.models.mealplan_model import MealPlan
from app.api.router import router

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_STR}/openapi.json"
)

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def app_init():
    db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).dining

    await init_beanie(
        database=db_client,
        document_models = [
            User,
            DiningMenu,
            MealPlan
        ]
    )

app.include_router(router,prefix=settings.API_STR)