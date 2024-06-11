import pandas as pd
from helpers.generarTabla import crearTablaHtml
from data.generators.generadorCalidadAire import generarDatosCalidadAire

#1. PARA ANALIZAR DATOS CON PYTHON DEBEMOS CONSTRUIR UN DATAFRAME

def construirDataFrameCalidadAire():
    #TRAIGO LOS DATOS GENERADOS EN EL MOCK
    datosCalidadAire = generarDatosCalidadAire()

    #CONSTRUYO EL DATAFRAME
    calidadAireDf = pd.DataFrame(datosCalidadAire,columns=['Comuna','Ttlpob','Muestra','ICA','Fecha','Nombre','id'])

    #LIMPIANDO EL DF

    #1. LIMPIANDO (REEMPLAZANDO VALORES)
    # print(calidadAireDf)
    calidadAireDf.replace('-',pd.NA,inplace=True)
    calidadAireDf.replace('sin',pd.NA,inplace=True)

    #2. Limpiando (Eliminando valores)
    calidadAireDf.replace('sin',pd.NA,inplace=True)
    calidadAireDf.dropna(inplace=True)

    #3. Filtrando datos para depurar la informacion
    #filtrar dtos es obtener nuevos datagrames
    #al aplicar condiciones logicas

    #Contar Datos

    #Consultar datos especificos
    # filtroICAPositivo = calidadAireDf.query("(ICA>=20)and(ICA<50)")
    # filtroICAModerado = calidadAireDf.query("(ICA>=50)and(ICA<70)")
    # filtroICAPeligroso = calidadAireDf.query("(ICA>=70)").value_counts()


    # print(filtroICAPositivo)
    # print(filtroICAModerado)
    # print(filtroICAPeligroso)

    #PROBANDO
    # print("\n")
    print(calidadAireDf)
    crearTablaHtml(calidadAireDf, "calidadAire")


construirDataFrameCalidadAire()