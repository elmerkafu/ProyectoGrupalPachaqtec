from conn_postgresql import Conexion

DATOS_CONEXION = {
    'server': 'localhost',
    'user': 'postgres',
    'password': '199705',
    'database': 'biblioteca'
}

class Biblioteca:

    def __init__(self, nombreBiblioteca="Biblioteca nacional"):
        self.nombreBiblioteca = nombreBiblioteca

    def __str__(self):
        return f"\nBiblioteca : {self.nombreBiblioteca}\n"

class Editorial:

    def insertarEditorial(self, nom_ed, pais_ed, telefono_ed):
        Conexion(**DATOS_CONEXION).consultas("""
            INSERT INTO editorial(nom_ed, pais_ed, telefono_ed) VALUES('{0}', '{1}', '{2}')
        """.format(nom_ed, pais_ed, telefono_ed))

    def mostrarDatosEditorial(self):
        Conexion(**DATOS_CONEXION).consultas("""
            SELECT * FROM editorial
        """)



    def __str__(self):
        return (
            "\n ----------- Editoriales ---------\n"
            f"\n - Codigo : {self.id_editorial}\n"
            f"\n - Nombre Editorial : {self.nom_ed}\n"
            f"\n - Pais : {self.pais_ed}\n"
            f"\n - telefono : {self.telefono_ed}\n"
            "\n ----------------------------\n"
        )

print(Editorial().mostrarDatosEditorial())
