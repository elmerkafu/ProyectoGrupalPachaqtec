from controlador_postgresql import(
    ControladorEditorial,
    ControladorLibro,
    ControladorTipoLibro,
    ControladorUsusario,
    ControladorPrestamos
)
from os import system


class vistaAdministrador:

    @staticmethod
    def menu():
        continuar = True
        while continuar:
            system('clear')
            print("Bienvenido a la seccion Registro de la biblioteca")
            print("-------------------------------------------------")
            print("Elija 1 para registrar Editorial")
            print("Elija 2 para registrar categoria de libro")
            print("Elija 3 para registrar Nuevo libro")
            print("Elija 4 para listar Editoriales")
            print("Elija 5 para listar Categorias")
            print("Elija 6 para listar Libros Registrados")
            print("Elija 7 para volver al menu principal")
            opcion = int(input("Eliga una opcion : "))
            if opcion == 1:
                system('clear')
                vistaAdministrador.ingreso_editorial()
            elif opcion == 2:
                system('clear')
                vistaAdministrador.ingreso_tipo_libro()
            elif opcion == 3:
                system('clear')
                vistaAdministrador.ingreso_libro()
            elif opcion == 4:
                system('clear')
                vistaAdministrador.listar_editorial()
            elif opcion == 5:
                system('clear')
                vistaAdministrador.listar_tipo_libro()
            elif opcion == 6:
                system('clear')
                vistaAdministrador.listar_libro()
            else:
                continuar = False
                
    @staticmethod
    def ingreso_editorial():
        nom_ed = input("Ingrese el nombre de la Editorial: ")
        pais_ed = input("Ingrese el pais de la Editorial: ")
        telefono_ed = input("Ingrese el telefono de la Editorial: ")
        DATOS_EDITORIAL = {
            'nom_ed': nom_ed,
            'pais_ed': pais_ed,
            'telefono_ed': telefono_ed
            }
        registro_correcto = ControladorEditorial.controladorRegistro(**DATOS_EDITORIAL)
        if registro_correcto[0]:
            print("La editorial se inserto correctamente.")
        else:
            print(registro_correcto[1])
        input("Presione cualquier tecla para continuar")

    @staticmethod
    def ingreso_tipo_libro():
        nombre_tipo = input("Ingrese nueva categoria de libro : ")
        DATOS_CATEGORIA = { 'nombre_tipo' : nombre_tipo }
        ControladorTipoLibro.controladorRegistro(**DATOS_CATEGORIA)
    
    @staticmethod
    def ingreso_libro():
        titulo = input("Ingrese el nombre del libro : ")
        autor = input("Ingrese el nombre del autor : ")
        id_ed = input("Ingrese el codigo Editorial : ")
        isbn = input("Ingrese el ISBN : ")
        paginas = input("Ingrese el numero de paginas : ")
        id_tipo_libro = input("Ingrese el codigo Categoria de libro : ")
        disponible = input("Ingrese disponibilidad : ")
        DATOS_LIBRO = {
            'titulo' : titulo,
            'autor' : autor,
            'id_ed' : id_ed,
            'isbn' : isbn,
            'paginas' : paginas,
            'id_tipo_libro' : id_tipo_libro,
            'disponible' : disponible
        }
        ControladorLibro.controladorRegistro(**DATOS_LIBRO)

    @staticmethod
    def listar_editorial():
        editoriales = ControladorEditorial.controladorMostrar()
        for editorial in editoriales:
            print(editorial)
        input("Presionar cualquier tecla para continuar")

    @staticmethod
    def listar_tipo_libro():
        tipos = ControladorTipoLibro.controladorMostrar()
        for tipo in tipos:
            print(tipo)
        input("Presionar cualquier tecla para continuar")
    
    @staticmethod
    def listar_libro():
        libros = ControladorLibro.controladorMostrar()
        for libro in libros:
            print(libro)
        input("Presionar cualquier tecla para continuar")

