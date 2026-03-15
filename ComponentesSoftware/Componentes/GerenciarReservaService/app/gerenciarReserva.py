from time import strptime
from typing import Optional
from fastapi import FastAPI, HTTPException
from conexao.conexao_mongo import conn
import requests
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

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
################################## RESERVA IMOVEL #########################################################
@app.post("/gerenciar-reserva/reservar-imovel/")
def reservar_imovel(cpf_cliente, nome_cliente, id_imovel, data_inicio, data_fim):

    try:
        ###########################  CONEXÃO  ######################################
        #Conecta ao Banco de dados
        db = conectar_banco()
        #Entra na coleção de resevas do banco de dados
        colecao = db['reservasImovel']
        ###########################################################################    


        ######################### BUSCA OS DADOS VIA API ######################################
        # Realiza a o consumo das APIs de Gerenciamento de Bens e Clientes para obter as informações necessárias para realizar a reserva.
        url1 = f"http://gerenciarbens_api/gerenciar-bens/imoveis/{id_imovel}/"
        # url2 = f"http://clientes_api/cliente/id/{id_cliente}/"

        #Captura o response da API de Gerenciamento de Bens e imprime o status code e o conteúdo da resposta para depuração.
        response1 = requests.get(url1)
        print(f"Status Code URL1: {response1.status_code}")
        print(f"Response URL1: {response1.json()}")
        #Verifica o codigo para garantir que a resposta foi bem sucessida
        if response1.status_code != 200:
            raise HTTPException(status_code=404, detail="Imóvel não encontrado")

        #Captura o response da API de Clientes e imprime o status code e o conteúdo da resposta para depuração.
        # response2 = requests.get(url2)
        # print(f"Status Code URL2: {response2.status_code}")
        # print(f"Response URL2: {response2.json()}")
        
        # #Verifica o codigo para garantir que a resposta foi bem sucessida
        # if response2.status_code != 200:
        #     raise HTTPException(status_code=404, detail="Cliente não encontrado")
        ####################################################################################################################

        
        ########################## VALIDAÇÃO DE CONFLITOS DE RESERVA  ######################################
        reservas_imovel_selecionado = colecao.find({"id_imovel": id_imovel})
        
        # Converte as datas recebidas do formulário para date
        data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d").date()
        data_fim = datetime.strptime(data_fim, "%Y-%m-%d").date()

        # verifica se as datas inseridas são validas, se a data de inicio é maior que a data de fim
        if data_inicio > data_fim:
            raise HTTPException(status_code=400, detail="A data de início não pode ser maior que a data de fim")
        
        # Verifica conflitos com reservas já existentes
        for reserva in reservas_imovel_selecionado:
            
            # transforma as datas das reservas existentes de string para date para facilitar a comparação com as novas datas recebidas do formulário.
            data_inicio_existente = datetime.strptime(reserva['data_inicio'], "%Y-%m-%d").date()
            data_fim_existente = datetime.strptime(reserva['data_fim'], "%Y-%m-%d").date()
            
            # print(f"Datas da reserva existente: {data_inicio_existente} a {data_fim_existente} / Datas da nova reserva: {data_inicio} a {data_fim}")
            # print(f"Tipo das datas: {type(data_inicio_existente)} e {type(data_fim_existente)} / Tipo das novas datas: {type(data_inicio)} e {type(data_fim)}")

            # valida se as datas da nova reserva se sobrepõem com as datas de reservas já existentes para o mesmo imóvel.
            if (data_inicio <= data_fim_existente and data_fim >= data_inicio_existente):
                # print("ENTROU NA VALIDAÇÃO DE CONFLITO")
                raise HTTPException(status_code=400, detail="O imóvel já está reservado para as datas selecionadas")
        ####################################################################################################################


        ################################# CRIA A RESERVA  #########################################################
        #Cria o JSON da reserva
        reserva = {
            'cpf': cpf_cliente,
            'nome_cliente': nome_cliente,
            'id_imovel': response1.json().get('_id'),
            'endereco_imovel': response1.json().get('endereco'),
            'data_inicio': data_inicio.strftime("%Y-%m-%d"),
            'data_fim': data_fim.strftime("%Y-%m-%d")
        }
        
        #Realiza a inserção da reserva no banco de dados
        reservaResult = colecao.insert_one(reserva)
        
        return {"reserva_id": str(reservaResult.inserted_id), "message": "Reserva realizada com sucesso!"}
        ###################################################################################################
    except Exception as e:
        #Imprime o erro ocorrido durante o processo de reserva para depuração e retorna uma mensagem de erro como resposta da API.
        print(f"Erro ao realizar reserva: {e}")
        return {"error": str(e)}
    
