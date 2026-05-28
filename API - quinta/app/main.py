from fastapi import FastAPI
from app.database import engine, Base
from app.rotas import rota

app = FastAPI(
    title="API Copa do Mundo",
    description="## API para fornecer informações sobre os jogos e grupos da Copa do Mundo",
)

Base.metadata.create_all(bind=engine)
app.include_router(rota)

@app.get("/", tags=["Informação se a API está funcionando"])
def home():

    return{
        "mensagem": "A API está funcionando!"
    }