#crear una clase de nombre user que tenga un constructor y atributos (mínimo 6),
#Getters/Setters
#Mètodo de nombre info donde se muestren, por pantalla, todos los datos (atributos) de user.

class user():
    def __init__(self, nombre, edad, nacionalidad, dni, sexo, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.dni = dni
        self.sexo = sexo
        self.ciudad = ciudad
        def getNombre(self):
            return self.nombre
        def setNombre(self, nombre):
            self.nombre = nombre
        def getEdad(self):
            return self.edad
        def setEdad(self, edad):
            self.edad = edad
        def getNacionalidad(self):
            return self.nacionalidad
        def setNacionalidad(self, nacionalidad):
            self.nacionalidad = nacionalidad
        def getDni(self):
            return self.dni
        def setDni(self, dni):
            self.dni = dni
        def getSexo(self):
            return self.sexo
        def setSexo(self, sexo):
            self.sexo = sexo
        def getCiudad(self):
            return self.ciudad
        def setCiudad(self, ciudad):
            self.ciudad = ciudad
        def salutacio(self):
            print("El nombre es: "+self.nombre+ "y tu edad es:"+ self.self.edad +"de nacionalidad "+ self.nacionalidad+ "y con dni "+ self.dni+ "de sexo "+ self.sexo +"de la ciudad de "+ self.ciudad)