import random

def generarRuido():
    listaDatos = []
    for i in range(1000):
        comuna = random.choice(['comuna 1 popular','comuna 2 sta cruz','comuna 12 la america','comuna 4 aranjuez','comuna 13 san javier', 'comuna 16 belen'])
        totalPoblacion = random.choice(['3000','4500','5000','10000'])
        tamanoMuestra = random.choice(['1000','2000','3500','6000'])
        decibelesNoche = random.choice(['20','30','40'])
        decibelesDia = random.choice(['20','30','40'])
        fechaEncuestada = random.choice(['2024/05/14','2024/05/15'])
        nombreEncuestado = random.choice(['pedro paramo','sandra mor','martina la peligrosa','kevin albeiro','valentina mor','juan jimeno'])
        nombreEdificio = random.choice(['ruiseñor','ruiseñor 2','montemar','montemar 2','cespedes'])
        id = random.randint(0,1000000)
        ruidoGenerado = [comuna,totalPoblacion,tamanoMuestra,decibelesDia,decibelesNoche,nombreEdificio,fechaEncuestada,nombreEncuestado,id]
        listaDatos.append(ruidoGenerado)

    return listaDatos
