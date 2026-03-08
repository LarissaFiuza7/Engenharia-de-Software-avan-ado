from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def conn(usuario,senha, banco_de_dados,componente,tag):
    
    uri = f"mongodb+srv://{usuario}:{senha}@{banco_de_dados}.{tag}/{componente}?appName={banco_de_dados}"

    client = MongoClient(uri, server_api=ServerApi("1"))

    try:
        client.admin.command("ping")
        print("Conectado ao MongoDB!")
        return client[componente]
    except Exception as e:
        print(f"Erro ao conectar no MongoDB: {e}")
        raise

