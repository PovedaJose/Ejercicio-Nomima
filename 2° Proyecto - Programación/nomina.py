from componentes import Menu,Valida
from helpers import borrarPantalla,gotoxy, mensaje
from crudArhivos import Archivo 
from entidadesRol import *
from datetime import date
import time
 
# Procesos de las Opciones del Menu Mantenimiento
def empAdministrativos(): # -- F U N C I O N A --
    borrarPantalla()
    validacion = Valida()
    gotoxy(20,2);print('INGRESO DE EMPLEADOS ADMINISTRATIVOS')
    gotoxy(15,3);print('---------------------------------------------')
    gotoxy(15,5);print('- Nombre          : ') 
    gotoxy(15,6);print('- Cedula          : ') 
    gotoxy(15,7);print('- telefono        : ') 
    gotoxy(15,8);print('- Dirección       : ')
    gotoxy(15,9);print('- Sueldo          : ') 
    gotoxy(15,10);print('- Fecha Ingreso   : [AAAA-MM-DD]') 
    gotoxy(15,11);print('- ID Cargo        : [   ]') 
    gotoxy(15,12);print('- ID departamento : [   ]') 
    NomEmpleA = validacion.solo_letras(' << ERROR. Solo ingresar letras >>',35,5) 
    cedulaAdmin = validacion.cedula_Telefono('<< ERROR. Solo ingresar numeros >>',35,6) 
    telefonoAdmin = validacion.cedula_Telefono('<< ERROR. Solo ingresar números >>',35,7) 
    gotoxy(35,8);direcAdmin = input().capitalize()
    sueldoAdmin = validacion.solo_numeros('<< ERROR. Solo ingresar enteros >>',35,9)
    feIngAdmin = validacion.fecha('<< ERROR. Ingresar el formato adecuado [AAAA-MM-DD] >>',36,10) 
    listaCrgo,entCrgo = [],None
    while not listaCrgo:
        gotoxy(37,11);idCrg = input().upper()
        archiCargo = Archivo('./archivos/cargo.txt', '|')
        listaCrgo = archiCargo.buscar(idCrg)
        if listaCrgo:
            entCrgo = Cargo(listaCrgo[1],listaCrgo[0])
            gotoxy(41,11);print(entCrgo.descripcion)
        else:
            gotoxy(41,11);print('No existe Cargo con dicho código.')
            time.sleep(1);gotoxy(41,11);print(' '*50)
    listaDepa,entDepa = [],None
    while not listaDepa:
        gotoxy(37,12);idDep = input().upper()
        archidepart = Archivo('./archivos/departamento.txt', '|')
        listaDepa = archidepart.buscar(idDep)
        if listaDepa:
            entDepa = Departamento(listaDepa[1],listaDepa[0])
            gotoxy(41,12);print(entDepa.descripcion) 
        else:
            gotoxy(41,12);print('No existe departamento con dicho código.')
            time.sleep(1);gotoxy(41,12);print(' '*50)
    gotoxy(15,14); print('Está seguro de Grabar el registro(s/n): ')
    gotoxy(54,14);grabar = input().lower()
    if grabar == 's':
        archiAdmin = Archivo('./archivos/administrativo.txt', '|')
        Admin = archiAdmin.leer()
        if Admin: codEmpleA = int(Admin[-1][0][1])+1
        else: codEmpleA=1
        cEmpleAdmin = 'A'+str(codEmpleA)
        eAdmin = Administrativo(NomEmpleA,entDepa,entCrgo,direcAdmin,cedulaAdmin,telefonoAdmin,feIngAdmin,sueldoAdmin,cEmpleAdmin)
        dato = eAdmin.getEmpleado() 
        dato = '|'.join(dato)
        archiAdmin.escribir([dato],'a')
        gotoxy(15,15);input('Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...')
    else:
        gotoxy(15,15);input("Registro No fue Grabado\n presione una tecla para continuar...")

