from fastapi import FastAPI
import requests

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
async def fetch_flavor(number: int):
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

    return {"flavor_text": flavor_text_ja}
