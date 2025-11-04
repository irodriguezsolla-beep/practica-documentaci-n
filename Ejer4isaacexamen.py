list_temperaturas = []
list_dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
suma = 0
'''El siguiente bucle lo que hace es pededir un numero 7 veces moviendonos en la lista de dias de la semana '''
for i in list_dias:
    temp = int(input("Dime la temperatura de: "))
    list_temperaturas.append(temp)
    suma = temp + suma

media_temperaturas = suma /7
print("La temperatura media es: " ,str(media_temperaturas))

'''La siguiente función lo que hace es calcular cual es la temperatura que supera la media en la lista de temperaturas'''
def calcularSuperior(superior, medias):
        Super = []
        for t in superior:
            if t > medias:
                Super.append(t)
        return Super

print("La temperatura que se pasa de la media es: ", calcularSuperior(list_temperaturas, media_temperaturas))
