from modelos.model_postgresql import Conexion


DATOS_CONEXION = {
    'server': 'localhost',
    'user': 'postgres',
    'password': '199705',
    'database': 'biblioteca'
}

class ControladorEditorial:

    @staticmethod      
    def controladorRegistro(nom_ed, pais_ed, telefono_ed):
        Conexion(**DATOS_CONEXION).consultas("""
        insert into editorial(nom_ed, pais_ed, telefono_ed) values('{0}', '{1}', '{2}');
        """.format(nom_ed, pais_ed, telefono_ed))

    @staticmethod
    def controladorMostrar(parametro=None):
        tabla = Conexion(**DATOS_CONEXION).mostrar("""
        SELECT * FROM editorial   
        """)
    
class ControladorTipoLibro:

    @staticmethod
    def controladorRegistro(nombre_tipo):
        Conexion(**DATOS_CONEXION).consultas("""
        insert into tipo_libro(nombre_tipo) values('{0}')
        """.format(nombre_tipo))

    @staticmethod
    def controladorMostrar(parametro = None):
        tabla = Conexion(**DATOS_CONEXION).mostrar("""
        SELECT * FROM tipo_libro   
        """)

class ControladorLibro:

    @staticmethod
    def controladorRegistro(
        titulo, autor, id_ed, isbn, paginas, id_tipo_libro, disponible
    ):
        Conexion(**DATOS_CONEXION).consultas("""
        insert into libro(
            titulo, autor, id_ed, isbn, paginas, id_tipo_libro, disponible
            ) values(
                {0}, {1}, {2}, {3}, {4}, {5}
            )
        """.format(
            titulo, autor, id_ed, isbn, paginas, id_tipo_libro, disponible
        ))
        
    @staticmethod
    def controladorMostrar(parametro=None):
        tabla = Conexion(**DATOS_CONEXION).mostrar("""
        SELECT * FROM libro   
        """)

class ControladorUsusario:

    @staticmethod
    def controladorRegistro(nombre, apellido, dni, pwd):
        Conexion(**DATOS_CONEXION).consultas("""
        insert into usuarios(
            nombre, apellido, dni, pwd
        ) values ('{0}','{1}','{2}','{3}')
        """.format(nombre, apellido, dni, pwd))

class ControladorPrestamos:

    @staticmethod
    def controladorRegistro(
        id_usuario, id_libro,fecha_devolucion
    ):

        Conexion(**DATOS_CONEXION).consultas("""
        insert into prestamos(
            id_usuario, id_libro,
            fecha_prestamo, fecha_devolucion 
        ) values('{0}','{1}',current_date ,'{2}')
        """.format(id_usuario, id_libro, fecha_devolucion))

        Conexion(**DATOS_CONEXION).consultas("""
        update libro set disponible = 'no-disponible' where id_libro = '{0}'
        and disponible = 'disponible'
        """.format(id_libro))


    @staticmethod
    def controladorDevolucion(id_usuario, id_libro):

        Conexion(**DATOS_CONEXION).consultas("""
        insert into prestamos(
            id_usuario, id_libro,
            fecha_prestamo, fecha_devolucion 
        ) values('{0}','{1}',current_date , current_date)
        """.format(id_usuario, id_libro))

        Conexion(**DATOS_CONEXION).consultas("""
        update libro set disponible = 'disponible' where id_libro = '{0}'
        and disponible = 'no-disponible'
        """.format(id_libro))

        ##select * from prestamos where fecha_prestamo = fecha_devolucion   
        ##para traer las devoluciones

    @staticmethod
    def controladorBusqueda(id_libro):
        Conexion(**DATOS_CONEXION).mostrarLibro("""
        SELECT titulo, autor, tipo_libro, isbn, paginas, nom_ed, disponible FROM libro 
        INNER JOIN editorial ON libro.id_ed = editorial.id_ed
        INNER JOIN tipo_libro ON libro.id_tipo_libro = tipo_libro.id_tipo_libro
        WHERE id_libro = '{0}'
        """.format(id_libro))
        
        
        
