import os

def gotoxy(x,y): 
    print("%c[%d;%df"%(0x1B,y,x),end="")
    #& gotoxy(5,2): print('hola')

def borrarPantalla():
    os.system("cls") 


