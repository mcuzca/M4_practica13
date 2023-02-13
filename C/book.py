#crear una clase de nombre book que tenga un constructor y atributos (mínimo 6),
#Getters/Setters
#Mètodo de nombre info donde se muestren, por pantalla, todos los datos (atributos) de book.

class book():
        def __init__(self, nombre, año, paginas, autor, editorial, premios):
            self.nombre = nombre
            self.año = año
            self.paginas = paginas
            self.autor = autor
            self.editorial = editorial
            self.premios = premios
        def getNombre(self):
            return self.nombre
        def setNombre(self, nombre):
            self.nombre = nombre
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

        def info(self):
            print("El nombre del libro es: " +set.nombre+ " en el año" +set.año+ "tiene" + set.paginas+ "paginas y su autor es "+set.autor +"de la editorial " +set.editorial + "y con" + set.premios +" premios")
