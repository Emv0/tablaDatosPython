import random
from faker import Faker

fake = Faker('es_Co')

def generarArboles():
    listaDatos = []
    for i in range(1000):
        corregimiento = random.choice(['San Sebastian de Palmitas','San Cristobal','Altavista','San Antonio de Prado','Santa Elena'])
        nombreEncuestado = fake.name()
        id = random.randint(0,1000000)
        hectareasSembradasUltimoAño = random.choice([10,20,30,40,50,60,70])
        especieSembrado = random.choice(['sauces','cocotero','nogales','encinos','sin','-'])
        arbolesSembrados = ([corregimiento,nombreEncuestado,id,hectareasSembradasUltimoAño,especieSembrado])
        listaDatos.append(arbolesSembrados)
        
        
    return listaDatos


