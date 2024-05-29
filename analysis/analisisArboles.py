import pandas as pd

from data.generators.generadorArboles import generarArboles

def analisisGenerarArboles():
    datosArboles = generarArboles()

    datosArbolesDf = pd.DataFrame(datosArboles,columns=['Corregimiento','Nombre','id','hectareasSembradas','EspeciesSembradas'])

    print(datosArbolesDf)

analisisGenerarArboles()