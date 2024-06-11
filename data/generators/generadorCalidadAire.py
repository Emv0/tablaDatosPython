#Rutina para generar de forma aleatoria multiples datos con python
from faker import Faker
import random


fake = Faker('es_Co')

def generarDatosCalidadAire():
    listaDatos = []
    for i in range(1000):
        comuna = random.choice(['comuna 1 popular','comuna 2 sta cruz','comuna 12 la america','comuna 4 aranjuez','comuna 13 san javier', 'comuna 16 belen','sin','-'])
        totalPoblacion = random.choice(['3000','4500','5000','10000'])
        tamanoMuestra = random.randint(0,int(totalPoblacion))
        ica = random.randint(20,100)
        fechaEncuestada = fake.date_between(start_date='-1y',end_date='now')
        nombreEncuestado = fake.name()
        id = random.randint(0,1000000)
        calidadAire = [comuna,totalPoblacion,tamanoMuestra,ica,fechaEncuestada,nombreEncuestado,id]

        listaDatos.append(calidadAire)
    return listaDatos
