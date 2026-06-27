# Variables
name = "Fernanda"
last_name = "Gonzalez"

# print(name)
#operadores matematicos 
num1 = 10
num2 = 5
suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
div = num1 / num2

# print(suma)
# print(resta)
# print(multi)
# print(div)

# print(f"El resultado de la suma es: {suma}")
# print(f"El resultado de la resta es: {resta}")
# print(f"resultado : {multi}")
# print(f"resultado : {div}")

# operadores de comparacion
#mayor que >
#menor que <
#mayor o igual que >=
#menor o igual que <=
#igual que ==
#diferente que !=

# print(num1 > num2)
# print(num1 <= num2)
# print(num1 == num2)
# print(num1 != num2)

#condicionales
# if num1 > num2:
#     print(f"{num1} es mayor que {num2}")
# if num2 > num1:
#     print(f"{num1} es mayor que {num2}")
# else:
#     print(f"{num2} es menor que {num1}")

#condicionales anidados
# edad = 19
# genero = "mujer"
# dia = "sabado"

# if edad >= 18:
#     if genero == "mujer":
#         if dia == "jueves":
#             print("puedes pasar")
#         else:
#             print("no puedes pasar, solo el jueves")
#     else:
#         print("no puedes pasar, solo mujer")
# else:
#     print("No eres mayor de edad, NO PUEDES pasar")

#operadores logicos
# if (edad >= 18) and (genero == "mujer") and ((dia == "jueves") or (dia == "sabado")):
#     print("puedes pasar")
# else:
#     print("no puedes pasar")

#condicionales encadenados para identificar el fin de semana
# if dia == "viernes ":
#     print("hoy es viernes fin de semana ")

# elif dia == "sabado":
#     print("hoy es sabado fin de semana ")

# elif dia == "domingo":
#     print("hoy es domingo fin de semana ")

# else:
#     print("hoy es un dia laboral")


player1 = "Messi"
player2 = "Ronaldo" 
sel_p1 = "tijera"
sel_p2 = "piedra"

print(f"Messi eligio {sel_p1}")
print(f"Ronaldo eligio {sel_p2}")

if sel_p1 == "piedra" and sel_p2 == "tijera":
    print("Messi gana")
elif sel_p2 == "piedra" and sel_p1 == "tijera":
    print("Ronaldo gana")
elif sel_p1 == "papel" and sel_p2 == "piedra":
    print("Messi gana")
elif sel_p2 == "papel" and sel_p1 == "piedra":
    print("Ronaldo gana")
elif sel_p1 == "tijera" and sel_p2 == "papel":
    print("Messi gana") 
elif sel_p2 == "tijera" and sel_p1 == "papel":
    print("Ronaldo gana")
else:
    print("Empate")

#estructura de datos 
#listas