
class Generarnuevagramatica():
    def __init__(self,nombre):
        self.nombre=nombre

    def siexiste(self,vector,nombre,posicion):
        si = False
        for x in vector:
            if nombre == x[posicion]:
                si = True
        return si

    def ingresarnoterminales(self):
        fin = True
        vector = []
        siexiste = False
        while (fin == True):
            siexiste = False
            print("Ingrese el no terminal que desea agregar: ")
            estadoa = input()
            for x in vector:
                if (estadoa == x):
                    print("El terminal ya está repetido, vuelva a ingresar otro")
                    siexiste = True
            if (siexiste == False):
                vector.append(estadoa)
                print("Terminal agregado con éxito")
            print("Desea agregar otro más? s/n ")
            paso = input()
            if (paso == 'n'):
                fin = False
        return vector

    def ingresarterminales(self):
        fin = True
        vector = []
        siexiste = False
        while (fin == True):
            siexiste = False
            print("Ingrese el terminal del lenguaje que desea agregar: ")
            alfabeto = input()
            for x in vector:
                if (alfabeto == x):
                    print("El terminal ingresado ya está repetido, vuelva a ingresar otro")
                    siexiste = True
            if (siexiste == False):
                vector.append(alfabeto)
                print("Terminal agregado con éxito")
            print("Desea agregar otro más? s/n ")
            paso = input()
            if (paso == 'n'):
                fin = False
            elif (paso != 's'):
                print("Caracter desconocido, se le volverá a preguntar por un nuevo terminal")
        return vector

    def terminalinicial(self,vector,cadena):
        siexiste = False
        for x in vector:
            if (cadena == x):
                siexiste = True
        if (siexiste == True):
            print("No terminal inicial ingresado con éxito")
            return cadena
        else:
            print("El no terminal inicial ingresado no coincide con los terminales ingresados antes o no hay terminales ingresados")

    def producciones(self,terminales,noterminales):
        fin=False
        produccionestotales=[]
        while fin==False:
            transiciones=[]
            paso = False
            paso1 = False
            esepsilon=False
            paso2 = False
            print("Ingrese las producciones: (bajo la instruccion Termina l> noTerminal Terminal: A > 0 B)")
            tran=input()
            transiciones=tran.split(" ")
            #Verificar que todos los terminales y no terminales existan
            for x in noterminales:
                if(x==transiciones[0]):
                    paso=True
            if(transiciones[1]!=">"):paso=False
            if(paso==True):
                if(transiciones[2]=="epsilon"):
                    paso1=True
                    paso2=True
                    esepsilon=True
                    print("Producccion con epsilon creada con éxito")
                #Evaluar si existe posicion [2]
                if(esepsilon==False):
                    for x in noterminales:
                        if(x==transiciones[2]):
                            paso1=True
                    for y in terminales:
                        if(y==transiciones[2]):
                            paso1=True
                    if(len(transiciones)==4):
                        for x in noterminales:
                            if (x == transiciones[3]):
                                paso2 = True
                        for y in terminales:
                            if (y == transiciones[3]):
                                paso2 = True
                    elif(len(transiciones)==3):
                        paso2=True
            if(paso and paso1 and paso2):
                print("Produccion ingresada con éxito")
                produccionestotales.append(tran)
            else:
                print("Error en el ingreso de los datos, verifique y vuelva a ingresarlos")

            print("Desea continuar ingresando producciones: s/n")
            paso=input()
            if(paso=='n'or paso=='N'):
                fin=True
            elif(paso!='s'):
                print("Caracter no reconocido, vuelva a intentarlo")
        return produccionestotales

    def gramaticatransformada(self,producciones,noterminales,terminales):
        grmsinrecursividadporizquierda=[]
        print("GRÁMATICA CON POSIBLE RECURSIVIDAD POR LA IZQUIERDA:")
        for y in producciones:
            print(y)
        print("GRÁMATICA SIN RECURSIVIDAD POR LA IZQUIERDA")
        siexisterecursividad=False
        paso = True
        yamodificado=[]
        cadena=""
        for y in producciones:
            paso=True
            transiciones=[]
            transiciones=y.split(" ")
            if(transiciones[0]==transiciones[2]):
                siexisterecursividad=True
                for x in yamodificado:
                    if (transiciones[0] == x and len(transiciones)==4):
                        cadena=transiciones[0]+"p > "+transiciones[3]+" "+transiciones[0]+"p"
                        print(cadena)
                        grmsinrecursividadporizquierda.append(cadena)
                        paso=False
                #Si no ha sido modificado entones hay que crear los no terminales hechos por la máquina para interpretar
                if(paso==True):
                    for produ in producciones:
                        transicion=[]
                        transicion=produ.split(" ")
                        if(transiciones[0]==transicion[0] and len(transicion)==3):
                            yamodificado.append(transicion[0])
                            #Agregar la variable prima como aceptacion epsilon
                            cadena=transiciones[0]+"p > epsilon"
                            print(cadena)
                            grmsinrecursividadporizquierda.append(cadena)
                            #Agregar la variable prima reemplazando la variable original
                            cadena=transiciones[0]+"p > "+transiciones[3]+" "+transiciones[0]+"p"
                            print(cadena)
                            grmsinrecursividadporizquierda.append(cadena)
                            cadena=transicion[0]+" > "+transicion[2]+" "+transicion[0]+"p"
                            print(cadena)
                            grmsinrecursividadporizquierda.append(cadena)
            else:
                paso1=True
                if(len(yamodificado)!=0):
                    for x in yamodificado:
                        if(x==transiciones[0]):
                            paso1=False
                    if(paso1==True):
                        grmsinrecursividadporizquierda.append(y)
                        print(y)
                else:
                    grmsinrecursividadporizquierda.append(y)
                    print(y)
        if(siexisterecursividad==False):
            print("La grámatica no tiene recursividad por la izquierda")
            grmsinrecursividadporizquierda.clear()
        return grmsinrecursividadporizquierda