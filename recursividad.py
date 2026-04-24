from random import choice, shuffle
##5to ejercicio
romanos={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500, "M":1000}
num=input("ingrese un número romano: ").upper()
def numrom(num: str) -> int:
    if len(num)==0:
        return 0
    if len(num)==1:
        return romanos [num[0]] 
    if romanos [num[0]] < romanos[num[1]]: 
        return - romanos[num[0]] + numrom(num[1:]) 
    else: 
        return romanos[num[0]] + numrom(num[1:]) 

print(numrom(num))



##ejercicio 22
mochila= ["Manzana","Túnica","guantes", "agua", "sanguche", "sable de madera","mapa", "cigarrillo"]

if choice([True,False]):
    mochila.append("sable de luz")

shuffle(mochila)
cont=-1

def usar_la_fuerza(cont:int, mochila: list)-> str:
    cont+=1
    aux=mochila.pop()
    if aux=="sable de luz":
    
        return f"Con ayuda de la fuerza consegui el {aux} despues de sacar {cont} objetos de la mochila! fue el objeto número {cont+1}"
    
    if len(mochila)==0:
        return "Me olvidé de ponerlo en la mochila, no puedo escapar..."
    
    else:
        return usar_la_fuerza(cont,mochila)
    

print(usar_la_fuerza(cont,mochila))
    