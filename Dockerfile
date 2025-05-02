# ベースとなるPythonイメージを指定 (例: Python 3.9の軽量版)
FROM python:3.9-slim

# コンテナ内の作業ディレクトリを設定
WORKDIR /app

# requirements.txt をコンテナにコピー
COPY requirements.txt requirements.txt

# requirements.txt に基づいて依存ライブラリをインストール
# --no-cache-dir オプションはイメージサイズを小さくするためにキャッシュを使用しない指定
RUN pip install --no-cache-dir -r requirements.txt

# プロジェクトのファイルを作業ディレクトリにコピー
COPY . .

# コンテナがリッスンするポートを指定 (FastAPIのデフォルトは8000)
EXPOSE 8000

# コンテナ起動時に実行するコマンド
# uvicorn を起動し、main.py 内の app インスタンスを実行
# --host 0.0.0.0 でコンテナ外からのアクセスを許可
# --port 8000 でポートを指定
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]