def empObreros(): # -- F U N C I O N A --
    borrarPantalla()
    validacion = Valida()
    gotoxy(20,2);print('INGRESO DE EMPLEADOS OBREROS')
    gotoxy(15,3);print('--------------------------------------')
    gotoxy(15,5);print('- Nombre          : ')
    gotoxy(15,6);print('- Cedula          : ') 
    gotoxy(15,7);print('- telefono        : ') 
    gotoxy(15,8);print('- Dirección       : ')
    gotoxy(15,9);print('- Sueldo          : ')
    gotoxy(15,10);print('- Fecha Ingreso   : [AAAA-MM-DD]')  
    gotoxy(15,11);print('- ID Cargo        : [   ]') 
    gotoxy(15,12);print('- ID departamento : [   ]') 
    NomEmpleO = validacion.solo_letras('<< Error. Solo ingresar letras>>',35,5) 
    cedulaObrer = validacion.cedula_Telefono('<< ERROR. Solo ingresar 10 números >>',35,6) 
    telefonoObrer = validacion.cedula_Telefono('<< ERROR. Solo ingresar números >>',35,7) 
    gotoxy(35,8);direcObrer = input()
    sueldoObrer = validacion.solo_numeros('<< Error.Solo ingresar numeros >>',35,9) 
    feIngObrer = validacion.fecha('<< ERROR. Ingresar el formato adecuado [AAAA-MM-DD] >>',36,10) 
    listaCrgo,entCrgo = [],None
    while not listaCrgo:
        gotoxy(37,11);idCrg = input().upper()
        archiCargo = Archivo('./archivos/cargo.txt', '|')
        listaCrgo = archiCargo.buscar(idCrg)
        if listaCrgo:
            entCrgo = Cargo(listaCrgo[1],listaCrgo[0])
            gotoxy(41,11);print(entCrgo.descripcion)
        else:
            gotoxy(41,11);print('No existe Cargo con dicho código.')
            time.sleep(1);gotoxy(41,11);print(' '*50)
    listaDepa,entDepa = [],None
    while not listaDepa:
        gotoxy(37,12);idDep = input().upper()
        archidepart = Archivo('./archivos/departamento.txt', '|')
        listaDepa = archidepart.buscar(idDep)
        if listaDepa:
            entDepa = Departamento(listaDepa[1],listaDepa[0])
            gotoxy(41,12);print(entDepa.descripcion) 
        else:
            gotoxy(41,12);print('No existe departamento con dicho código.')
            time.sleep(1);gotoxy(41,12);print(' '*50)
    gotoxy(15,14); print('Está seguro de Grabar el registro(s/n): ')
    gotoxy(54,14);grabar = input().lower()
    if grabar == 's':
        archiObrer = Archivo('./archivos/obrero.txt', '|')
        Obrer = archiObrer.leer()
        if Obrer: codEmpleO = int(Obrer[-1][0][1])+1
        else: codEmpleO=1
        cObrero = 'O'+str(codEmpleO)
        eObrer = Obrero(NomEmpleO,entDepa,entCrgo,direcObrer,cedulaObrer, telefonoObrer, feIngObrer,sueldoObrer, cObrero)
        dato = eObrer.getEmpleado() 
        dato = '|'.join(dato)
        archiObrer.escribir([dato],'a')
        gotoxy(15,15);input('Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...')
    else:
        gotoxy(15,15);input("Registro No fue Grabado\n presione una tecla para continuar...")

def cargos():
    borrarPantalla()     
    gotoxy(20,2);print("MANTENIMIENTO DE CARGOS")
    gotoxy(15,3);print('----------------------------------')
    gotoxy(15,4);print("Codigo: --")
    gotoxy(15,5);print("Descripcion Cargo: ")
    gotoxy(33,5)
    desCargo = input()
    gotoxy(15,7); print('Está seguro de Grabar el registro(s/n): ')
    gotoxy(54,7);grabar = input().lower() 
    if grabar == 's':
        archiCargo = Archivo("./archivos/cargo.txt","|")
        cargos = archiCargo.leer()
        if cargos : idSig = int(cargos[-1][0])+1
        else: idSig=1
        cargo = Cargo(desCargo,idSig)
        datos = cargo.getCargo()
        datos = '|'.join(datos)
        archiCargo.escribir([datos],"a")
        gotoxy(15,8);input('Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...')
    else:
        gotoxy(15,8);input("Registro No fue Grabado\n presione una tecla para continuar...")


