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

crea_ventana = Tk()
crea_ventana.title("Fase1_200925238, Analizador Lexico")
crea_ventana.geometry("570x490")
text = Text(crea_ventana, height=30, width=68)
scroll = Scrollbar(crea_ventana, command=text.yview)
mis_tokens = []
mis_errores = []

def msjApertura(texto):
    print ("Abriendo Archivos en C:/")

def abrir_xval(abrir_otro_xval):
    ruta_archivo_xval = askopenfile(filetypes =(("expr. evaluator", "*.xval"),("All files", "*.*")))
    lee_cadena = ruta_archivo_xval
    x = lee_cadena.read()
    text.insert(CURRENT,x)

def guardar_xval(event):
    archivo_actual=asksaveasfile(filetypes =(("expr. evaluator", "*.xval"),("All files", "*.*")))
    print(archivo_actual)

def salir_interfaz_evaluator(sale_de_app):
    m_sale = tkMessageBox.askokcancel(title = "Fase 1 Front End, Fase 2 Back End-->Del Compilador", message = "Desea Salir del Proyecto Evaluator Fase 1, Front End?")
    if m_sale > 0:
        crea_ventana.destroy()
        return

def mNew(editar_nuevO_existente):
    crea_ventana_otra = Text(crea_ventana, height=30, width=68).pack()
    return

def Analizar_Todo_Evaluator():
    a = []
    a = text.get().split("\n")
    flag = False
    for j in len(a):
        for i in len(a[j]):
              if str(a[j][i]) == '@' or str(a[j][i]) == '$' or str(a[j][i]) == '^' or str(a[j][i]) == '%':
                 print('Cadena')
              else:
                 flag = True
                 error = Tabla_error_lexico
                 error.numError = j
                 error.caracter = str[j]
                 error.linea = j
                 error.columna=i
                 mis_errores.append(error)
    if flag == False:
        for x in len(a):
            for y in len(a[x]):
                if str.isalpha(str(a[x][y])):
                    palabra = ''
                    while y < len(a[x]) & str.isalpha(str(a[x][y])):
                        palabra = palabra + a[x][y]
                        y+=1
                    otro_token = Tabla_simbolo_lexico
                    otro_token.token = 1
                    otro_token.lexema = palabra
                    otro_token.numero_linea = x
                    otro_token.numero_columna = y - palabra.__len__()
                    otro_token.palabra_reservada = 'Si'
                    otro_token.tipo = 'identificador'
                    mis_tokens.append(otro_token)
                if y < len(a[x]) & str.isdigit(a[x].a[y]):
                    palabra = ''
                    otro_token_1 = Tabla_simbolo_lexico
                    while y < len(a[x]) & str.isalpha(a[x].a[y]):
                        palabra = palabra + a[x].a[y]
                        if (y+2) < len(a[x]) & a[x].a[y+1] == '.' & str.isdigit(a[x].a[y+2]):
                            otro_token_1.tipo='Numero_decimal'
                            palabra = palabra + a[x].a[y+1] + a[x].a[y+2]
                            y += 2
                    y += 1
                    otro_token_1.lexema = palabra
                    if otro_token_1.tipo.__eq__(''):
                       otro_token_1.tipo= 'Numero: ' + palabra
                    else:
                       otro_token_1.tipo = otro_token_1.tipo + palabra

                otro_token_1.tipo=2
                otro_token_1.numero_linea= x
                otro_token_1.numero_columna = y - len(palabra)
                mis_tokens.append(otro_token_1)

