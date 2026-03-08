from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from conexao.conexao_mongo import conn

app = FastAPI()

@app.get("/gerenciar-bens/imoveis")
def get_imoveis():
    db = conn("Inserir as credenciais")
    colecao = db['imoveis']
    dados = list(colecao.find())

    for item in dados:
        item["_id"] = str(item["_id"])
    return dados

@app.get("/gerenciar-bens/imoveis/filtro/")
def get_imoveis_filtrado(
                        cidade: Optional[str] = None,
                        estado: Optional[str] = None,
                        qtde_comodos: Optional[int] = None
                        ):
    
    filtro = {}

    if cidade:
            filtro['cidade'] = cidade
    if estado:
            filtro['estado'] = estado   
    if qtde_comodos:
            filtro['qtde_comodos'] = qtde_comodos

    db = conn("Inserir as credenciais")
    colecao = db['imoveis']

    dados = list(colecao.find(filtro))

    for item in dados:
        item["_id"] = str(item["_id"])
    return dados

@app.post("/gerenciar-bens/imoveis/adicionar-imovel/")
def post_imovel(endereco,numero,estado,cidade,qtde_comodos,metros_quadrados):
    imovel = {
        'endereco':endereco,
        'numero':numero,
        'estado':estado,
        'cidade':cidade,
        'qtde_comodos':qtde_comodos,
        'metros_quadrados':metros_quadrados
    }
    try:
        db = conn("Inserir as credenciais")
        colecao = db['imoveis']
        colecao.insert_one(imovel)

        print(f"Imovel inserido:"
                    f"Endereço: {imovel[endereco]}\n" 
                    f"Numero:{imovel[numero]}\n" 
                    f"Estado: {imovel[estado]}\n" 
                    f"Cidade: {imovel[cidade]}\n" 
                    f"Comodos: {imovel[qtde_comodos]}\n"
                    f"m³: {imovel[metros_quadrados]}")
    except Exception as e:
        print(f"erro: {e}")
        return {"erro": str(e)} 
    
  

# @app.put("/feito/{pos}")
# def marcar_feito(pos: int):
#     tarefas[pos].feito = True
#     return tarefas[pos]

# @app.delete("/deletar/{pos}")
# def deletar_tarefa(pos: int):
#     tarefa = tarefas.pop(pos)
#     return tarefa
