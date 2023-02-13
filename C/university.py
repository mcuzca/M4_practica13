#crear una clase de nombre university que tenga un constructor, atributos (mínimo 6),
#Getters/Setters
#Mètodo de nombre info donde se muestren, por pantalla, todos los datos (atributos) de book.

class university():
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
        def info1(self):
            print("E+self.nombre+ +self.biblioteca +self.clases+self.alumnos+self.profesores+self.materias)


#LLamade de funciones
import book as bk
import user as usr
import university as univ

b1 = bk.book("El gato con botas", 1996, 122,"Alejandro Perez", "AJK", 5)
b1.info()

u1 = usr.user("Sara", 24, "Panameña", 54983765, "Femenino", "Peru")
u1.salutacio()

uni1 = univ.university("Oxford", 1, 12, 21, 18, 8)
uni1.info1()