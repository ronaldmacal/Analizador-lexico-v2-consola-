class Evaluar():
    def soloevaluarcadena(self,afd,gramatica,grmrecursiva,nombre):
        #Buscar primero el afd o gramatica
        siexiste=False
        vectordatos=[]
        vectorsolucion=[]
        posibleestadoinicial=""
        eaceptacion=[]
        quees=""
        for x in afd:
            if(nombre==x[0]):
                quees="afd"
                vectordatos=x[5]
                posibleestadoinicial=x[3]
                eaceptacion=x[4]
        for x in gramatica:
            if(nombre==x[0]):
                quees="gramatica"
                vectordatos=x[4]
                posibleestadoinicial=x[3]
        for x in grmrecursiva:
            if(nombre==x[0]):
                vectordatos=x[1]
        if(quees=="afd"):
            afd=[]
            afd.append(nombre)
            print("Ingrese la cadena a evaluar en el AFD: ")
            cadena=input()
            afd.append(cadena)
            vec=[]
            vec=self.evaluarcadenaafd(vectordatos,cadena,posibleestadoinicial,eaceptacion)
            afd.append(vec[0])
            if(vec[0]=="Inválida"):print("La cadena es inválida")
            return afd
        elif(quees=="gramatica"):
            grm=[]
            grm.append(nombre)
            print("Ingrese la cadena a evaluar en la gramatica: ")
            cadena=input()
            grm.append(cadena)
            vec=[]
            vec=self.evaluarcadenagramatica(vectordatos,cadena,posibleestadoinicial)
            grm.append(vec[0])
            if(vec[0]=="Inválida"):print("La cadena es inválida")
            return grm
        else:
            print("No existe el nombre ingresado, vuelva a intentarlo")
            self.soloevaluarcadena(afd,gramatica,grmrecursiva,nombre)

    #Metodos para evaluar las cadenas si son afd o gramaticas.
    #Debe retornar si es valida o no y su ruta
    def evaluarcadenaafd(self,vector,cadena,inicio,eaceptacion):
        transiciones=[]
        rutayvalido=[]
        rutaafd=""
        n=0
        for x in vector:
           if(n!=0):
               transiciones.append(x)
           n=1
        estadoactual=inicio
        #zzzz
        for letraactual in cadena:
            paso=False
            n=0
            for trans in transiciones:
                eyalfa=trans.split(";")
                estados=eyalfa[0].split(",")
                if(estados[0]==estadoactual and eyalfa[1]==letraactual and n==0):
                    paso=True
                    rutaafd=rutaafd+estadoactual+","+estados[1]+","+letraactual+"; "
                    estadoactual=estados[1]
                    n=1
            if(paso!=True):
                print("La cadena es: Inválida")
                rutayvalido.append("Inválida")
                rutayvalido.append(rutaafd)
                return rutayvalido
        if(eaceptacion.count(estadoactual)!=0):
            print("La cadena es: Válida")
            rutayvalido.append("Válida")
            rutaafd=rutaafd+" Válida"
            rutayvalido.append(rutaafd)
            return rutayvalido
        rutayvalido.append("Inválida")
        rutayvalido.append(rutaafd)
        return rutayvalido

    def rutaenafd(self,afd,nombre):
        print("Ruta en AFD")
        vectordatos = []
        eaceptacion=[]
        valida = ""
        posibleestadoinicial = ""
        paso = False
        for x in afd:
            if (nombre == x[0]):
                vectordatos = x[5]
                posibleestadoinicial = x[3]
                eaceptacion=x[4]
                paso = True
        if (paso == True):
            print("Ingrese la cadena a evaluar en el AFD: ")
            cadena = input()
            valida = self.evaluarcadenaafd(vectordatos, cadena, posibleestadoinicial,eaceptacion)
            afdhecho = []
            afdhecho.append(nombre)
            afdhecho.append(cadena)
            afdhecho.append(valida[0])
            if (valida[0] == "Inválida"):
                print("La cadena ingresada es: Inválida")
                print(valida[1])
            else:
                print("Ruta en AFD ")
                print(valida[1])
            return afdhecho
        else:
            print("No existe el afd con ese nombre: "+nombre)
            self.rutaenafd(afd,nombre)

    def evaluarcadenagramatica(self,vector,cadena,estadoactual):
        rutagramatica=estadoactual+"-> "
        acumularcadena=""
        rutayvalido=[]
        for letraactual in cadena:
            acumularcadena=acumularcadena+letraactual
            paso=False
            n=0
            for x in vector:
                estaaqui=[]
                estaaqui=x.split(" ")
                if(estaaqui[0]==estadoactual and estaaqui[2]==letraactual and n==0):
                    paso=True
                    estadoactual=estaaqui[3]
                    rutagramatica=rutagramatica+acumularcadena+estadoactual+" -> "
                    n=1
            if (paso != True):
                print("Cadena ingresada es Inválida")
                rutayvalido.append("Inválida")
                rutayvalido.append(rutagramatica)
                return rutayvalido
        for x in vector:
            esvalido=[]
            esvalido=x.split(" ")
            if(esvalido[0]==estadoactual and esvalido[2]=="epsilon"):
                print("Cadena ingresada es Válida")
                rutayvalido.append("Válida")
                rutagramatica = rutagramatica + cadena + "(epsilon) --> " + cadena + " válida"
                rutayvalido.append(rutagramatica)
                return rutayvalido
        rutayvalido.append("Inválida")
        rutayvalido.append(rutagramatica)
        return rutayvalido

    def expandircongramatica(self, gramatica, grmrecursiva,nombre):
        print("Expandir con gramatica")
        vectordatos=[]
        valida=""
        posibleestadoinicial=""
        paso=False
        for x in gramatica:
            if(nombre==x[0]):
                vectordatos=x[4]
                posibleestadoinicial=x[3]
                paso=True
        for x in grmrecursiva:
            if(nombre==x[0]):
                vectordatos=x[1]
        if(paso==True):
            print("Ingrese la cadena a evaluar en la gramatica: ")
            cadena = input()
            valida=self.evaluarcadenagramatica(vectordatos,cadena,posibleestadoinicial)
            grm = []
            grm.append(nombre)
            grm.append(cadena)
            grm.append(valida[0])
            if(valida[0]=="Inválida"):
                print("La cadena ingresada es: Inválida")
            else:
                print("Expansión en gramática: ")
                print(valida[1])
            return grm
        else:
            print("No existe gramatica con nombre: "+nombre)
            self.expandircongramatica(gramatica,grmrecursiva,nombre)