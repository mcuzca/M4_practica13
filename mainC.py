# Llamada de funciones
from book import book
from user import user
from university import university

book1 = book("El gato con botas", "1996", "122","Alejandro Perez", "AJK", "5")
book1.salutacio()
book1.setPaginas("420")
book1.salutacio()

book2 = book ("Alicia en el pais de las maravillas", "1995", "112", "Megan T", "MIU", "27")
book2.salutacio()
book2.setPagines("120")
book2.salutacio()

u1 = user ("Sara", "24", "Panameña", "54983765", "Femenino", "Peru")
u1.salutacio()
u1.setEdad("22")
u1.salutacio()

u2 = user ("Lara", "20", "Colombiana", "54342536", "Femenino", "Chile")
u2.salutacio()
u2.setDni("54343534")
u2.salutacio()

uni1 = university ("Oxford", "3", "12", "24", "16", "8")
uni1.salutacio()
uni1.setMaterias("10")
uni1.salutacio()

uni2 = university ("Harvard", "2", "11", "22", "17", "9")
uni2.salutacio()
uni2.setAlumnos("23")
uni2.salutacio()