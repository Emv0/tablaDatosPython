import pandas as pd
from helpers.generarTabla import crearTablaHtml

from data.generators.generadorCalidadAire import generarDatosCalidadAire

#1. PARA ANALIZAR DATOS CON PYTHON DEBEMOS CONSTRUIR UN DATAFRAME

def construirDataFrameCalidadAire():
    #TRAIGO LOS DATOS GENERADOS EN EL MOCK
    datosCalidadAire = generarDatosCalidadAire()

    #CONSTRUYO EL DATAFRAME
    calidadAireDf = pd.DataFrame(datosCalidadAire,columns=['Comuna','Ttlpob','Muestra','ICA','Fecha','Nombre','id'])

    #PROBANDO
    print(calidadAireDf)
    crearTablaHtml(calidadAireDf,"calidadAire")

construirDataFrameCalidadAire()