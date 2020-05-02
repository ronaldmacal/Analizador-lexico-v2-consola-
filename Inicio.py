import sys
import os
#Proyecto 2
from GramaticaTipo2 import Gramatica2
from AutomataPila import automatapila
from ValidarCadenas import Validar
from prueba import inicio
#Proyecto 1
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

#Variables del proyecto 2
global gramaticatipo2existente
gramaticatipo2existente=[]
global automatapilaexistente
automatapilaexistente=[]
global gramaticatipo2sinrecursividad
gramaticatipo2sinrecursividad=[]

class Principalinicio():
    #-------------------------------------------------------------------------------------------------------------------
    #Proyecto 1
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
        print("***********Menú Principal - Proyecto 1***********")
        print("1. Crear AFD")
        print("2. Crear grámatica")
        print("3. Evaluar cadenas")
        print("4. Reportes")
        print("5. Cargar archivo de entrada")
        print("6. Guardar archivos .grm y .afd")
        print("7. Volver a caratula")
        print("8. Salir de la aplicación")
        print("Ingrese una opción del menú")
        opcion = input()
        if (opcion == '7'):
            self.caratula()
        elif(opcion=='8'):
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

    #-------------------------------------------------------------------------------------------------------------------
    #Parte de proyecto 2, aqui van todos los métodos del proyecto 2
    def ingresargramatica2(self,nombre,modificar,grmtipo2):
        print(grmtipo2)
        os.system("cls")
        vterminales=[]
        vnoterminales=[]
        vproducciones=[]
        vinicio=""
        fin=False
        grm=Gramatica2()
        while(fin==False):
            print("***********Menú Ingresar grámatica Tipo 2:"+nombre+"***********")
            print("1. Ingresar terminales")
            print("2. Ingresar no terminales")
            print("3. Ingresar producciones")
            print("4. Borrar producciones")
            print("5. No terminal inicial")
            print("6. Volver a menu principal")
            opcion = input()
            siyamodifico=0
            if (opcion == '6'):
                fin=True
            elif (opcion == '1'):
                vterminales=grm.cargarterminales(modificar,grmtipo2,nombre)
            elif (opcion == '2'):
                siyamodifico=1
                vnoterminales=grm.cargarnoterminales(modificar,grmtipo2,nombre)
            elif (opcion == '3'):
                print("Ingresar producciones")
                vproducciones=grm.ingresarproducciones(modificar,grmtipo2,nombre)
            elif (opcion == '4'):
                elimina=grm.borrarproducciones(modificar,vproducciones)
                for x in elimina:
                    for y in vproducciones:
                        if(x==y):
                            vproducciones.remove(x)
            elif(opcion=='5'):
                if(modificar==1):
                    if(siyamodifico==1):
                        vinicio=grm.cargarnoterminalinicial(vnoterminales)
                    else:
                        vinicio=grm.cargarnoterminalinicial(grmtipo2[2])
                else:
                    vinicio=grm.cargarnoterminalinicial(vnoterminales)
            else:
                print("Caracter no válido, ingrese una opción válida")
        #En esta parte agregar los datos del vector si es nuevo
        if(modificar==1):
            #Eliminar la existente antes de modificarla
            gramaticatipo2existente.remove(grmtipo2)
            #Quitar la recursividad que ya existía si existe. Para luego generar una nueva
            for x in gramaticatipo2sinrecursividad:
                if(nombre==x[0]):
                    gramaticatipo2sinrecursividad.remove(x)
        nuevagrm = []
        nuevagrm.append(nombre)
        nuevagrm.append(vterminales)
        nuevagrm.append(vnoterminales)
        nuevagrm.append(vinicio)
        nuevagrm.append(vproducciones)
        gramaticatipo2existente.append(nuevagrm)

        recurgrm=[]
        recurgrm.append(nombre)
        recurgrm.append(vterminales)
        recurgrm.append(vnoterminales)
        recurgrm.append(vinicio)
        vrecursiva=[]
        vrecursiva=grm.quitarrecursividad(vproducciones)
        recurgrm.append(vrecursiva)
        if(len(vrecursiva)!=0):
            gramaticatipo2sinrecursividad.append(recurgrm)
        self.menuproyecto2()

    def nombregramaticatipo2(self):
        print("Ingrese un nombre para esta gramatica tipo 2:")
        nombre = input()
        if (nombre == ""):
            print("Ingrese un valor que sea válido")
            self.nombregramaticatipo2()
        else:
            #Validar que existe el valor
            vector=[]
            modificar=0
            for x in gramaticatipo2existente:
                if(nombre==x[0]):
                    modificar=1
                    print("Hay que modificar")
                    vector=x
            self.ingresargramatica2(nombre,modificar,vector)

    def generarautomatapila(self):
        print("***********Menú Generar autómata de pila***********")
        print("Ingrese el nombre de la gramatica tipo 2")
        nombre=input()
        vector=[]
        siexiste=False
        for x in gramaticatipo2existente:
            if(nombre==x[0]):
                siexiste=True
                vector=x
        if(siexiste==True):
            for x in automatapilaexistente:
                if(nombre==x[0]):
                    automatapilaexistente.remove(x)
            automata=automatapila()
            vector=automata.generarautomata(vector)
            automatapilaexistente.append(vector)
        else:
            print("El nombre de la gramatica no existe, vuelva a intentarlo")
        self.menuproyecto2()

    def visualizarautomata(self):
        print("***********Menú Visualizar automata***********")
        print("Ingrese el nombre de automata")
        nombre=input()
        siexiste=False
        auto = automatapila()
        for x in automatapilaexistente:
            if(nombre==x[0]):
                siexiste=True
                auto.verautomata(x)
        if(siexiste==False):
            print("El automata no existe o no se ha creado aún, revise y vuelva a intentarlo")
        self.menuproyecto2()

    def validarcadena(self):
        print("Ingrese el nombre de la gramática donde se van a evaluar cadenas: ")
        nombre=input()
        siexiste=False
        for x in gramaticatipo2existente:
            if(nombre==x[0]):
                siexiste=True
        if(siexiste==False):
            print("No existe esa gramática, vuelva a intentarlo")
        else:
            val=Validar()
            paso=True
            cadena=""
            while(paso==True):
                print("***********Menú Validar cadena***********")
                print("1. Ingresar cadena")
                print("2. Validar cadena y mostrar árbol")
                print("3. Reporte")
                print("4. Volver")
                opcion=input()
                if(opcion=='1'):
                    print("Ingrese la cadena a validar: ")
                    cadena=input()
                    print("Cadena guardada con éxito")
                elif(opcion=='2'):
                    val.validarcadenaygenerararbol(gramaticatipo2existente,gramaticatipo2sinrecursividad,cadena,nombre)
                elif(opcion=='3'):
                    val.reportedecadena(automatapilaexistente,cadena,nombre)
                elif(opcion=='4'):
                    paso=False
                else:
                    print("Opción no válida, vuelva a intentarlo")
        self.menuproyecto2()

    def menuproyecto2(self):
        os.system("cls")
        print(gramaticatipo2existente)
        print(automatapilaexistente)
        print(gramaticatipo2sinrecursividad)
        print("***********Menú Principal - Proyecto 2***********")
        print("1. Ingresar o modificar gramatica")
        print("2. Generar Autómata de Pila")
        print("3. Visualizar autómata")
        print("4. Validar cadena")
        print("5. Regresar a la carátula")
        print("6. Salir de la aplicacion")
        print("Ingrese una opción: ")
        opcion = input()
        if (opcion == '5'):
            self.caratula()
        elif (opcion == '6'):
            sys.exit(0)
        elif (opcion == '1'):
            self.nombregramaticatipo2()
        elif (opcion == '2'):
            self.generarautomatapila()
        elif (opcion == '3'):
            self.visualizarautomata()
        elif (opcion == '4'):
            self.validarcadena()
        else:
            print("Caracter no válido, ingrese una opción válida")
            self.menuproyecto2()

    def caratula(self):
        print("                      __")
        print("                    .'  '.")
        print("                 _.-'/  |  \\")
        print("    ,        _.-'  ,|  /  0 `-.")
        print("    |\    .-'       `--''-.__.'=====================-,")
        print("    \ '-'`        .___.--._)=========================|")
        print("     \            .'      |                          |")
        print("      |     /,_.-'        | Lenguajes formales y de  |")
        print("    _/   _.'(             |       programación       |")
        print("   /  ,-' \  \            |        201612151         |")
        print("   \  \    `-'            |            B-            |")
        print("    `-'                   '--------------------------'")
        print("             Proyecto 1 y 2")
        print("1.- Proyecto 1")
        print("2.- Proyecto 2")
        print("3.- Salir")
        print("Ingrese un valor: ")
        numero = input()
        if (numero == '1'):
            self.menuprincipal()
        elif (numero == '2'):
            self.menuproyecto2()
        else:
            sys.exit(0)
#Parte del proyecto 2
#menu=Principalinicio()
#menu.caratula()
pr=inicio()
pr.inicio()
