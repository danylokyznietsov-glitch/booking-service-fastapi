from pydantic import BaseModel, ConfigDict, EmailStr



class SHostel(BaseModel):
    title: str
    price: int

    model_config = ConfigDict(from_attributes=True)
    
    
    
class SUserRegister(BaseModel):
    email: EmailStr
    password: str
    
    
class SUserInfo(BaseModel):
    id: int
    email: EmailStr
    
    
    
class SHotel(BaseModel):
    id: int
    name: str
    location: str
    services: list[str]
    rooms_quantity: int
    image_id: int