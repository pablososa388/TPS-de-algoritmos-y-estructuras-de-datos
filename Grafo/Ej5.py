# Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos necesarios
# para resolver las tareas, listadas a continuación:
# a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor,
# router, switch, impresora;

from graph import Graph

# h. debe utilizar un grafo no dirigido
g=Graph(is_dir=False)


vertices=[
    ("Red Hat", "notebook"),
    ("Debian", "notebook"),
    ("Arch","notebook"),
    ("Ubuntu","PC"),
    ("Mint","PC"),
    ("Fedora","PC"),
    ("Manjaro","PC"),
    ("Parrot","PC"),
    ("Impresora","Impresora"),
    ("Guarani","Servidor"),
    ("MongoDB","Servidor"),
    ("Switch1","Switch"),
    ("Switch2","Switch"),
    ("Router1","Router"),
    ("Router2","Router"),
    ("Router3","Router")

    ]
aristas=[
    (25,"Red Hat", "Router2"),
    (17,"Debian", "Switch1"),
    (56,"Arch","Switch2"),
    (18,"Ubuntu","Switch1"),
    (80,"Mint","Switch1"),
    (3,"Fedora","Switch2"),
    (40,"Manjaro","Switch2"),
    (12,"Parrot","Switch2"),
    (22,"Impresora","Switch1"),
    (9,"Guarani","Router2"),
    (5,"MongoDB","Switch2"),
    (29,"Switch1","Router1"),
    (61,"Switch2","Router3"),
    (37,"Router1","Router2"),
    (50,"Router2","Router3"),
    (43,"Router1","Router3")

    ]


def cargar_vertex():
    for nombre, tipo in vertices:
        g.add_vertex(nombre,tipo)

def cargar_arista():
    for peso, origen, destino in aristas:
        g.add_edge(peso,origen, destino)
# b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook:
def pto_b():
    nobuks=["Red Hat","Debian","Arch"]
    for nbk in nobuks:
        print(f"Profundidad desde: {nbk}")
        g.deep_show(nbk)
        print()
        print(f"amplitud desde: {nbk}")
        g.amplitude_show(nbk)
        print()
        print("---------------------------")
        print()
# c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro,
# Red Hat, Fedora hasta la impresora;
def pto_c():
    if g.exist_path("Manjaro","Impresora"):
        camino = g.dijkstra("Impresora")
        info = {}
        while camino.size() > 0:
            nombre, costo, anterior = camino.pop()
            info[nombre] = (costo, anterior)

        pcs = ["Manjaro", "Red Hat", "Fedora"]
        mejor_pc = None
        mejor_costo = None

        for pc in pcs:
            recorrido = []
            actual = pc
            while actual is not None:
                recorrido.append(actual)
                actual = info[actual][1]

            costo = info[pc][0]
            print(f"Desde {pc} :  -> {recorrido} --- costo: {costo}")

            if mejor_costo is None or costo < mejor_costo:
                mejor_costo = costo
                mejor_pc = pc

        print(f"El camino más corto para imprimir es desde {mejor_pc} con costo {mejor_costo}")

# d. encontrar el árbol de expansión mínima;
def pto_d():
    arbol=g.kruskal("Impresora")
    aristas=arbol.split(";")
    total=0
    for a in aristas:
        origen, destino, peso = a.split("-")
        print(f"{origen} - {destino} peso:  {peso}")
        total += int(peso)
    print(f"Peso total del árbol de expansión mínima: {total}")

# e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”;
def pto_e():
    camino = g.dijkstra("Guarani")
    info = {}
    while camino.size() > 0:
        nombre, costo, anterior = camino.pop()
        info[nombre] = (costo, anterior)

    mejor_pc = None
    mejor_costo = None

    for nombre in info:
        pos = g.search(nombre, "value")
        if g[pos].other_values == "PC":
            costo = info[nombre][0]
            if mejor_costo is None or costo < mejor_costo:
                mejor_costo = costo
                mejor_pc = nombre

    recorrido = []
    actual = mejor_pc
    while actual is not None:
        recorrido.append(actual)
        actual = info[actual][1]

    print(f"Camino:  -> {recorrido}")
    print(f"El camino más corto hasta el servidor Guarani es desde {mejor_pc} con costo {mejor_costo}")

# f. indicar desde que computadora del switch 01 es el camino más corto
# al servidor “MongoDB”;
def pto_f():
    camino = g.dijkstra("MongoDB")
    info = {}
    while camino.size() > 0:
        nombre, costo, anterior = camino.pop()
        info[nombre] = (costo, anterior)
 
    pcs = ["Ubuntu", "Mint", "Debian"]
    mejor_pc = None
    mejor_costo = None

    for pc in pcs:
        recorrido = []
        actual = pc
        while actual is not None:
            recorrido.append(actual)
            actual = info[actual][1]

        costo = info[pc][0]
        print(f"Desde {pc} :  -> {recorrido} --- costo: {costo}")

        if mejor_costo is None or costo < mejor_costo:
            mejor_costo = costo
            mejor_pc = pc

    print(f"El camino más corto al servidor MongoDB es desde {mejor_pc} con costo {mejor_costo}")

# g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b;

def pto_g():
    g.delete_edge("Impresora","Switch1")
    g.add_edge(22,"Impresora","Router2")
    pto_b()

cargar_vertex()
cargar_arista() 
# pto_b()
# pto_c()
# pto_d()    
# pto_e()
# pto_f()
pto_g()