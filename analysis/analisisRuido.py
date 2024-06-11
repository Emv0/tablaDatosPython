import pandas as pd
from helpers.generarTabla import crearTablaHtml
from data.generators.generadorRuido import generarRuido

def analisisRuido():

    datosRuido = generarRuido()

    generarRuidoDf = pd.DataFrame( datosRuido,columns=[ 'Comuna', 'TtlPoblacion', 'tamañoMuestra', 'dcblsNoche', 'dcblsDia', 'nombreEdificio', 'fechaEncuesta', 'nombreEncuestado', 'Id' ] )

    generarRuidoDf.replace( 'sin', pd.NA, inplace=True )
    generarRuidoDf.replace( '-', pd.NA,inplace=True )
    generarRuidoDf.dropna( inplace=True )
    
    dcblsNoche = generarRuidoDf[ 'dcblsNoche' ].mean()
    dcblsDia = generarRuidoDf[ 'dcblsDia' ].mean()
    
    crearTablaHtml( generarRuidoDf, "ruido" )
    
    print( generarRuidoDf, "Promedio de ruido en el día: {:.0f}".format(dcblsDia), "Promedio de ruido en la noche: {:.0f}".format(dcblsNoche))

analisisRuido()