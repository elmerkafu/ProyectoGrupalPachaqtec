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

    def registroMasivo(self, sql, pedidos):
        self.cursor.executemany(sql, pedidos)
        self.db.commit()

    def mostrar(self, sql, parametro=None):
        self.cursor.execute(sql, parametro)
        tabla = self.cursor.fetchall()
        for dato in tabla:
            print(dato)

    def obtener_registro(self, sql, parametro=None):
        respuesta = None
        try:
            self.cursor.execute(sql, parametro)
            respuesta = self.cursor.fetchone()
        except Exception as e:
            print("La obtencion de registro fallo")
            print(e)
        return respuesta

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


class ConexionEditorial(Conexion):

    def insertar(self, nom_ed, pais_ed, telefono_ed):
        insercion_realizada = False
        informacion_adicional = "Problema de insercion"
        if self._comprobar_existencia(nom_ed, pais_ed, telefono_ed) is None:
            super().consultas(
                "insert into editorial(nom_ed, pais_ed, telefono_ed) values(%s, %s, %s);",
                (nom_ed, pais_ed, telefono_ed)
            )
            insercion_realizada = True
        else:
            informacion_adicional = "El registro ya existe"
        return (insercion_realizada, informacion_adicional)
        

    def _comprobar_existencia(self, nom_ed, pais_ed, telefono_ed):
        return super().obtener_registro(
            "SELECT * FROM editorial WHERE nom_ed=%s AND pais_ed=%s AND telefono_ed=%s;",
            (nom_ed, pais_ed, telefono_ed)
        )

    def mostrar(self):
        respuesta = []
        sql = "SELECT * FROM editorial"
        self.cursor.execute(sql)
        registros = self.cursor.fetchall()
        for registro in registros:
            respuesta.append(
                Editorial(
                    registro[1],
                    registro[2],
                    registro[3],
                    registro[0]
                )
            )
        return respuesta

class ConexionTipoLibro(Conexion):

    def insertar(self, nombre_tipo):
        super().consultas(
            "INSERT INTO tipo_libro(nombre_tipo) VALUES (%s)",
            (nombre_tipo,)
        )

    def mostrar(self):
        respuesta = []
        sql = "SELECT * FROM tipo_libro"
        self.cursor.execute(sql)
        registros = self.cursor.fetchall()
        for registro in registros:
            respuesta.append(
                Tipo_libro(
                    registro[1],
                    registro[0]
                )
            )
        return respuesta

class ConexionLibro(Conexion):

    def insertar(self, titulo, autor, id_ed, isbn, paginas, id_tipo_libro, disponible):
        super().consultas(
            """
            insert into libro(
            titulo, autor, id_ed, isbn, paginas, id_tipo_libro, disponible
            ) values(%s, %s, %s, %s, %s, %s, %s)
            """,(titulo, autor, id_ed, isbn, paginas, id_tipo_libro, disponible)
        )

    def mostrar(self):
        respuesta = []
        sql = "SELECT * FROM libro"
        self.cursor.execute(sql)
        registros = self.cursor.fetchall()
        for registro in registros:
            respuesta.append(
                Libro(
                    registro[1],
                    registro[2],
                    registro[3],
                    registro[4],
                    registro[5],
                    registro[6],
                    registro[7],
                    registro[0]
                )
            )
        return respuesta

class ConexionUsuario(Conexion):

    def insertar(self, nombre, apellido, dni, pwd):
        super().consultas("""
         insert into usuarios(
            nombre, apellido, dni, pwd
        ) values (%s, %s, %s, %s)                   
        """,(nombre, apellido, dni, pwd)
        ) 

