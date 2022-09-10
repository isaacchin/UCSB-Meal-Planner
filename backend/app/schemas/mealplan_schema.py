from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field
from datetime import date


class MealPlanCreate(BaseModel):
    meal_name: str = Field(..., title='Meal name', max_length=55, min_length=1)
    
    calories_goal: Optional[float] = 648.0
    fat_goal: Optional[float] = 22.0
    carbs_goal: Optional[float] = 68.0
    protein_goal: Optional[float] = 45.0

    calories_count: Optional[float] = 0.0
    fat_count: Optional[float] = 0.0
    carbs_count: Optional[float] = 0.0
    protein_count: Optional[float] = 0.0

class MealPlanUpdate(BaseModel):
    meal_name: Optional[str] = Field(..., title='Meal name', max_length=55, min_length=1)

    calories_goal: Optional[float] = 648.0
    fat_goal: Optional[float] = 22.0
    carbs_goal: Optional[float] = 68.0
    protein_goal: Optional[float] = 45.0

    calories_count: Optional[float] = 0.0
    fat_count: Optional[float] = 0.0
    carbs_count: Optional[float] = 0.0
    protein_count: Optional[float] = 0.0

class MealPlanOut(BaseModel):
    mealplan_id: UUID
    meal_name: str
    created_at: date
    
    calories_goal: float
    fat_goal: float
    carbs_goal: float
    protein_goal: float

    calories_count: float
    fat_count: float
    carbs_count: float
    protein_count: float



    