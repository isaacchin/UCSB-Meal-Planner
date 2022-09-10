from dataclasses import dataclass
from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends
from app.models.user_model import User
from app.api.deps.user_deps import get_current_user
from app.services.mealplan_service import MealPlanService
from app.models.mealplan_model import MealPlan
from app.schemas.mealplan_schema import MealPlanCreate, MealPlanUpdate, MealPlanOut

mealplan_router = APIRouter()

@mealplan_router.get('/', summary="Get all meal plans of the current user", response_model=List[MealPlan])
async def list(current_user: User = Depends(get_current_user)):
    return await MealPlanService.list_mealplans(current_user)

@mealplan_router.post('/create', summary="Create a meal plan", response_model=MealPlan)
async def create_mealplan(data: MealPlanCreate, current_user: User = Depends(get_current_user)):
    return await MealPlanService.create_mealplan(current_user, data)

@mealplan_router.get('/{mealplan_id}', summary="Get a meal plan by mealplan_id", response_model=MealPlanOut)
async def retrieve(mealplan_id: UUID, current_user: User = Depends(get_current_user)):
    return await MealPlanService.retrieve_mealplan(current_user, mealplan_id)

@mealplan_router.put('/{mealplan_id}', summary="Update a meal plan by mealplan_id", response_model=MealPlanOut)
async def retrieve(mealplan_id: UUID, data: MealPlanUpdate, current_user: User = Depends(get_current_user)):
    return await MealPlanService.update_mealplan(current_user, mealplan_id, data)

@mealplan_router.delete('/{mealplan_id}', summary="Delete a meal plan by mealplan_id")
async def retrieve(mealplan_id: UUID, current_user: User = Depends(get_current_user)):
    await MealPlanService.delete_mealplan(current_user, mealplan_id)
    return None
