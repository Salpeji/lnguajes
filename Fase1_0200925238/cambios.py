__author__ = 'sammy'
import sys
import Tabla_error_lexico
import Tabla_simbolo_lexico
from Tkinter import *
from tkFileDialog import askopenfile
from tkFileDialog import asksaveasfile
from tkFileDialog import *
from tkMessageBox import *
from tkColorChooser import *
import tkMessageBox
from HTMLParser import HTMLParser
from Tabla_simbolo_lexico import *
from Tabla_error_lexico import *
import os
from collections import *

crea_ventana = Tk()
crea_ventana.title("Fase1_200925238, Analizador Lexico")
crea_ventana.geometry("570x490")
text = Text(crea_ventana, height=30, width=68)
scroll = Scrollbar(crea_ventana, command=text.yview)
lista_tokens = [] #arrays
#mis_errores = []
estado = 0
lexema = " "
token_es = " "
tokenllevado = 0 #llevo token Simbolos
tokenllevado2 = 0 #llevo token Errores
# mis_tokens = []
# mis_errores = []
Tabla = []
mis_tokenes = Tabla_simbolo_lexico
mis_errores = Tabla_error_lexico
Lista_token = []
Lista_tokenE = []
tkn = deque ([]) #token
lx = deque ([]) #lexema
numL = deque ([]) #numeroLinea
numC = deque ([]) #numeroColumna
pR = deque ([]) # palabraReservada
tipo = deque ([]) # tipo de Palabra
Token = []
TokenEncontr=[]
TokenEsperad=[]
ColumnaSinta =[]
LineaSintact = []
global contador
global preanalisis
piensa_analisa = " "


def msjApertura(texto):
    print ("Abriendo Archivos en C:/")

def mostrar_cursor(ubica_cursor, event=None):
    text.mark_set(text, INSERT)
    print (text.mark_gravity(text,HORIZONTAL ))

def abrir_xval():
    archivo_actual = askopenfilename(parent=text.master, defaultextension='.xval', initialdir=os.getcwd(), filetypes=(("expr. evaluator", "*.xval"), ("All files", "*.*")))
    try:
        file = open(archivo_actual, 'r')
        contenido = file.read()
        text.delete('1.0', END)
        text.insert('1.0', contenido)
        file.close()
    except Exception as e:
        print "Error al abrir el archivo: " + str(e)

def guardar_xval():
    archivo_actual = asksaveasfilename(parent=text.master, defaultextension='.xval', initialdir = os.getcwd(), filetypes=(("expr. evaluator", "*.xval"), ("All files", "*.*")))
    try:
        file = open(archivo_actual, 'w')
        salida = text.get('1.0', END)
        file.write(salida)
        file.close()
    except Exception as e:
        print 'Archivo No Guardado, Busque en navegador web: ' + str(e)
# estado == estadoprincipal
# z == cadenaconcatenar
#lexema ==  token
def salir_interfaz_evaluator(sale_de_app):
    m_sale = tkMessageBox.askokcancel(title="Fase 1 Front End, Fase 2 Back End-->Del Compilador",
                                      message="Desea Salir del Proyecto Evaluator Fase 1, Front y Back End?")
    if m_sale > 0:
        crea_ventana.destroy()
        return

def mNew(editar_nuevO_existente):
    crea_ventana_otra = Text(crea_ventana, height=30, width=68).pack()
    return
