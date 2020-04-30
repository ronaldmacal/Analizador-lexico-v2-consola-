from graphviz import Digraph

class automatapila:
    def generarautomata(self,datos):
        print("Generar automata de pila basado en grámatica libre de contexto")
        vectorres=[]
        nombre=datos[0]
        terminales=datos[1]
        noterminales=datos[2]
        noterminalinicial=datos[3]
        producciones=datos[4]
        #Paso 0: Guardar el nombre
        vectorres.append(nombre)

        #Paso 1: Crear el alfabeto del automata y los simbolos de sistema
        vectorres.append(terminales)
        simbolos=[]
        for x in terminales:
            simbolos.append(x)
        for y in noterminales:
            simbolos.append(y)
        simbolos.append("#")
        vectorres.append(simbolos)

        #Paso 2: Crear los estados, estado inicial y estado final
        estados=['i','p','q','f']
        vectorres.append(estados)
        vectorres.append(noterminalinicial)
        vectorres.append("f")

        transiciones = []
        cadena = ""
        #Paso 3: crear transicion de ley (i,l',l';p,#)
        cadena="i,l',l';p,#"
        transiciones.append(cadena)

        #Paso 4: Crear transición con estado inicial S (p,l',l';q,S)
        cadena="p,l',l';q,"+noterminalinicial+""
        transiciones.append(cadena)

        #Paso 5: Transiciones (q,l',1;q,2) -->1:Produccion lado izquierdo. 2: Transicion lado derecho
        for pro in producciones:
            vector=pro.split(">")
            izquierdo=vector[0].strip(" ")
            derecho=vector[1].strip(" ")
            cadena="q,l',"+izquierdo+";q,"+derecho
            transiciones.append(cadena)

        #Paso 6: Transiciones (q,1,1;q,l') --> 1: Para cada alfabeto
        for ter in terminales:
            cadena="q,"+ter+","+ter+";q,l'"
            transiciones.append(cadena)

        #Paso 7: Transicion del final
        cadena="q,l',#;f,l'"
        transiciones.append(cadena)
        vectorres.append(transiciones)

        #Revisar el vector de salida
        print("Automata de pila Creado con éxito, vaya a Visualizar automata para ver el automata")
        return vectorres

    def verautomata(self,automata):
        print("Visualizar el automata")
        print("Séxtupla del automata de pila "+automata[0]+":")
        print("1. Estados")
        for x in automata[3]:
            print("     "+x)
        print("")
        print("2. Alfabeto de la máquina")
        for x in automata[1]:
            print("     "+x)
        print("")
        print("3. Conjunto finito de simbolos de pila")
        for x in automata[2]:
            print("     " + x)
        print("")
        print("4. Estado inicial")
        print("     "+automata[4])
        print("")
        print("5. Estado aceptación")
        print("     " + automata[5])
        print("")
        print("6. Transiciones")
        for x in automata[6]:
            print("     " + x)

        #Hacer el grafico del automata
        print("Mostrar el grafico del automata de pila")
        f=Digraph('finite_state_machine',filename='automatadepila.sv')
        f.attr(rankdir='LR',size='8.5')
        f.attr('node',shape='doublecircle')
        f.node('f')
        f.attr('node', shape='circle', size='15')
        f.node('q')
        f.attr('node',shape='circle')
        # Parte para generar las transiciones
        trans = []
        for x in automata[6]:
            primer = x.split(";")
            izquierda = primer[0].split(",")
            derecha = primer[1].split(",")
            f.edge(izquierda[0],derecha[0],label=izquierda[1]+","+izquierda[2]+";"+derecha[1])
        f.view()