from fastapi import APIRouter
from services.pokemon_services import fetch_data, fetch_flavor_ja
router = APIRouter()


@router.get("/fetch/{number}")
async def fetch_poke_data(number: int):
    """
    入力した図鑑番号からGETリクエストでデータを取得するエンドポイント
    """
    return fetch_data(number)


@router.get("/flavor/{number}")
def fetch_flavor(number: int):
    """
    入力した図鑑番号から日本語のデータのみを取得する
    """
    return fetch_flavor_ja(number)
