from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session  
from app.database import get_db
from app.model.serie import SerieModel
from app.schema.serie import SerieSchema

serie = APIRouter()

@serie.post("/")
async def criar_serie(dados: SerieSchema, db: Session = Depends(get_db)):
    nova_serie = SerieModel(**dados.model_dump())
    db.add(nova_serie)
    db.commit()
    db.refresh(nova_serie)
    return nova_serie

@serie.get("/")
async def listar_series(db: Session = Depends(get_db)):
    return db.query(SerieModel).all()

#tarefa 1: resolve todos os erros da sua aplicação
#tarefa 2: Crie as novas rotas de atualização de deleção da API
#tarefa 3: Resolva todos os erros das novas rotas
#Versione

#Extra: resolva o erro de importação das variáveis de ambiente detectado no 
# módulo python-dotenv e utilize corretamente a importação com a função
#load_dotenv() em seu database.py