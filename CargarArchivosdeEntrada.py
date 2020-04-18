class CargarArchivos():
    def cargarafd(self):
        #Debe devolver un vector con los datos en el orden estipulado en el vector
        print("Cargar un archivo AFD")
        print("Ingrese el nombre del archivo a cargar (el archivo debe estar en carpeta Archivosleer): ")
        nombrearchivo=input()
        nombrearchivo=nombrearchivo+".afd"
        print("Ingrese el nombre del AFD: (este es el nombre para guardarlo en el programa)")
        nombreafd=input()
        afddatos = []
        transiciones=[]
        afd=open("Archivosleer/"+nombrearchivo,"r")
        for linea in afd.readlines():
            linea=linea.strip("\n")
            transiciones.append(linea)
        afd.close()
        #Ahora utilizar los datos del archivo para crear los datos
        plistadoestados=[]
        plistadoalfabeto=[]
        pinicial=""
        pestadoaceptacion=[]
        vectortransiciones=[]
        n=0
        #Estas variables con solamente para ver si el estado ya esta registrado
        estados=[]
        alfabeto=[]
        vectortransiciones.append("1")
        for trans in transiciones:
            derechoizquierdo=trans.split(";")
            derecho=derechoizquierdo[1].split(",")
            izquierdo=derechoizquierdo[0].split(",")
            #Otorgar estado inicial
            if(n==0):
                pinicial=izquierdo[0]
                n=1
            #Crear la transicion
            vectortransiciones.append(izquierdo[0]+","+izquierdo[1]+";"+izquierdo[2])
            #Revisar alfabeto y estado
            yaesta=False
            for x in alfabeto:
                if(izquierdo[2]==x):
                    yaesta=True
            if(yaesta==False):alfabeto.append(izquierdo[2])
            #Esto es para el estado de origen
            yaesta=False
            for y in estados:
                if(izquierdo[0]==y[0]):
                    yaesta=True
                    y[1]=derecho[0]
            if(yaesta==False):
                arreglo=[]
                arreglo.append(izquierdo[0])
                arreglo.append(derecho[0])
                estados.append(arreglo)
            # Esto es para el estado de destino
            yaesta = False
            for y in estados:
                if (izquierdo[1] == y[0]):
                    yaesta = True
                    y[1] = derecho[1]
            if (yaesta == False):
                arreglo = []
                arreglo.append(izquierdo[1])
                arreglo.append(derecho[1])
                estados.append(arreglo)
            #Ahora hay que registrar los estados y luego si son de aceptacion
        for y in estados:
            plistadoestados.append(y[0])
            if(y[1]=="true"):
                pestadoaceptacion.append(y[0])
        afddatos.append(nombreafd)
        afddatos.append(plistadoestados)
        plistadoalfabeto=alfabeto
        afddatos.append(plistadoalfabeto)
        afddatos.append(pinicial)
        afddatos.append(pestadoaceptacion)
        afddatos.append(vectortransiciones)
        print("Carga de: "+nombrearchivo+" realizada con éxito")
        return afddatos

    def cargargramatica(self):
        print("Ingrese el nombre del archivo a cargar (el archivo debe estar en carpeta Archivosleer): ")
        nombrearchivo = input()
        nombrearchivo = nombrearchivo + ".grm"
        print("Ingrese el nombre de la gramatica: (este es el nombre para guardarlo en el programa)")
        nombregrm = input()
        grm = open("Archivosleer/" + nombrearchivo, "r")
        producciones=[]
        for linea in grm.readlines():
            linea = linea.strip("\n")
            producciones.append(linea)
        grm.close()
        gnoterminales=[]
        gterminales=[]
        gnoterminalinicial=""
        gproducciones=[]
        n=0
        for p in producciones:
            estado=p.split(" ")
            if(n==0):
                gnoterminalinicial=estado[0]
                n=1
            if(gnoterminales.count(estado[0])==0):
                gnoterminales.append(estado[0])
        #Verificar lo terminales
        siexiste=False
        for m in producciones:
            estado=m.split(" ")
            siexiste = False
            siesepsilon=False
            for est in gnoterminales:
                if(estado[2]==est):
                    siexiste=True
                elif(estado[2]=="epsilon"):
                    siesepsilon=True
            if(siexiste==False and estado[2]!="epsilon"):
                #aqui
                siexiste = False
                for x in gterminales:
                    if (x == estado[2]): siexiste = True
                if (siexiste == False): gterminales.append(estado[2])
            if(len(estado)==4):
                siexiste = False
                for est in gnoterminales:
                    if(estado[3]==est):
                        siexiste=True
                if(siexiste==False):
                    #aqui
                    siexiste=False
                    for x in gterminales:
                        if(x==estado[3]):siexiste=True
                    if(siexiste==False):gterminales.append(estado[3])
        #Ingresar todas la producciones
        for y in producciones:
            gproducciones.append(y)
        arreglog=[]
        arreglog.append(nombregrm)
        arreglog.append(gnoterminales)
        arreglog.append(gterminales)
        arreglog.append(gnoterminalinicial)
        arreglog.append(gproducciones)
        print("Archivo con nombre: "+nombrearchivo+" cargado con éxito")
        return arreglog
