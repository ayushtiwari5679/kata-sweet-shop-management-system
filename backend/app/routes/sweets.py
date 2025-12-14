
from fastapi import APIRouter
router = APIRouter(prefix="/api/sweets")

@router.get("")
def get_sweets():
    return []
