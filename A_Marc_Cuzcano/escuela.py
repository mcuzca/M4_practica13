class escuela:
    def __init__(self,name,años,empleados,ubicacion,alumnos,aulas):
        self.name = name
        self.años = años
        self.empleados = empleados
        self.ubicacion = ubicacion
        self.alumnos = alumnos
        self.aulas = aulas




    def getName(self):
        return self.name

    def setName(self,name):
        self.name = name

    def getAños(self):
        return self.años

    def setAños(self,años):
        self.años = años

    def getEmpleados(self):
        return self.empleados

    def setEmpleados(self,empleados):
        self.empleados = empleados

    def getUbicacion(self):
        return self.ubicacion

    def setUbicacion(self,ubicacion):
        self.ubicacion = ubicacion

    def getAlumnos(self):
        return self.alumnos

    def setAlumnos(self,alumnos):
        self.alumnos = alumnos

    def getAulas(self):
        return self.aulas

    def setAulas(self,aulas):
        self.aulas = aulas

    def saludo(self):
        print("Nombre de la escuela : " + self.name)
        print("Años en activo : " + self.años)
        print("Numero de empleados : " + self.empleados)
        print("Ubicacion: " + self.ubicacion)
        print("Numero de alumnos : " + self.alumnos)
        print("Numero de aulas : " + self.aulas)