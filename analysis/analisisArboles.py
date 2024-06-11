import pandas as pd
from helpers.generarTabla import crearTablaHtml
from data.generators.generadorArboles import generarArboles

def analisisGenerarArboles():
    datosArboles = generarArboles()

    datosArbolesDf = pd.DataFrame(datosArboles,columns=['Corregimiento','Nombre','id','hectareasSembradas','EspeciesSembradas'])
    
    datosArbolesDf.replace('-',pd.NA,inplace=True)
    datosArbolesDf.replace('sin',pd.NA,inplace=True)
    datosArbolesDf.dropna(inplace=True)
    
    crearTablaHtml(datosArbolesDf, "arboles")

    print(datosArbolesDf)

analisisGenerarArboles()