from datetime import datetime
from http.client import HTTPException
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import ValidationError
from app.core.config import settings
from app.models.user_model import User
from app.schemas.auth_schema import TokenPayload
from app.services.user_service import UserService

from jose import jwt

reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_STR}/auth/login",
    scheme_name="JWT"
)

async def get_current_user(token: str = Depends(reuseable_oauth)) -> User:
    try:
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)

        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired", headers={"WWW-Authenticate": "Bearer"})
    
    except(jwt.JWTError, ValidationError):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})

    user = await UserService.get_user_by_id(token_data.sub)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Could not find user")

    return user

async def current_user_is_admin(user: User = Depends(get_current_user)) -> bool:
    current_user_email = user.email
    if current_user_email == settings.ADMIN_USER: return True

    return False