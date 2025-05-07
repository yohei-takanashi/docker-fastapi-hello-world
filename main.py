from fastapi import FastAPI
import requests
import os

app = FastAPI()


@app.get("/")
async def read_root():
    """
    ルートパスにアクセスされた場合に "Hello World" を含むJSONを返すエンドポイント
    """
    return {"message": "Hello World"}


@app.get("/fetch")
async def fetch_data(url: str = "https://pokeapi.co/api/v2/pokemon-species/25/"):
    """
    指定されたURLからGETリクエストでデータを取得するエンドポイント（requests使用例）
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # HTTPエラーがあれば例外を発生させる
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


@app.get("/abilities/{number}")
async def fetch_abilities(number: int):
    url: str = f"https://pokeapi.co/api/v2/pokemon-species/{number}/"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


@app.get("/flavor/{number}")
def fetch_flavor(number: int):
    url: str = f"https://pokeapi.co/api/v2/pokemon-species/{number}/"
    response = requests.get(url)
    response.raise_for_status()
    poke_data = response.json()

    flavor_text_ja = []
    flavor_text_entries: list = poke_data.get("flavor_text_entries")
    for i in flavor_text_entries:
        language = i.get("language")
        language_name = language.get("name")
        if language_name in ["ja", "ja-Hrkt"]:
            flavor_text = i.get("flavor_text")
            flavor_text_ja.append(flavor_text)
    return flavor_text_ja


from dotenv import load_dotenv
from google import genai


def post_gemini(query) -> str:
    """
    Gemini APIにPOSTリクエストを送信する関数
    """
    load_dotenv()
    API_KEY = os.environ.get("API_KEY")
    client = genai.Client(api_key=API_KEY)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"以下の文は特定のポケモンの説明文を集めたものです。これらからポケモンの名前を予想して。その後説明文を総合した説明文を作って。以下の形式で出力して。(ポケモンの名前):(総合した説明文)。{query}",
    )
    return response.text


@app.post("/gemini")
def post_gemini_endpoint(query: str):
    """
    Gemini APIにPOSTリクエストを送信するエンドポイント
    """
    result = post_gemini(query)
    return {"result": result}


def flavor_summary(number: int) -> str:
    flavor_text = fetch_flavor(number)
    query = flavor_text
    llm_result = post_gemini(query)
    return llm_result


@app.post("/gemini_summary")
def post_gemini_endpoint2(number: int):
    result = flavor_summary(number)
    return {"result": result}
