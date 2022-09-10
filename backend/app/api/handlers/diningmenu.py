from io import StringIO
from typing import List, Optional
from unicodedata import name
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from app.api.deps.user_deps import current_user_is_admin
from app.schemas.diningmenu_schema import DiningMenuCreate, DiningMenuUpdate, DiningMenuOut
from app.services.diningmenu_service import DiningMenuService
from app.models.diningmenu_model import DiningMenu

import csv
import codecs

diningmenu_router = APIRouter()

@diningmenu_router.get('/', summary="Get all dining menus", response_model=List[DiningMenuOut])
async def list():
    return await DiningMenuService.list_diningmenus()

@diningmenu_router.get('/commons/{commons_name}', summary="Get all dining menus that belong to a specific dining commons", response_model=List[DiningMenuOut])
async def list_by_commons(commons_name: str):
    return await DiningMenuService.list_diningmenus_by_diningcommons(commons_name)

@diningmenu_router.get('/{diningmenu_id}', summary="Get a dining menu by diningmenu_id", response_model=DiningMenuOut)
async def retrieve(diningmenu_id: UUID):
    return await DiningMenuService.retrieve_diningmenu(diningmenu_id)

@diningmenu_router.post('/create', summary="Create dining menu", response_model=DiningMenu)
async def create_diningmenu(menu_name: str, commons_name: str, file: UploadFile, user_is_admin: bool = Depends(current_user_is_admin)):
    if user_is_admin:
        csv_reader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))
        data = []
        for row in csv_reader:
            data.append(row)
        file.file.close()

        new_menu = DiningMenuCreate(name=menu_name, diningcommons_name=commons_name, food_items=data)
        return await DiningMenuService.create_diningmenu(new_menu)
    else:
        return HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Must be an admin user to access endpoint")

@diningmenu_router.put('{diningmenu_id}', summary="Update dining menu by diningmenu_id", response_model=DiningMenuOut)
async def update(diningmenu_id: UUID, menu_name: Optional[str], commons_name: Optional[str], file: Optional[UploadFile], 
            user_is_admin: bool = Depends(current_user_is_admin)):
    if user_is_admin:
        updated_menu = DiningMenuUpdate()
        if not menu_name == None:
            updated_menu.name = menu_name
        if not commons_name == None:
            updated_menu.diningcommons_name = commons_name
        if not file == None:
            csv_reader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))
            data = []
            for row in csv_reader:
                data.append(row)
            file.file.close()
            updated_menu.food_items = data
        return await DiningMenuService.update_diningmenu(diningmenu_id, updated_menu)
    else:
        return HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Must be an admin user to access endpoint")

@diningmenu_router.delete('{diningmenu_id}', summary="Delete dining menu by diningmenu_id")
async def delete (diningmenu_id: UUID, user_is_admin: bool = Depends(current_user_is_admin)):
    if not user_is_admin:
        return HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Must be an admin user to access endpoint")
    else:
        await DiningMenuService.delete_diningmenu(diningmenu_id)
        return None