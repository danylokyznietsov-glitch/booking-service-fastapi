from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_async_session
from app.schemas import SUserRegister, SUserInfo
from fastapi import HTTPException
import app.crud as crud
from app.auth import get_password_hash
from app.auth import authenticate_user, create_access_token, get_current_user
from fastapi.security import OAuth2PasswordRequestForm





router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
async def register_user(user_data: SUserRegister, session: AsyncSession = Depends(get_async_session)):
    existing_user = await crud.get_user_email(session=session, email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=409, detail="Користувач вже існує")
    hashed_pwd = get_password_hash(password=user_data.password)
    await crud.create_user(session=session, email=user_data.email, hashed_password=hashed_pwd)
    return {"message": "Ви успішно зареєструвалися!"}


@router.post("/login")
async def login_user(user_data: OAuth2PasswordRequestForm = Depends(), session: AsyncSession = Depends(get_async_session)):
    user = await authenticate_user(session=session, email=user_data.username, password=user_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Неправильна пошта або пароль")
    token_data = {"sub": str(user.id)}
    access_token = create_access_token(token_data)
    return {"access_token": access_token, "token_type": "bearer"}



@router.get("/me", response_model=SUserInfo)
async def get_my_profile(current_user = Depends(get_current_user)):
    return current_user 

    
    



