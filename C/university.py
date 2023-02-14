#crear una clase de nombre university que tenga un constructor, atributos (mínimo 6),
#Getters/Setters
#Mètodo de nombre info donde se muestren, por pantalla, todos los datos (atributos) de book.
class university:
    def __init__(self, nombre, biblioteca, clases, alumnos, profesores, materias):
        self.nombre = nombre
        self.biblioteca = biblioteca
        self.clases = clases
        self.alumnos = alumnos
        self.profesores = profesores
        self.materias = materias

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre

    def getBiblioteca(self):
        return self.biblioteca
    def setBiblioteca(self, biblioteca):
        self.biblioteca = biblioteca

    def getClases(self):
        return self.clases
    def setClases(self, clases):
        self.clases = clases

    def getAlumnos(self):
        return self.alumnos
    def setAlumnos(self, alumnos):
        self.alumnos = alumnos

    def getProfesores(self):
        return self.profesores
    def setProfesores(self, profesores):
        self.profesores = profesores

    def getMaterias(self):
        return self.materias
    def setMaterias(self, materias):
        self.materias = materias

    def salutacio(self):
        print("El nombre es: " + self.nombre)
        print("Consta de" + self.biblioteca + "bibliotecas")
        print("Tiene" + self.clases + "clases")
        print("Tiene " + self.alumnos + "alumnos")
        print("Tiene " + self.profesores + "profesores")
        print("Tiene " + self.materias + "materias")

