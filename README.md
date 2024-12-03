# Manipulando datos en JSON con Python

## Enunciado del ejercicio

Hay dos vehiculos. Uno de ellos es gris y el otro es negro. El gris es
una Toyota Hilux de 2018 y el negro es un Peugot 206 de 1985.
Ambos pertenecen a Juan Fernandez, un abogado de solo 26 anios.

Despues esta Sara Tustra, una mujer de 50 anios que se dedica a la
ingenieria electromecanica. Ella tiene una F-150 Raptor del 2023 de color
rosado.

## Notas

Usando el metodo **enumerate()** se puede obtener el indice y el valor
de los elementos en un ciclo **for**:

```python
for index, v in enumerate(p["vehiculo"]):
   print(f"- Vehiculo {index + 1}:")
   print(f"    Marca: {v['marca']}")
   print(f"    Modelo: {v['modelo']}")
   print(f"    Anio: {v['anio']}")
```

## Instrucciones de uso

1. **No es necesaria la configuracion de un entorno virtual**.

2. **Ejecutar el script**:
   - Ejecutar el script con el siguiente comando:

     ```bash
     python nombre_del_script.py
     ```

3. **Resultado**:
   - El script mostrara en la consola los datos de cada persona, sus vehiculos y el total de vehiculos.