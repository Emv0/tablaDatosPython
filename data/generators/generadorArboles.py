import random

def generarArboles():
    listaDatos = []
    for i in range(1000):
        corregimiento = random.choice(['san sebastian de palmitas','san cristobal','altavista','san antonio de prado','santa elena'])
        nombreEncuestado = random.choice(['pedro paramo','sandra mor','martina la peligrosa','kevin albeiro','valentina mor','juan jimeno'])
        id = random.randint(0,1000000)
        hectareasSembradasUltimoAño = random.randint(10,40)
        especieSembrado = random.choice(['sauces','cocotero','nogales','encinos'])
        arbolesSembrados = ([corregimiento,nombreEncuestado,id,hectareasSembradasUltimoAño,especieSembrado])
        listaDatos.append(arbolesSembrados)
    return listaDatos


