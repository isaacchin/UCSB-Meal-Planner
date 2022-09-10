from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, Field

class DiningMenuCreate(BaseModel):
    name: str = Field(..., name='Name of dining menu')
    diningcommons_name: str = Field(..., name='Name of dining commons that this menu belongs to')
    food_items: List[dict] = Field(..., name='List of food items on this menu')

class DiningMenuUpdate(BaseModel):
    name: Optional[str] = Field(any, name='Name of dining menu')
    diningcommons_name: Optional[str] = Field(any, name='Name of dining commons that this menu belongs to')
    food_items: Optional[List[dict]] = Field(any, name='List of food items on this menu')

class DiningMenuOut(BaseModel):
    diningmenu_id: UUID
    name: str
    diningcommons_name: str
    food_items: List[dict]