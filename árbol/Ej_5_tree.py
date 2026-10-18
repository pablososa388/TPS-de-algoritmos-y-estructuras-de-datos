# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe
# (MCU), desarrollar un algoritmo que contemple lo siguiente:
# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano
# que indica si es un héroe o un villano, True y False respectivamente;
# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.



from super_heroes_data import superheroes
from tree import BinaryTree

class MarvelCharacter():

    def __init__(self, nombre, anio, casa, bio):
        self.name = nombre
        self.year = anio
        self.house = casa
        self.bio = bio

    def __str__(self):
        return f"{self.name} - {self.year} - {self.house}"
    


arbol_marvel = BinaryTree()
arbol_heroes=BinaryTree()
arbol_villanos= BinaryTree()
print(f'cantidad de elementos {len(superheroes)}')
#A
for marvel_character in superheroes:
    arbol_marvel.insert_node(marvel_character['name'], other_value=marvel_character)

# #B
arbol_marvel.inorden_villain()


# #C
arbol_marvel.inorden_hero_star_with('An')

# #D
print(f'cantidad de heroes: {arbol_marvel.count_heroes()}')

# E
search_str = input('ingrese lo que quiere buscar: ')
arbol_marvel.proxy_search(search_str.lower())

search_str = input('ingrese lo que quiere modificar: ')

node = arbol_marvel.search(search_str)
if node is not None:
    new_name = input('ingrese el nuevo nombre: ')
    delete_value, delete_other_value = arbol_marvel.delete_node(node.value)
    delete_other_value['name'] = new_name
    arbol_marvel.insert_node(new_name, delete_other_value)

print()
arbol_marvel.inorden_hero_star_with('D')

# # F
# arbol_marvel.postorden_hero()

print()
#G
arbol_marvel.inorden_bosque(arbol_heroes,arbol_villanos)
arbol_heroes.inorden()
arbol_villanos.inorden()

print()

#I. determinar cuántos nodos tiene cada árbol
print(f"el arbol de heroes tiene {arbol_heroes.count_heroes()} nodos")
print()
print(f"el arbol de villanos tiene {arbol_villanos.count_villains()} nodos")

# II. realizar un barrido ordenado alfabéticamente de cada árbol.
print()
print("arbol de heroes ordenado alfabeticamente: ")
arbol_heroes.inorden()
print()
print("arbol de villanos ordenado alfabeticamente: ")
arbol_villanos.inorden()