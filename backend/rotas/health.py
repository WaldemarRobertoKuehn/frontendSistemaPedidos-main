# Rota operacional que só confirma que o servidor está no ar.
from fastapi import APIRouter

router = APIRouter()


@router.get("")
def health():
    return {"status": "ok"}
