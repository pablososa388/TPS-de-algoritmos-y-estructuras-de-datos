from stack import Stack
from random import shuffle
class PersonajeMcu:

    def __init__(self, nombre, peliculas):
        self.nombre=nombre
        self.peliculas=peliculas

class PilaMcu:
    def __init__(self):
        self.ListaDePersonajes=Stack()

    def cargar(self):
        personajes=[PersonajeMcu("Iron man",10),
                    PersonajeMcu("Groot",6),
                    PersonajeMcu("Rocket Racoon",6),
                    PersonajeMcu("Spider man",6),
                    PersonajeMcu("Black Widow",9),
                    PersonajeMcu("Hulk",9),
                    PersonajeMcu("Doctor Strange",6),
                    PersonajeMcu("Deadpool",4),
                    PersonajeMcu("Captain america",11),
                    PersonajeMcu("Green Goblin",1),
                    ]
        shuffle(personajes)
        for pj in personajes:
            self.ListaDePersonajes.push(pj)
    
    def posicionRRyG(self,search_value):
        aux=Stack()
        cont=0
        encontrado=False
        while self.ListaDePersonajes.size()>0:
            value= self.ListaDePersonajes.pop()
            if not encontrado:
                cont+=1
            if value.nombre.lower()==search_value:
                encontrado=True
            aux.push(value)
        while aux.size()>0:
            value=aux.pop()
            self.ListaDePersonajes.push(value)
        if not encontrado:
            print(f"El nombre buscado {search_value} no se encontró")
        if encontrado:
            print (f"Se encontró el buscado {search_value}, estaba en la posición {cont} de la pila")
    
    def BuscarCantPelis(self,search):
        aux=Stack()
        while self.ListaDePersonajes.size()>0:
            value=self.ListaDePersonajes.pop()
            if value.nombre.lower()==search:
                print(f"{value.nombre} participa en {value.peliculas}")
            aux.push(value)
        while aux.size()>0:
            value=aux.pop()
            self.ListaDePersonajes.push(value)  

    def EmpiezaConCDG(self):
        auxx=Stack()
        while self.ListaDePersonajes.size()>0:
            value=self.ListaDePersonajes.pop()
            if value.nombre[0].lower()== "c" or value.nombre[0].lower()=="g" or value.nombre[0].lower()=="d":
                print (f"Nombres que comienzan con C, D o G: {value.nombre} ")
            auxx.push(value)
            
        while auxx.size()>0:
            value=auxx.pop()
            self.ListaDePersonajes.push(value)
        
    def CincoMasPelis(self):

        pilaux=Stack()
        pilaux2=Stack()
        while self.ListaDePersonajes.size()>0:
            value=self.ListaDePersonajes.pop()

            if value.peliculas>=5:
                pilaux.push(value)

            else:
                pilaux2.push(value)
        
        while pilaux.size()>0:
            value=pilaux.pop()         
            print(value.nombre, value.peliculas)        
            self.ListaDePersonajes.push(value)
        
        while pilaux2.size()>0:
            value=pilaux2.pop()
            self.ListaDePersonajes.push(value)          


pila_mcu = PilaMcu()
pila_mcu.cargar()
pila_mcu.posicionRRyG("groot")
pila_mcu.posicionRRyG("rocket racoon")
search_value=input("Ingrese el nombre del personaje buscado, en este caso Groot y Rocket Racoon ya han sido buscados, busque otro si así lo desea:")
pila_mcu.posicionRRyG(search_value.lower())
print("Personajes que participaron en 5 o mas peliculas de la saga")    
pila_mcu.CincoMasPelis()
pila_mcu.BuscarCantPelis("black widow")
search=input("Ya se buscó a Black Widow, busque otro si lo desea")
pila_mcu.BuscarCantPelis(search.lower())
pila_mcu.EmpiezaConCDG()  
#a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila; DONE
#    b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar
# la cantidad de películas en la que aparece; 
# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
