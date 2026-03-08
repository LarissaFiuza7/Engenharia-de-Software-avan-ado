from fastapi import FastAPI
from pydantic import BaseModel
from conexao.conexao_mongo import conn

app = FastAPI()

@app.get("/cliente/")
def get_clientes():
    db = conn("Inserir as credenciais")
    colecao = db['clientes']
    dados = list(colecao.find())

    for item in dados:
        item["_id"] = str(item["_id"])
    return dados


@app.post("/cliente/cadastrar-cliente/")
def post_cliente(nome,cpf,email,senha,data_nascimento,numero_telefone,cep,endereco,numero_endereco,estado):
    cliente = {
        'nome_completo':nome,
        'cpf':cpf,
        'email': email,
        'senha': senha,
        'data_nascimento':data_nascimento,
        'numero_telefone': numero_telefone,
        'cep':cep,
        'endereco':endereco,
        'numero_endereco':numero_endereco,
        'estado': estado
        
    }
    try:
        db = conn("Inserir as credenciais")
        colecao = db['clientes']
        colecao.insert_one(cliente)

        print(f"Cliente inserido:"
                    f"Nome: {cliente[nome]}\n" 
                    f"CPF: {cliente[cpf]}\n"
                    f"Email: {cliente[email]}\n"
                    f"Senha: {cliente[senha]}\n"
                    f"Data de Nascimento: {cliente[data_nascimento]}\n"
                    f"Telefone: {cliente[numero_telefone]}\n"
                    f"CEP: {cliente[cep]}\n"
                    f"Endereço: {cliente[endereco]}\n"
                    f"Número do Endereço: {cliente[numero_endereco]}\n"
                    f"Estado: {cliente[estado]}\n"
                    )
                   
    except Exception as e:
        print(f"erro: {e}")
        return {"erro": str(e)} 