def Gra1_HTML (reporta_evaluator):
    mi_token = Tabla_simbolo_lexico
    mi_error = Tabla_error_lexico
    t_simbolos = [mi_token]
    errores = [mi_error]
    lista_tokens = [mi_token]
    lista_errores = [mi_error]
    text1 = text.get('0.0',END)
    lector = text1.split(' ')

    mi_file = open('Tabla_d_simbolos.html', 'w')
    mi_file.close()
    mi_file = open('Tabla_d_simbolos.html', 'a')
    mi_file.write('<html>')
    mi_file_error = open('Errores_Lexicos.html', 'w')
    mi_file_error.close()
    mi_file_error = open('Errores_Lexicos.html', 'a')
    mi_file_error.write('<html>')
    Linea=0
    Fila=0

    for x in lector:
       print("--x--" + x)
       Linea = Linea+1
       Fila=0
       for y in x:
          Fila = Fila+1
          print("---y---" + y)
          if x == "[a-z]":
              mi_token.token = 0
              mi_token.lexema = "a-zA-Z"
              mi_token.numero_linea = Linea
              mi_token.numero_columna= Fila
              mi_token.palabra_reservada = "Si"
              mi_token.tipo = "Palabra Reservada"
              lista_tokens.append(mi_token)
          elif x == '[0-9]':
              mi_token.token = 1
              mi_token.lexema = "\d"
              mi_token.numero_linea = Linea
              mi_token.numero_columna = Fila
              mi_token.palabra_reservada = "No"
              mi_token.tipo = "digito"
              lista_tokens.append(mi_token)
          elif x == ",":
              mi_token.token = 2
              mi_token.lexema = ","
              mi_token.numero_linea = Linea
              mi_token.numero_columna = Fila
              mi_token.palabra_reservada = "No"
              mi_token.tipo = "Signo de Coma"
              lista_tokens.append(mi_token)
          elif x == "\\":
              mi_token.token = 3
              mi_token.lexema = "\\"
              mi_token.numero_linea = Linea
              mi_token.numero_columna = Fila
              mi_token.palabra_reservada = "No"
              mi_token.tipo = "Signo Grafico"
              lista_tokens.append(mi_token)
          elif x == "#":
              mi_token.token = 4
              mi_token.lexema = "#"
              mi_token.numero_linea = Linea
              mi_token.numero_columna = Fila
              mi_token.palabra_reservada = "Si"
              mi_token.tipo = "Signo de Comentario"
              lista_tokens.append(mi_token)
          elif x == "<":
              mi_token.token = 5
              mi_token.lexema = "<"
              mi_token.numero_linea = Linea
              mi_token.numero_columna = Fila
              mi_token.palabra_reservada = "No"
              mi_token.tipo = "Delimitador Inicio"
              lista_tokens.append(mi_token)
          elif x == ">":
              mi_token.token = 6
              mi_token.lexema = ">"
              mi_token.numero_linea = Linea
              mi_token.numero_columna = Fila
              mi_token.palabra_reservada = "Si"
              mi_token.tipo = "Delimitador Fin"
              lista_tokens.append(mi_token)
              break
          elif x == "{":
              mi_token.token = 7
              mi_token.lexema = "{"
              mi_token.numero_linea = Linea
              mi_token.numero_columna = Fila
              mi_token.palabra_reservada= "No"
              mi_token.tipo = "Llave Apertura"
              lista_tokens.append(mi_token)
          elif x == "}":
              mi_token.token = 8
              mi_token.lexema = "}"
              mi_token.numero_linea = Linea
              mi_token.numero_columna = Fila
              mi_token.palabra_reservada= "No"
              mi_token.tipo = "Llave cierre"
              lista_tokens.append(mi_token)
          elif x == "[":
              mi_token.token = 9
              mi_token.lexema = "["
              mi_token.numero_linea = Linea
              mi_token.numero_columna = Fila
              mi_token.palabra_reservada= "No"
              mi_token.tipo = "Corchete Apertura"
              lista_tokens.append(mi_token)
          elif x == "]":
              mi_token.token = 10
              mi_token.lexema = "]"
              mi_token.numero_linea = Linea
              mi_token.numero_columna = Fila
              mi_token.palabra_reservada = "No"
              mi_token.tipo = "Corchete Cierre"
              lista_tokens.append(mi_token)
          elif x == "(":
              mi_token.token = 11
              mi_token.lexema = "("
              mi_token.numero_linea = Linea
              mi_token.numero_columna = Fila
              mi_token.palabra_reservada = "No"
              mi_token.tipo = "Parentesis Apertura"
              lista_tokens.append(mi_token)
          elif x == ")":
              mi_token.token = 12
              mi_token.lexema = ")"
              mi_token.numero_linea = Linea
              mi_token.numero_columna = Fila
              mi_token.palabra_reservada = "No"
              mi_token.tipo = "Parentesis Cierre"
              lista_tokens.append(mi_token)
          elif x == ":":
              mi_token.token = 13
              mi_token.lexema = ":"
              mi_token.numero_linea = Linea
              mi_token.numero_columna = Fila
              mi_token.palabra_reservada = "No"
              mi_token.tipo = "Signo de Puntuacion"
              lista_tokens.append(mi_token)
          elif x == ".":
              mi_token.token = 14
              mi_token.lexema = "."
              mi_token.numero_linea = Linea
              mi_token.numero_columna = Fila
              mi_token.palabra_reservada = "No"
              mi_token.tipo = "Signo Punto"
              lista_tokens.append(mi_token)
          elif x == ";":
              mi_token.token = 15
              mi_token.lexema = ";"
              mi_token.numero_linea = Linea
              mi_token.numero_columna = Fila
              mi_token.palabra_reservada = "No"
              mi_token.tipo = "Signo de Punto && Coma"
              lista_tokens.append(mi_token)
              break
          elif x == " ' ":
              mi_token.token = 16
              mi_token.lexema = " ' "
              mi_token.numero_linea = Linea
              mi_token.numero_columna = Fila
              mi_token.palabra_reservada = "No"
              mi_token.tipo = "Comilla Simple"
              lista_tokens.append(mi_token)
          elif x == "|":
              mi_token.token = 17
              mi_token.lexema = "|"
              mi_token.numero_linea = Linea
              mi_token.numero_columna = Fila
              mi_token.palabra_reservada = "No"
              mi_token.tipo = "Barra Vertical"
              lista_tokens.append(mi_token)
          elif x == "+":
              mi_token.token = 18
              mi_token.lexema = "+"
              mi_token.numero_linea = Linea
              mi_token.numero_columna = Fila
              mi_token.palabra_reservada = "Si"
              mi_token.tipo = "Operador Aditivo"
              lista_tokens.append(mi_token)
          elif x == "-":
              mi_token.token = 19
              mi_token.lexema = "-"
              mi_token.numero_linea = Linea
              mi_token.numero_columna = Fila
              mi_token.palabra_reservada = "Si"
              mi_token.tipo = "Operador Resta"
              lista_tokens.append(mi_token)
          elif x == "*":
              mi_token.token = 20
              mi_token.lexema = "*"
              mi_token.numero_linea = Linea
              mi_token.numero_columna = Fila
              mi_token.palabra_reservada = "Si"
              mi_token.tipo = "Operador Producto"
              lista_tokens.append(mi_token)
          elif x == "/":
              mi_token.token = 21
              mi_token.lexema = "/"
              mi_token.numero_linea = Linea
              mi_token.numero_columna = Fila
              mi_token.palabra_reservada = "Si"
              mi_token.tipo = "Operador Division"
              lista_tokens.append(mi_token)
          elif x == "=":
              mi_token.token = 22
              mi_token.lexema = "="
              mi_token.numero_linea = Linea
              mi_token.numero_columna = Fila
              mi_token.palabra_reservada = "Si"
              mi_token.tipo = "Signo_Igual"
              lista_tokens.append(mi_token)
          elif x == "<<EVALUADOR>>":
              mi_token.token = 23
              mi_token.lexema = "EVALUADOR"
              mi_token.numero_linea= Linea
              mi_token.numero_columna = Fila
              mi_token.palabra_reservada = 'Si'
              mi_token.tipo = 'Palabra Reservada'
              lista_tokens.append(mi_token)
          elif x == "<<DECLARACIONES>>":
              mi_token.token = 24
              mi_token.lexema = 'DECLARACIONES'
              mi_token.numero_linea = Linea
              mi_token.numero_columna = Fila
              mi_token.palabra_reservada = 'Si'
              mi_token.tipo = 'Palabra Reservada'
              lista_tokens.append(mi_token)
          elif x == "<<DEFINICIONES>>":
              mi_token.token = 25
              mi_token.lexema = "DEFINICIONES"
              mi_token.numero_linea = Linea
              mi_token.numero_columna = Fila
              mi_token.palabra_reservada = "Si"
              mi_token.tipo = "Palabra Reservada"
              lista_tokens.append(mi_token)
          elif x == "RESULTADOS":
              mi_token.token = 26
              mi_token.lexema = "RESULTADOS"
              mi_token.numero_linea = Linea
              mi_token.numero_columna = Fila
              mi_token.palabra_reservada = "Si"
              mi_token.tipo = "Palabra Reservada"
              lista_tokens.append(mi_token)
          elif x == "PROYECTO_LFP":
              mi_token.token = 27
              mi_token.lexema = "PROYECTO_LFP"
              mi_token.numero_linea = Linea
              mi_token.numero_columna = Fila
              mi_token.palabra_reservada = "Si"
              mi_token.tipo = "Palabra Reservada"
              lista_tokens.append(mi_token)
          elif x == "FIN EVALUADOR":
              mi_token.token = 28
              mi_token.lexema = "FIN EVALUADOR"
              mi_token.numero_linea = Linea
              mi_token.numero_columna = Fila
              mi_token.palabra_reservada = "Si"
              mi_token.tipo = "Palabra Reservada"
              lista_tokens.append(mi_token)

    token_leido = Tabla_simbolo_lexico
    mi_file = open('Tabla_d_simbolos.html', 'a')
    mi_file.write('<title>Tabla de Simbolos 1.2</title>\n')
    mi_file.write('<body>\n')
    mi_file.write('<center><img src="logo.jpg" WIDTH=100% HEIGHT=180></center>\n')
    mi_file.write('<center><h2>Tabla de Simbolos</h2></center>\n')
    mi_file.write('<TABLE ALIGN = \"center\"border=\"1\"WIDTH=80%>\n')
    mi_file.write('<TR BGCOLOR=\"white\">\n')
    mi_file.write('<td>Token</td><td>Lexema</td><td>No_Linea</td><td>No_Columna</td><td>Palabra_Reservada</td><td>Tipo</td>\n')
    mi_file.write('</TR>\n')
    for i in range(len(lista_tokens)):
        #token_leido = lista_tokens[i]
        print(len(lista_tokens))
        mi_file.write('<TR>')
        mi_file.write('<td>' + str(lista_tokens[i].token) + '</td>'+'<td>'+str(lista_tokens[i].lexema)+'</td>'+'<td>'+str(lista_tokens[i].numero_linea)+'</td>'+'<td>'+str(lista_tokens[i].numero_columna)+'</td>'+'<td>'+str(lista_tokens[i].palabra_reservada)+'</td>'+'<td>'+str(lista_tokens[i].tipo)+'</td>')
        mi_file.write('</TR>')
    mi_file.write('</TABLE>\n')
    mi_file.write('</body>\n')
    mi_file.write('</html>\n')
    mi_file.close()

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
    for j in range(len(lista_errores)):
        token_leido_err = lista_errores[j]
        print(len(lista_errores))
        mi_file_error.write('<TR>')
        mi_file_error.write('<td>' + str(token_leido_err.numError) + '</td>' + '<td>' + str(token_leido_err.caracter) + '</td>' + '<td>'+str(token_leido_err.linea) + '</td>'+'<td>' + str(token_leido_err.columna) + '</td>')
        mi_file_error.write('</TR>')
    mi_file_error.write('</TABLE>\n')
    mi_file_error.write('</body>\n')
    mi_file_error.write('</html>\n')
    mi_file_error.close()

