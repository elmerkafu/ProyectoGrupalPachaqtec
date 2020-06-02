from pymongo import MongoClient, errors


class Conexion:

    def __init__(self, url, database):
        self.client = MongoClient(url)
        self.db = self.client[database]
    
    def insertarRegistro(self, collection, data):
        collection = self.db[collection]
        result = collection.insert_one(data)  

    def mostrarRegistros(self, collection, condicion={}):
        collection = self.db[collection]
        data = collection.find(condicion)
        for datos in data:
            print(datos)

    def actualizarRegistros(self, collection, condicion, change):
        collection = self.db[collection]
        collection.update_one(condicion, {
            '$set': change
        })
        print(f'Actualizacion Correcta')

    def eliminarRegistros(self, collection, condicion):
        collection = self.db[collection]
        collection.delete_one(condicion)
        print(f'Registro Eliminado')
