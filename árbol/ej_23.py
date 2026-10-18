from criaturas_data import criaturas_mitologicas
from tree import BinaryTree


# Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:
# o dios que la capturo;


class criatura:
    def __init__(self,nombre,derrotada_por,capturada_por,short_descrip):
        self.nombre=nombre
        self.derrotada_por=derrotada_por
        self.capturada_por=capturada_por
        self.short_descrip=short_descrip

    def __str__(self):
        return f"{self.nombre} - {self.derrotada_por} - {self.capturada_por} - {self.short_descrip}"


arbol_creaturas=BinaryTree()

# a. listado inorden de las criaturas y quienes la derrotaron;
for criaturitas in criaturas_mitologicas:
    arbol_creaturas.insert_node(criaturitas['nombre'], other_value=criaturitas)

arbol_creaturas.inorden_criaturas()

# b. se debe permitir cargar una breve descripción sobre cada criatura;
search_str=input("ingrese la criatura que desea buscar: ")
arbol_creaturas.proxy_search(search_str.lower())

search_str=input("ingrese lo que desea MODIFICAR: ")
node=arbol_creaturas.search(search_str)

if node is not None:
    node.other_values['short_descrip']=input("ingrese la descripción de la criatura: ")

print(node.other_values)

print()
# c. mostrar toda la información de la criatura Talos;
print("Info de Talos:")
tal=arbol_creaturas.search('Talos')
if tal is not None:
    print (tal.other_values)

print()
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
print()
arbol_creaturas.top_derrotadores()

# e. listar las criaturas derrotadas por Heracles;
print()
arbol_creaturas.inorden_heracles()
print()
# f. listar las criaturas que no han sido derrotadas;
arbol_creaturas.inorden_No_Derr()

# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
print()
op=input("Desea buscar una criatura para agegar quién la capturó? presione y/n: ")
while op=="y":
    search_str=input("ingrese la criatura que desea buscar: ")
    arbol_creaturas.proxy_search(search_str.lower())

    search_str=input("ingrese lo que desea MODIFICAR: ")
    node=arbol_creaturas.search(search_str)

    if node is not None:
        node.other_values['capturada_por']=input("ingrese quien capturó a la criatura: ")

    print(node.other_values)
    op=input("Desea buscar otra criatura? y/n: ")


# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
print()
search_str='Cerbero'
node=arbol_creaturas.search(search_str)
if node is not None:
    node.other_values['capturada_por']="Heracles"
print (node.other_values)

print()
search_str='Toro de Creta'
node=arbol_creaturas.search(search_str)
if node is not None:
    node.other_values['capturada_por']="Heracles"
print (node.other_values)

print()
search_str='Toro de Creta'
node=arbol_creaturas.search(search_str)
if node is not None:
    node.other_values['capturada_por']="Heracles"
print (node.other_values)

print()
search_str='Cierva de Cerinea'
node=arbol_creaturas.search(search_str)
if node is not None:
    node.other_values['capturada_por']="Heracles"
print (node.other_values)

print()
search_str='Jabalí de Erimanto'
node=arbol_creaturas.search(search_str)
if node is not None:
    node.other_values['capturada_por']="Heracles"
print (node.other_values)


# i. se debe permitir búsquedas por coincidencia;
print()
op=input("Desea buscar una criatura? presione y/n: ")
while op=="y":
    search_str=input("ingrese la criatura que desea buscar: ")
    arbol_creaturas.proxy_search(search_str.lower())

    op=input("desea realizar otra búsqueda? y/n: ")




# j. eliminar al Basilisco y a las Sirenas;
print()
busc="Basilisco"
basi=arbol_creaturas.search(busc)
if basi is not None:
    arbol_creaturas.delete_node(basi.value)
if arbol_creaturas.search("Basilisco") is None:
    print("Basilisco eliminado correctamente")
    
    
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
print()
search_str='Aves del Estínfalo'
node=arbol_creaturas.search(search_str)
if node is not None:
    node.other_values['short_descrip']="Heracles derrotó a varias de estas criaturas"
    node.other_values['derrotado_por']="Heracles"
print (node.other_values)

print()
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
search_str='Ladón'
node=arbol_creaturas.search(search_str)
if node is not None:
    new_name="Dragón Ladón"
    delete_value, delete_other_value = arbol_creaturas.delete_node(node.value)
    delete_other_value['nombre'] = new_name
    arbol_creaturas.insert_node(new_name, delete_other_value)
print (node.other_values)

# m. realizar un listado por nivel del árbol;
print()
arbol_creaturas.by_level()

print()
# n. muestre las criaturas capturadas por Heracles.
arbol_creaturas.inorden_heracles2()