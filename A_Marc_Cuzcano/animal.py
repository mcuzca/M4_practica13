
class animal:
    def __init__(self,name,familia,comida,habitat,vida,sexo):
        self.name = name
        self.familia = familia
        self.comida = comida
        self.habitat = habitat
        self.vida = vida
        self.sexo = sexo

    def getName(self):
        return self.name
    def setName(self,name):
        self.name = name

    def getHabitat(self):
        return self.habitat
    def setHabitat(self,habitat):
        self.habitat = habitat

    def getComida(self):
        return self.comida
    def setComida(self,comida):
        self.comida = comida

    def getVida(self):
        return self.vida
    def setVida(self,vida):
        self.vida = vida

    def getFamilia(self):
        return self.familia
    def setFamilia(self,familia):
        self.familia = familia

    def getSexo(self):
        return self.sexo
    def setSexo(self,sexo):
        self.sexo = sexo

    def saludo(self):
        print("Nombre comun del animal : " + self.name)
        print("Habitat natural : " + self.habitat)
        print("Familia del animal : " + self.familia)
        print("Comida  : " + self.comida)
        print("Años de vida : " + self.vida)
        print("Sexo : " + self.sexo)