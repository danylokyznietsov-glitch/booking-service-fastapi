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