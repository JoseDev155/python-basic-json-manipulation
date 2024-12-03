import json

# Abrimos el archivo JSON que contiene la informacion de las personas
with open("./data/info.json") as file:
    # Cargamos el contenido del archivo JSON en la variable "data"
    data = json.load(file)

# Inicializamos el contador de vehiculos en 0
count_vehicles = 0

# Iteramos sobre la lista de personas contenida en el JSON
for p in data["personas"]:
    # Incrementamos el contador de vehiculos con el numero de vehículos de cada persona.
    count_vehicles += len(p["vehiculo"])
    
    # Imprimimos la información de cada persona
    print(f"Nombre: {p['nombre']}")
    print(f"Edad: {p['edad']}")
    print(f"Profesión: {p['profesion']}")
    print("Vehiculos:")

    # Iteramos sobre la lista de vehículos de la persona
    for index, v in enumerate(p["vehiculo"]):
        # Imprimimos la información detallada de cada vehiculo
        print(f"- Vehiculo {index + 1}:")
        print(f"    Marca: {v['marca']}")
        print(f"    Modelo: {v['modelo']}")
        print(f"    Anio: {v['anio']}")
    
    # Imprimimos una línea en blanco para separar personas
    print("")

# Imprimimos el total de vehiculos contados
print(f"En total hay: {count_vehicles} vehiculos")