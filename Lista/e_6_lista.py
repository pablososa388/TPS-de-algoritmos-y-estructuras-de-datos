

from list_ import List


superheroes = [
    {
      "nombre": "Spider-Man",
      "anio_aparicion": 1962,
      "casa": "Marvel",
      "biografia": "Peter Parker fue mordido por una araña radiactiva y obtuvo poderes de superhéroe. Trabaja como fotógrafo freelance en el Daily Bugle mientras protege Nueva York."
    },
    {
      "nombre": "Iron Man",
      "anio_aparicion": 1963,
      "casa": "Marvel",
      "biografia": "Tony Stark, genio multimillonario e inventor, construyó una armadura tecnológica para escapar de sus captores. Fundador de los Vengadores y director de Stark Industries."
    },
    {
      "nombre": "Wolverine",
      "anio_aparicion": 1974,
      "casa": "Marvel",
      "biografia": "Logan posee un esqueleto recubierto de adamantium y garras retráctiles. Su factor de curación acelerada lo hace casi inmortal. Miembro icónico de los X-Men."
    },
    {
      "nombre": "Thor",
      "anio_aparicion": 1962,
      "casa": "DC",
      "biografia": "Dios nórdico del trueno e hijo de Odín. Empuña el martillo Mjolnir y defiende tanto Asgard como la Tierra. Miembro fundador de los Vengadores."
    },
    {
      "nombre": "Black Widow",
      "anio_aparicion": 1964,
      "casa": "Marvel",
      "biografia": "Natasha Romanoff fue entrenada desde niña en el programa Habitación Roja. Es una espía y agente de élite de S.H.I.E.L.D., experta en artes marciales y tecnología."
    },
    {
      "nombre": "Batman",
      "anio_aparicion": 1939,
      "casa": "DC",
      "biografia": "Bruce Wayne presenció el asesinato de sus padres de niño y juró proteger Gotham. Sin poderes, usa su inteligencia, fortuna y entrenamiento físico para combatir el crimen. Usando un traje con muchas herramientas"
    },
    {
      "nombre": "Superman",
      "anio_aparicion": 1938,
      "casa": "DC",
      "biografia": "Kal-El fue enviado desde el planeta Krypton antes de su destrucción. Adoptado como Clark Kent en Kansas, usa sus poderes solares para defender la Tierra."
    },
    {
      "nombre": "Mujer Maravilla",
      "anio_aparicion": 1941,
      "casa": "DC",
      "biografia": "Diana, princesa de las Amazonas de la isla Temyscira, fue criada como guerrera. Porta el lazo de la verdad y las brazaletes indestructibles. Embajadora de paz y justicia."
    },
    {
      "nombre": "The Flash",
      "anio_aparicion": 1956,
      "casa": "DC",
      "biografia": "Barry Allen era un científico forense que fue alcanzado por un rayo durante un experimento. Obtuvo la capacidad de moverse a velocidades superlumínicas conectado a la Fuerza de la Velocidad."
    },
    {
      "nombre": "Green Lantern",
      "anio_aparicion": 1959,
      "casa": "DC",
      "biografia": "Hal Jordan fue elegido por el anillo de poder de los Guardianes del Universo. El anillo le permite crear construcciones de energía verde limitadas solo por su voluntad e imaginación."
    },
    {
        "nombre": "Dr. Strange",
        "anio_aparicion": 1963,
        "casa": "DC",
        "biografia": "Stephen Strange, un neurocirujano brillante, sufrió un accidente que le impidió continuar con su carrera. Tras viajar al Tíbet, aprendió las artes místicas y se convirtió en el Hechicero Supremo."
    },
    {
    "nombre": "Capitana Marvel",
    "anio_aparicion": 1968,
    "casa": "Marvel",
    "biografia": "Carol Danvers, una piloto de la Fuerza Aérea, obtuvo poderes extraordinarios tras un accidente relacionado con tecnología alienígena. Se convirtió en una de las heroínas más poderosas del universo Marvel."
},
{
    "nombre": "Star-Lord",
    "anio_aparicion": 1976,
    "casa": "Marvel",
    "biografia": "Peter Quill, conocido como Star-Lord, fue abducido de la Tierra cuando era niño y creció como un aventurero espacial. Lidera a los Guardianes de la Galaxia y utiliza sus habilidades de combate, sus blásters y su ingenio para proteger el universo."
}
]




class Superhero():

    def __init__(self, nombre, anio, casa, bio):
        self.name = nombre
        self.year = anio
        self.house = casa
        self.bio = bio

    def __str__(self):
        return f"{self.name} - {self.year} - {self.house}"

def by_name(item):
    return item.name

def by_year(item):
    return item.year
def by_house(item):
    return item.house

list_heroes = List()
list_heroes.add_criterion('name', by_name)
list_heroes.add_criterion('year', by_year)
list_heroes.add_criterion('house',by_house)

for hero in superheroes:
    list_heroes.append(
        Superhero(hero['nombre'], hero['anio_aparicion'], hero['casa'], hero['biografia'])
    )

#eliminar el nodo que contiene la información de Linterna Verde;
print("linterna verde eliminado: ")
deleted_value = list_heroes.delete_value("Green Lantern", 'name')
print(f'valor eliminado {deleted_value}')

print()
# mostrar el año de aparición de Wolverine
wolverine = list_heroes.search("Wolverine", 'name')
if wolverine is not None:
    print(f'el año de aparición de {list_heroes[wolverine].name} es {list_heroes[wolverine].year}')
else:
    print('no está en la lista')

# c. cambiar la casa de Dr. Strange a Marvel
print("la casa de strange es ahora marvel:")
strange = list_heroes.search("Dr. Strange", 'name')
if strange is not None:
    list_heroes[strange].house = 'Marvel'
    print(list_heroes[strange])

print()
# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# “traje” o “armadura”;
print("pjs con traje o armadira en su bio")
list_heroes.filter_contain_on_bio(['traje', 'armadura'])

print()
# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# sea anterior a 1963;
print("nombre y casa de pjs con fecha de aparición anterior a 1963: ")
for hero in list_heroes:
    if hero.year < 1963:
        print(hero)

print()
# h. listar los superhéroes que comienzan con la letra B, M y S;
print("superhéroes que comienzan con letra B, M y/o S")
list_heroes.filter_start_with(('B', 'M', 'S'))
print()
# mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
cmarvel=list_heroes.search("Capitana Marvel",'name')
if cmarvel is not None:
    print(f"la casa de capitana marvel es: {list_heroes[cmarvel].house}")
print()
wwoman= list_heroes.search("Mujer Maravilla", 'name')
if wwoman is not None:
    print(f"La casa de la wonder woman es: {list_heroes[wwoman].house}")
print()

# g. mostrar toda la información de Flash y Star-Lord;
print("info de flash y starlord")
flash=list_heroes.search("The Flash",'name')
if flash is not None:
    print(f"info de The Flash: {list_heroes[flash]}")

print()
slord=list_heroes.search("Star-Lord",'name')
if slord is not None:
    print(f"info de Star lord: {list_heroes[slord]}")
    
# list_heroes.sort_by_criterion('year')
# list_heroes.show()
# determinar cuántos superhéroes hay de cada casa de comic.
# cmvel=0
# cdece=0
# for s in list_heroes:
   
#     if s.house=="Marvel":
#         cmvel+=1
#     elif s.house=="DC":
#         cdece+=1
# print existen  
print("héroes de Marvel: ")
list_heroes.filter_contain_on_casa(["marvel"])

print()
print("héroes de DC: ")
list_heroes.filter_contain_on_casa(["dc"])