from sqlalchemy.orm import Mapped, mapped_column
from .database import Base




class Hotel(Base):

    title: Mapped[str]
    
    price: Mapped[int | None] 
    
       
class User(Base):
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    email: Mapped[str] = mapped_column(unique=True)
    
    hashed_password: Mapped[str]
    