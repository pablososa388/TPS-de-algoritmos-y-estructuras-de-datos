from queue_ import Queue
from stack import Stack
from datetime import time



# Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
# de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
# resolver las siguientes actividades:
# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
# la palabra ‘Python’, sin perder datos en la cola;
# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
# 11:43 y las 15:57, y determinar cuántas son.
class Notificacion:
    def __init__(self, hora,minuto, aplicacion, mensaje):       
        self.hora=time(hora, minuto) 
        self.aplicacion=aplicacion
        self.mensaje=mensaje
    def __str__(self):
        return f"{self.hora} - {self.aplicacion}: {self.mensaje}"
datovichs=[(10, 30, "Facebook", "Mensaje 1"),
        (11, 45, "Twitter", "Python es genial"),
        (14, 20, "Instagram", "Mensaje 3"),
        (12,00,"Spotify","paga spotify premium"),(9, 15, "Facebook", "Tu amigo comentó tu foto"),
        (10, 30, "Twitter", "Python 4.0 fue anunciado hoy"),
        (11, 43, "Instagram", "Nueva historia de un seguidor"),
        (11, 50, "Facebook", "Tienes un nuevo mensaje"),
        (12, 10, "YouTube", "Nuevo video de tu canal favorito"),
        (23, 25, "Twitter", "Python es el lenguaje del futuro"),
        (14, 40, "YouTube", "Tu video alcanzó 1000 vistas"),
        (15, 00, "Facebook", "Tienes una nueva solicitud de amistad"),
        (15, 30, "Twitter", "Alguien retuiteó tu Python tip"),
        (16, 20, "Instagram", "Te mencionaron en una historia")]
    
def cargar(cola):
    for hora, minuto, aplicacion, mensaje in datovichs:
        cola.arrive(Notificacion(hora,minuto,aplicacion,mensaje))



def eliminar_feibu(cola:Queue):
    for i in range(cola.size()):
        noti=cola.on_front()
        if noti.aplicacion=="Facebook":
            cola.attention()
        else:
            cola.move_to_end()
    cola.show()


def show_tw_py(cola:Queue):
    for i in range(cola.size()):
        noti=cola.on_front()
        if noti.aplicacion=="Twitter" and "Python" in noti.mensaje:
            print(cola.on_front())
        
        cola.move_to_end()
# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
# 11:43 y las 15:57, y determinar cuántas son.
def pilardium(cola:Queue):
    pila=Stack()
    for i in range(cola.size()):
        notific=cola.on_front()
        if notific.hora> time(11,43) and notific.hora<time(15,57):
            pila.push(notific)
        cola.move_to_end()
    pila.show()
    while pila.size()>0:
        cola.arrive(pila.pop())    


cola = Queue()
cargar(cola)

print("notis de tw con la palabra Python sin perder nada:")
show_tw_py(cola)
print()
print ("cola aun completa:")
cola.show()
print()
print("Pila con las notificaciones entre los horarios 11:43 y 15:57:")
pilardium(cola)
print()
print("Cola sin notis de Fb:")
eliminar_feibu(cola)