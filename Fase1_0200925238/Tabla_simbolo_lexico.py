__author__ = 'sammy'
class Tabla_simbolo_lexico:
    token = None
    lexema = None
    numero_linea = None
    numero_columna = None
    palabra_reservada= None
    tipo = None

    def Tabla_simbolo_lexico(self, token=0, lexema=" ", numero_linea=0, numero_columna=0, palabra_reservada=" ", tipo =" "):
        self.token = token;
        self.lexema = lexema;
        self.numero_linea = numero_linea;
        self.numero_columna = numero_columna;
        self.palabra_reservada = palabra_reservada;
        self.tipo = tipo;