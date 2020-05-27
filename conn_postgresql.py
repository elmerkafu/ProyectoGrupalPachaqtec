import psycopg2


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

    def consultas(self, sql, parametro=None):
        self.cursor.execute(sql, parametro)
        self.db.commit()

    def mostrar(self, sql, parametro=None):
        self.cursor.execute(sql, parametro)
        tabla = self.cursor.fetchall()
        for dato in tabla:
            self.id_editorial == dato[0]
            self.nom_ed == dato[1]
            self.pais_ed == dato[2]
            self.telefono_ed == dato[3]

    def registroEditorial(self, pedidos):
        self.cursor.executemany(
            "INSERT INTO compras(cont, idproducto, cantidad) VALUES ('%s', '%s','%s')",
            pedidos
        )
        self.db.commit()
