import pandas as pd

from data.generators.generadorCalidadAgua import generadorCalidadAgua

def analisisCalidadAgua():

    datosCalidadAgua = generadorCalidadAgua()

    datosCalidadAguaDf = pd.DataFrame(datosCalidadAgua,columns=['Comuna','Nombre','Id','SaborAgua','ColorAgua'])

    print(datosCalidadAguaDf)

analisisCalidadAgua()

