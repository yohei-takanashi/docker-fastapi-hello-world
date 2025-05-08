import requests


def fetch_data(number: int) -> dict:
    """
    図鑑番号を入力してデータを取得する
    """
    try:
        url: str = f"https://pokeapi.co/api/v2/pokemon-species/{number}/"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def fetch_flavor_ja(number: int) -> list:
    """
    図鑑番号を入力して取得したデータから日本語のデータのみを取り出す
    """
    flavor_text_ja = []
    flavor_text_entries: list = fetch_data(number).get("flavor_text_entries")
    for i in flavor_text_entries:
        language: dict = i.get("language")
        language_name: str = language.get("name")
        if language_name in ["ja", "ja-Hrkt"]:
            flavor_text: str = i.get("flavor_text")
            flavor_text_ja.append(flavor_text)
    return flavor_text_ja
