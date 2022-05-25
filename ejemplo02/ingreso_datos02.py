from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

archivo = open("data/datos_jugadores.txt", "r")
registros = archivo.readlines();


for i in registros:
        nombre = i.split(";")[3]
        dorsal = i.split(";")[2]
        posicion = i.split(";")[1]
        club = i.split(";")[0]
        print(nombre)
        print(dorsal)
        print(posicion)
        print(club)
        jugador = Jugador(nombre = nombre, dorsal = dorsal, posicion = posicion , club = club)
        session.add(jugador)

session.commit()