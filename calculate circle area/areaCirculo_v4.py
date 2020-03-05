#!/usr/bin/python3.6
from math import pi

if __name__ == "__main__":
    raio = input("Digite o valor do raio: ")
    area = (float(raio) ** 2) * pi 
    print ( f'Calculo da Area do Circulo de raio: {raio} = {area}' )