from fastapi import FastAPI
from app.core.config import settings
from app.core.database import get_pool, close_pool
from app.api.ai_routes import router as ai_router
from app.api.v1.endpoints.health import router as health_router

# Initialize FastAPI app with project settings
app = FastAPI(title=settings.PROJECT_NAME)

# ---------------------------------------------------------------------------
# Lifecycle events
# ---------------------------------------------------------------------------
@app.on_event("startup")
async def startup():
    # Initialize database connection pool
    await get_pool()

@app.on_event("shutdown")
async def shutdown():
    # Close database connection pool
    await close_pool()

# ---------------------------------------------------------------------------
# Routers
# ---------------------------------------------------------------------------
# AI routes (chat, generate, usage, health)
app.include_router(ai_router)

# Providers health route
app.include_router(health_router)

# ---------------------------------------------------------------------------
# Root + Health endpoints
# ---------------------------------------------------------------------------
@app.get("/")
async def root():
    return {"message": "InternOps AI Service is running!"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}

print("main.py loaded")
