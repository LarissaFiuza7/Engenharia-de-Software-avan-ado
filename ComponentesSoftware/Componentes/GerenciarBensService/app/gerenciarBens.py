from typing import Optional

from bson import ObjectId
from fastapi import FastAPI
from pydantic import BaseModel
from conexao.conexao_mongo import conn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # em produção, coloque só o domínio do front
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Facilita a conexão com o banco de dados, evitando repetição de código em cada endpoint. 
# Se as credenciais ou o nome do banco de dados mudarem, basta atualizar esta função, e todas as partes do código que a utilizam serão automaticamente atualizadas. 
# Isso torna o código mais limpo, organizado e fácil de manter.
def conectar_banco():
    return conn('Credenciais')
########################################## IMOVEIS #######################################################################################################

# metodo get para listar os imoveis disponiveis
@app.get("/gerenciar-bens/imoveis/")
def listar_imoveis():

    try:
        # cria conexão com banco de dados   
        db = conectar_banco()
        #Entra na coleção de imoveis do banco de dados
        colecao = db['imoveis']
        #Cria uma lista com os imoveis disponiveis
        imoveis = list(colecao.find())

        #Converte o campo _id de ObjectId para string para facilitar a leitura e o manuseio dos dados.
        for item in imoveis:
            item["_id"] = str(item["_id"])

        #retorna o resultado
        return imoveis
    
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
        imovel = list(colecao.find(filtro))

        #Converte o campo _id de ObjectId para string para facilitar a leitura e o manuseio dos dados.
        for item in imovel:
            item["_id"] = str(item["_id"])
        #retorna o resultado
        return imovel

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
def cadastrar_bem_imovel(cep,endereco,bairro,cidade,estado,numero,complemento,qtde_comodos,metros_quadrados,valor,proprietario):

    #cria um dicionario para armazenar as informações do imóvel para ser cadastrado.
    imovel = {
        'cep': cep,
        'endereco':endereco,
        'bairro': bairro,
        'cidade':cidade,
        'estado':estado,
        'numero':numero,
        'complemento':complemento,
        'comodos':qtde_comodos,
        'metros_quadrados':metros_quadrados,
        'valor':valor,
        'proprietario': proprietario
    }

    try:
        #cria a conexão com o banco de dados
        db = conectar_banco()
        #Entra na coleção de imoveis do banco de dados
        colecao = db['imoveis']
        #Realiza a inserção do imóvel no banco de dados
        colecao.insert_one(imovel)
        #Imprime as informações do imóvel cadastrado para depuração e confirmação de que o processo foi concluído com sucesso.
        return {"message": f"Imovel inserido:"
                    f"CEP: {imovel['cep']}\n"
                    f"Endereço: {imovel['endereco']}\n"
                    f"Bairro: {imovel['bairro']}\n"
                    f"Cidade: {imovel['cidade']}\n"
                    f"Estado: {imovel['estado']}\n"
                    f"Número: {imovel['numero']}\n"
                    f"Complemento: {imovel['complemento']}\n"
                    f"Cômodos: {imovel['comodos']}\n"
                    f"m²: {imovel['metros_quadrados']}\n"
                    f"Valor: {imovel['valor']}\n"
                    f"Proprietário: {imovel['proprietario']}\n"}
        
    except Exception as e:
        #Imprime o erro ocorrido durante o processo de inserção do imóvel no banco de dados para depuração e retorna uma mensagem de erro como resposta da API.
        print(f"erro: {e}")
        return {"erro": str(e)} 


########################################### VEICULOS #######################################################################################################