def departamento():  # -- F U N C I O N A --
    borrarPantalla()
    gotoxy(20,2);print('MANTENIMIENTO DE DEPARTAMENTO')
    gotoxy(15,3);print('----------------------------------------')
    gotoxy(15,4);print('Código: -- ')
    gotoxy(15,5);print('Descripción: ')
    gotoxy(28,5)
    desDepar = input()
    gotoxy(15,7); print('Está seguro de Grabar el registro(s/n): ')
    gotoxy(54,7);grabar = input().lower() 
    if grabar == 's':
        archiDepar = Archivo('./archivos/departamento.txt', '|')
        depas = archiDepar.leer()
        if depas : idsig = int(depas[-1][0])+1 
        else: idsig=1
        depart = Departamento(desDepar,idsig)
        datos = depart.getDepartamento()
        datos = '|'.join(datos)
        archiDepar.escribir([datos],'a')
        gotoxy(15,8);input('Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...')
    else:
        gotoxy(15,8);input("Registro No fue Grabado\n presione una tecla para continuar...")


def empresa(): # -- F U N C I O N A --
    borrarPantalla()  
    validacion = Valida()    
    gotoxy(20,2);print("MANTENIMIENTO DE EMPRESA")
    gotoxy(15,3);print('------------------------------------')
    gotoxy(15,4);print("Razon Social : ")
    gotoxy(15,5);print("Dirección    : ")
    gotoxy(15,6);print("Telefono     : ")
    gotoxy(15,7);print("Ruc          : ")
    gotoxy(30,4);razonSocial = input()
    gotoxy(30,5);direccion = input()
    tel=validacion.solo_numeros("Error: Solo numeros",30,6)
    ruc=validacion.solo_numeros("Error: Solo numeros",30,7)
    gotoxy(15,9);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54,9);grabar = input().lower()
    if grabar == "s":
        archiEmpresa = Archivo("./archivos/empresa.txt","|")
        archiEmpresa.leer()
        emp = Empresa(razonSocial,direccion,tel,ruc)
        datos = emp.getEmpresa()
        datos = '|'.join(datos)
        archiEmpresa.escribir([datos],"w")
        gotoxy(15,10);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
        gotoxy(15,10);input("Registro No fue Grabado\n presione una tecla para continuar...")

def parametro():
    borrarPantalla()  
    validacion = Valida()    
    gotoxy(20,2);print("MANTENIMIENTO DE DEDUCCIONES")
    gotoxy(15,3);print('------------------------------------')
    gotoxy(15,4);print("Iess       : ")
    gotoxy(15,5);print("Comisión   : ")
    gotoxy(15,6);print("Antiguedad : ")
    iess=validacion.solo_decimales("Error: Solo numeros",33,4) 
    comision=validacion.solo_decimales("Error: Solo numeros",33,5)
    antiguedad=validacion.solo_decimales("Error: Solo numeros",33,6)
    gotoxy(15,8);print("Esta seguro de Grabar El registro(S/N):")
    gotoxy(54,8);grabar = input().upper()
    if grabar == "S":
        archiDeducciones = Archivo("./archivos/deducciones.txt","|")
        archiDeducciones.leer()
        dedu = Deduccion(iess,comision,antiguedad)
        datos= dedu.getDeduccion()
        datos = '|'.join(datos)
        archiDeducciones.escribir([datos],"w")
        gotoxy(15,8);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
        gotoxy(15,8);input("Registro No fue Grabado\n presione una tecla para continuar...")


