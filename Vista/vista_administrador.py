import Controladores.controlador_postgresql
from os import system

class vistaAdministrador:

    @staticmethod
    def menu():
        continuar = True
        while continuar:
            system('clear')
            print("Bienvenido a la seccion Registro de Editoriales")
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
        ControladorEditorial.controladorRegistro(**DATOS_EDITORIAL)

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
        cantidad = input("Ingrese la cantidad de ejemplares : ")
        DATOS_LIBRO = {
            'titulo' : titulo,
            'autor' : autor,
            'id_ed' : id_ed,
            'isbn' : isbn,
            'paginas' : paginas,
            'id_tipo_libro' : id_tipo_libro,
            'cantidad' : cantidad
        }
        ControladorLibro.controladorRegistro(**DATOS_LIBRO)

    @staticmethod
    def listar_editorial():
        print(ControladorEditorial.controladorMostrar())
        input("Presionar cualquier tecla para continuar")

    @staticmethod
    def listar_tipo_libro():
        print(ControladorTipoLibro.controladorMostrar())
        input("Presionar cualquier tecla para continuar")
    
    @staticmethod
    def listar_libro():
        print(ControladorLibro.controladorMostrar())
        input("Presionar cualquier tecla para continuar")

vistaAdministrador.menu()