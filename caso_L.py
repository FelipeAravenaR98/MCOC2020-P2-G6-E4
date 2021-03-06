from reticulado import Reticulado
from barra import Barra
from math import *

def caso_L():
    

    # Unidades base
    m = 1.
    kg = 1.
    s = 1. 
    
    #Unidades derivadas
    N = kg*m/s**2
    cm = 0.01*m
    mm = 0.001*m
    KN = 1000*N
    
    Pa = N / m**2
    KPa = 1000*Pa
    MPa = 1000*KPa
    GPa = 1000*MPa
    
    #Parametros
    L1 = 5.0  *m
    L2 = 2 * m
#    F = 100*KN
    qL = ((400*kg)/(m**2))
    
    
    #Inicializar modelo
    ret = Reticulado()
    
    #Nodos
    ret.agregar_nodo(0     , 0   ,  0         )
    ret.agregar_nodo(L1     , 0   ,  0         )
    ret.agregar_nodo(2*L1   , 0   ,  0         )
    ret.agregar_nodo(3*L1   , 0   ,  0         )  
    
    ret.agregar_nodo(L1/2     , L2/2   , 3.5         )
    ret.agregar_nodo(L1 + L1/2     , L2/2   , 3.5)
    ret.agregar_nodo(2*L1 + L1/2   , L2/2   , 3.5          )
    
    ret.agregar_nodo(0   , L2 , 0)
    ret.agregar_nodo(L1 , L2 , 0)
    ret.agregar_nodo(2*L1   , L2   ,  0         )
    ret.agregar_nodo(3*L1   , L2   ,  0         )  
    
    
    
    
    
    #Barras

    props = [8*cm, 5*mm, 200*GPa, 0*7600*kg/m**3, 420*MPa]

    
    
    ret.agregar_barra(Barra(0, 1, *props))   # 0
    ret.agregar_barra(Barra(1, 2, *props))   # 1
    ret.agregar_barra(Barra(2, 3, *props))   # 2
    ret.agregar_barra(Barra(3, 10, *props))  # 3
    ret.agregar_barra(Barra(9, 10, *props))  # 4
    ret.agregar_barra(Barra(8, 9, *props))   # 5
    ret.agregar_barra(Barra(7, 8, *props))   # 6
    ret.agregar_barra(Barra(0, 7, *props))   # 7
    ret.agregar_barra(Barra(1, 7, *props))   # 8
    ret.agregar_barra(Barra(0, 8, *props))   # 9
    ret.agregar_barra(Barra(1, 8, *props))   # 10
    ret.agregar_barra(Barra(2, 8, *props))   # 11
    ret.agregar_barra(Barra(1, 9, *props))   # 12
    ret.agregar_barra(Barra(2, 9, *props))   # 13
    ret.agregar_barra(Barra(3, 9, *props))   # 14
    ret.agregar_barra(Barra(2, 10, *props))  # 15
    ret.agregar_barra(Barra(4, 7, *props))   # 16
    ret.agregar_barra(Barra(0, 4, *props))   # 17
    ret.agregar_barra(Barra(4, 8, *props))   # 18
    ret.agregar_barra(Barra(1, 4, *props))   # 19
    ret.agregar_barra(Barra(5, 8, *props))   # 20
    ret.agregar_barra(Barra(1, 5, *props))   # 21
    ret.agregar_barra(Barra(5, 9, *props))   # 22
    ret.agregar_barra(Barra(2, 5, *props))   # 23
    ret.agregar_barra(Barra(6, 9, *props))   # 24
    ret.agregar_barra(Barra(2, 6, *props))   # 25
    ret.agregar_barra(Barra(6, 10, *props))  # 26
    ret.agregar_barra(Barra(3, 6, *props))   # 27
    ret.agregar_barra(Barra(4, 5, *props))   # 28
    ret.agregar_barra(Barra(5, 6, *props))   # 29
    
    
    ret.agregar_restriccion(0, 0, 0)
    ret.agregar_restriccion(0, 1, 0)
    ret.agregar_restriccion(0, 2, 0)
    
    ret.agregar_restriccion(7, 0, 0)
    ret.agregar_restriccion(7, 1, 0)
    ret.agregar_restriccion(7, 2, 0)
    
    ret.agregar_restriccion(3, 1, 0)
    ret.agregar_restriccion(3, 2, 0)
    
    ret.agregar_restriccion(10, 1, 0)
    ret.agregar_restriccion(10, 2, 0)
    
    qL1 = -qL*(7.5*m**2)* 9.8
    qL2 =  -qL*(15*m**2)* 9.8
    
    ret.agregar_fuerza(0, 2, qL1)
    ret.agregar_fuerza(3, 2, qL1)
    ret.agregar_fuerza(7, 2, qL1)
    ret.agregar_fuerza(10, 2, qL1)
    
    ret.agregar_fuerza(1, 2, qL2)
    ret.agregar_fuerza(2, 2, qL2)
    ret.agregar_fuerza(8, 2, qL2)
    ret.agregar_fuerza(9, 2, qL2)
    
    return ret
    