class vistaUsuario:

    @staticmethod
    def menu():
        continuar = True
        while continuar:
            system('clear')
            print("Bienvenido a la seccion de Usuarios")
            print("--------------------------------------------")
            print("Elija 1 para registrar Nuevo Usuario")
            print("Elija 2 para mostrar ranking de prestamos")
            print("Elija 3 Registrar Prestamos")
            print("Elija 4 para volver al menu principal")
            opcion = int(input("Eliga una opcion : "))
            if opcion == 1:
                system('clear')
                vistaUsuario.ingreso_usuario()
            elif opcion == 2:
                system('clear')
                pass
            elif opcion == 3:
                system('clear')
                vistaPrestamos.menu()
            else:
                continuar = False
    
    @staticmethod
    def ingreso_usuario():
        nombre = input("Ingrese su nombre : ")
        apellido = input("Ingrese su apellido : ")
        dni = input("Ingrese su dni : ")
        pwd = input("Ingrese una contraseña : ")
        DATOS_USUARIO = {
            'nombre' : nombre,
            'apellido' : apellido,
            'dni' : dni,
            'pwd' : pwd
        }
        ControladorUsusario.controladorRegistro(**DATOS_USUARIO)

class vistaPrestamos:

    @staticmethod
    def menu():
        continuar = True
        while continuar:
            system('clear')
            print("Bienvenido a la seccion de PRESTAMOS Y DEVOLUCIONES")
            print("---------------------------------------------------")
            print("Elija 1 para registrar Prestamo")
            print("Elija 2 buscar libros disponibles")
            print("Elija 3 para registrar devolucion")
            print("Elija 4 para volver al menu principal")
            opcion = int(input("Eliga una opcion : "))
            if opcion == 1:
                system('clear')
                vistaPrestamos.ingreso_prestamo()
            elif opcion == 2:
                system('clear')
                vistaPrestamos.busqueda_libro()
            elif opcion == 3:
                system('clear')
                vistaPrestamos.devolicion_libro()
            else:
                continuar = False
    
    @staticmethod
    def ingreso_prestamo():
        id_usuario = input("Ingrese su codigo Usuario : ")
        id_libro = input("Ingrese el codigo del libro : ")
        print("FORMATO DE LA FECHA AAAA-MM-DD")
        fecha_devolucion = input("Ingrese la fecha de devolucion  : ")
        DATOS_PRESTAMO = {
            'id_usuario' : id_usuario,
            'id_libro' : id_libro,
            'fecha_devolucion' : fecha_devolucion
        }
        ControladorPrestamos.controladorRegistro(**DATOS_PRESTAMO)

    @staticmethod
    def devolicion_libro():
        id_usuario = input("Ingrese su codigo Usuario : ")
        id_libro = input("Ingrese el codigo del libro : ")
        DATOS_PRESTAMO = {
            'id_usuario' : id_usuario,
            'id_libro' : id_libro
        }
        ControladorPrestamos.controladorDevolucion(**DATOS_PRESTAMO)        

    @staticmethod
    def busqueda_libro():
        print("Bienvenido a la seccion de busqueda de libros")
        print("--------------------------------------------") 
        id_libro = input("Ingrese Codigo de libro : ")
        libros = ControladorPrestamos.controladorBusqueda(id_libro)
        for libro in libros:
            print(libro)
        input("Presione cualquier tecla para continuar")

class vistaApp:

    @staticmethod
    def menu():
        continuar = True
        while continuar:
            system('clear')
            print("Bienvenido a la Biblioteca bob")
            print("------------------------------")
            print("Elija 1 para ingresar al ADMINISTRADOR")
            print("Elija 2 para ingresar al USUARIO")
            opcion = int(input("Eliga una opcion : "))

            if opcion == 1:
                system('clear')
                vistaAdministrador.menu()
            elif opcion == 2:
                system('clear')
                vistaUsuario.menu()
            else:
                continuar = False
        