# ...........................................................................................
# Opciones del Menu Novedades
def sobretiempos():
   borrarPantalla()     
   gotoxy(20,2);print("INGRESO DE HORAS EXTRAS")
   gotoxy(15,3);print('------------------------------------')
   empleado,entEmpleado = [],None
   aamm,h50,h100=0,0,0
   while not empleado:
      gotoxy(15,5);print("Empleado ID[    ]: ")
      gotoxy(28,5);id = input().upper()
      archiEmpleado = Archivo("./archivos/obrero.txt","|")
      empleado = archiEmpleado.buscar(id)
      if empleado:
          entEmpleado = Obrero(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],empleado[8],empleado[0]) 
          gotoxy(35,5);print(entEmpleado.nombre)
      else: 
         gotoxy(27,5);print("No existe Empleado con ese codigo[{}]:".format(id))
         time.sleep(2);gotoxy(27,5);print(" "*40) 
   gotoxy(15,6);print("Periodo[aaaamm]")
   gotoxy(15,7);print("Horas50:")
   gotoxy(15,8);print("Horas100:")
   validar = Valida()   #--VALIDACIONES--
   aamm=validar.solo_numeros("<< Error: Solo numeros >>",23,6)
   h50=validar.solo_numeros("<< Error: Solo numeros >>",23,7)
   h100=validar.solo_numeros("<< Error: Solo numeros >>",24,8)
   gotoxy(15,9);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,9);grabar = input().lower()
   if grabar == "s":
        archiSobretiempo = Archivo("./archivos/sobretiempo.txt","|")
        sobretiempos = archiSobretiempo.leer()
        if sobretiempos : idSig = int(sobretiempos[-1][0])+1
        else: idSig=1
        sobretiempo = Sobretiempo(entEmpleado,aamm,h50,h100,True,idSig)
        datos = sobretiempo.getSobretiempo()
        datos = '|'.join(datos)
        archiSobretiempo.escribir([datos],"a")                 
        gotoxy(10,10);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(10,10);input("Registro No fue Grabado\n presione una tecla para continuar...")     


def prestamos(): # -- F U N C I O N A --
    borrarPantalla()     
    gotoxy(20,2);print("INGRESO DE PRESTAMO")
    gotoxy(15,3);print('-----------------------------')
    empleado,entEmpleado = [],None
    aamm,valor, numP, saldo=0,0,0,0
    while not empleado:
        gotoxy(15,5);print("Empleado ID[    ]: ")
        gotoxy(27,5);id = input().upper()
        archiEmpleado1 = Archivo("./archivos/obrero.txt","|")
        archiEmpleado2 = Archivo("./archivos/administrativo.txt","|")
        empleado1 = archiEmpleado1.buscar(id)
        empleado2 = archiEmpleado2.buscar(id)
        if empleado1:
            entEmpleado = Obrero(empleado1[1],empleado1[2],empleado1[3],empleado1[4],empleado1[5],empleado1[6],empleado1[7],empleado1[8],empleado1[0]) 
            gotoxy(35,5);print(entEmpleado.nombre)
            break
        elif empleado2:
            entEmpleado = Administrativo(empleado2[1],empleado2[2],empleado2[3],empleado2[4],empleado2[5],empleado2[6],empleado2[7],empleado2[8],empleado2[0]) 
            gotoxy(35,5);print(entEmpleado.nombre)
            break
        else: 
            gotoxy(27,5);print("No existe Empleado con ese codigo[{}]:".format(id))
            time.sleep(2);gotoxy(27,5);print(" "*40)
    gotoxy(15,6);print("Periodo[aaaamm]")
    gotoxy(15,7);print("Valor:")
    gotoxy(15,8);print("Número de Pago:")
    gotoxy(15,9);print("Saldo:")
    validar = Valida() #--VALIDACIONES--
    aamm=validar.solo_numeros("<< Error: Solo numeros >>",23,6)
    valor=validar.solo_decimales("<< Error: Solo numeros >>",23,7)
    numP=validar.solo_enteros("<< Error: Solo enteros >>",31,8)
    saldo=validar.solo_decimales("<< Error: Solo numeros >>",23,9)
    gotoxy(15,9);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54,9);grabar = input().lower()
    if grabar == "s":
        archiPrestamo = Archivo("./archivos/prestamo.txt","|")
        prestamos = archiPrestamo.leer()
        if prestamos : idSig = int(prestamos[-1][0])+1
        else: idSig=1
        prestamos = Prestamo(entEmpleado,aamm,valor,numP, saldo,True,idSig)
        datos = prestamos.getPrestamo()
        datos = '|'.join(datos)
        archiPrestamo.escribir([datos],"a")                 
        gotoxy(10,10);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
        gotoxy(10,10);input("Registro No fue Grabado\n presione una tecla para continuar...")


