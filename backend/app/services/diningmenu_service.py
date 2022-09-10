from typing import List
from uuid import UUID
from app.models.diningmenu_model import DiningMenu
from app.schemas.diningmenu_schema import DiningMenuCreate, DiningMenuUpdate

class DiningMenuService:
    @staticmethod
    async def list_diningmenus() -> List[DiningMenu]:
        diningmenu_list = await DiningMenu.find_all().to_list()
        return diningmenu_list

    @staticmethod
    async def list_diningmenus_by_diningcommons(commons_name: str) -> List[DiningMenu]:
        diningmenu_list = await DiningMenu.find(DiningMenu.diningcommons_name == commons_name).to_list()
        return diningmenu_list

    @staticmethod
    async def create_diningmenu(data: DiningMenuCreate) -> DiningMenu:
        diningmenu = DiningMenu(**data.dict())
        return await diningmenu.insert()

    @staticmethod
    async def retrieve_diningmenu(diningmenu_id: UUID):
        diningmenu = await DiningMenu.find_one(DiningMenu.diningmenu_id == diningmenu_id)
        return diningmenu

    @staticmethod
    async def update_diningmenu(diningmenu_id: UUID, data: DiningMenuUpdate):
        diningmenu = await DiningMenuService.retrieve_diningmenu(diningmenu_id)
        await diningmenu.update({"$set": data.dict(exclude_unset=True)})

        await diningmenu.save()
        return diningmenu

    @staticmethod
    async def delete_diningmenu(diningmenu_id: UUID) -> None:
        diningmenu = await DiningMenuService.retrieve_diningmenu(diningmenu_id)
        if diningmenu:
            await diningmenu.delete()
        return None