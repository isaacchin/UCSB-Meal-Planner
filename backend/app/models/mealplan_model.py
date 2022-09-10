from uuid import UUID, uuid4
from beanie import Document, Indexed, Link
from pydantic import Field
from datetime import date
from .user_model import User

class MealPlan(Document):
    mealplan_id: UUID = Field(default_factory=uuid4, unique=True)
    meal_name: Indexed(str)
    owner: Link[User]
    created_at: date = Field(default_factory=date.today)
    
    calories_goal: float = Field(default=0.0)
    fat_goal: float = Field(default=0.0)
    carbs_goal: float = Field(default=0.0)
    protein_goal: float = Field(default=0.0)

    calories_count: float = Field(default=0.0)
    fat_count: float = Field(default=0.0)
    carbs_count: float = Field(default=0.0)
    protein_count: float = Field(default=0.0)

    def __repr__(self) -> str:
        return f"<Meal Plan {self.meal_name}>"

    def __str__(self) -> str:
        return self.meal_name

    def __hash__(self) -> int:
        return hash(self.meal_name)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, MealPlan):
            return self.mealplan_id == other.mealplan_id
        return False

    class Collection:
        name = "mealplan"

    class Settings:
        bson_encoders = {
            date: str
        }