def AFD_Analizador_lexico():
    columna = 0
    Texto_lee = text.get('0.0', END)
    separa_liniea = Texto_lee.split("\n")
    for i in range(len(separa_liniea)-1):
        Linea_Leida = separa_liniea[i]
        if(Linea_Leida != "" ):
            Liniea_sin_Espacio = Linea_Leida.split(' ')
            agregados = Linea_Leida.split()
            for e1 in xrange(0,len(Liniea_sin_Espacio)):
                subCadena = Liniea_sin_Espacio[e1]
                if(len(subCadena)==0):
                    columna = columna+len(subCadena)+1
                else:
                    columna = columna + len(subCadena)
                if  re.match('[0-9]', subCadena):
                    tkn.append(0)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append("No")
                    tipo.append("Numero")
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporta_evaluator')
                elif re.match('[a-z0-9 or a-z ]', subCadena):
                    tkn.append(1)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append("No")
                    tipo.append('Identificador')
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporte_evaluator')
                elif subCadena == ",":
                    tkn.append(2)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append("No")
                    tipo.append('Signo Coma')
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporte_evaluator')
                elif subCadena == "\\":
                    tkn.append(3)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append('No')
                    tipo.append('Barra Reservada')
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporte_evaluator')
                elif subCadena == "#":
                    tkn.append(4)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append('No')
                    Lista_token.append('Signo Comentario')
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporte_evaluator')
                elif subCadena == '<':
                    tkn.append(5)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append('No')
                    tipo.append("Delimitador Inicio")
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporte_evaluator')
                elif subCadena == '>':
                    tkn.append(6)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append('No')
                    tipo.append('Fin Delimitador')
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporta_evaluator')
                    break
                elif subCadena == "{":
                    tkn.append(7)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append('No')
                    tipo.append("Llave Apertura")
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporta:evaluator')
                elif subCadena == "}":
                    tkn.append(8)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append("No")
                    tipo.append("Llave cierre")
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporta_evaluator')
                elif subCadena == "[":
                    tkn.append(9)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append("No")
                    tipo.append("Corchete Apertura")
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporta_evaluator')
                elif subCadena == "]":
                    tkn.append(10)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append( "No")
                    tipo.append("Corchete Cierre")
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporta_evaluator')
                elif subCadena == "(":
                    tkn.append(11)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append("No")
                    tipo.append("Parentesis Apertura")
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporta_evaluator')
                elif subCadena == ")":
                    tkn.append(12)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append("No")
                    tipo.append("Parentesis Cierre")
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporta_evaluator')
                elif subCadena == ":":
                    tkn.append(13)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append('No')
                    tipo.append("Signo de Puntuacion")
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporta_evaluator')
                elif subCadena == ".":
                    tkn.append(14)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append("No")
                    tipo.append("Signo Punto")
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporta_evaluator')
                elif subCadena == ";":
                    tkn.append(15)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append("No")
                    tipo.append("Signo Punto & Coma")
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporta_evalutor')
                    break
                elif subCadena == " ' ":
                    tkn.append(16)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append("No")
                    tipo.append("Comilla Simple")
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporta_evaluator')
                elif subCadena == '|':
                    tkn.append(17)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append('No')
                    tipo.append('Signo Alternar')
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporta_evaluator')
                elif subCadena == "+":
                    tkn.append(18)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append("Si")
                    tipo.append("Operador Aditivo")
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporta_evaluator')
                elif subCadena == "-":
                    tkn.append(19)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append('No')
                    tipo.append('Operador Resta')
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporta_evaluator')
                elif subCadena == "*":
                    tkn.append(20)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append('No')
                    tipo.append('Operador Producto')
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporta_evaluator')
                elif subCadena == "/":
                    tkn.append(21)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append('No')
                    tipo.append('Operador Dividir')
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporta_evaluator')
                elif subCadena == "=":
                    tkn.append(22)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append('No')
                    tipo.append('Signo Igual')
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporta_evaluator')
                elif subCadena == '< EVALUADOR >':
                    tkn.append(23)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append('Si')
                    tipo.append('Palabra Reservada')
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporta_evaluator')
                elif subCadena == '<< DECLARACIONES >>':
                    tkn.append(24)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append('Si')
                    tipo.append('Palabra Reservada')
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporta_evaluator')
                elif subCadena == '<<DEFINICIONES>>':
                    tkn.append(25)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append('Si')
                    tipo.append('Palabra Reservada')
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporta_evaluator')
                elif subCadena == '<<RESULTADOS>>':
                    tkn.append(26)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append('Si')
                    tipo.append('Palabra Reservada')
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporta_evaluator')
                elif subCadena == 'Proyecto_LFP':
                    tkn.append(27)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append('Si')
                    tipo.append('Palabra Reservada')
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporta_evaluator')
                elif subCadena == "<FIN EVALUADOR>":
                    tkn.append(28)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append('Si')
                    tipo.append('Palabra Reservada')
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporta_evalautor')
                elif subCadena == '@':
                    tkn.append(29)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    Lista_tokenE.append(mis_errores)
                    Gra2_HTML('reporte_error')
                elif subCadena == '%':
                    tkn.append(30) #numero Error
                    lx.append(subCadena) #simbolo
                    numL.append(str(i+1)) #linea
                    numC.append(columna) #columna
                    Lista_tokenE.append(mis_errores)
                    Gra2_HTML('reporte_error')
                elif subCadena == '&':
                    tkn.append(31)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    Lista_tokenE.append(mis_errores)
                    Gra2_HTML('reporte_error')
                elif subCadena == '$':
                    tkn.append(32)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    Lista_tokenE.append(mis_errores)
                    Gra2_HTML('reporte_error')
                elif subCadena == '|':
                    tkn.append(33)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporta_evaluator')
                elif subCadena == 'Sumar':
                    tkn.append(34)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append('Si')
                    tipo.append('Palabra Reservada f(x)')
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporta_evaluator')
                elif subCadena == 'Restar':
                    tkn.append(35)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append('Si')
                    tipo.append('Palabra Reservada f(x)')
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporta_evaluator')
                elif subCadena == 'Multiplicar':
                    tkn.append(36)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append('Si')
                    tipo.append('Palabra Reservada')
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporta_evaluator')
                elif subCadena == 'Dividir':
                    tkn.append(37)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append('Si')
                    tipo.append('Palabra Reservada')
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reportar_evaluator')
                elif subCadena == 'Escribir':
                    tkn.append(38)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append('Si')
                    tipo.append('Palabra Reservada')
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reportar_evaluator')
                elif subCadena == 'Graph':
                    tkn.append(39)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append('Si')
                    tipo.append('Palabra Reservada')
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporta_evaluator')
                elif subCadena == 'Caracter':
                    tkn.append(40)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append('Si')
                    tipo.append('Palabra Reservada')
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporta_evaluator')
                elif subCadena == 'Entero':
                    tkn.append(41)
                    lx.append(subCadena)
                    numL.append(str(i+1))
                    numC.append(columna)
                    pR.append('Si')
                    tipo.append('Palabra Reservada')
                    Lista_token.append(mis_tokenes)
                    Gra1_HTML('reporta_evaluator')
        columna = 0
            #Gra1_HTML("Tabla_d_simbolos")
        #else:
            #Gra2_HTML("Errores_Lexicos")
