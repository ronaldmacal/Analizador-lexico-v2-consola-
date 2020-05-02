from graphviz import Digraph
import csv

class Validar:
    def validarcadenaygenerararbol(self,grmexistente,grmrecursiva,cadena,nombre):
        esrecursiva=False
        valida=[]
        for x in grmrecursiva:
            if(nombre==x[0]):
                esrecursiva=True
        if(esrecursiva==True):
            valida=self.recursiva(grmrecursiva,cadena,nombre)
        else:
            valida=self.sinrecursividad(grmexistente,cadena,nombre)
        print(valida[0])
        if(esrecursiva==True and valida[0]=="Cadena válida. Aceptada"):
            self.creararbolrecursivo(valida[1])
        elif(valida[0]=="Cadena válida. Aceptada"):
            self.creararbolnorecursivo(valida[1])

    def recursiva(self,grmrecursiva,cadena,nombre):
        vproducciones=[]
        vterminales=[]
        vnoterminales=[]
        vinicio=""
        for x in grmrecursiva:
            if(nombre==x[0]):
                vproducciones=x[4]
                vterminales=x[1]
                vnoterminales=x[2]
                vinicio=x[3]
        ruta=[]
        rutayvalido=[]
        eanterior=""
        edoble=""
        eactual = vinicio
        for letra in cadena:
            for produ in vproducciones:
                datos=produ.split(" ")
                for x in vterminales:
                    if(eactual==x):
                        if(letra==eactual):
                            eactual=eanterior
                            edoble=eactual

                if(eactual==datos[0]):
                    esnoter=False
                    for y in vnoterminales:
                        if(datos[2]==y):
                            esnoter=True
                            eanterior=eactual
                            eactual=datos[2]
                            ruta.append(eanterior+":"+eactual)
                    if(esnoter==False):
                        for y in vterminales:
                            if(datos[2]==y):
                                if(y==letra):
                                    eanterior=eactual
                                    eactual=datos[3]
                                    r = eanterior + ":"
                                    dist = 0
                                    num=0
                                    for n in datos:
                                        if (dist > 1):
                                            if(num==0):
                                                r = r + n
                                                num=num+1
                                            else:
                                                r=r+","+n
                                        dist = dist + 1
                                    ruta.append(r)
                                elif(edoble==datos[0]):
                                    eanterior=eactual
                                    eactual=datos[4]
                                    edoble=""
        esvalida=False
        for produ in vproducciones:
            datos=produ.split(" ")
            if(eactual==datos[0] and datos[2]=='epsilon'):
                esvalida=True
        if(esvalida==False):
            rutayvalido.append("Cadena inválida. No Aceptada")
        elif(esvalida==True):
            rutayvalido.append("Cadena válida. Aceptada")
            ruta.append(eactual+":epsilon")
        rutayvalido.append(vproducciones)
        return rutayvalido

    def sinrecursividad(self,grmexistente,cadena,nombre):
        rutayvalido=[]
        ruta=[]
        vnoterminales = []
        vterminales = []
        vinicio = ""
        vproducciones = []
        for x in grmexistente:
            if(nombre==x[0]):
                vnoterminales.append(x[2])
                vterminales.append(x[1])
                vinicio = x[3]
                vproducciones.append(x[4])
        # Algoritmo para validar cadena
        eactual = vinicio
        pila = []
        rastro = []
        regreso=False
        eanterior=""

        #Leer letra por letra
        for letra in cadena:
            #Validar si va de regreso
            if(regreso==False):
                #Leer produccion por produccion
                yaentro=False
                for produ in vproducciones:
                    dat = produ.split(" ")
                    if (eactual == dat[0] and regreso==False and yaentro==False):
                        paso=True
                        if(len(dat)==3):
                            if(letra==dat[2]):
                                regreso=True
                                paso=False
                        #Parte solo para guardar el rastro
                        n = 0
                        pila=[]
                        for pr in dat:
                            if (n >= 2):
                                pila.append(pr)
                            n = n + 1
                        #Validar si lo que viene es terminal  o no terminal
                        esno=False
                        for y in vnoterminales:
                            if(dat[2]==y):
                                esno=True
                                eanterior=eactual
                                eactual=dat[2]
                        if(esno==False and paso==True):
                            for x in vterminales:
                                if(dat[2]==x):
                                    if(letra==x):
                                        yaentro=True
                                        eanterior=eactual
                                        eactual=dat[3]
                                        pila.pop(0)
                                        pila.pop(0)
                                        rastro.append(pila)
            else:
                pos=len(rastro)-1
                vector=rastro[pos]
                if(letra==vector[0]):
                    if (len(vector) == 1):
                        rastro.remove(vector)
                    else:
                        vector.remove(vector[0])
                        rastro[pos] = vector
                    eactual=eanterior
                yaentro=False
                for y in vnoterminales:
                    if(vector[0]==y):
                        eactual=y
                        if (len(vector) == 1):
                            rastro.remove(vector)
                        else:
                            vector.remove(vector[0])
                            rastro[pos] = vector
                        for produ in vproducciones:
                            dat = produ.split(" ")
                            if (eactual == dat[0] and regreso == True and yaentro == False):
                                # Parte solo para guardar el rastro
                                n = 0
                                pila = []
                                for pr in dat:
                                    if (n >= 2):
                                        pila.append(pr)
                                    n = n + 1
                                # Validar si lo que viene es terminal  o no terminal
                                esno = False
                                for y in vnoterminales:
                                    if (dat[2] == y):
                                        esno = True
                                        eanterior=eactual
                                        eactual = dat[2]
                                if (esno == False):
                                    for x in vterminales:
                                        if (dat[2] == x):
                                            if (letra == x):
                                                yaentro = True
                                                eanterio=eactual
                                                eactual = dat[3]
                                                pila.pop(0)
                                                pila.pop(0)
                                                rastro.append(pila)
                                                regreso=False
        for produ in vproducciones:
            dat = produ.split(" ")
            if(len(dat)==3 and eactual==dat[0]):
                rutayvalido.append("Cadena inválida. No Aceptada")
            else:
                rutayvalido.append("Cadena válida. Aceptada")
        rutayvalido.append(ruta)
        return rutayvalido

    def creararbolnorecursivo(self,cadena):
        print("Mostrando el arbol generado por cadena")
        u = Digraph('unix', filename='arbolcadenarecursiva.gv', node_attr={'color': 'lightblue2', 'style': 'filled'})
        u.attr(size='6,6')
        for lista in cadena:
            opcion = lista.split(":")
            origen = opcion[0]
            destinos = opcion[1].split(",")
            for x in destinos:
                u.edge(origen, x)
        u.view()

    def creararbolrecursivo(self,cadena):
        print("Mostrando el arbol generado por cadena")
        u = Digraph('unix', filename='arbolcadenarecursiva.gv', node_attr={'color': 'lightblue2', 'style': 'filled'})
        u.attr(size='6,6')
        for lista in cadena:
            opcion=lista.split(":")
            origen=opcion[0]
            destinos=opcion[1].split(",")
            for x in destinos:
                u.edge(origen,x)
        u.view()

    def reportedecadena(self,automatapila,cadena,nombre):
        vtransiciones=[]
        for pr in automatapila:
            if(nombre==pr[0]):
                vtransiciones=pr[6]
        datos = []
        encabezados = ["Pila", "Cadena", "Transicion usada"]
        datos.append(encabezados)
        estadoactual = "i"
        pila = []
        for t in vtransiciones:
            d = t.split(";")
            izquierda = d[0].split(",")
            derecha = d[1].split(",")
            if (estadoactual == "i" or estadoactual == "p"):
                estadoactual = derecha[0]
                if (derecha[1] != "lambda"):
                    pila.append(derecha[1])
                    linea = []
                    test = ""
                    for z in pila:
                        test = test + z
                    linea = [test, "", t]
                    datos.append(linea)
        # Ahora en el estado q utilizar  cadena y transiciones
        cadenadelecturas = ""
        for letra in cadena:
            if (len(pila) > 0):
                tam = len(pila) - 1
            else:
                tam = 0
            paso1 = True
            paso2 = True
            if (letra == pila[tam]):
                pila.pop()
                for t in vtransiciones:
                    if (paso1 == True):
                        d = t.split(";")
                        izquierda = d[0].split(",")
                        derecha = d[1].split(",")
                        if (izquierda[1] == letra and derecha[1] == "lambda"):
                            cadenadelecturas = cadenadelecturas + letra
                            l = ""
                            for lo in pila:
                                l = l + lo
                            linea = [l, cadenadelecturas, t]
                            datos.append(linea)
                            paso1 = False
            else:
                for t in vtransiciones:
                    d = t.split(";")
                    izquierda = d[0].split(",")
                    derecha = d[1].split(",")
                    if (paso2 == True):
                        if (izquierda[1] == "lambda" and izquierda[2] == pila[tam]):
                            vecto = derecha[1].split(" ")
                            vecto.reverse()
                            pila.pop()
                            for i in vecto:
                                pila.append(i)
                            l = ""
                            for lo in pila:
                                l = l + lo
                            linea = [l, cadenadelecturas, t]
                            datos.append(linea)
                            paso2 = False
                            vtransiciones.remove(t)
                    if (len(pila) > 0):
                        tam = len(pila) - 1
                    else:
                        tam = 0
                    if (letra == pila[tam]):
                        pila.pop()
                        for t in vtransiciones:
                            if (paso1 == True):
                                d = t.split(";")
                                izquierda = d[0].split(",")
                                derecha = d[1].split(",")
                                if (izquierda[1] == letra and derecha[1] == "lambda"):
                                    cadenadelecturas = cadenadelecturas + letra
                                    l = ""
                                    for lo in pila:
                                        l = l + lo
                                    linea = [l, cadenadelecturas, t]
                                    datos.append(linea)
                                    paso1 = False
        if (len(pila) == 1):
            linea = ["----", cadenadelecturas, "q,lambda,#;f,lambda"]
            datos.append(linea)
            linea = ["----", cadenadelecturas, "Cadena Aceptada"]
            datos.append(linea)
            print("La cadena es válida, por lo tanto se acepta")
        else:
            linea = ["----", cadenadelecturas, "Cadena No Aceptada"]
            datos.append(linea)
            print("La cadena es inválida, no se acepta")
        myFile = open('pilasentradastransicion.csv', 'w', newline='')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(datos)
        print("Archivo de reporte creado con éxito")