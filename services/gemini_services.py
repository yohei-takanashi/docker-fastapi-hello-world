from config.setting import setting
from google import genai


def post_gemini(query) -> str:
    """
    Gemini APIを呼び出す関数
    """
    client = genai.Client(api_key=setting.API_KEY)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"以下の文は特定のポケモンの説明文を集めたものです。これらからポケモンの名前を予想して。その後説明文を総合した説明文を作って。以下の形式で出力して。(ポケモンの名前):(総合した説明文)。出力する文章は200字以内にして。{query}",
    )
    return response.text