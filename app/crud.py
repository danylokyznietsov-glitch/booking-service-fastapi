from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models import Hotel, User
from app.schemas import SHotel





async def get_hotels(session: AsyncSession):
    query = select(Hotel)
    result = await session.execute(query)
    hotels = result.scalars().all()
    return hotels
    
       
async def delete_hotel(session: AsyncSession, hotel_id: int):
    hotel_to_delete = await session.get(Hotel, hotel_id)
    if not hotel_to_delete:
        return False
    await session.delete(hotel_to_delete)
    await session.commit()
    return True



async def put_hotel(session: AsyncSession, hotel_id: int, hotel_data: SHotel):
    hotel_to_update = await session.get(Hotel, hotel_id)
    if not hotel_to_update:
        return False
    
    hotel_to_update.title = hotel_data.title
    hotel_to_update.price = hotel_data.price
    await session.commit()
    return True


async def create_hotel(session: AsyncSession, hotel: SHotel):
    new_hotel = Hotel(
        name=hotel.name,
        location=hotel.location,
        services=hotel.services,
        rooms_quantity=hotel.rooms_quantity,
        image_id=hotel.image_id
    )
    session.add(new_hotel)
    await session.commit()
    await session.refresh(new_hotel)
    
    return new_hotel


async def get_user_email(session: AsyncSession, email: str):
    query = select(User).where(User.email==email)
    result = await session.execute(query)
    return result.scalar_one_or_none()


async def create_user(session: AsyncSession, email: str, hashed_password: str):
    create = User(email=email, hashed_password=hashed_password)
    session.add(create)
    await session.commit()
    return create





async def get_user_by_id(session: AsyncSession, user_id: int):
    query = select(User).where(User.id == user_id)
    result = await session.execute(query)
    return result.scalar_one_or_none()
