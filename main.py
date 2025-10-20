from fastapi import FastAPI
from app.routes import product_routes, sales_routes, forecast_routes

app = FastAPI(
    title="AI-Based Inventory Management API",
    description="Backend for managing inventory, sales, and demand forecasting",
    version="1.0.0"
)

# Include route modules
app.include_router(product_routes.router, prefix="/products", tags=["Products"])
app.include_router(sales_routes.router, prefix="/sales", tags=["Sales"])
app.include_router(forecast_routes.router, prefix="/forecast", tags=["Forecast"])

@app.get("/")
def root():
    return {"message": "Welcome to the AI-Based Inventory Management API!"}