########################################## RESERVA VEICULO #########################################################

@app.post("/gerenciar-reserva/reservar-veiculo/")
def reservar_veiculo(cpf_cliente,nome_cliente, id_veiculo, data_inicio, data_fim):

    try:
        ###########################  CONEXÃO  ######################################
        #Conecta ao Banco de dados
        db = conectar_banco()
        #Entra na coleção de resevas do banco de dados
        colecao = db['reservasVeiculo']
        ###########################################################################    


        ######################### BUSCA OS DADOS VIA API ######################################
        # Realiza a o consumo das APIs de Gerenciamento de Bens e Clientes para obter as informações necessárias para realizar a reserva.
        url1 = f"http://gerenciarbens_api/gerenciar-bens/veiculos/{id_veiculo}/"
        # url2 = f"http://clientes_api/cliente/id/{id_cliente}/"

        #Captura o response da API de Gerenciamento de Bens e imprime o status code e o conteúdo da resposta para depuração.
        response1 = requests.get(url1)
        print(f"Status Code URL1: {response1.status_code}")
        print(f"Response URL1: {response1.json()}")
        #Verifica o codigo para garantir que a resposta foi bem sucessida
        if response1.status_code != 200:
            raise HTTPException(status_code=404, detail="Veículo não encontrado")

        #Captura o response da API de Clientes e imprime o status code e o conteúdo da resposta para depuração.
        # response2 = requests.get(url2)
        # print(f"Status Code URL2: {response2.status_code}")
        # print(f"Response URL2: {response2.json()}")
        
        # #Verifica o codigo para garantir que a resposta foi bem sucessida
        # if response2.status_code != 200:
        #     raise HTTPException(status_code=404, detail="Cliente não encontrado")
        ####################################################################################################################

        
        ########################## VALIDAÇÃO DE CONFLITOS DE RESERVA  ######################################
        reservas_veiculo_selecionado = colecao.find({"id_veiculo": id_veiculo})
        
        # Converte as datas recebidas do formulário para date
        data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d").date()
        data_fim = datetime.strptime(data_fim, "%Y-%m-%d").date()

        # verifica se as datas inseridas são validas, se a data de inicio é maior que a data de fim
        if data_inicio > data_fim:
            raise HTTPException(status_code=400, detail="A data de início não pode ser maior que a data de fim")
        
        # Verifica conflitos com reservas já existentes
        for reserva in reservas_veiculo_selecionado:
            
            # transforma as datas das reservas existentes de string para date para facilitar a comparação com as novas datas recebidas do formulário.
            data_inicio_existente = datetime.strptime(reserva['data_inicio'], "%Y-%m-%d").date()
            data_fim_existente = datetime.strptime(reserva['data_fim'], "%Y-%m-%d").date()
            
            # print(f"Datas da reserva existente: {data_inicio_existente} a {data_fim_existente} / Datas da nova reserva: {data_inicio} a {data_fim}")
            # print(f"Tipo das datas: {type(data_inicio_existente)} e {type(data_fim_existente)} / Tipo das novas datas: {type(data_inicio)} e {type(data_fim)}")

            # valida se as datas da nova reserva se sobrepõem com as datas de reservas já existentes para o mesmo veículo.
            if (data_inicio <= data_fim_existente and data_fim >= data_inicio_existente):
                # print("ENTROU NA VALIDAÇÃO DE CONFLITO")
                raise HTTPException(status_code=400, detail="O veículo já está reservado para as datas selecionadas")
        ####################################################################################################################


        ################################# CRIA A RESERVA  #########################################################
        #Cria o JSON da reserva
        reserva = {
            'cpf': cpf_cliente,
            'nome_cliente': nome_cliente,
            'id_veiculo': response1.json().get('_id'),
            'endereco_veiculo': response1.json().get('endereco'),
            'data_inicio': data_inicio.strftime("%Y-%m-%d"),
            'data_fim': data_fim.strftime("%Y-%m-%d")
        }
        
        #Realiza a inserção da reserva no banco de dados
        reservaResult = colecao.insert_one(reserva)
        
        return {"reserva_id": str(reservaResult.inserted_id), "message": "Reserva realizada com sucesso!"}
        ###################################################################################################
    except Exception as e:
        #Imprime o erro ocorrido durante o processo de reserva para depuração e retorna uma mensagem de erro como resposta da API.
        print(f"Erro ao realizar reserva: {e}")
        return {"error": str(e)}