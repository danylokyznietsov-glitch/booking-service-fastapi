from sqlalchemy.orm import Mapped, mapped_column
from .database import Base
from sqlalchemy import JSON



class Hotel(Base):

    __tablename__ = "hotels"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    name: Mapped[str]
    
    location: Mapped[str]
    
    services: Mapped[list[str]] = mapped_column(JSON)
    
    rooms_quantity: Mapped[str]
    
    image_id: Mapped[int] 
    
       
class User(Base):
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    email: Mapped[str] = mapped_column(unique=True)
    
    hashed_password: Mapped[str]
    
    
    

    
    