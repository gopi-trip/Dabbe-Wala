from fastapi import FastAPI
from contextlib import asynccontextmanager
from routes.orders import router as orders_router
from routes.stats import router as stats_router
from database import create_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create database tables on startup
    create_tables()
    print("Database tables created successfully.")
    yield
    # Perform any cleanup tasks here if needed
    print("Application shutdown complete.")

app = FastAPI(
    title="Dabbe Wala API",
    description="API for managing orders and tracking their status in the Dabbe Wala system.",
    version="1.0.0",
    lifespan=lifespan
)

@app.get("/health", tags=["Health"])
def read_root():
    return {"message": "Welcome to the Dabbe Wala API!"}

app.include_router(orders_router)
app.include_router(stats_router)