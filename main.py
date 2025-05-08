from fastapi import FastAPI
from api.routes import base, pokemon, gemini

app = FastAPI()

app.include_router(base.router)
app.include_router(pokemon.router)
app.include_router(gemini.router)