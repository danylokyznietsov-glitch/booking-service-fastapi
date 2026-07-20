from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Hotel
from app.database import get_async_session
from sqlalchemy import select
from app.schemas import SHotel
import app.crud as crud
from fastapi import HTTPException




router = APIRouter(tags=["Hotels"], prefix="/hotel")

@router.post("")
async def create_hotel(hotel: SHotel, session: AsyncSession = Depends(get_async_session)):
    new_hotel = await crud.create_hotel(session=session, hotel=hotel)
    return new_hotel

@router.get("", response_model=list[SHotel])
async def get_hotels(session: AsyncSession = Depends(get_async_session)):
    hotel_list = await crud.get_hotels(session=session)
    return hotel_list


@router.delete("/{hotel_id}")
async def delete_hotel(hotel_id: int, session: AsyncSession = Depends(get_async_session)):
    result = await crud.delete_hotel(session=session, hotel_id=hotel_id)
    if not result:
        raise HTTPException(status_code=404, detail="Готель не знайдено")
    return {"message": "Готель успішно видалено"}

    

@router.put("/{hotel_id}")
async def update_hotel(hotel_id: int, hotel_data: SHotel, session: AsyncSession = Depends(get_async_session)):
    put_hotel = await crud.put_hotel(session=session, hotel_id=hotel_id, hotel_data=hotel_data)
    return put_hotel
    
    

