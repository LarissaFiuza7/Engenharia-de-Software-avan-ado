from typing import Optional
from fastapi import FastAPI
from conexao.conexao_mongo import conn
import requests

app = FastAPI()

# Facilita a conexão com o banco de dados, evitando repetição de código em cada endpoint. 
# Se as credenciais ou o nome do banco de dados mudarem, basta atualizar esta função, e todas as partes do código que a utilizam serão automaticamente atualizadas. 
# Isso torna o código mais limpo, organizado e fácil de manter.
def conectar_banco():
    return conn('Suas Credenciais')

@app.post("/gerenciar-reserva/reservar-imovel/")
def reservar_imovel(id_cliente, id_imovel, data_inicio, data_fim):

    try:
        #Conecta ao Banco de dados
        db = conectar_banco()

        # Realiza a o consumo das APIs de Gerenciamento de Bens e Clientes para obter as informações necessárias para realizar a reserva.
        url1 = f"http://gerenciarbens_api/gerenciar-bens/imoveis/{id_imovel}"
        url2 = f"http://clientes_api/cliente/{id_cliente}"

        #Captura o response da API de Gerenciamento de Bens e imprime o status code e o conteúdo da resposta para depuração.
        response1 = requests.get(url1)
        print(f"Status Code URL1: {response1.status_code}")
        print(f"Response URL1: {response1.json()}")
        #Verifica o codigo para garantir que a resposta foi bem sucessida
        if response1.status_code != 200:
            return {"error": "Imóvel não encontrado"}

        #Captura o response da API de Clientes e imprime o status code e o conteúdo da resposta para depuração.
        response2 = requests.get(url2)
        print(f"Status Code URL2: {response2.status_code}")
        print(f"Response URL2: {response2.json()}")

        #Verifica o codigo para garantir que a resposta foi bem sucessida
        if response2.status_code != 200:
            return {"error": "Cliente não encontrado"}

        #Entra na coleção de resevas do banco de dados
        colecao = db['reservas']
        
        #Cria o JSON da reserva
        reserva = {
            'cpf': response2.json().get('cpf'),
            'nome_cliente': response2.json().get('nome_completo'),
            'id_imovel': response1.json().get('_id'),
            'endereco_imovel': response1.json().get('endereco'),
            'data_inicio': data_inicio,
            'data_fim': data_fim
        }
        
        #Realiza a inserção da reserva no banco de dados
        reservaResult = colecao.insert_one(reserva)
        
        return {"reserva_id": str(reservaResult.inserted_id), "message": "Reserva realizada com sucesso!"}
    
    except Exception as e:
        #Imprime o erro ocorrido durante o processo de reserva para depuração e retorna uma mensagem de erro como resposta da API.
        print(f"Erro ao realizar reserva: {e}")
        return {"error": str(e)}