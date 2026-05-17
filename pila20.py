from stack import Stack
from random import shuffle


# Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son
# cantidad de pasos y dirección –suponga que el robot solo puede moverse en ocho direcciones:
# norte, sur, este, oeste, noreste, noroeste, sureste y suroeste–. Luego desarrolle otro algoritmo
# que genere la secuencia de movimientos necesarios para hacer volver al robot a su lugar de
# partida, retornando por el mismo camino que fue.

class Robot:
    def __init__(self,cantPasos,direccion):
        self.cantPasos=cantPasos
        self.direccion=direccion
    

class RoboPila:
    def __init__(self):
        self.Movimientos=Stack()
    
    def cargarPasos(self):
        p=int(input("ingrese la cantidad de acciones del robot: "))

        for i in range(p):
            pasos=input("ingrese la cantidad de pasos que dará el robot:  ")
            direccion= input("ingrese la direccion (norte,sur,este,oeste,noreste,sureste,noroeste,suroeste: ").lower()
            movimiento=Robot(pasos,direccion)
            self.Movimientos.push(movimiento)
    def volveraPartida(self):
        pilaux=Stack()

        while self.Movimientos.size()>0:
            value=self.Movimientos.pop()
            print(f"C3P-O vuelve {value.cantPasos} pasos desde el {value.direccion}")
            pilaux.push(value)
        print("y así llegó a su posición original")
        while pilaux.size()>0:
            value=pilaux.pop()
            self.Movimientos.push(value)

            


    
C3P_O=RoboPila()
C3P_O.cargarPasos()
C3P_O.volveraPartida()

