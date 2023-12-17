# Guia 8
import re
#Ejercicio 1 a
def contarlineas()->int:
    nombre_archivo = input("ingrese el nombre del archivo: ")
    archivo = open(nombre_archivo,"r")
    cont:int = 0
    for lineas in archivo.readlines():
        cont+=1
    archivo.close() 
    return cont

#Ejercicio 1 b
def existepalabra(palabra_a_ver:str,nombre_archivo:str)->bool:
    archivo = open(nombre_archivo,"r")
    for linea in archivo.readlines():
        if palabra_a_ver in linea:
            print(linea)
            return True
    archivo.close()       
    return False

# Ejercicio 1 c
def cantidadapariciones(palabra_a_ver:str,nombre_archivo:str)->int:
    archivo = open(nombre_archivo,"r")
    cont:int=0
    for linea in archivo:
        for palabra in linea.split():
            if palabra_a_ver == palabra:
                cont+=1
    return cont

# Ejercicio 2
def clonarsincomentarios(nombre_archivo:str):
    archivo = open(nombre_archivo,"r")
    clonado = open("clonado.txt","w")
    for linea in archivo.readlines():
        if linea[0] != "#": # Si el primer caracter de la linea es un # entonces no escribe la linea
            clonado.write(linea)
    archivo.close()
    clonado.close()

# Ejercicio 3
def invertirtexto(nombre_archivo:str):
    archivo = open(nombre_archivo,"r")
    reverso = open("reverso4.txt","w")
    lineasInversas = archivo.readlines()[0:0:-1]
    reverso.writelines(lineasInversas)
    archivo.close()
    reverso.close()

# Ejercicio 4
def frasefinal(nombre_archivo:str,frase:str):
    with open(nombre_archivo,"a") as archivo:
        archivo.writelines("\n"+frase)
# Ejercicio 5
def fraseinicial(nombre_archivo:str,frase:str):
    with open(nombre_archivo,"r") as orig:
        origtext = orig.read()
        with open(nombre_archivo,"w") as orig:
            orig.write(frase+"\n")
            orig.write(origtext)

# Ejercicio 6
def binariolegible(nombre_archivo):
    with open(nombre_archivo,"rb") as archivo:
        contenido = archivo.read()
        contenido_texto = contenido.decode('utf-8')
            # Divide la cadena de texto en palabras
        lista_palabras = re.split('[^\w_]+',contenido_texto) # Use la libreria re para usar el comando re.split(delimitador, texto/archivo)
                                # dentro de las comillas estan los delimitadores, \w es para decir caracter alfanumerico y [^] para indicar la negacion de esto
                                # entonces queda que separa las palabras si no es una seguidilla de caracteres alfanumericos o guion bajo.
            # Filtra las palabras con 5 o más letras y las agrega a la lista
        palabras = [palabra for palabra in lista_palabras if len(palabra) >= 5]
    return palabras
# La verdad que no se como mejorarlo. Lo hice con ayuda de chatgpt
# hace mas o menos lo que deberia pero por ejemplo si es tiene una parte de string como otorrino\?naringologico lo toma como dos palabras validas y no como una invalida.

# sacando el ""detallito"" creo que hace lo que tendria que hacer.

# Ejercicio 7
# Mirar Ejercicio aparte
# Ejercicio 19
def agrupar_por_longitud(nombrearchivo:str)->dict:
    resdict = {}
    with open(nombrearchivo,'r') as archivo:
        texto = archivo.read().split()
        print(len(texto))
        for palabra in texto:
            if len(palabra) not in resdict:
                resdict[len(palabra)] = 0
                resdict[len(palabra)] +=1
            else:
                resdict[len(palabra)] +=1
        return resdict


# Ejercicio 20
def lupromedios(libretauni:str)->dict:
    resdict = {}
    with open(libretauni,'r') as libreta:
        lu = libreta.readlines()
        for linea in lu[1::]:
            row = linea.split()
            for dato in row:
                datosexamen = dato.split(',')
                numerolibreta = datosexamen[0]
                nota = datosexamen[3]
                if datosexamen[0] not in resdict:
                    resdict[numerolibreta] = {}
                    resdict[numerolibreta]['nota'] = 0
                    resdict[numerolibreta]['nota'] += int(nota)
                    resdict[numerolibreta]['cantidadnotas'] = 0
                    resdict[numerolibreta]['cantidadnotas'] += 1
                else:
                    resdict[numerolibreta]['nota'] += int(nota)
                    resdict[numerolibreta]['cantidadnotas'] += 1
            resdict[numerolibreta]['promedio'] = resdict[numerolibreta]['nota'] / resdict[numerolibreta]['cantidadnotas']
        res = {}
        for alumno in resdict:
            res[alumno] = resdict[alumno]['promedio']
    return res
# a fuerza bruta lo hice, funcionar funciona pero se puede mejorar MUCHISIMO.
