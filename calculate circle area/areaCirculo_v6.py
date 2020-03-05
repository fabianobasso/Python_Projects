#!/usr/bin/python3.6
from math import pi
import sys 

def Circulo(raio):
    return (float(raio) ** 2) * pi 
    


if __name__ == "__main__":
    raio = sys.argv[1]
    area = Circulo(raio)
    print ( f'Calculo da Area do Circulo de raio: {raio} = {area}' )