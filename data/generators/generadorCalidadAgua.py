import random

def generadorCalidadAgua():
    listaDatos = []
    for i in range(1000):
        comuna = random.choice(['comuna 1 popular','comuna 2 sta cruz','comuna 12 la america','comuna 4 aranjuez','comuna 13 san javier', 'comuna 16 belen'])
        nombreEncuestado = random.choice(['pedro paramo','sandra mor','martina la peligrosa','kevin albeiro','valentina mor','juan jimeno'])
        id = random.randint(0,1000000)
        saborAgua = random.choice(['Buena','Regular','Mala'])
        colorAgua = random.choice(['trasparente','Blanca','Marron'])
        calidadAgua = [comuna,nombreEncuestado,id,saborAgua,colorAgua]
        listaDatos.append(calidadAgua)
        
    return listaDatos



