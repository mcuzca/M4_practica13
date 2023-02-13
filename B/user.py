class user:
    def __init__(self, nom, cognom, edad, dataN, DNI, genere):
        self.nom = nom
        self.cognom = cognom
        self.edad = edad
        self.dataN = dataN
        self.DNI = DNI
        self.genere = genere

    def salutacio(self):
        print("El meu nom es: " + self.nom)
        print("El meu cognom es: " + self.cognom)
        print("Tinc: " + self.edad + " anys")
        print("Vaig neixer el: " + self.dataN)
        print("El meu DNI es: " + self.DNI)
        print("Soc un/a: " + self.genere)

    def getNom(self):
        return self.nom
    def setNom(self, nom):
        self.nom = nom

    def getCognom(self):
        return self.cognom
    def setCognom(self, cognom):
        self.cognom = cognom

    def getEdad(self):
        return self.edad
    def setEdad(self, edad):
        self.edad = edad

    def getDataN(self):
        return self.dataN
    def setDataN(self, dataN):
        self.dataN = dataN

    def getDNI(self):
        return self.DNI
    def setDNI(self, DNI):
        self.DNI = DNI

    def getGenere(self):
        return self.genere
    def setGenere(self, genere):
        self.genere = genere
