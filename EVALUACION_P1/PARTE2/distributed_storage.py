from pymongo import MongoClient
import random

class DistributedStorage:
    def __init__(self):
        # Conectar a dos instancias de MongoDB con chequeo de conexión
        self.clients = []
        self.dbs = []
        self.collections = []
        puertos = [27017, 27018]
        for i, puerto in enumerate(puertos):
            try:
                uri = f'mongodb://localhost:{puerto}/'
                client = MongoClient(uri, serverSelectionTimeoutMS=3000)
                client.server_info()  # Prueba la conexión
                print(f"Conexión exitosa a MongoDB nodo {i+1} en puerto {puerto}")
                self.clients.append(client)
                db = client['distributed_db']
                self.dbs.append(db)
                self.collections.append(db['documents'])
            except Exception as e:
                print(f"Error al conectar a MongoDB nodo {i+1} en puerto {puerto}: {e}")

    def insert_document(self, data):
        """Inserta documento distribuyéndolo entre nodos (round robin simple)"""
        # Selecciona el nodo según el id o aleatorio
        node = random.choice(self.collections)
        result = node.insert_one(data)
        return result.inserted_id

    def find_document(self, document_id):
        """Busca documento en todos los nodos"""
        for collection in self.collections:
            doc = collection.find_one({'_id': document_id})
            if doc:
                return doc
        return None

    def get_stats(self):
        """Obtiene estadísticas de distribución"""
        stats = {}
        for i, collection in enumerate(self.collections):
            stats[f'nodo_{i+1}'] = collection.count_documents({})
        return stats

if __name__ == "__main__":
    ds = DistributedStorage()
    # Limpiar las colecciones antes de insertar para evitar duplicados
    for collection in ds.collections:
        collection.delete_many({})
    # Generar 100 documentos de ejemplo
    for i in range(100):
        doc = {'_id': f'doc_{i}', 'valor': random.randint(1, 100)}
        ds.insert_document(doc)
    print("Estadísticas de distribución:", ds.get_stats())
    # Buscar un documento
    print("Buscar doc_42:", ds.find_document('doc_42'))
