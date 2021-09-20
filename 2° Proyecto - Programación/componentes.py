from datetime import date, datetime
from helpers import borrarPantalla, gotoxy
import time

class Menu:
    def __init__(self,titulo="",opciones=[],col=6,fil=1):
        self.titulo=titulo
        self.opciones=opciones
        self.col=col
        self.fil=fil
        
    def menu(self):
        gotoxy(self.col,self.fil);print(self.titulo)
        self.col-=5
        for opcion in self.opciones:
            self.fil +=1
            gotoxy(self.col,self.fil);print(opcion)
        gotoxy(self.col+5,self.fil+2)
        opc = input("Elija opcion[1...{}]:".format(len(self.opciones))) 
        return opc   

class Valida:
    def solo_numeros(self,mensajeError,col,fil):
        while True: 
            gotoxy(col,fil)            
            valor = input()
            try:
                if int(valor) > 0:
                    break
            except:
                gotoxy(col,fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col,fil);print(" "*len(mensajeError))
        return valor

    def solo_letras(self,mensajeError,col,fil):
        while True: 
            gotoxy(col,fil)            
            valor = input()
            try:
                v = valor.isalpha()
                if v == True:
                    break    
            except:
                gotoxy(col,fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col,fil);print(" "*len(mensajeError))
        return valor

    def solo_decimales(self,mensajeError,col,fil):
        while True: 
            gotoxy(col,fil)            
            valor = input()
            try:
                if float(valor) > 0:
                    break
            except:
                gotoxy(col,fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col,fil);print(" "*len(mensajeError))
        return float(valor)

    def solo_enteros(self,mensajeError,col,fil):
        while True: 
            gotoxy(col,fil)            
            valor = input()
            try:
                if int(valor) > 0:
                    break
            except:
                gotoxy(col,fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col,fil);print(" "*len(mensajeError))
        return int(valor)

    def cedula_Telefono(self,mensajeError,col,fil):
        while True:
            gotoxy(col,fil)            
            valor = input()
            try:
                v = int(valor)
                val = str(valor)
                if v>0 and len(val)==10:
                    break 
            except:
                gotoxy(col,fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col,fil);print(" "*len(mensajeError))
        return valor

    def fecha(self,mensajeError,col,fil):
        while True: 
            gotoxy(col,fil)            
            valor = input()
            try:
                if datetime.strptime(valor,'%Y-%m-%d'):
                    break
            except:
                gotoxy(col,fil);print(mensajeError)
                time.sleep(2)
                gotoxy(col,fil);print(" "*len(mensajeError))
        return valor
        
    
class otra:
    pass 
    

