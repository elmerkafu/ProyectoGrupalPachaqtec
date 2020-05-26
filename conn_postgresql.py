import psycopg2
import psycopg2.extensions


class Conexion:

    def __init__(self, server, user, password, database):
        self.db = psycopg2.connect(
            host=server, user=user, password=password, database=database
        )
        self.cursor = self.db.cursor()

    def __del__(self):
        self.cerrar_conexion()

    def cerrar_conexion(self):
        self.db.close()

    def registros(self, sql, parametro=None):
        self.cursor.execute(sql, parametro)
        self.db.commit()

    def registro_libros(self, pedidos):
        self.cursor.executemany(
            "INSERT INTO compras(cont, idproducto, cantidad) VALUES ('%s', '%s','%s')",
            pedidos
        )
        self.db.commit()
