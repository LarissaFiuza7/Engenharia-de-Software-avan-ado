from typing import Optional

from bson import ObjectId
from fastapi import FastAPI
from pydantic import BaseModel
from conexao.conexao_mongo import conn

app = FastAPI()

# Facilita a conexão com o banco de dados, evitando repetição de código em cada endpoint. 
# Se as credenciais ou o nome do banco de dados mudarem, basta atualizar esta função, e todas as partes do código que a utilizam serão automaticamente atualizadas. 
# Isso torna o código mais limpo, organizado e fácil de manter.
def conectar_banco():
    return conn('manager_componet', '987321','componentsoftware','ComponentReservas','urkfjzm.mongodb.net')

# metodo get para listar os imoveis disponiveis
@app.get("/gerenciar-bens/imoveis")
def listar_imoveis():

    try:
        # cria conexão com banco de dados   
        db = conectar_banco()
        #Entra na coleção de imoveis do banco de dados
        colecao = db['imoveis']
        #Cria uma lista com os imoveis disponiveis
        dados = list(colecao.find())

        #Converte o campo _id de ObjectId para string para facilitar a leitura e o manuseio dos dados.
        for item in dados:
            item["_id"] = str(item["_id"])

        #retorna o resultado
        return dados
    
    except Exception as e:
        #Imprime o erro ocorrido durante o processo de inserção do imóvel no banco de dados para depuração e retorna uma mensagem de erro como resposta da API.
        print(f"erro: {e}")
        return {"erro": str(e)} 

# metodo get para listar os imoveis disponiveis com filtro
@app.get("/gerenciar-bens/imoveis/filtro/")
def listar_imoveis_filtrados(
                        cidade: Optional[str] = None,
                        estado: Optional[str] = None,
                        qtde_comodos: Optional[int] = None
                        ):
    
    #Cria um dicionário de filtro vazio para armazenar os critérios de filtragem com base nos parâmetros fornecidos na solicitação.
    filtro = {}

    # Verifica se cada parâmetro de filtro foi fornecido na solicitação e, se sim, adiciona o critério correspondente ao dicionário de filtro.
    if cidade:
            filtro['cidade'] = cidade
    if estado:
            filtro['estado'] = estado   
    if qtde_comodos:
            filtro['qtde_comodos'] = qtde_comodos

    try:
        #cria a conexão com o banco de dados
        db = conectar_banco()
        #Entra na coleção de imoveis do banco de dados
        colecao = db['imoveis']

        #Cria uma lista com os imoveis disponiveis de acordo com o filtro aplicado
        dados = list(colecao.find(filtro))

        #Converte o campo _id de ObjectId para string para facilitar a leitura e o manuseio dos dados.
        for item in dados:
            item["_id"] = str(item["_id"])
        #retorna o resultado
        return dados

    except Exception as e:
        #Imprime o erro ocorrido durante o processo de inserção do imóvel no banco de dados para depuração e retorna uma mensagem de erro como resposta da API.
        print(f"erro: {e}")
        return {"erro": str(e)}

# metodo get para listar um imovel especifico
@app.get("/gerenciar-bens/imoveis/{id}/")
def buscar_imovel(id):

    try:
        #cria a conexão com o banco de dados
        db = conectar_banco()
        #Entra na coleção de imoveis do banco de dados
        colecao = db['imoveis']

        #Busca um imóvel específico no banco de dados usando o ID fornecido como parâmetro na URL. 
        imovel = colecao.find_one({"_id": ObjectId(id)})

        #Converte o campo _id de ObjectId para string para facilitar a leitura e o manuseio dos dados.
        if imovel:
            imovel["_id"] = str(imovel["_id"])

        #retorna o resultado
        return imovel
    
    except Exception as e:
        #Imprime o erro ocorrido durante o processo de inserção do imóvel no banco de dados para depuração e retorna uma mensagem de erro como resposta da API.
        print(f"erro: {e}")
        return {"erro": str(e)}

# metodo post para adicionar um novo imovel
@app.post("/gerenciar-bens/imoveis/adicionar-imovel/")
def cadastrar_bem_imovel(endereco,numero,estado,cidade,qtde_comodos,metros_quadrados):

    #cria um dicionario para armazenar as informações do imóvel para ser cadastrado.
    imovel = {
        'endereco':endereco,
        'numero':numero,
        'estado':estado,
        'cidade':cidade,
        'qtde_comodos':qtde_comodos,
        'metros_quadrados':metros_quadrados
    }

    try:
        #cria a conexão com o banco de dados
        db = conectar_banco()
        #Entra na coleção de imoveis do banco de dados
        colecao = db['imoveis']
        #Realiza a inserção do imóvel no banco de dados
        colecao.insert_one(imovel)
        #Imprime as informações do imóvel cadastrado para depuração e confirmação de que o processo foi concluído com sucesso.
        print(f"Imovel inserido:"
                    f"Endereço: {imovel[endereco]}\n" 
                    f"Numero:{imovel[numero]}\n" 
                    f"Estado: {imovel[estado]}\n" 
                    f"Cidade: {imovel[cidade]}\n" 
                    f"Comodos: {imovel[qtde_comodos]}\n"
                    f"m³: {imovel[metros_quadrados]}")
        
    except Exception as e:
        #Imprime o erro ocorrido durante o processo de inserção do imóvel no banco de dados para depuração e retorna uma mensagem de erro como resposta da API.
        print(f"erro: {e}")
        return {"erro": str(e)} 
    
  

