import random

def generadorGastoAgua():
    listaDatos = []
    for i in range(1000):
        corregimiento = random.choice(['san sebastian de palmitas','san cristobal','altavista','san antonio de prado','santa elena'])
        nombreEncuestado = random.choice(['pedro paramo','sandra mor','martina la peligrosa','kevin albeiro','valentina mor','juan jimeno'])
        id = random.randint(0,1000000)
        registroContador = random.randint(0,1000000)
        gastoAgua = [corregimiento,nombreEncuestado,id,registroContador]
        listaDatos.append(gastoAgua)

    return listaDatos

