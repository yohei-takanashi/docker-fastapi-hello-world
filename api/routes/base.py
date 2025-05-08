from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def read_root():
    """
    ルートパスにアクセスされた場合に "Hello World" を含むJSONを返すエンドポイント
    """
    return {"message": "Hello World"}