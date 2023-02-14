#crear una clase de nombre book que tenga un constructor y atributos (mínimo 6),
#Getters/Setters
#Mètodo de nombre info donde se muestren, por pantalla, todos los datos (atributos) de book.
class book:
    def __init__(self, titulo, año, paginas, autor, editorial, premios):
        self.titulo = titulo
        self.año = año
        self.paginas = paginas
        self.autor = autor
        self.editorial = editorial
        self.premios = premios

    def getTitulo(self):
        return self.titulo
    def setTitulo(self, titulo):
        self.titulo = titulo

    def getAño(self):
        return self.año
    def setAño(self, año):
        self.año = año

    def getPaginas(self):
        return self.paginas
    def setPaginas(self, paginas):
        self.paginas = paginas

    def getAutor(self):
        return self.autor
    def setAutor(self, autor):
        self.autor = autor

    def getEditorial(self):
        return self.editorial
    def setEditorial(self, editorial):
        self.editorial = editorial

    def getPremios(self):
        return self.premios
    def setPremios(self, premios):
        self.premios = premios

    def salutacio(self):
        print("El nombre es: " + set.titulo)
        print("Publicado en el año" + set.año)
        print("Tiene" + set.paginas + "paginas")
        print("Su autor es " + set.autor)
        print("la editorial es " + set.editorial)
        print("Tiene" + set.premios + "premios")