# metodo post para adicionar um novo veiculo
@app.post("/gerenciar-bens/veiculos/adicionar-veiculo/")
def cadastrar_bem_veiculo(marca,modelo,ano,valor,cep,endereco,bairro,cidade,estado,numero,proprietario):

    #cria um dicionario para armazenar as informações do veiculo para ser cadastrado.
    veiculo = {
        'marca': marca,
        'modelo': modelo,
        'ano': ano,
        'valor': valor,
        'cep': cep,
        'endereco':endereco,
        'bairro': bairro,
        'cidade':cidade,
        'estado':estado,
        'numero':numero,

        'proprietario': proprietario
    }

    try:
        #cria a conexão com o banco de dados
        db = conectar_banco()
        #Entra na coleção de veiculos do banco de dados
        colecao = db['veiculos']
        #Realiza a inserção do veiculo no banco de dados
        colecao.insert_one(veiculo)
        #Imprime as informações do veiculo cadastrado para depuração e confirmação de que o processo foi concluído com sucesso.
        return {"message": f"Veículo inserido:"
                    f"Marca: {veiculo['marca']}\n"
                    f"Modelo: {veiculo['modelo']}\n"
                    f"Ano: {veiculo['ano']}\n"
                    f"Valor: {veiculo['valor']}\n"
                    f"CEP: {veiculo['cep']}\n"
                    f"Endereço: {veiculo['endereco']}\n"
                    f"Bairro: {veiculo['bairro']}\n"
                    f"Cidade: {veiculo['cidade']}\n"
                    f"Estado: {veiculo['estado']}\n"
                    f"Número: {veiculo['numero']}\n"
                    f"Proprietário: {veiculo['proprietario']}\n"}
        
    except Exception as e:
        #Imprime o erro ocorrido durante o processo de inserção do imóvel no banco de dados para depuração e retorna uma mensagem de erro como resposta da API.
        print(f"erro: {e}")
        return {"erro": str(e)} 

# metodo get para listar os veiculos disponiveis
@app.get("/gerenciar-bens/veiculos/")
def listar_veiculos():

    try:
        # cria conexão com banco de dados   
        db = conectar_banco()
        #Entra na coleção de veiculos do banco de dados
        colecao = db['veiculos']
        #Cria uma lista com os veiculos disponiveis
        veiculos = list(colecao.find())

        #Converte o campo _id de ObjectId para string para facilitar a leitura e o manuseio dos dados.
        for item in veiculos:
            item["_id"] = str(item["_id"])

        #retorna o resultado
        return veiculos
    
    except Exception as e:
        #Imprime o erro ocorrido durante o processo de inserção do imóvel no banco de dados para depuração e retorna uma mensagem de erro como resposta da API.
        print(f"erro: {e}")
        return {"erro": str(e)} 


# metodo get para listar um veiculo especifico
@app.get("/gerenciar-bens/veiculos/{id}/")
def buscar_veiculo(id):

    try:
        #cria a conexão com o banco de dados
        db = conectar_banco()
        #Entra na coleção de veiculos do banco de dados
        colecao = db['veiculos']

        #Busca um veiculo específico no banco de dados usando o ID fornecido como parâmetro na URL. 
        veiculo = colecao.find_one({"_id": ObjectId(id)})

        #Converte o campo _id de ObjectId para string para facilitar a leitura e o manuseio dos dados.
        if veiculo:
            veiculo["_id"] = str(veiculo["_id"])

        #retorna o resultado
        return veiculo
    
    except Exception as e:
        #Imprime o erro ocorrido durante o processo de inserção do veiculo no banco de dados para depuração e retorna uma mensagem de erro como resposta da API.
        print(f"erro: {e}")
        return {"erro": str(e)}

# metodo get para listar os veiculos disponiveis com filtro
@app.get("/gerenciar-bens/veiculos/filtro/")
def listar_veiculos_filtrados(
                        cidade: Optional[str] = None,
                        estado: Optional[str] = None,
                        marca: Optional[str] = None,
                        modelo: Optional[str] = None,
                        ano: Optional[int] = None
                        ):
    
    #Cria um dicionário de filtro vazio para armazenar os critérios de filtragem com base nos parâmetros fornecidos na solicitação.
    filtro = {}

    # Verifica se cada parâmetro de filtro foi fornecido na solicitação e, se sim, adiciona o critério correspondente ao dicionário de filtro.
    if cidade:
            filtro['cidade'] = cidade
    if estado:
            filtro['estado'] = estado   
    if marca:
            filtro['marca'] = marca
    if modelo:
            filtro['modelo'] = modelo
    if ano:
            filtro['ano'] = ano

    try:
        #cria a conexão com o banco de dados
        db = conectar_banco()
        #Entra na coleção de veiculos do banco de dados
        colecao = db['veiculos']

        #Cria uma lista com os veiculos disponiveis de acordo com o filtro aplicado
        veiculo = list(colecao.find(filtro))

        #Converte o campo _id de ObjectId para string para facilitar a leitura e o manuseio dos dados.
        for item in veiculo:
            item["_id"] = str(item["_id"])
        #retorna o resultado
        return veiculo

    except Exception as e:
        #Imprime o erro ocorrido durante o processo de inserção do veiculo no banco de dados para depuração e retorna uma mensagem de erro como resposta da API.
        print(f"erro: {e}")
        return {"erro": str(e)}