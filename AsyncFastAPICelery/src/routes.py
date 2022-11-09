# api/routes/__init__.py

from fastapi import APIRouter

from src.calculation import calc_routes
from src.data import data_routes

router = APIRouter()

# calculation

router.include_router(calc_routes.router, tags=["Async Tasks"])

# data

router.include_router(data_routes.router, tags=["Async Tasks"])
