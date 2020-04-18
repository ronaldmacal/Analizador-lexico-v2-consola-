class Generarnuevoafd():
    def __init__(self,nombre):
        self.nombre=nombre

    def siexisteafd(self,vector,nombre):
        si=False
        for x in vector:
            if(nombre==x[0]):
                si=True
        return si

    def ingresarestados(self):
        fin=True
        vector=[]
        siexiste=False
        while (fin==True):
            siexiste=False
            print("Ingrese el estado que desea agregar: ")
            estadoa=input()
            for x in vector:
                if(estadoa==x):
                    print("El estado ya está repetido, vuelva a ingresar otro")
                    siexiste=True
            if(siexiste==False):
                vector.append(estadoa)
                print("Estado agregado con éxito")
            print("Desea agregar otro más? s/n ")
            paso=input()
            if(paso=='n'):
                fin=False
        return vector

    def ingresaralfabeto(self):
        fin = True
        vector = []
        siexiste = False
        while (fin == True):
            siexiste = False
            print("Ingrese el alfabeto del lenguaje que desea agregar: ")
            alfabeto = input()
            for x in vector:
                if (alfabeto == x):
                    print("El alfabeto ingresado ya está repetido, vuelva a ingresar otro")
                    siexiste = True
            if (siexiste == False):
                vector.append(alfabeto)
                print("Alfabeto agregado con éxito")
            print("Desea agregar otro más? s/n ")
            paso = input()
            if (paso == 'n'):
                fin = False
            elif(paso!='s'):
                print("Caracter desconocido, se le volverá a preguntar por un nuevo terminal")
        return vector

    def estadoinicial(self,vector,cadena):
        siexiste = False
        for x in vector:
            if (cadena == x):
                siexiste = True
        if (siexiste == True):
            print("Estado inicial creado con éxito, recuerde que solo debe haber un estado inicial")
            return cadena
        else:
            print("El estado inicial ingresado no coincide con los estados ingresados antes o no hay estados ingresados")

    def estadoaceptacion(self,vector):
        paso=True
        cadena=[]
        while (paso==True):
            print("Ingresar los estados de aceptacion:")
            estado=input()
            siexiste=False
            si=False
            for x in vector:
                if(estado==x):
                    for y in cadena:
                        if(estado==y):
                            print("Ya está repetido ese estado de aceptación")
                            siexiste=True
                    if(siexiste==False):
                        si=True
                        print("Estado de aceptación creado con éxito")
                        cadena.append(estado)
            if(si==False):
                print("El estado ingresado no existe en lo que se declararon anteriormente")
            print("Desea continuar ingresando estado de aceptacion? s/n")
            continuar=input()
            if(continuar=='n'):
                paso=False
            elif(continuar!='s'):
                print("No se ingreso un caracter conocido")
                paso=False
        return cadena

    def transiciones(self):
        vector=[]
        print("Ingrese en que modo ingresará las transiciones: Modo 1 o Modo 2")
        print("Solo ingrese el numero: ")
        modo=input()
        if(modo=='1'):
            print("MODO 1")
            vector.append('1')
            paso=True
            yaingresados=[]
            siesta=False
            while(paso==True):
                print("Ingrese la transición:")
                transicion=input()
                #Guardar primero el origen y alfabeto
                estadosyalfabeto=transicion.split(";")
                estados=estadosyalfabeto[0].split(",")
                for y in yaingresados:
                    if(y==(estados[0]+":"+estadosyalfabeto[1])):
                        siesta=True
                if(siesta):
                    print("La transicion ingresada es incorrecta debido a que existen dos no terminales saliendo del mismo estado.")
                else:
                    yaingresados.append(estados[0]+":"+estadosyalfabeto[1])
                    vector.append(transicion)
                    print("Transición creada con éxito")

                print("Desea ingresar otra transicion? s/n")
                si=input()
                if(si=='n') :
                    paso=False
                elif(si!='s'):
                    paso=False
                    print("Opción no válida, será redirigido al menú principal")
            return vector

        elif(modo=='2'):
            print("MODO 2")
            vector.append('2')
            print("Ingrese la transicion por partes")
            print("Terminales separados por coma: (ejemplo:a,b)")
            terminales=input()
            vterminales=terminales.split(",")
            print("Ingrese los no terminales separados por comas: (ejemplo: A,B,C,D)")
            noterminales=input()
            vnoterminales=noterminales.split(",")
            print("Ingrese los simbolos de destino: (ejemplo): A,C;A,C;B,D;--,-- ")
            simbolos=input()
            vsimbolos=simbolos.split(";")
            print("NOTA: si en dado caso hubo un error vuelva a escribir los valores del modo 2")
            vector.append(vterminales)
            vector.append(vnoterminales)
            vector.append(vsimbolos)
            return vector
        else:
            print("Se ingresó una opcion incorrecta, vuelva a intentarlo")