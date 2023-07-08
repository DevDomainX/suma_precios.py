#!/usr/bin/env python3 
#creador: Hans Saldias
from colorama import init, Fore, Back, Style
init()
print(Style.BRIGHT+Fore.LIGHTYELLOW_EX+"""
Author:      Hans Saldias
Creado:      viernes 07 de julio 2023
Uso:         lista de compras sumar todo y dar el resultado final
Motivo:      practica de programacion
Lenguaje:    python
\n""")
print("""
                           ######################################
                           || lista de precios de supermercado ||
                           ######################################
      
\n\n""")
contador = 0
sumador = 0
print("Script para lista de precios, solo ingresa precios y estos se sumaran solos dando un resultado total\n\npara terminar y ver resultado ingresa 0\n\n")

while True:
    try:
        precio = int(input("Ingresa el precio del producto: "))
        sumador += precio
        contador +=1 
        if precio == 0:
            print(f"\nEl resultado de todos los productos es ${sumador} pesos\n")
            print("Gracias por usar mi script")
            break
    except ValueError:
        print("intente ingresar valores sin punto ni comas eje: $2000 Dosmil")