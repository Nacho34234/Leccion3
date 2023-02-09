
diccionario={
    "Leo":"Motos",
    "Nacho":"Videojuegos",
    "Allan":"Gym",
    "Cristian":"Deporte Contacto",
    "Carlos":"Bici",
    "Jose":"Futbol",
    "Ithamar":"Comer"
    }
#print(diccionario["Nacho"])

diccionario["Kevin"]="leer"
#print(diccionario)

menu={"Hamburguesa":{
        "ingredientes":["pan", "tomate","carne","lechuga"],
        "precio":1500
        }
     "Tacos":{
        "ingredientes":["Repollo","Carne","Salsa"],
        "precio":700
     }
    }

#print(menu["Hamburguesa"]["ingredientes"][2])
print(menu.keys())
