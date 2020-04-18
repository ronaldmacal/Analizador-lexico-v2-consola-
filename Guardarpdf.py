class Guardar():
    def guardararchivo(self,afdexistente,gramatica,grmrecursiva):
        print("Indique el nombre del automata o gramatica a guardar: ")
        nombre=input()
        paso=False
        if(nombre==""):
            print("No se ingresó nombre, vuelva a intentarlo")
            self.guardararchivo(afdexistente,gramatica,grmrecursiva)
        else:paso=True
        if(paso==True):
            quees=""
            produccionesotransiciones=[]
            eaceptacion=[]
            #Averiguar primero que tipo de archivo es
            for a in afdexistente:
                if(nombre==a[0]):
                    quees="afd"
                    eaceptacion=a[4]
                    produccionesotransiciones=a[5]
                    self.guardarafd(eaceptacion,produccionesotransiciones)
            for g in gramatica:
                if(nombre==g[0]):
                    quees="gramatica"
                    produccionesotransiciones=g[4]
                    self.guardargramatica(produccionesotransiciones)

    def guardarafd(self,eaceptacion,modoytransicion):
        print("Ingrese el nombre para guardar su AFD: (Advertencia: no deje el nombre vacío)")
        nombrearchivo=input()
        nombrearchivo=nombrearchivo+".afd"
        afd=open("Archivosguardados/"+nombrearchivo,"w")
        n=0
        transiciones=[]
        #Extraer primero las transiciones
        for trans in modoytransicion:
           if(n!=0):
               transiciones.append(trans)
           n=1
        #Ahora hay que agrear al documento los datos
        for trans in transiciones:
            aceptaorigen = "false"
            aceptadestino = "false"
            estalfa=trans.split(";")
            estados=estalfa[0].split(",")
            for acepta in eaceptacion:
                if(acepta==estados[0]):
                    aceptaorigen="true"
            for acepta in eaceptacion:
                if(acepta==estados[1]):
                    aceptadestino="true"
            cadena=estados[0]+","+estados[1]+","+estalfa[1]+";"+aceptaorigen+","+aceptadestino
            afd.write(cadena+"\n")
        print("Archivo creado con éxito, puede buscarlo en la carpeta Archivosguardados con el nombre: "+nombrearchivo)
        afd.close()

    def guardargramatica(self,producciones):
        print("Ingrese el nombre para guardar su Gramatica: (Advertencia: no deje el nombre vacío)")
        nombrearchivo=input()
        nombrearchivo=nombrearchivo+".grm"
        gramatica=open("Archivosguardados/"+nombrearchivo,"w")
        for produ in producciones:
            gramatica.write(produ+'\n')
        print("Archivo guardado con éxito bajo el nombre: "+nombrearchivo)
        gramatica.close()