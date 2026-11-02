# 14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes
# tareas:
# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista
# es la distancia entre los ambientes, se debe cargar en metros;

from graph import Graph

g=Graph(is_dir=False)

vertex = [
    "Cocina", "Comedor", "Cochera", "Quincho", "Baño 1", "Baño 2",
    "Habitación 1", "Habitación 2", "Sala de estar", "Terraza", "Patio"
]

aristas = [
    (4, "Cocina", "Comedor"),
    (6, "Cocina", "Sala de estar"),
    (5, "Cocina", "Patio"),
    (8, "Cocina", "Quincho"),
    (7, "Cocina", "Baño 1"),
    (3, "Comedor", "Sala de estar"),
    (6, "Comedor", "Terraza"),
    (5, "Sala de estar", "Habitación 1"),
    (4, "Sala de estar", "Baño 1"),
    (7, "Sala de estar", "Terraza"),
    (3, "Habitación 1", "Baño 1"),
    (4, "Habitación 1", "Habitación 2"),
    (3, "Habitación 2", "Baño 2"),
    (5, "Habitación 2", "Baño 1"),
    (6, "Baño 2", "Terraza"),
    (8, "Baño 2", "Patio"),
    (4, "Cochera", "Patio"),
    (5, "Cochera", "Quincho"),
    (9, "Cochera", "Terraza"),
    (3, "Quincho", "Patio"),
]

def cargar():
    for v in vertex:
        g.add_vertex(v)
    for peso, origen, destino in aristas:
        g.add_edge(peso,origen,destino)



# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;
def pto_c():
    arbol_em=g.kruskal("Cocina")
    aristas=arbol_em.split(";")
    total=0
    for a in aristas:
        origen, destino, peso=a.split("-")
        print(f"{origen}-{destino}, peso: {peso}") 
        total+=int(peso)
    print(f"Se necesitan {total} metros de cables para conectar todos los ambientes")


# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el
# Smart Tv.
def pto_d():
    if g.exist_path("Habitación 1","Sala de estar"):
            camino = g.dijkstra("Sala de estar")
            info = {}
            while camino.size() > 0:
                nombre, costo, anterior = camino.pop()
                info[nombre] = (costo, anterior)

            recorrido=[]
            actual="Habitación 1"

            while actual is not None:
                recorrido.append(actual)
                actual = info[actual][1]

            print(f"camino: {recorrido}")
            print(f"se necesitan {info["Habitación 1"][0]} metros de cable de red para conectar el router con el smart tv")
     
     

cargar()
pto_c()
pto_d()