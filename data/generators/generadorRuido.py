from faker import Faker
import random

fake = Faker('es_Co')

def generarRuido():
    listaDatos = []
    for i in range(1000):
        comuna = random.choice(['comuna 1 popular','comuna 2 sta cruz','comuna 12 la america','comuna 4 aranjuez','comuna 13 san javier', 'comuna 16 belen'])
        totalPoblacion = random.choice(['3000','4500','5000','10000'])
        tamanoMuestra = random.randint(20,int(totalPoblacion))
        decibelesNoche = random.choice([20, 30, 40, 50, 60, 70, 80, 90, 100])
        decibelesDia = random.choice([20, 30, 40, 50, 60, 70, 80, 90, 100])
        fechaEncuestada = random.choice(['2024/05/14','2024/05/15'])
        nombreEncuestado = fake.name()
        nombreEdificio = random.choice(['Ruiseñor','Ruiseñor 2','Montemar','Montemar 2','Cespedes','El castillo','El castillo 2','Vicuña','Vicuña 2','-','sin'])
        id = random.randint(0,1000000)
        ruidoGenerado = [comuna,totalPoblacion,tamanoMuestra,decibelesDia,decibelesNoche,nombreEdificio,fechaEncuestada,nombreEncuestado,id]
        listaDatos.append(ruidoGenerado)

    return listaDatos
