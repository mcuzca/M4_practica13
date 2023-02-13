
class vehiculo:
    def __init__(self,tipo,marca,color,combustible,propietario,velocidad):
        self.tipo = tipo
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.propietario = propietario
        self.velocidad = velocidad

    def saludo(self):
        print("Tipo de vehiculo : " + self.tipo)
        print("Marca  : " + self.marca)
        print("Color  : " + self.color)
        print("Combustible  : " + self.combustible)
        print(" Nombre del propietario: " + self.propietario)
        print("Velocidad maxima (km): " + self.velocidad)

    def getTipo(self):
        return self.tipo

    def setTipo(self,tipo):
         self.tipo = tipo

    def getMarca(self):
        return self.marca

    def setMarca(self,marca):
         self.marca = marca

    def getColor(self):
        return self.color

    def setColor(self,color):
        self.color = color

    def getCombustible(self):
        return self.combustible

    def setCombustible(self,combustible):
        self.combustible = combustible

    def getPropietario(self):
        return self.propietario

    def setPropietario(self,propietario):
         self.propietario = propietario

    def getVelocidad(self):
        return self.velocidad

    def setVelocidad(self,velocidad):
         self.velocidad = self.velocidad


