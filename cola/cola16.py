# 16. Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
# criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
# siguiente situación:

from heap import Heap

# a. cargue tres documentos de empleados (cada documento se representa solamente con
# un nombre).

monti=Heap()
monti.arrive("doc1empleado", 1)
monti.arrive("doc2empleado",1)
monti.arrive("doc3empleado",1)


# b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
priority, value = monti.attention()
print(value)

# c. cargue dos documentos del staff de TI.
monti.arrive("doc1TI",2)
monti.arrive("doc2TI",2)

# d. cargue un documento del gerente.
monti.arrive("docgerente",3)

# e. imprima los dos primeros documentos de la cola.
print()
for docs in range (2):
    priority, value=monti.attention()
    print(value)

# f. cargue dos documentos de empleados y uno de gerente.
monti.arrive("doc3empleado",1)
monti.arrive("doc4empleado",1)
monti.arrive("docgerente2",3)

# g. imprima todos los documentos de la cola de impresión.
print()
for docs in range(monti.size()):
    priority, value=monti.attention()
    print(value)