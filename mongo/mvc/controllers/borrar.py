import web
import app
import ssl
import pymongo
from pymongo import MongoClient
render = web.template.render("mongo/views/")
class Delete:
    def GET(self):
        client = MongoClient(
          "mongodb://MarlenCL:carmona12345@proyecto1-shard-00-00.vtyw4.mongodb.net:27017,proyecto1-shard-00-01.vtyw4.mongodb.net:27017,proyecto1-shard-00-02.vtyw4.mongodb.net:27017/<Proyecto1>?ssl=true&replicaSet=atlas-9tnhx7-shard-0&authSource=admin&retryWrites=true&w=majority")
        db = client.get_database('Eliminar')
        Alumnos_collection=db.Alumnos
        contenedor=list(Alumnos_collection.find())
        tam=Alumnos_collection.count()
        return render.delete(contenedor,tam)
    def POST(self):
        print("entrando a metdo form POST")
        try:
            valor_borrar=web.input()
            print("el id a borrar es")
            print(valor_borrar)
            client = MongoClient("mongodb://MarlenCL:carmona12345@proyecto1-shard-00-00.vtyw4.mongodb.net:27017,proyecto1-shard-00-01.vtyw4.mongodb.net:27017,proyecto1-shard-00-02.vtyw4.mongodb.net:27017/<Eliminar>?ssl=true&replicaSet=atlas-9tnhx7-shard-0&authSource=admin&retryWrites=true&w=majority")
            db = client.get_database('Eliminar')
            Alumnos_collection=db.Alumnos
            print("antes de borrar hay:")
            contador=Alumnos_collection.count()
            print(contador)
            borrar=valor_borrar.borrar
            print(borrar)
            Alumnos_collection.delete_one({'_id':str(borrar)})
            contenedor=list(Alumnos_collection.find())
            tam=Alumnos_collection.count()
            print("despues de borrar hay:")
            print(tam)
            return render.delete(contenedor,tam)
        except Exception as error:
            return "Error" +str(error)