class ConexionPrestamos(Conexion):

    def insertarPrestamo(self, id_usuario, id_libro, fecha_devolucion):

        super().consultas("""
        insert into prestamos(
            id_usuario, id_libro, 
            fecha_prestamo, fecha_devolucion
        ) values(%s, %s, current_date , %s)                   
        """,(id_usuario, id_libro, fecha_devolucion)
        )

        super().consultas("""
        update libro set disponible = 'no-disponible' where id_libro = %s
        and disponible = 'disponible'
        """,(id_libro,)
        )

    def insertarDevolucion(self, id_usuario, id_libro):

        super().consultas("""
        insert into prestamos(
            id_usuario, id_libro,
            fecha_prestamo, fecha_devolucion 
        ) values(%s, %s, current_date, current_date)
        """,(id_usuario, id_libro)
        )

        super().consultas("""
        update libro set disponible = 'disponible' where id_libro = %s
        and disponible = 'no-disponible'
        """,(id_libro,)
        )

    def mostrar(self):
            respuesta = []
            sql = """
                SELECT titulo, autor, tipo_libro, isbn, paginas, nom_ed, disponible FROM libro 
                INNER JOIN editorial ON libro.id_ed = editorial.id_ed
                INNER JOIN tipo_libro ON libro.id_tipo_libro = tipo_libro.id_tipo_libro
                WHERE id_libro = '{0}'
            """.format(id_libro)
            self.cursor.execute(sql)
            registros = self.cursor.fetchall()
            for registro in registros:
                respuesta.append(
                    Prestamos(
                        registro[0],
                        registro[1],
                        registro[2],
                        registro[3],
                        registro[4],
                        registro[5],
                        registro[6]
                    )
                )
            return respuesta

##SECCION IMPRIMIR EN PANTALLA

class Prestamos:

    def __init__(
        self, titulo, autor, tipo_libro, isbn, 
        paginas, nom_ed, disponible
    ):
        self.titulo = titulo
        self.autor = autor
        self.tipo_libro = tipo_libro
        self.isbn = isbn
        self.paginas = paginas
        self.nom_ed = nom_ed
        self.disponible = disponible

    def __str__(self):
        return (
            f" TITULO : {self.titulo}\n"
            f" AUTOR: {self.autor}\n"
            f" CATEGORIA: {self.tipo_libro}\n"
            f" ISBN : {self.isbn}\n"
            f" PAGINAS : {self.paginas}\n"
            f" EDITORIAL : {self.nom_ed}\n"
            f" DISPONIBILIDAD  : {self.disponible}\n"
        )


class Libro:

    def __init__(
        self, titulo, autor, id_ed, isbn, 
        paginas, id_tipo_libro, disponible, libro_id=None
    ):
        self.titulo = titulo
        self.autor = autor
        self.id_ed = id_ed
        self.isbn = isbn
        self.paginas = paginas
        self.id_tipo_libro = id_tipo_libro
        self.disponible = disponible
        self.libro_id = libro_id

    def __str__(self):
        return (
            f"ID LIBRO: {self.libro_id}\n"
            f" TITULO : {self.titulo}\n"
            f" AUTOR: {self.autor}\n"
            f" ID EDITORIAL: {self.id_ed}\n"
            f" ISBN : {self.isbn}\n"
            f" PAGINAS : {self.paginas}\n"
            f" CATEGORIA : {self.id_tipo_libro}\n"
            f" DISPONIBILIDAD  : {self.disponible}\n"
        )

class Tipo_libro:

    def __init__(self, nombre, tipo_libro_id=None):
        self.nombre = nombre
        self.tipo_libro_id = tipo_libro_id

    def __str__(self):
        return (
            f"ID Editorial: {self.tipo_libro_id}\n"
            f"Nombre Editorial: {self.nombre}\n"
        )

class Editorial:

    def __init__(self, nombre, pais, telefono, editorial_id=None):
        self.nombre = nombre
        self.pais = pais
        self.telefono = telefono
        self.editorial_id = editorial_id

    def __str__(self):
        return (
            f"ID Editorial: {self.editorial_id}\n"
            f"Nombre Editorial: {self.nombre}\n"
            f"Pais Editorial: {self.pais}\n"
            f"Telefono Editorial: {self.telefono}\n"
        )