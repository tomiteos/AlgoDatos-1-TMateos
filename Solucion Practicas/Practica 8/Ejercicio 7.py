# Ejercicio 7
import pandas as pd

def lucsv(lu:str):
    if lu.endswith('.xlsx'):
        contenido = pd.read_excel(lu, header=None)
        #print(contenido)
    elif lu.endswith('.csv'):
        contenido = pd.read_csv(lu,skiprows = 0)
        #print(contenido)
    nombres = contenido.iloc[:,0].values.flatten().tolist() #crea lista de nombre con los alumnos
    notas = contenido.iloc[:,3:].values.flatten().tolist() #crea lista de notas
    #print(nombres)
    #print(notas)
    promedios = {}
    for n in range(len(nombres)):
        alumno = nombres[n]
        nota = notas[n]
        if alumno not in promedios:
            promedios[alumno] = [nota,1]
        else:
                promedios[alumno][0] += nota
                promedios[alumno][1] += 1
    for alumno ,(sumanotas,cantidadnotas) in promedios.items():
            promedios[alumno] = round(sumanotas/cantidadnotas,1)
    print(promedios)
    return promedios

lucsv('lu.xlsx')

    """ 
        La funcion lee el archivo ingresado (xlsx o csv) y devuelve un diccionario con el alumno y su promedio.

        Ya que se puede encontrar la forma de hacer el ejercicio solo para csv facilmente
        me tome la libertad de replicarlo para que funcione ademas con archivos de excel
        
        Lo que no me termina de convencer es haber usado un diccionario para representar el alumno y los promedios (pero se me ocurrio eso y le mande).
        Seguro se puede usar una lista para hacerse mas facil.
    """