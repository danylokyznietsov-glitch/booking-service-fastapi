from fastapi import FastAPI
import uvicorn
from app.routers.hotels import router as hotels_router
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers.users import router as user_router

 

app = FastAPI()

app.include_router(hotels_router, prefix="/hotels")
app.include_router(user_router)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
