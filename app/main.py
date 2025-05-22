from fastapi import FastAPI
from app.routes import product_routes, user_routes, order_routes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_routes.router, prefix="/products")
app.include_router(user_routes.router, prefix="/users")
app.include_router(order_routes.router, prefix="/orders")
 