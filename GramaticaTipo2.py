class Gramatica2:
    def cargarterminales(self,modifica,grmtipo2,nombre):
        mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if(modifica==0):
            vterminales=[]
            paso=True
            while(paso==True):
                print("Ingrese el terminal a ingresar:")
                terminal=input()
                if terminal in mayusculas:
                    print("Se ingresó una mayuscula, no es permitido las letras mayusculas; vuelva a intentarlo.")
                else:
                    repetido=False
                    for x in vterminales:
                        if(x==terminal):
                            repetido=True
                            print("El terminal ingresado está repetido, vuelva a intentarlo")
                    if(repetido==False):
                        vterminales.append(terminal)
                        print("Terminal guardado con éxito")
                print("Desea ingresar un nuevo terminal? s/n")
                respuesta=input()
                if(respuesta=='n' or respuesta=='N'):
                    paso=False
            return vterminales
        else:
            vterminalesnuevos=[]
            print("Los terminales ya ingresados son: ")
            print(grmtipo2[1])
            #Ahora modificar
            paso = True
            while (paso == True):
                print("Ingrese el terminal a ingresar:")
                terminal = input()
                if terminal in mayusculas:
                    print("Se ingresó una mayuscula, no es permitido las letras mayusculas; vuelva a intentarlo.")
                else:
                    repetido = False
                    for x in grmtipo2[1]:
                        if (x == terminal):
                            repetido = True
                            print("El terminal ingresado está repetido, vuelva a intentarlo")
                    for x in vterminalesnuevos:
                        if (x == terminal):
                            repetido = True
                            print("El terminal ingresado está repetido, ya lo ingreso anteriormente")
                    if (repetido == False):
                        vterminalesnuevos.append(terminal)
                        print("Terminal guardado con éxito")
                print("Desea ingresar un nuevo terminal? s/n")
                respuesta = input()
                if (respuesta == 'n' or respuesta == 'N'):
                    paso = False
            #esto es para agregar los terminales que ya estaban en el listado
            for x in grmtipo2[1]:
                vterminalesnuevos.append(x)
            return vterminalesnuevos

    def cargarnoterminales(self,modificar,grmtipo2,nombre):
        mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if(modificar==0):
            vnterminales = []
            paso = True
            while (paso == True):
                print("Ingrese el no terminal a ingresar:")
                terminal = input()
                pos=0
                correcto=False
                for i in terminal:
                    if(pos==0):
                        if i in mayusculas:
                            correcto=True
                        pos=1
                        if(correcto==False):
                            print("El no terminal no es correcto, vuelva a intentar ingresarlo. Debe tener por lo menos una mayuscula al inicio")
                if(correcto==True):
                    repetido = False
                    for x in vnterminales:
                        if (x == terminal):
                            repetido = True
                            print("El no terminal ingresado está repetido, vuelva a intentarlo")
                    if (repetido == False):
                        vnterminales.append(terminal)
                        print("No terminal guardado con éxito")
                print("Desea ingresar un nuevo no terminal? s/n")
                respuesta = input()
                if (respuesta == 'n' or respuesta == 'N'):
                    paso = False
            return vnterminales
        else:
            print("Los no terminales ya ingresados son:")
            print(grmtipo2[2])
            vnterminalesn = []
            paso = True
            while (paso == True):
                print("Ingrese el no terminal a ingresar:")
                terminal = input()
                pos = 0
                correcto = False
                for i in terminal:
                    if (pos == 0):
                        if i in mayusculas:
                            correcto = True
                        pos = 1
                        if (correcto == False):
                            print(
                                "El no terminal no es correcto, vuelva a intentar ingresarlo. Debe tener por lo menos una mayuscula al inicio")
                if (correcto == True):
                    repetido = False
                    for x in vnterminalesn:
                        if (x == terminal):
                            repetido = True
                            print("El no terminal ingresado está repetido, vuelva a intentarlo")
                    for y in grmtipo2[2]:
                        if (y == terminal):
                            repetido = True
                            print("El no terminal ingresado está repetido, vuelva a intentarlo")
                    if (repetido == False):
                        vnterminalesn.append(terminal)
                        print("No terminal guardado con éxito")
                print("Desea ingresar un nuevo no terminal? s/n")
                respuesta = input()
                if (respuesta == 'n' or respuesta == 'N'):
                    paso = False
            for x in grmtipo2[2]:
                vnterminalesn.append(x)
            return vnterminalesn

    def cargarnoterminalinicial(self,noterminales):
        print("Ingrese un no terminal inicial:")
        terminal=input()
        siexiste=False
        for x in noterminales:
            if(x==terminal):
                siexiste=True
        if(siexiste==True):
            print("No terminal inicial guardado con éxito!")
            return terminal
        else:
            print("El no terminal ingresado no existe en el listado original de no terminales")

    def ingresarproducciones(self,modificar,grmtipo2,nombre):
        if(modificar==0):
            paso = True
            vproduccion=[]
            while (paso == True):
                repetida = False
                print("Ingrese una produccion usando la sintaxis: A > b M b")
                produccion=input()
                for x in vproduccion:
                    if(x==produccion):
                        print("Esa producción está repetida, vuelva a intentarlo")
                        repetida=True
                if(repetida!=True):
                    vproduccion.append(produccion)
                    print("Produccion guardada con éxito.")
                print("Desea ingresar otra produccion? s/n")
                respuesta = input()
                if (respuesta == 'n' or respuesta == 'N'):
                    paso = False
            return vproduccion
        else:
            print("Las producciones ya ingresadas son:")
            print(grmtipo2[4])
            paso = True
            vproduccion = []
            while (paso == True):
                print("Ingrese una produccion usando la sintaxis: A > b M b")
                repetida = False
                produccion = input()
                for x in vproduccion:
                    if (x == produccion):
                        print("Esa producción está repetida, vuelva a intentarlo")
                        repetida = True
                for x in grmtipo2[4]:
                    if(x==produccion):
                        repetida=True
                        print("Esa produccion esta repetida, revise los datos anteriores antes de continuar")
                if (repetida != True):
                    vproduccion.append(produccion)
                    print("Produccion guardada con éxito.")
                print("Desea ingresar otra produccion? s/n")
                respuesta = input()
                if (respuesta == 'n' or respuesta == 'N'):
                    paso = False
            for x in grmtipo2[4]:
                vproduccion.append(x)
            return vproduccion

    def borrarproducciones(self,modificar,vproducciones):
        print("Borrar Producciones")
        paso=True
        veliminadas=[]

        while(paso==True):
            siexiste = False
            print("Ingrese una produccion a eliminar")
            produccion=input()
            for x in vproducciones:
                if(x==produccion):
                    siexiste=True
                    veliminadas.append(produccion)
                    print("Producción eliminada")
            if(siexiste==False):
                print("La produccion no está registrada, por lo tanto no se puede eliminar")
            print("Desea ingresar otra produccion? s/n")
            respuesta = input()
            if (respuesta == 'n' or respuesta == 'N'):
                paso = False
        return veliminadas

    def quitarrecursividad(self,producciones):
        sitiene=False
        vproducciones=[]
        noterminalesrecursivos=[]
        for produccion in producciones:
            dividir=produccion.split(">")
            izquierda=dividir[0].split(" ")
            derecha=dividir[1].split(" ")
            prima=izquierda[0]+"p"
            yatiene=False
            #Verificar si ya esta resuelta la recursividad
            for y in noterminalesrecursivos:
                yatiene = False
                if(y==izquierda[0]):
                    cadena=izquierda[0]+" > "
                    n=0
                    for x in derecha:
                        if(n!=0):
                            cadena=cadena+x+" "
                        n=1
                    cadena=cadena+prima
                    vproducciones.append(cadena)
                    yatiene=True

            if(izquierda[0]==derecha[1]):
                sitiene=True
                noterminalesrecursivos.append(izquierda[0])
                cadena=prima+" > "
                n=0
                for x in derecha:
                    if(n>=2):
                        cadena=cadena+x+" "
                    n=n+1
                cadena=cadena+prima
                vproducciones.append(cadena)
                cadena=prima+" > epsilon"
                vproducciones.append(cadena)
            elif(yatiene==False):
                vproducciones.append(produccion)
            #Quitar la recursividad
        if(sitiene==False):
            print("La gramática no tiene recursividad")
            vproducciones.clear()
        return vproducciones