def Analizar_sintactico():
    estado = []
    auxiliar = []
    numero = []
    n_fila = []
    n_columna = []
    num_T_simbolos = None
def parea(self, x ):
    self.POP()
    self.Tipo_d_var(x)

def Gra1_HTML(reporta_evaluator):
    mi_file = open('Tabla_d_simbolos.html', 'w')
    mi_file.close()
    mi_file = open('Tabla_d_simbolos.html', 'a')
    mi_file.write('<html>')
    token_leido = Tabla_simbolo_lexico
    mi_file = open('Tabla_d_simbolos.html', 'a')
    mi_file.write('<title>Tabla de Simbolos 1.2</title>\n')
    mi_file.write('<body>\n')
    mi_file.write('<center><img src="logo.jpg" WIDTH=100% HEIGHT=180></center>\n')
    mi_file.write('<center><h2>Tabla de Simbolos</h2></center>\n')
    mi_file.write('<TABLE ALIGN = \"center\"border=\"1\"WIDTH=80%>\n')
    mi_file.write('<TR BGCOLOR=\"white\">\n')
    mi_file.write(
        '<td>Token</td><td>Lexema</td><td>No_Linea</td><td>No_Columna</td><td>Palabra_Reservada</td><td>Tipo</td>\n')
    mi_file.write('</TR>\n')
    for i in xrange(0, len(Lista_token)):
        token_leido = Lista_token[i]
        print(len(lista_tokens))
        mi_file.write('<TR>')
        mi_file.write('<td>' + str(tkn[i]) + '</td>' + '<td>' + str(lx[i]) + '</td>' + '<td>' + str(numL[i]) + '</td>' + '<td>' +
                      str(numC[i]) + '</td>' + '<td>' + str(pR[i]) + '</td>' + '<td>' + tipo[i] + '</td>')
        mi_file.write('</TR>')
    mi_file.write('</TABLE>\n')
    mi_file.write('</body>\n')
    mi_file.write('</html>\n')
    mi_file.close()


