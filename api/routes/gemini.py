from fastapi import APIRouter
from services.gemini_services import post_gemini
from services.pokemon_services import fetch_flavor_ja

router = APIRouter()


@router.post("/gemini_summary")
def post_gemini_endpoint2(number: int):
    """
    図鑑番号を入力して、日本語だけの説明文をgeminiに渡し要約してもらう
    """
    flavor_text = fetch_flavor_ja(number)
    query = flavor_text
    llm_result = post_gemini(query)
    return llm_result