# ..........................................................................................
#  O P C I O N E S   D E   R O L   D E   P A G O
def rolAdministrativo():
   borrarPantalla()     
   gotoxy(20,2);print("ROL ADMINISTRATIVO")
   aamm=0
   gotoxy(15,6);print("Periodo[aaaamm]")
   validar = Valida()
   aamm=validar.solo_numeros("Error: Solo numeros",23,6)
   gotoxy(15,7);print("Esta seguro de Procesar el Rol(s/n):")
   gotoxy(54,7);grabar = input().lower()
   entEmpAdm = None
   if grabar == "s":
        archiEmp = Archivo("./archivos/administrativo.txt","|")
        ListaEmpAdm = archiEmp.leer()
        if ListaEmpAdm : 
            archiEmpresa = Archivo("./archivos/empresa.txt","|")
            empresa = archiEmpresa.leer()[0]
            entEmpresa = Empresa(empresa[0],empresa[1],empresa[2],empresa[3])
            archiDeducciones = Archivo("./archivos/deducciones.txt","|")
            deducciones = archiDeducciones.leer()[0]
            entDeduccion = Deduccion(float(deducciones[0]),float(deducciones[1]),float(deducciones[2]))
            nomina = Nomina(date.today(),aamm)
            for empleado in ListaEmpAdm:
              entEmpAdm = Administrativo(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],float(empleado[8]),empleado[0]) 
              nomina.calcularNominaDetalle(entEmpAdm,entDeduccion)
            datosCab = nomina.getNomina()
            datosCab = '|'.join(datosCab)
            archiRol = Archivo("./archivos/rolCabAdm.txt","|")
            archiRol.escribir([datosCab],"a")
            archiDet = Archivo("./archivos/rolDetAdm.txt","|")
            datosDet = nomina.getDetalle()        
            for dt in datosDet:
                dt = nomina.aamm+'|'+'|'.join(dt)
                archiDet.escribir([dt],"a")          
            nomina.mostrarCabeceraNomina(entEmpresa.razonSocial,entEmpresa.direccion,entEmpresa.telefono,entEmpresa.ruc,"A D M I N I S T R A T I V O")
            nomina.mostrarDetalleNomina()
   else:
       gotoxy(10,10);input("Rol No fue Procesado\n presione una tecla para continuar...")
   print(' ')     
   input("\n Presione una tecla continuar...")  

def consultaRol():
   borrarPantalla()
   validar = Valida()   
   gotoxy(20,2);print("CONSULTA DE ROL OBRERO - ADMINISTRATIVO")
   rol=0
   aamm=""
   gotoxy(15,4);print("Obrero-Administrativo(O/A): ")
   gotoxy(15,6);print("Periodo[aaaamm]")
   gotoxy(44,4)
   rol=input().upper()
   aamm=validar.solo_numeros("Error: Solo numeros",23,6)
   gotoxy(15,7);print("Esta seguro de consultar el Rol(s/n):")
   gotoxy(54,7);procesar = input().lower()
   if procesar == "s":
        if rol == "A": 
            tit = "A D M I N I S T R A T I V O"
            archiRolCab = Archivo("./archivos/rolCabAdm.txt","|")
            archiRolDet = Archivo("./archivos/rolDetAdm.txt","|")
        else: 
            tit = "O B R E R O"
            archiRolCab = Archivo("./archivos/rolCabObre.txt","|")
            archiRolDet = Archivo("./archivos/rolDetObre.txt","|")
        cabrol = archiRolCab.buscar(aamm)
        if cabrol:
            entCabRol = Nomina(cabrol[1],cabrol[0])
            entCabRol.totIngresos=float(cabrol[2])
            entCabRol.totDescuentos=float(cabrol[3])
            entCabRol.totPagoNeto=float(cabrol[4])
            detalle= archiRolDet.buscarLista(aamm)
            for det in detalle:
                entCabRol.detalleNomina.append(det[1:])       
            archiEmpresa = Archivo("./archivos/empresa.txt","|")
            empresa = archiEmpresa.leer()[0]
            entEmpresa = Empresa(empresa[0],empresa[1],empresa[2],empresa[3])
            entCabRol.mostrarCabeceraNomina(entEmpresa.razonSocial,entEmpresa.direccion,entEmpresa.telefono,entEmpresa.ruc,tit)
            entCabRol.mostrarDetalleNomina()
        else:
            gotoxy(10,10);input("No existe rol con ese periodo\n presione una tecla para continuar...")            
   else:
       gotoxy(10,10);input("Consulta Cancelada\n presione una tecla para continuar...")  
   print(' ')   
   input("\n Presione una tecla continuar...")  


