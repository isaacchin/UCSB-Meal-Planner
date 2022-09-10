from typing import List, Optional
from uuid import UUID, uuid4
from beanie import Document, Indexed
from pydantic import Field

class DiningMenu(Document):
    diningmenu_id: UUID = Field(default_factory=uuid4, unique=True)
    name: Indexed(str)
    diningcommons_name: Indexed(str)
    food_items: List[dict]

    def __repr__(self) -> str:
        return f"<{self.name} Dining Menu>"

    def __str__(self) -> str:
        return self.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, DiningMenu):
            return self.diningmenu_id == other.diningmenu_id
        return False

    class Collection:
        name = "diningmenu"