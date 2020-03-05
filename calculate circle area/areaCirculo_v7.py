#!/usr/bin/python3.6
from math import pi
import sys 

def Circulo(raio):
    return (float(raio) ** 2) * pi 


def Help():
    print ("É necessário informar o raio do círculo")
    print (f"Sintaxe: {sys.argv[0][2:]}  <raio>")


if __name__ == "__main__":
    if len(sys.argv) < 2: # O argv recebe uma lista onde o primeiro sempre é o nome da função
        Help()
    elif not sys.argv[1].isnumeric():
        Help()
        print ("O raio deve ser um valor númerico")
    else:    
        raio = sys.argv[1]
        area = Circulo(raio)
        print ( f'Calculo da Area do Circulo de raio: {raio} = {area}' )