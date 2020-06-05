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

    def registroMasivo(self, pedidos):
        self.cursor.executemany(sql, pedidos)
        self.db.commit()

    def mostrar(self, sql, parametro=None):
        self.cursor.execute(sql, parametro)
        tabla = self.cursor.fetchall()
        for dato in tabla:
            print(dato)

    def mostrarLibro(self, sql, parametro=None):
        self.cursor.execute(sql, parametro)
        tabla = self.cursor.fetchone()
        print("""
            TITTULO : {0}
            AUTOR : {1} -- CATEGORIA : {2}
            ISBN : {3} --  PAGINAS: {4}
            EDITORIAL : {5}
            DISPONIBILIDAD : {6}
        """.format(
            tabla[0], tabla[1], tabla[2],
            tabla[3], tabla[4], tabla[5],
            tabla[6]
            ))


