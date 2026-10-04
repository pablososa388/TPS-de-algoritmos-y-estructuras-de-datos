from list_ import List
from listaentrenadores import entrenadores
from listapokemon import pokemons

class entrenador:
    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas
        self.pokemons=List()

    def __str__(self):
        pokemons = ""
        for p in self.pokemons:
            pokemons += str(p) + "\n"

        return f"Nombre: {self.nombre}, Torneos Ganados: {self.torneos_ganados}, Batallas Perdidas: {self.batallas_perdidas}, Batallas Ganadas: {self.batallas_ganadas}\nPokemons:\n{pokemons}" 


class pokemon:
    def __init__(self, nombre, nivel, tipo, subtipo,entrenadores):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo
        self.entrenadores=List(entrenadores)

    def __str__(self):
        return f"Nombre: {self.nombre}, Nivel: {self.nivel}, Tipo: {self.tipo}, Subtipo: {self.subtipo}, entrenadores:{self.entrenadores}"
def by_nombre(item):
    return item.nombre
def by_nivel(item): 
    return item.nivel
def by_tipo(item):
    return item.tipo or ""
def by_subtipo(item):
    return item.subtipo or ""


l_e=List()
l_p=List()
l_e.add_criterion('nombre', by_nombre)
l_p.add_criterion('nombre', by_nombre)
l_p.add_criterion('nivel', by_nivel)    
l_p.add_criterion('tipo', by_tipo)
l_p.add_criterion('subtipo', by_subtipo)

def cargar_entrenadores():
    for e in entrenadores:
        l_e.append(entrenador(e["nombre"], e["torneos_ganados"], e["batallas_perdidas"], e["batallas_ganadas"]))

def cargar_pokemons():
    for p in pokemons:
        l_p.append(pokemon(p["nombre"], p["nivel"], p["tipo"], p["subtipo"],p["entrenadores"]))

def definir_entrenadores():
    for p in l_p:
        for nombre in p.entrenadores:
            pos=l_e.search(nombre,'nombre')
            if pos is not None:
                l_e[pos].pokemons.append(p)


# a. obtener la cantidad de Pokémons de un determinado entrenador;

def cantidad_pokemons_entrenador(nombre_entrenador):
    pos=l_e.search(nombre_entrenador,'nombre')
    if pos is not None:
        return l_e[pos].pokemons.size()
    
# b. listar los entrenadores que hayan ganado más de tres torneos;

def entrenadores_3_torneos():
    for e in l_e:
        if e.torneos_ganados>3:
            print(e)

# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
def poke_mayor_lvl_mas_torneos_gana2():
    max_torneos = 0
    entrenador_max = None
    for e in l_e:
        if e.torneos_ganados > max_torneos:
            max_torneos = e.torneos_ganados
            entrenador_max = e
    if entrenador_max is not None:
        max_nivel = 0
        pokemon_max = None
        for p in entrenador_max.pokemons:
            if p.nivel > max_nivel:
                max_nivel = p.nivel
                pokemon_max = p
        return pokemon_max
    return None

# d. mostrar todos los datos de un entrenador y sus Pokémos;
def mostrar_todo_de_un_entrenador(nombre_entrenador):
    pos=l_e.search(nombre_entrenador,'nombre')
    if pos is not None:
        print(f" entrenador buscado: {l_e[pos]}")
        for p in l_e[pos].pokemons:
            print(f"pokemons: {p}")
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
def entrenadores_79porc():
    for e in l_e:
        total_batallas= e.batallas_perdidas+e.batallas_ganadas
        porcentaje_De_wins=(e.batallas_ganadas/total_batallas)*100
        if porcentaje_De_wins>79:
            print(f"entrenadores con mas del 79%de batallas ganadas:{e.nombre} con un porcentaje de {porcentaje_De_wins}%")


# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);
def fuegoPlanta_aguaVolador():
    for e in l_e:
        if e.pokemons.filter_tipo_subtipo("Fuego", "Planta"):
             print(f"entrenador con pokemon tipo fuego y subtipo planta: {e.nombre}")
        if e.pokemons.search("Agua", 'tipo') is not None or e.pokemons.search("Volador", 'subtipo') is not None:
           print(f"entrenador con pokemon de tipo agua o subtipo volador: {e.nombre}")
        
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
def promedioLVLpokemon():
    # #nombre=input("ingrese el nombre del entrenador para calcular el promedio de nivel de sus pokemons: ")
    buscado=l_e.search("Red",'nombre') 
    if buscado is not None:
        lvltotal=0
        for p in l_e[buscado].pokemons:   
            lvltotal+=p.nivel
        lvlpromedio=lvltotal/(l_e[buscado].pokemons.size())
        print(f"el promedio de nivel de los pokemons del entrenador {l_e[buscado].nombre} es: {lvlpromedio}")
    # #else: print(f"No existe el entrenador {nombre}")

# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
def cuantosTienenXpokemon():
    nombre="Dragonite"
    buscado=l_p.search(nombre, 'nombre')
    
    if buscado is not None:
        print (f"la cantidad de entrenadores que tienen un {nombre} es: {l_p[buscado].entrenadores.size()}")
   

# i. mostrar los entrenadores que tienen Pokémons repetidos;
def pokemonRepetido():
    print("Entrenadores con pokemon repetidos: ")
    for p in l_p:
        if p.entrenadores.size() > 1:
            print(f"{p.nombre}: {p.entrenadores}")

# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion
# o Wingull;

def buscarTyraTerra():
    tyra=l_p.search("Tyrantrum",'nombre')
    if tyra is not None:
        for entrenador in l_p[tyra].entrenadores:
            print(f"{entrenador} tiene a {l_p[tyra].nombre}")

    terra=l_p.search("Terrakyon", 'nombre')
    if terra is not None:
        for entrenador in l_p[terra].entrenadores:
            print(f"{entrenador} tiene a {l_p[terra].nombre}")

    wing=l_p.search("Wingull", 'nombre')
    if wing is not None:
        for entrenador in l_p[wing].entrenadores:
            print(f"{entrenador} tiene a {l_p[wing].nombre}")
    
        
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;

def xy():
    n_entrenadro=input("ingrese el nombre del entrenador: ").lower()
    n_pokemon=input("ingrese el nombre del pokemon: ").lower()

    entrenador=l_e.search(n_entrenadro,'nombre')
    pokemon=l_p.search(n_pokemon,"nombre")

    if entrenador is not None and pokemon is not None:
        if l_p[pokemon] in l_e[entrenador].pokemons:
            print(l_e[entrenador])
            print()
            print(l_p[pokemon])
    else: print("valores ingresados no válidos")


cargar_entrenadores()
cargar_pokemons()
definir_entrenadores()
fuegoPlanta_aguaVolador()
promedioLVLpokemon()
cuantosTienenXpokemon()
pokemonRepetido()
buscarTyraTerra()
xy()

