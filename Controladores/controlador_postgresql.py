import Modelos.model_postgresql
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
        for dato in tabla:
            return tabla
    
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
        for dato in tabla:
            return tabla

class ControladorLibro:

    @staticmethod
    def controladorRegistro(
        titulo, autor, id_ed, isbn, paginas, id_tipo_libro, cantidad
    ):
        Conexion(**DATOS_CONEXION).consultas("""
        insert into libro(
            titulo, autor, id_ed, isbn, paginas, id_tipo_libro, cantidad
            ) values(
                {0}, {1}, {2}, {3}, {4}, {5}
            )
        """.format(
            titulo, autor, id_ed, isbn, paginas, id_tipo_libro, cantidad
        ))
    @staticmethod
    def controladorMostrar(parametro=None):
        tabla = Conexion(**DATOS_CONEXION).mostrar("""
        SELECT * FROM libro   
        """)
        for dato in tabla:
            return tabla

##SE PROPONE EL REGISTRO MASIVO DE LOS LIBROS USANDO LISTAS
##print(ControladorLibro().controladorMostrar())