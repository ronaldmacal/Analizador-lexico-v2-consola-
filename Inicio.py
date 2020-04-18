import sys
from Crearafd import Generarnuevoafd
from Creargramatica import Generarnuevagramatica
from Reportes import Reportar
from Guardarpdf import Guardar
from EvaluarCadenas import Evaluar
from CargarArchivosdeEntrada import CargarArchivos

global afdexistente
afdexistente=[]
global gramaticaexistente
gramaticaexistente=[]
global gramaticasinrecursividadporizquierda
gramaticasinrecursividadporizquierda=[]
global cadenasevaluadas
cadenasevaluadas=[]

class Principalinicio():
    def mostrarmenugramatica(self,nombre):
        fin=True
        # Verirficar primero si existe el nombre para reemplazarlo
        gramatica = Generarnuevagramatica(nombre)
        si = gramatica.siexiste(gramaticaexistente, nombre,0)
        if (si):
            print("Ese nombre ya existe entre los afd, por lo tanto los valores anteriores se quitaran para que puedan ser editados")
            for y in gramaticaexistente:
                if (nombre == y[0]):
                    gramaticaexistente.remove(y)
        #Variables para crear el arreglo para guardar la gramática
        noterminales=[]
        gnoterminales=""
        gterminales=""
        gnoterminalinicial=""
        gproducciones=""
        while fin==True:
            print("*************Menú datos de grámatica: " + nombre)
            print("1. Ingresar no terminales")
            print("2. Ingresar terminales")
            print("3. No terminal inicial")
            print("4. Producciones")
            print("5. Gramatica transformada")
            print("6. Ayuda")
            print("7. Regresar")
            print("Ingrese una opción: ")
            opcion = input()
            if (opcion == '1'):
                gnoterminales=gramatica.ingresarnoterminales()
            elif (opcion == '2'):
                gterminales=gramatica.ingresarterminales()
            elif (opcion == '3'):
                print("Ingrese el terminal inicial a utilizar:")
                noterminalinicial = input()
                gnoterminalinicial = gramatica.terminalinicial(gnoterminales, noterminalinicial)
            elif (opcion == '4'):
                print("Producciones de la grámatica")
                gproducciones=gramatica.producciones(gterminales,gnoterminales)
            elif (opcion == '5'):
                print("Transformada de grámatica")
                arreg=[]
                arreg.append(nombre)
                prueba=gramatica.gramaticatransformada(gproducciones,gnoterminales,gterminales)
                if(len(prueba)!=0):
                    arreg.append(prueba)
                    gramaticasinrecursividadporizquierda.append(arreg)
            elif (opcion == '6'):
                print("**************************************************************")
                print("     Lenguajes Formales y de programación, sección B-")
                print("                 Aux. Luis Yela")
                print("                        1")
                print("**************************************************************")
            elif (opcion == '7'):
                #Guardar el arreglo para guardar la gramatica
                arreglog=[]
                arreglog.append(nombre)
                arreglog.append(gnoterminales)
                arreglog.append(gterminales)
                arreglog.append(gnoterminalinicial)
                arreglog.append(gproducciones)
                gramaticaexistente.append(arreglog)
                fin=False
            else:
                print("Opcion nó válida, vuelva a ingresar una opción")
        self.menuprincipal()

    def nombregramatica(self):
        print("Ingrese un nombre para esta gramatica:")
        nombre = input()
        if (nombre == ""):
            print("Ingrese un valor que sea válido")
            self.nombregramatica()
        else:
            self.mostrarmenugramatica(nombre)

    def mostrarmenuafd(self, nombre):
        fin=True
        #Verirficar primero si existe el nombre para reemplazarlo
        afd = Generarnuevoafd(nombre)
        si=afd.siexisteafd(afdexistente,nombre)
        if(si):
            print("Ese nombre ya existe entre los afd, por lo tanto los valores anteriores se quitaran para que puedan ser editados")
            for y in afdexistente:
                if(nombre==y[0]):
                    afdexistente.remove(y)
        #Variables a utilizar para crear el arreglo que se cuida
        afdestados=[]
        vectortransiciones = []
        plistadodeestados=""
        plistadoalfabeto = ""
        pinicial=""
        pestadoaceptacion = ""
        while fin==True:
            print("*******Menú datos de AFD: " + nombre)
            print("1. Ingresar estados")
            print("2. Ingresar alfabeto")
            print("3. Estado inicial")
            print("4. Estados de aceptación")
            print("5. Transiciones")
            print("6. Ayuda")
            print("7. Regresar")
            print("Ingrese una opción: ")
            opcion = input()
            if (opcion == '1'):
                plistadodeestados=afd.ingresarestados()
            elif (opcion == '2'):
                plistadoalfabeto=afd.ingresaralfabeto()
            elif (opcion == '3'):
                print("Ingrese el estado inicial a utilizar:")
                pinicial=input()
                pinicial=afd.estadoinicial(plistadodeestados,pinicial)
            elif (opcion == '4'):
                pestadoaceptacion=afd.estadoaceptacion(plistadodeestados)
            elif (opcion == '5'):
                vectortransiciones=afd.transiciones()
            elif (opcion == '6'):
                print("**************************************************************")
                print("     Lenguajes Formales y de programación, sección B-")
                print("                 Aux. Luis Yela")
                print("                        1")
                print("**************************************************************")
            elif (opcion == '7'):
                # Guardar los datos hasta terminar de ingresar los datos del afd
                arreglo=[]
                arreglo.append(nombre)
                arreglo.append(plistadodeestados)
                arreglo.append(plistadoalfabeto)
                arreglo.append(pinicial)
                arreglo.append(pestadoaceptacion)
                arreglo.append(vectortransiciones)
                afdexistente.append(arreglo)
                fin=False
            else:
                print("Opcion nó válida, vuelva a ingresar una opción")
        self.menuprincipal()

    def nombreafd(self):
        print("Ingrese un nombre para este automata:")
        nombre = input()
        if (nombre == ""):
            print("Ingrese un valor que sea válido")
            self.nombreafd()
        else:
            self.mostrarmenuafd(nombre)

    def menuevaluarcadenas(self):
        fin=False
        evaluar=Evaluar()
        while fin==False:
            print("***********Menú Evaluar Cadenas***********")
            print("1. Validar una cadena")
            print("2. Ruta en Automata Finito Determinista (AFD)")
            print("3. Expandir con gramática")
            print("4. Ayuda")
            print("5. Volver al Menú Principal")
            print("Ingrese una opción del menú")
            opcion = input()
            if (opcion == '5'):
                fin=True
            elif (opcion == '1'):
                #Debe retornar la cadena evaluada y el nombre en un vector para guardar los datos
                print("Ingrese el nombre del afd o gramatica a evaluar")
                nombre = input()
                siexiste=False
                for x in afdexistente:
                    if(nombre==x[0]):
                        siexiste=True
                for y in gramaticaexistente:
                    if(nombre==y[0]):
                        siexiste=True
                if(siexiste==False):
                    print("No se identificó el nombre, vuelva a intentarlo")
                else:
                    vector=[]
                    vector=evaluar.soloevaluarcadena(afdexistente,gramaticaexistente,gramaticasinrecursividadporizquierda,nombre)
                    cadenasevaluadas.append(vector)
            elif (opcion == '2'):
                print("Ingrese el nombre del AFD a utilizar: ")
                nombre = input()
                siexiste=False
                for x in afdexistente:
                    if (nombre == x[0]):
                        siexiste = True
                if (siexiste == False):
                    print("No se identificó el nombre, vuelva a intentarlo")
                else:
                    vector2=[]
                    vector2=evaluar.rutaenafd(afdexistente,nombre)
                    cadenasevaluadas.append(vector2)
            elif (opcion == '3'):
                print("Ingrese el nombre de la gramatica a utilizar ruta: ")
                nombre = input()
                siexiste=False
                for y in gramaticaexistente:
                    if(nombre==y[0]):
                        siexiste=True
                if(siexiste==False):
                    print("No se identificó el nombre, vuelva a intentarlo")
                else:
                    vector3=[]
                    vector3=evaluar.expandircongramatica(gramaticaexistente,gramaticasinrecursividadporizquierda,nombre)
                    cadenasevaluadas.append(vector3)
            elif (opcion == '4'):
                print("**************************************************************")
                print("     Lenguajes Formales y de programación, sección B-")
                print("                 Aux. Luis Yela")
                print("                        1")
                print("**************************************************************")
            else:
                print("Caracter no válido, ingrese una opción válida")
                self.menuevaluarcadenas()
        self.menuprincipal()

    def nombrereporte(self):
        print("Ingrese el nombre de la grámatica o el afd para reportar:")
        nombre = input()
        if (nombre == ""):
            print("Ingrese un valor que sea válido")
            self.nombrereporte()
        else:
            self.reportes(nombre)

    def reportes(self,nombre):
        fin=False
        reporte=Reportar()
        while fin==False:
            print("***********Menú Reportes para: "+nombre)
            print("1. Ver detalle")
            print("2. Generar Reporte")
            print("3. Ayuda")
            print("4. Volver")
            print("Ingrese una opción del menú")
            opcion = input()
            if (opcion == '4'):
                fin = True
            elif (opcion == '1'):
                reporte.verdetalle(nombre,afdexistente,gramaticaexistente,gramaticasinrecursividadporizquierda,cadenasevaluadas)
            elif (opcion == '2'):
                reporte.generarreporte(nombre,afdexistente,gramaticaexistente,gramaticasinrecursividadporizquierda,cadenasevaluadas)
            elif (opcion == '3'):
                print("**************************************************************")
                print("     Lenguajes Formales y de programación, sección B-")
                print("                 Aux. Luis Yela")
                print("                        1")
                print("**************************************************************")
            else:
                print("Caracter no válido, ingrese una opción válida")
                self.reportes(nombre)
        self.menuprincipal()

    def cargararchivose(self):
        fin = False
        carga = CargarArchivos()
        while fin == False:
            print("***********Menú Cargar archivos al programa***********")
            print("1. Cargar AFD")
            print("2. Cargar Grámatica")
            print("3. Ayuda")
            print("4. Volver")
            print("Ingrese una opción del menú")
            opcion = input()
            if (opcion == '4'):
                fin = True
            elif (opcion == '1'):
                vectorafd=[]
                vectorafd=carga.cargarafd()
                afdexistente.append(vectorafd)
            elif (opcion == '2'):
                vectorgramatica=[]
                vectorgramatica= carga.cargargramatica()
                #El vector gramatica viene con dos vectores, la gramatica normal y la gramatica sin recursividad
                gramaticaexistente.append(vectorgramatica)
                #Ahora hay que agregar la recursividad por la izquierda si la tiene
                arreg = []
                arreg.append(vectorgramatica[0])
                grm=Generarnuevagramatica(vectorgramatica[0])
                prueba = grm.gramaticatransformada(vectorgramatica[4], vectorgramatica[1], vectorgramatica[1])
                if (len(prueba) != 0):
                    arreg.append(prueba)
                    gramaticasinrecursividadporizquierda.append(arreg)
            elif (opcion == '3'):
                print("**************************************************************")
                print("     Lenguajes Formales y de programación, sección B-")
                print("                 Aux. Luis Yela")
                print("                        1")
                print("**************************************************************")
            else:
                print("Caracter no válido, ingrese una opción válida")
                self.cargararchivose()
        self.menuprincipal()

    def guardararchivo(self):
        fin = False
        guardado = Guardar()
        while fin == False:
            print("***********Menú Guardar archivo***********")
            print("1. Guardar archivo")
            print("2. Ayuda")
            print("3. Volver")
            print("Ingrese una opción del menú")
            opcion = input()
            if (opcion == '3'):
                fin = True
            elif (opcion == '1'):
                guardado.guardararchivo(afdexistente,gramaticaexistente,gramaticasinrecursividadporizquierda)
            elif (opcion == '2'):
                print("**************************************************************")
                print("     Lenguajes Formales y de programación, sección B-")
                print("                 Aux. Luis Yela")
                print("                        1")
                print("**************************************************************")
            else:
                print("Caracter no válido, ingrese una opción válida")
                self.guardararchivo()
        self.menuprincipal()

    def menuprincipal(self):
        print("***********Menú Principal***********")
        print("1. Crear AFD")
        print("2. Crear grámatica")
        print("3. Evaluar cadenas")
        print("4. Reportes")
        print("5. Cargar archivo de entrada")
        print("6. Guardar archivos .grm y .afd")
        print("7. Salir")
        print("Ingrese una opción del menú")
        opcion = input()
        if (opcion == '7'):
            sys.exit(0)
        elif (opcion == '1'):
            self.nombreafd()
        elif (opcion == '2'):
            self.nombregramatica()
        elif (opcion == '3'):
            self.menuevaluarcadenas()
        elif (opcion == '4'):
            self.nombrereporte()
        elif (opcion == '5'):
            self.cargararchivose()
        elif (opcion == '6'):
            self.guardararchivo()
        else:
            print("Caracter no válido, ingrese una opción válida")
            self.menuprincipal()

menu=Principalinicio()
menu.menuprincipal()
