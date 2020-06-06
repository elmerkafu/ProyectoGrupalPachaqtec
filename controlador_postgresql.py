from modelos.model_postgresql import (
    Conexion, ConexionEditorial,
    ConexionTipoLibro, ConexionLibro,
    ConexionUsuario, ConexionPrestamos
)


DATOS_CONEXION = {
    'server': 'localhost',
    'user': 'postgres',
    'password': '199705',
    'database': 'biblioteca'
}

class ControladorEditorial:

    @staticmethod      
    def controladorRegistro(nom_ed, pais_ed, telefono_ed):
        datos_insercion = ConexionEditorial(
            **DATOS_CONEXION
        ).insertar(
            nom_ed, pais_ed, telefono_ed
        )
        return datos_insercion


    @staticmethod
    def controladorMostrar(parametro=None):
        tabla = ConexionEditorial(**DATOS_CONEXION).mostrar()
        return tabla
    
class ControladorTipoLibro:

    @staticmethod
    def controladorRegistro(nombre_tipo):
        ConexionTipoLibro(**DATOS_CONEXION).insertar(nombre_tipo)

    @staticmethod
    def controladorMostrar(parametro = None):
        tabla = ConexionTipoLibro(**DATOS_CONEXION).mostrar()
        return tabla

class ControladorLibro:

    @staticmethod
    def controladorRegistro(
        titulo, autor, id_ed, isbn, paginas, id_tipo_libro, disponible
    ):
        ConexionLibro(**DATOS_CONEXION).insertar(
            titulo, autor, id_ed, isbn, 
            paginas, id_tipo_libro, 
            disponible
        )
        
    @staticmethod
    def controladorMostrar(parametro=None):
        tabla = ConexionLibro(**DATOS_CONEXION).mostrar()
        return tabla

class ControladorUsusario:

    @staticmethod
    def controladorRegistro(nombre, apellido, dni, pwd):
        ConexionUsuario(**DATOS_CONEXION).insertar(
            nombre, apellido, dni, pwd
        )

class ControladorPrestamos:

    @staticmethod
    def controladorRegistro(id_usuario, id_libro,fecha_devolucion):

        ConexionPrestamos(**DATOS_CONEXION).insertarPrestamo(
            id_usuario, id_libro,fecha_devolucion
        )

    @staticmethod
    def controladorDevolucion(id_usuario, id_libro):

        ConexionPrestamos(**DATOS_CONEXION).insertarDevolucion(
            id_usuario, id_libro
        )

    @staticmethod
    def controladorBusqueda(id_libro):
        tabla = ConexionPrestamos(**DATOS_CONEXION).mostrar(id_libro)
        return tabla
        
        
        
