from fastapi import APIRouter, HTTPException
from sqlalchemy import or_
from app.database import sessaoLocal
from app.models import modelo
from app.api import consumir_API
from app.transformando import transformar_dados

rota = APIRouter()

@rota.get("/update", tags=["Atualizar dados"])
def update_banco():
    
    db = sessaoLocal()
    try:
        data = consumir_API()
        if "erro" in data:
            raise HTTPException(
                status_code=500,
                detail=data["erro"]
            )

        jogos = transformar_dados(data)
        db.query(modelo).delete()
        for jogo in jogos:
            novo_jogo = modelo(**jogo)
            db.add(novo_jogo)
        db.commit()
        
        return {
            "mensagem": "Banco atualizado!",
            "quantidade de jogos": len(jogos)
        }
        
    finally:
        db.close()

@rota.get("/jogos", tags=["Ver jogos"])
def get_jogos():

    db = sessaoLocal()
    try:
        jogos = db.query(modelo).all()
        if not jogos:
            raise HTTPException(
                status_code=404,
                detail="Nenhum jogo encontrado"
            )
        return jogos

    finally:
        db.close()

@rota.get("/grupos", tags=["Ver grupos"])
def get_grupos():

    db = sessaoLocal()
    try:
        jogos = db.query(modelo).all()
        if not jogos:
            raise HTTPException(
                status_code=404,
                detail="Nenhum grupo encontrado"
            )

        grupos = {}

        for jogo in jogos:
            grupo = jogo.grupo
            if grupo == "N/A":
                continue
            if grupo not in grupos:
                grupos[grupo] = []
            if jogo.mandante not in grupos[grupo]:
                grupos[grupo].append(jogo.mandante)
            if jogo.visitante not in grupos[grupo]:
                grupos[grupo].append(jogo.visitante)
        return grupos

    finally:
        db.close()

@rota.get("/jogos/grupo/{grupo}", tags=["Ver jogos de um grupo específico"])
def jogos_por_grupo(grupo: str):

    db = sessaoLocal()
    try:
        grupo = f"GROUP_{grupo.upper()}"
        jogos = db.query(modelo).filter(
            modelo.grupo == grupo
        ).all()

        if not jogos:
            raise HTTPException(
                status_code=404,
                detail="Grupo não encontrado"
            )
        return jogos

    finally:
        db.close()

@rota.get("/jogos/selecao/{selecao}", tags=["Ver jogos de uma seleção específica"])
def jogos_por_selecao(selecao: str):

    db = sessaoLocal()
    try:
        jogos = db.query(modelo).filter(
            or_(
                modelo.mandante.ilike(f"%{selecao}%"),
                modelo.visitante.ilike(f"%{selecao}%")
            )
        ).all()

        if not jogos:
            raise HTTPException(
                status_code=404,
                detail="Seleção não encontrada"
            )
        return jogos

    finally:
        db.close()