#Funcion generica para convertir un df en html

def crearTablaHtml(dataFrame,nombreTabla):
    #volvemos el dataframe en html
    archivoHTML = dataFrame.to_html()

    archivo = open(f"./tables/{nombreTabla}.html","w")
    #Escribimos la info en el archivo
    archivo.write(
    '''
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            ''')
    archivo.write(archivoHTML)
    archivo.write(
        '''
        </body>
        </html>
        '''
    )
    archivo.close()
        