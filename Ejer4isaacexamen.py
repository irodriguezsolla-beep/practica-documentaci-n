list_temperaturas = []
list_dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
suma = 0
# Primero creamos una lista vacia y ota con los dias de la semana.
for i in list_dias:
    temp = int(input("Dime la temperatura de: "))
    list_temperaturas.append(temp)
    suma = temp + suma

media_temperaturas = suma /7
print("La temperatura media es: " ,str(media_temperaturas))
'''La siguiente función lo que hace es calcular cual es la temperatura que supera la media en la lista de temperaturas'''
def Superior(superior, medias):
        Super = []
        for t in superior:
            if t > medias:
                Super.append(t)
        return Super

print("La temperatura que se pasa de la media es: ", Superior(list_temperaturas, media_temperaturas))
