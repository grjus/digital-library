from fastapi import APIRouter

router = APIRouter()


@router.get("/", response_description="Health Check")
def health_check():
    return {"status": "ok"}
