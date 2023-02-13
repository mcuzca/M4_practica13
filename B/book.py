class book:
    def __init__(self, titol, autor, data, tapa, pagines, editioral):
        self.titol = titol
        self.autor = autor
        self.data = data
        self.tapa = tapa
        self.pagines = pagines
        self.editioral = editioral

    def salutacio(self):
        print("El titol del llibre és: " + self.titol)
        print("El autor és: " + self.autor)
        print("La data de la publicació és: " + self.data)
        print("La tapa del llibre és: " + self.tapa)
        print("El llibre conte " + self.pagines + " pagines")
        print("La editorial del llibre és: " + self.editioral)

    def getTitol(self):
        return self.titol
    def setTitol(self, titol):
        self.titol = titol

    def getAutor(self):
        return self.autor
    def setAutor(self, autor):
        self.autor = autor

    def getData(self):
        return self.data
    def setData(self, data):
        self.data = data

    def getTapa(self):
        return self.tapa
    def setTapa(self, tapa):
        self.tapa = tapa

    def getPagines(self):
        return self.pagines
    def setPagines(self, pagines):
        self.pagines = pagines

    def getEditorial(self):
        return self.editioral
    def setEditorial(self, editioral):
        self.editioral = editioral
