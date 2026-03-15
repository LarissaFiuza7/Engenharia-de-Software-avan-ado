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
    
# metodo onde lista todos os clientes cadastrados no banco de dados
@app.get("/cliente/")
def get_clientes():

    try:    
        #conecta ao banco de dados  
        db = conectar_banco()
        #Entra na coleção de clientes do banco de dados
        colecao = db['clientes']
        #cria uma lista com a resposta da consulta ao banco de dados
        clientes = list(colecao.find())

        #transforma o campo _id de ObjectId para string para facilitar a leitura e o manuseio dos dados.
        for item in clientes:
            item["_id"] = str(item["_id"])
        #retorna o resultado
        return clientes

    except Exception as e:
        #Imprime o erro ocorrido durante o processo de inserção do imóvel no banco de dados para depuração e retorna uma mensagem de erro como resposta da API.
        print(f"erro: {e}")
        return {"erro": str(e)}
    
@app.get("/cliente/login/")
def login_cliente(email, senha):

    try:
        #conecta com o banco de dados
        db = conectar_banco()
        #Entra na coleção de clientes do banco de dados
        colecao = db['clientes']
        #Busca um cliente específico no banco de dados usando o email e senha fornecidos como parâmetro na URL.
        cliente = colecao.find_one({"email": email, "senha": senha})

        #Converte o campo _id de ObjectId para string, caso o cliente exista para facilitar a leitura e o manuseio dos dados.
        if not cliente:
            return {"error": "Email ou senha inválidos"}

        cliente["_id"] = str(cliente["_id"])
        #retorna o resultado
        print(f"Login bem sucedido para o cliente: {cliente['nome_completo']}")
        return cliente
    except Exception as e:
        #Imprime o erro ocorrido durante o processo de inserção do imóvel no banco de dados para depuração e retorna uma mensagem de erro como resposta da API.
        print(f"erro: {e}")
        return {"erro": str(e)}  
    
#metodo para buscar um cliente especifico pelo id, onde o id é passado como parametro na url
@app.get("/cliente/id/{id_cliente}/")
def get_cliente(id_cliente: str):

    try:
        if not ObjectId.is_valid(id_cliente):
            return {"error": "ID de cliente inválido"}
        #conecta com o banco de dados
        db = conectar_banco()
        #Entra na coleção de clientes do banco de dados
        colecao = db['clientes']
        #Busca um cliente específico no banco de dados usando o ID fornecido como parâmetro na URL.
        cliente = colecao.find_one({"_id": ObjectId(id_cliente)})

        #Converte o campo _id de ObjectId para string para facilitar a leitura e o manuseio dos dados.
        if cliente:
            cliente["_id"] = str(cliente["_id"])
        #retorna o resultado
        return cliente

    except Exception as e:
        #Imprime o erro ocorrido durante o processo de inserção do imóvel no banco de dados para depuração e retorna uma mensagem de erro como resposta da API.
        print(f"erro: {e}")
        return {"erro": str(e)}

# metodo para cadastrar um cliente
@app.post("/cliente/cadastrar-cliente/")
def post_cliente(nome,cpf,email,senha,data_nascimento,numero_telefone):

    #cria um dicionário para armazenar as informações do cliente para ser cadastrado.
    cliente = {
        'nome_completo':nome,
        'cpf':cpf,
        'email': email,
        'senha': senha,
        'data_nascimento':data_nascimento,
        'numero_telefone': numero_telefone
    }

    try:
        #conecta com o banco de dados
        db = conectar_banco()
        #Entra na coleção de clientes do banco de dados
        colecao = db['clientes']
        #cria uma lista com a resposta da consulta ao banco de dados
        dados = list(colecao.find())
        #Valida se CPF ou email ja estão cadastrados
        for item in dados:
            if item['cpf'] == cpf:
                return {"error": "CPF já cadastrado"}
            if item['email'] == email:
                return {"error": "Email já cadastrado"}
            
        #Realiza a inserção do cliente no banco de dados
        colecao.insert_one(cliente)

        #Imprime as informações do cliente cadastrado para depuração e confirmação de que o processo foi concluído com sucesso.
        return {"message": f"Cliente inserido:"
                    f"Nome: {cliente['nome_completo']}\n" 
                    f"CPF: {cliente['cpf']}\n"
                    f"Email: {cliente['email']}\n"
                    f"Senha: {cliente['senha']}\n"
                    f"Data de Nascimento: {cliente['data_nascimento']}\n"
                    f"Telefone: {cliente['numero_telefone']}"
        }
                  
    except Exception as e:
        #Imprime o erro ocorrido durante o processo de inserção do imóvel no banco de dados para depuração e retorna uma mensagem de erro como resposta da API.
        print(f"erro: {e}")
        return {"erro": str(e)} 