def Gra2_HTML(reporte_error):
    mi_file_error = open('Errores_Lexicos.html', 'w')
    mi_file_error.close()
    mi_file_error = open('Errores_Lexicos.html', 'a')
    mi_file_error.write('<html>')
    token_leido_err = Tabla_error_lexico
    mi_file_error = open('Errores_Lexicos.html', 'a')
    mi_file_error.write('<title>Tabla de Simbolos 1.1 </title>\n')
    mi_file_error.write('<body>\n')
    mi_file_error.write('<center><img src="logo.jpg" WIDTH=100% HEIGHT=180><center>\n')
    mi_file_error.write('<center><h2>Tabla de Errores Lexicos</h2></center>\n')
    mi_file_error.write('<TABLE ALIGN = \"center\"border=\"1\"WIDTH=80%>\n')
    mi_file_error.write('<TR BGCOLOR=\"white\">\n')
    mi_file_error.write('<td>Numero_Error</td><td>Simbolo</td><td>Numero_fila</td><td>Numero_columna</td>')
    mi_file_error.write('</TR>\n')
    for j in xrange(0, len(Lista_tokenE)):
        token_leido_err = Lista_tokenE[j]
        print(len(Lista_tokenE))
        mi_file_error.write('<TR>')
        mi_file_error.write('<td>' + str(tkn[j]) + '</td>' + '<td>' + str(lx[j]) + '</td>' + '<td>' +
                            str(numL[j]) + '</td>' + '<td>' + str(numC[j]) + '</td>')
        mi_file_error.write('</TR>')
    mi_file_error.write('</TABLE>\n')
    mi_file_error.write('</body>\n')
    mi_file_error.write('</html>\n')
    mi_file_error.close()

def Gra2_HTML(reporte_error):
    mi_file_error = open('Error_Sintactico.html', 'w')
    mi_file_error.close()
    mi_file_error = open('Error_Sintactico.html', 'a')
    mi_file_error.write('<html>')
    token_leido_err = Tabla_error_lexico
    mi_file_error = open('Error_Sintactico.html', 'a')
    mi_file_error.write('<title>Tabla de Error Sintactico </title>\n')
    mi_file_error.write('<body>\n')
    mi_file_error.write('<center><img src="logo.jpg" WIDTH=100% HEIGHT=180><center>\n')
    mi_file_error.write('<center><h2>Tabla de Errores Sintactico</h2></center>\n')
    mi_file_error.write('<TABLE ALIGN = \"center\"border=\"1\"WIDTH=80%>\n')
    mi_file_error.write('<TR BGCOLOR=\"white\">\n')
    mi_file_error.write('<td>Numero_Error</td><td>Simbolo</td><td>Numero_fila</td><td>Numero_columna</td><td>Tipo_d_Error</td>')
    mi_file_error.write('</TR>\n')
    for s in xrange(0, len(Lista_tokenE)):
        token_leido_err = Lista_tokenE[s]
        print(len(Lista_tokenE))
        mi_file_error.write('<TR>')
        mi_file_error.write('<td>' + str(tkn[s]) + '</td>' + '<td>' + str(lx[s]) + '</td>' + '<td>' +
                            str(numL[s]) + '</td>' + '<td>' + str(numC[s]) + '</td>')
        mi_file_error.write('</TR>')
    mi_file_error.write('</TABLE>\n')
    mi_file_error.write('</body>\n')
    mi_file_error.write('</html>\n')
    mi_file_error.close()

def Match(tkn):
    if(piensa_analisa == tkn):
            global cta
            cta = cta + 1
            global piensa_analisa

            try:
                piensa_analisa=Token[cta]
                print 'TOKEN:', cta
            except IndexError:
                print 'Termina todas las Listas de Tokens'

    elif(piensa_analisa != tkn):
        #global d
        global cta
        cta=cta+1
        #global piensa_analisa

        try:
            TokenEncontr.append("'"+[int(piensa_analisa)]+"'")
            TokenEsperad.append("'"+[int(tkn)]+"'")
            ColumnaSinta.append(numL[cta])
            LineaSintact.append(numC[cta])
            print 'Se predecia: "' + [int(tkn)] + '" Y ser vio "' + [int(piensa_analisa)] + '"'
            piensa_analisa=Token[cta]
            print 'TOKEN: ', cta
        except IndexError:
            print 'Esto es un Error'

def Numero_rango():
    if(Token[cta] == tkn):
        parea('0')

