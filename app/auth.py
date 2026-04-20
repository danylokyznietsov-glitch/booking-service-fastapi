from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
import app.crud as crud
import jwt
from datetime import datetime, timedelta, timezone


SECRET_KEY = "my_super_secret_key" 
ALGORITHM = "HS256"


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    hashed_password = pwd_context.hash(password)
    return hashed_password


def verify_password(plain_password: str, hashed_password: str) -> bool:
    hash_verify = pwd_context.verify(plain_password, hashed_password)
    return hash_verify


async def authenticate_user(session: AsyncSession, email: str, password: str):
    user = await crud.get_user_email(session=session, email=email)
    if not user:
        return None
    is_password_correct =  verify_password(plain_password=password, hashed_password=user.hashed_password)
    if not is_password_correct:
        return None
    return user



def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt