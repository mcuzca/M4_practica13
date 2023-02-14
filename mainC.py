#LLamada de funciones

from book0 import book0
from user0 import user0
from university0 import university0

book1 = book0 ("El gato con botas", 1996, 122,"Alejandro Perez", "AJK", 5)
book1.info()
book1.setPaginas(420)
book1.info()

book2 = book0 ("Alicia en el pais de las maravillas", 1995, 112, "Megan T", "MIU", 7)
book2.info()
book2.setPagines(120)
book2.info()

u1 = user0 ("Sara", 24, "Panameña", 54983765, "Femenino", "Peru")
u1.salutacio()
u1.setEdad(22)
u1.salutacio()

u2 = user0 ("Lara", 20, "Colombiana", 54342536, "Femenino", "Chile")
u2.salutacio()
u2.setDni(54343534)
u2.salutacio()

uni1 = university0 ("Oxford", 3, 12, 24, 16, 8)
uni1.info1()
uni1.setMaterias(10)
uni1.info1()

uni2 = university0 ("Harvard", 2, 11, 22, 17, 9)
uni2.info1()
uni2.setAlumnos(23)
uni2.info1()