def rolObrero(): 
    borrarPantalla()    
    gotoxy(20,2);print("ROL OBRERO")
    aamm=0
    gotoxy(15,6);print("Periodo[aaaamm]")
    validar = Valida()
    aamm=validar.solo_numeros("Error: Solo numeros",23,6)
    gotoxy(15,7);print("Esta seguro de Procesar el Rol(s/n):")
    gotoxy(54,7);grabar = input().lower()
    entEmpObr = None
    if grabar == "s":
        archiEmp = Archivo("./archivos/obrero.txt","|")
        ListaEmpObr = archiEmp.leer()
        if ListaEmpObr : 
            archiEmpresa = Archivo("./archivos/empresa.txt","|")
            empresa = archiEmpresa.leer()[0]
            entEmpresa = Empresa(empresa[0],empresa[1],empresa[2],empresa[3])
            archiDeducciones = Archivo("./archivos/deducciones.txt","|")
            deducciones = archiDeducciones.leer()[0]
            entDeduccion = Deduccion(float(deducciones[0]),float(deducciones[1]),float(deducciones[2]))
            nomina = Nomina(date.today(),aamm)
            for empleado in ListaEmpObr:
                entEmpObr = Obrero(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],int(empleado[7][:4]),float(empleado[8]),empleado[0]) 
                nomina.calcularNominaDetalle(entEmpObr,entDeduccion)
            datosCab = nomina.getNomina()
            datosCab = '|'.join(datosCab)
            archiRol = Archivo("./archivos/rolCabObre.txt","|")
            archiRol.escribir([datosCab],"a")
            archiDet = Archivo("./archivos/rolDetObre.txt","|")
            datosDet = nomina.getDetalle()          
            for dt in datosDet:
                dt = nomina.aamm+'|'+'|'.join(dt)
                archiDet.escribir([dt],"a")
            nomina.mostrarCabeceraNomina(entEmpresa.razonSocial,entEmpresa.direccion,entEmpresa.telefono,entEmpresa.ruc,"O B R E R O S")
            nomina.mostrarDetalleNomina()
    else:
        gotoxy(10,10);input("Rol No fue Procesado\n presione una tecla para continuar...")  
    print(' ')   
    input("\n Presione una tecla continuar...")


# Menu Proceso Principal
opc=''
while opc !='4':  
    borrarPantalla()      
    menu = Menu("MENU PRINCIPAL",["1) Mantenimiento","2) Novedades","3) Rol de Pago","4) Salir"],20,10)
    opc = menu.menu()
    if opc == "1":
        opc1 = ''
        while opc1 !='7':
            borrarPantalla()    
            menu1 = Menu("MENU MANTENIMIENTO",["1) Empleados Administratvos","2) Empleados Obreros","3) Cargos","4) Departamentos","5) Empresa","6) Parametros","7) Salir"],20,10)
            opc1 = menu1.menu()
            if opc1 == "1":
                empAdministrativos()
            elif opc1 == '2':
                empObreros()
            elif opc1 == "3":
                cargos() 
            elif opc1 == '4':
                departamento()
            elif opc1 == '5':
                empresa()
            elif opc1 == '6':
                parametro()                       
    elif opc == "2":
            borrarPantalla() 
            menu2 = Menu("MENU NOVEDADES",["1) Sobretiempo","2) Prestamos","3) Salir"],20,10)
            opc2 = menu2.menu()
            if opc2 == "1":
                sobretiempos()
            elif opc2 == "2":
                prestamos()
    elif opc == "3":
            borrarPantalla()
            menu3 = Menu("MENU ROL",["1) Rol Administrativos","2) Rol Obreros","3) Consulta Rol","4) Salir"],20,10)
            opc3 = menu3.menu()
            if opc3 == "1":
                rolAdministrativo() 
            elif opc3 == "2":
                rolObrero()
            elif opc3 == "3":
                consultaRol()
    elif opc == "4":
           borrarPantalla()
           print("Gracias por su visita....")
    else:
          print("Opcion no valida") 

input("Presione una tecla para salir")
borrarPantalla()

