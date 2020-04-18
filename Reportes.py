from reportlab.pdfgen import canvas

class Reportar():
    def verdetalle(self,nombre,afdexistente,gramaticaexistente,gramaticasinrecursividadporizquierda,cadenasevaluadas):
        print("********Detalle general de: "+nombre)
        print("Nombre: "+nombre)
        for y in afdexistente:
            if(nombre==y[0]):
                print("Es un Automáta Finito Determinista")
                print("Estados: ")
                print(y[1])
                print("")
                print("Alfabeto: ")
                print(y[2])
                print("")
                print("Estado Inicial: ")
                print(y[3])
                print("")
                print("Estados aceptación: ")
                print(y[4])
                print("")
                print("Transiciones: ")
                n=0
                for x in y[5]:
                    if(n==0):
                        print("Modo 1")
                        n=1
                    else:print(x)
        for g in gramaticaexistente:
            if(nombre==g[0]):
                print("Es una gramática regular")
                print("No terminales: ")
                print(g[1])
                print("")
                print("Terminales: ")
                print(g[2])
                print("")
                print("No terminal inicial: ")
                print(g[3])
                print("")
                print("Producciones: ")
                for x in g[4]:
                    print(x)
        for r in gramaticasinrecursividadporizquierda:
            if(nombre==r[0]):
                print("Tiene recursividad por izquierda")
                print("Producciones sin recursividad por izquierda")
                for x in r[1]:
                    print(x)
        print("")
        print("Cadenas que se evaluaron: ")
        for e in cadenasevaluadas:
            if(nombre==e[0]):
                print("Cadena: "+e[1]+" es: "+e[2])
        print("-------------------------------------")

    def generarreporte(self,nombre,afdexistente,gramaticaexistente,gramaticasinrecursividadporizquierda,cadenasevaluadas):
        fileName = 'Reporteenpdf.pdf'
        documentTitle = 'Reporte en PDF'
        title = 'Nombre: '+nombre
        pdf = canvas.Canvas(fileName)
        pdf.setTitle(documentTitle)
        text=pdf.beginText(0,0)
        for y in afdexistente:
            if (nombre == y[0]):
                text.textLine("Es un Automáta Finito Determinista")
                text.textLine("Estados: ")
                for k in y[1]: text.textLine(k)
                text.textLine("")
                text.textLine("Alfabeto: ")
                for k in y[2]: text.textLine(k)
                text.textLine("")
                text.textLine("Estado Inicial: ")
                for k in y[3]: text.textLine(k)
                text.textLine("")
                text.textLine("Estados aceptación: ")
                for k in y[4]: text.textLine(k)
                text.textLine("")
                text.textLine("Transiciones: ")
                n = 0
                for x in y[5]:
                    if (n == 0):
                        text.textLine("Modo 1")
                        n = 1
                    else:
                        text.textLine(x)
        for g in gramaticaexistente:
            if (nombre == g[0]):
                text.textLine("Es una gramática regular")
                text.textLine("No terminales: ")
                for k in g[1]: text.textLine(k)
                text.textLine("")
                text.textLine("Terminales: ")
                for k in g[2]: text.textLine(k)
                text.textLine("")
                text.textLine("No terminal inicial: ")
                for k in g[3]: text.textLine(k)
                text.textLine("")
                text.textLine("Producciones: ")
                for x in g[4]:
                    text.textLine(x)
        for r in gramaticasinrecursividadporizquierda:
            if (nombre == r[0]):
                text.textLine("Tiene recursividad por izquierda")
                text.textLine("Producciones sin recursividad por izquierda")
                for x in r[1]:
                    text.textLine(x)
        text.textLine("")
        text.textLine("Cadenas que se evaluaron: ")
        for e in cadenasevaluadas:
            if (nombre == e[0]):
                text.textLine("Cadena: " + e[1] + " es: " + e[2])
        pdf.setFont("Times-Roman", 12)
        pdf.drawText(text)
        pdf.save()