menu1 = Menu(crea_ventana)
crea_ventana.config(menu=menu1)
menu1_1 = Menu(menu1, tearoff=0)
menu1.add_cascade(label="Edicion", menu=menu1_1)
menu1_1.add_command(label="Abrir .xval", command=lambda: abrir_xval("Abrir .xval"))
menu1_1.add_command(label="Guardar archivo", command=lambda: guardar_xval("Guardar archivo"))
menu1_1.add_separator()
menu1_1.add_command(label="New Area Edicion", command=lambda: mNew("New Area Edicion"))
menu1_1.add_command(label="Salir Evaluator", command=lambda: salir_interfaz_evaluator("Salir Evaluator"))


menu1_2 = Menu(menu1, tearoff=0)
menu1.add_cascade(label="Mostrar", menu=menu1_2)
menu1_2_1 = Menu(menu1_2, tearoff=0)
menu1_2.add_cascade(label="Analisis Lexico", menu= menu1_2_1)
menu1_2_1.add_command(label="Tabla de Errores 1.1", command=lambda: msjApertura("Tabla de Errores"))
menu1_2_1.add_command(label="Tabla de Simbolos 1.2", command=lambda: Gra1_HTML("Tabla de Simbolos"))
menu1_2_1_2 = Menu(menu1_2_1, tearoff=0)
menu1_2.add_cascade(label="Front End", menu=menu1_2_1_2)
menu1_2_1_2.add_command(label="Analizador Sintactico", command=lambda: msjApertura("Analizador Sintactico"))
menu1_2_1_2.add_command(label="Analizador Semantico", command=lambda: msjApertura("Analizador Semantico"))
menu1_2_1_2.add_separator()
menu1_2_1_2_3 = Menu(menu1_2_1_2, tearoff=0)
menu1_2_1_2.add_cascade(label="Tabla de Errores 2.0", menu=menu1_2_1_2_3)
menu1_2_1_2_3.add_command(label="Error Sintactico", command=lambda: msjApertura("Error Sictactico"))
menu1_2_1_2_3.add_command(label="Error Semantico", command=lambda: msjApertura("Error Semantico"))


