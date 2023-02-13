from animal import animal
from vehiculo import vehiculo
from escuela import escuela


es1 = escuela("Balmes","cinco","cien","Barcelona","doscientos","ocho")
es1.saludo()
es2 = escuela("Balmes","cinco","cien","Barcelona","doscientos","ocho")
es2.saludo()

an1 = animal("Gato","Felino","Atun","Bosque","ochenta","Femenino")
an1.saludo()
an2 = animal("Gato","Felino","Atun","Bosque","ochenta","Femenino")
an2.saludo()
es1 = vehiculo("coche","mercedez","negro","diesel","Paco","veinte-cinco")
es1.saludo()
es2 = vehiculo("coche","mercedez","negro","diesel","Paco","veinte-cinco")
es2.setTipo("Camion")
es2.saludo()
