from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# minhas credenciais ('manager_componet', '987321','componentsoftware','ComponentClientes','urkfjzm.mongodb.net')

# metodo para realizar a conexão com banco de dados
def conn(usuario,senha, banco_de_dados,componente,tag):

    #URI de conexão com mongoDB
    uri = f"mongodb+srv://{usuario}:{senha}@{banco_de_dados}.{tag}/{componente}?appName={banco_de_dados}"
    client = MongoClient(uri, server_api=ServerApi("1"))
    
    try:
        client.admin.command("ping")
        print("Conectado ao MongoDB!")
        return client[componente]
    except Exception as e:
        print(f"Erro ao conectar no MongoDB: {e}")
        raise

