from graphviz import Digraph

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
        print(valida)

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
                    if(esnoter==False):
                        for y in vterminales:
                            if(datos[2]==y):
                                if(y==letra):
                                    eanterior=eactual
                                    eactual=datos[3]
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
        rutayvalido.append(ruta)
        return rutayvalido

    def sinrecursividad(self,grmexistente,cadena,nombre):
        print("No es recursiva")



    def creararbol(self,cadena):
        print("Metodo que crea tu arbol")
        u = Digraph('unix', filename='arbolcadena.gv', node_attr={'color': 'lightblue2', 'style': 'filled'})
        u.attr(size='6,6')
        # u.edge('origen', 'destino')
        u.edge('S', 'A')
        u.view()

    def reportedecadena(self,automatapila,cadena,nombre):
        print("Reporte general de cadena")