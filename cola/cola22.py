from queue_ import Queue
from stack import Stack
 

# Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce
# el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino
# F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff,
# Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:
# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.

class Personajes:
    def __init__(self, nombre_p,nombre_s,genero):
        self.nombre_p=nombre_p
        self.nombre_s=nombre_s
        self.genero=genero

    def __str__(self):
        return f"{self.nombre_p}-{self.nombre_s}-{self.genero}"
   

    
pejotas=[("Tony Stark", "Iron Man", "M"),
("Steve Rogers", "Capitán América", "M"),
("Natasha Romanoff", "Black Widow", "F"),
("Bruce Banner", "Hulk", "M"),
("Thor Odinson", "Thor", "M"),
("Clint Barton", "Hawkeye", "M"),
("Peter Parker", "Spider-Man", "M"),
("Scott Lang", "Ant-Man", "M"),
("Hope van Dyne", "Wasp", "F"),
("T'Challa", "Black Panther", "M"),
("Shuri", "Black Panther", "F"),
("Wanda Maximoff", "Scarlet Witch", "F"),
("Vision", "Vision", "M"),
("Sam Wilson", "Falcon", "M"),
("Bucky Barnes", "Winter Soldier", "M"),
("Stephen Strange", "Doctor Strange", "M"),
("Carol Danvers", "Capitana Marvel", "F"),
("James Rhodes", "War Machine", "M"),
("Peter Quill", "Star-Lord", "M"),
("Gamora", "Gamora", "F")
]



def cargar(cola=Queue):
    for nombre_p,nombre_s,genero in pejotas:
        cola.arrive(Personajes(nombre_p,nombre_s,genero))


# # a. determinar el nombre del personaje de la superhéroe Capitana Marvel;

def capitanaM(cola:Queue):
    for i in range(cola.size()):
        pj=cola.on_front()
        if pj.nombre_s=="Capitana Marvel":
            print(f"el nombre del personaje de la cap marvel es {pj.nombre_p}")
        cola.move_to_end()
# # # b. mostrar los nombre de los superhéroes femeninos;
def mostrarfem(cola:Queue):
    print(f"Nombre de superheroes femeninos:")
    for minitas in range(cola.size()):
        mina=cola.on_front()
        if mina.genero=="F":
            print(mina.nombre_s)
        cola.move_to_end()

#     # c. mostrar los nombres de los personajes masculinos;
def mostrarmasc(cola:Queue):
    print("Nombres de los personajes masculinos:")
    for flacos in range(cola.size()):
        mister=cola.on_front()
        if mister.genero=="M":
            print(mister.nombre_p)
        cola.move_to_end()

#  #d. determinar el nombre del superhéroe del personaje Scott Lang;
def search_scotty(cola:Queue):
    print("El nombre del superhéroe de Scott Lang es:")

    for i in range(cola.size()):
        
        sty=cola.on_front()
        if sty.nombre_p=="Scott Lang":
            print(sty.nombre_s)
        cola.move_to_end()    

# # e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# # con la letra S;

def pibes_con_s(cola:Queue):
    sola=Queue()
    for s in range(cola.size()):        
        ese=cola.on_front()
        if ese.nombre_s[0]=="S" or ese.nombre_p[0]=="S":
            sola.arrive(ese)
        cola.move_to_end()
    print("superhéroes o personaje cuyos nombres comienzan con la letra S:")
    sola.show()
    while sola.size()>0:
        cola.arrive(sola.attention())


cola=Queue()
cargar(cola)
mostrarfem(cola)
print()
capitanaM(cola)
print()
mostrarmasc(cola)
print()
search_scotty(cola)
print()
pibes_con_s(cola)

#

# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.