menu1_3 = Menu(menu1, tearoff=0)
menu1.add_cascade(label="Posicion_Actual", menu= menu1_3)
menu1_3.add_command(label="Ubicar-Cursor", command=lambda: msjApertura("Ubicar-Cursor"))


menu1_4 = Menu(menu1, tearoff=0)
menu1.add_cascade(label="Compilar", menu= menu1_4)
menu1_4.add_command(label="Generar Documento", command=lambda: msjApertura("Generar Documento"))
menu1_4.add_command(label="Reporte .PDF", command=lambda: msjApertura("Reporte .PDF"))


menu1_5 = Menu(menu1, tearoff=0)
menu1.add_cascade(label="Acerca de...", menu=menu1_5)
menu1_5.add_command(label="Est.: Samuel Alberto Perez Jimenez", command=lambda: msjApertura("Est.: Samuel Alberto Perez Jimenez"))
menu1_5.add_command(label="Carnet: 2009-25238", command=lambda: msjApertura("Carnet: 200925238"))

text.configure(yscrollcommand=scroll.set)
text.tag_configure('bold_italics', font=('Verdana', 12, 'bold', 'italic'))
text.tag_configure('big', font=('Verdana', 24, 'bold'))
text.tag_configure('color', foreground='blue', font=('Tempus Sans ITC', 14))
text.tag_configure('groove', relief=GROOVE, borderwidth=2)
text.tag_bind('bite', '<1>', lambda e, t=text: t.insert(END, "Text"))

text.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)

#boton_abrir = Button(crea_ventana, text = "Abrir Archivo .xval", command=msjApertura)
#boton_abrir.pack()

#caja_txt = Entry(crea_ventana)
#caja_txt.pack()

mainloop()