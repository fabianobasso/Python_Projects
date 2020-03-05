#!/usr/bin/python3.6
from math import pi


def Circulo(raio):
    return (float(raio) ** 2) * pi 
    


if __name__ == "__main__":
    raio = input("Digite o valor do raio: ")
    area = Circulo(raio)
    print ( f'Calculo da Area do Circulo de raio: {raio} = {area}' )