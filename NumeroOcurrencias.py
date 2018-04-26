# texto determinado por uno mismo
texto = 'hola mi nombre es Miguel Angel hola Miguel'

# Creamos una lista apartir del texto con split
palabraslist = texto.split()

# creamos un arreglo vacio
OcurrenciaPalabras = []

# utilizamos el ciclo for para contar las palabras de la lista
# usamos append para agregar elementos a una lista o arreglo
for a in palabraslist:
    OcurrenciaPalabras.append(palabraslist.count(a))

# uzamos str para convertir los objetos en cadenas,
# el lista para crear una lista y el zip para que coincidan los  2 arreglo
lista = str(list(zip(palabraslist, OcurrenciaPalabras)))
print(lista)
