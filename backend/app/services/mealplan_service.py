from typing import List
from uuid import UUID
from app.models.user_model import User
from app.models.mealplan_model import MealPlan
from app.schemas.mealplan_schema import MealPlanCreate, MealPlanUpdate

class MealPlanService:
    @staticmethod
    async def list_mealplans(user: User) -> List[MealPlan]:
        mealplans = await MealPlan.find(MealPlan.owner.id == user.id).to_list()
        return mealplans
    
    @staticmethod
    async def create_mealplan(user: User, data: MealPlanCreate) -> MealPlan:
        mealplan = MealPlan(**data.dict(), owner=user)
        return await mealplan.insert()

    @staticmethod
    async def retrieve_mealplan(user: User, mealplan_id: UUID):
        mealplan = await MealPlan.find_one(MealPlan.mealplan_id == mealplan_id, MealPlan.owner.id == user.id)
        return mealplan
    
    @staticmethod
    async def update_mealplan(user: User, mealplan_id: UUID, data: MealPlanUpdate):
        mealplan = await MealPlanService.retrieve_mealplan(user, mealplan_id)
        await mealplan.update({"$set": data.dict(exclude_unset=True)})

        await mealplan.save()
        return mealplan

    @staticmethod
    async def delete_mealplan(user: User, mealplan_id: UUID) -> None:
        mealplan = await MealPlanService.retrieve_mealplan(user, mealplan_id)
        if mealplan:
            await mealplan.delete()

        return None