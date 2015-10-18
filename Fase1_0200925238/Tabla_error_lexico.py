__author__ = 'sammy'
class Tabla_error_lexico:
    numError = None
    caracter = None
    linea = None
    columna = None
    def Tabla_error_lexico(self, numError=0, caracter = ' ', linea=0, columna=0 ):
            self.numError = numError;
            self.caracter = caracter;
            self.linea = linea;
            self.columna = columna;