def Traer():
    if(piensa_analisa == '0' ):
        #aqui va Gramatica estructurada
        global cta
        cta = cta +1
        Token[cta]
        parea('0')
    elif(Token[cta] == '1'):
        parea('1')
    elif(piensa_analisa == '2'):
        print('Hola')

def Evaluador():
    Match(tkn)

def Sintactico():
    cta = 0
    cta  = cta+1
    global piensa_analisa
    piensa_analisa = Token[0]
    Traer()
    Evaluador()

def Dec():
    Match(tkn)

def Def():
    print('print')

def Res():
    print('print')

menu1 = Menu(crea_ventana)
crea_ventana.config(menu=menu1)
menu1_1 = Menu(menu1, tearoff=0)
menu1.add_cascade(label="Edicion", menu=menu1_1)
menu1_1.add_command(label="Abrir .xval", command=lambda: abrir_xval())
menu1_1.add_command(label="Guardar archivo", command=lambda: guardar_xval())
menu1_1.add_separator()
menu1_1.add_command(label="New Area Edicion", command=lambda: mNew("New Area Edicion"))
menu1_1.add_command(label="Salir Evaluator", command=lambda: salir_interfaz_evaluator("Salir Evaluator"))

menu1_2 = Menu(menu1, tearoff=0)
menu1.add_cascade(label="Mostrar", menu=menu1_2)
menu1_2_1 = Menu(menu1_2, tearoff=0)
menu1_2.add_cascade(label="Analisis Lexico", menu=menu1_2_1)
menu1_2_1.add_command(label="Tabla de Errores 1.1", command=lambda: AFD_Analizador_lexico())
menu1_2_1.add_command(label="Tabla de Simbolos 1.2", command=lambda: AFD_Analizador_lexico())
menu1_2_1_2 = Menu(menu1_2_1, tearoff=0)
menu1_2.add_cascade(label="Front End", menu=menu1_2_1_2)
menu1_2_1_2.add_command(label="Analizador Sintactico", command=lambda: Match(tkn))
menu1_2_1_2.add_command(label="Analizador Semantico", command=lambda: msjApertura("Analizador Semantico"))
menu1_2_1_2.add_separator()
menu1_2_1_2_3 = Menu(menu1_2_1_2, tearoff=0)
menu1_2_1_2.add_cascade(label="Tabla de Errores 2.0", menu=menu1_2_1_2_3)
menu1_2_1_2_3.add_command(label="Error Sintactico", command=lambda: msjApertura("Error Sictactico"))
menu1_2_1_2_3.add_command(label="Error Semantico", command=lambda: msjApertura("Error Semantico"))

menu1_3 = Menu(menu1, tearoff=0)
menu1.add_cascade(label="Posicion_Actual", menu=menu1_3)
menu1_3.add_command(label="Ubicar-Cursor", command=lambda: mostrar_cursor("Ubicar-Cursor"))

menu1_4 = Menu(menu1, tearoff=0)
menu1.add_cascade(label="Compilar", menu=menu1_4)
menu1_4.add_command(label="Generar Documento", command=lambda: msjApertura("Generar Documento"))
menu1_4.add_command(label="Reporte .PDF", command=lambda: msjApertura("Reporte .PDF"))

menu1_5 = Menu(menu1, tearoff=0)
menu1.add_cascade(label="Acerca de...", menu=menu1_5)
menu1_5.add_command(label="Est.: Samuel Alberto Perez Jimenez",
                    command=lambda: msjApertura("Est.: Samuel Alberto Perez Jimenez"))
menu1_5.add_command(label="Carnet: 2009-25238", command=lambda: msjApertura("Carnet: 200925238"))

text.configure(yscrollcommand=scroll.set)
text.tag_configure('bold_italics', font=('Verdana', 12, 'bold', 'italic'))
text.tag_configure('big', font=('Verdana', 24, 'bold'))
text.tag_configure('color', foreground='blue', font=('Tempus Sans ITC', 14))
text.tag_configure('groove', relief=GROOVE, borderwidth=2)
text.tag_bind('bite', '<1>', lambda e, t=text: t.insert(END, "Text"))

text.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)

# boton_abrir = Button(crea_ventana, text = "Abrir Archivo .xval", command=msjApertura)
# boton_abrir.pack()

# caja_txt = Entry(crea_ventana)
# caja_txt.pack()

mainloop()
