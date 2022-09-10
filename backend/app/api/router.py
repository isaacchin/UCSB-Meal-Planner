from fastapi import APIRouter
from app.api.handlers import user
from app.api.handlers import diningmenu
from app.api.handlers import mealplan
from app.api.auth.jwt import auth_router

router = APIRouter()

router.include_router(user.user_router, prefix='/users', tags=["users"])
router.include_router(auth_router, prefix='/auth', tags=["auth"])
router.include_router(diningmenu.diningmenu_router, prefix='/diningmenu', tags=["diningmenu"])
router.include_router(mealplan.mealplan_router, prefix='/mealplan', tags=["mealplan"])