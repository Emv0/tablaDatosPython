import pandas as pd

from data.generators.generadorRuido import generarRuido

def analisisRuido():

    datosRuido = generarRuido()

    generarRuidoDf = pd.DataFrame(datosRuido,columns=['Comuna','TtlPoblacion','tamanoMuestra','dcblsNoche','dcblsDia','nombreEdificio','fechaEncuesta','nombreEncuestado','Id'])

    print(generarRuidoDf)

analisisRuido()