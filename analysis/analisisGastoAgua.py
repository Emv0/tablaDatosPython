import pandas as pd

from data.generators.generadorGastoAgua import generadorGastoAgua

def analisisGastoAgua():

    datosGastoAgua = generadorGastoAgua()

    datosGastoAguaDf = pd.DataFrame(datosGastoAgua,columns=['Corregimiento','Nombre','Id','RegistroContador'])

    print(datosGastoAguaDf)

analisisGastoAgua()
