from itertools import product # modulo que calcula las combinaciones
from subprocess import run # modulo para ejecutar procesos
from time import sleep # modulo de herramientas del tiempo
from time import time
from os import system # modulo para ejecutar comandos del systema en consola
import re # modulo para filtros
import hashlib # modulo de tratamiento de hashes para librerias
from imap_tools import MailBox # modulo para manipular el correo electronico
from lib_printLogo import printLogo # modulo para imprimir el Logo al Inicio
from lib_AreThereCreatedAccounts import AreThereCreatedAccounts # modulo para verificar si existen cuentas ya creadas

# Defino Funciones --------------------------
def CreatingAccounts():# modulo desencadenador para crear cuentas de mega
    system("cls") # Limpio la consola
    print("Gmail: ",gmail)
    print("Contraseña: ",opcionDeContrasenia)
    print("\n")
    print("Cuantas cuentas de MEGA decea crear ?")
    print("Minimo = 1   |   Maximo = ",numeroCuentasPosibles)
    numeroCuentasCrear = input("Ingrece cantidad: ")
    system("cls")
    listGmail = GeneratingMallaGmails(gmail)
    f_cuentasMEGA = open("cuentas_mega.dat","a+")
    sleep(2)
    system("cls")
    print("Pasando a ejecutar Script de creacion de cuentas ..")
    print('* ANTENCION !! a partir de aky evite manipular los componentes como el Mouse y el Teclado')
    sleep(6)
    system("cls")
    i=0
    while i < int(numeroCuentasCrear): # Creo la cantidad de cuentas de mega espesificada
        inicio = time() # Establesco el tiempo para medir el tiempo que le toma ejecutar la accion
        if opcionDeContrasenia == 'Random': # Establesco la contraseña de la cuenta de MEGA
            contraseniaCuentaMega = random.randrange(100000, 1000000) # genero un numero aleatorio
        else:
            contraseniaCuentaMega = opcionDeContrasenia # Establesco como contraseña la ingrezada por el usuario
        run(["RegGmail.exe", str(listGmail[i]),str(contraseniaCuentaMega)]) # ejecuta la primer etapa de la creacion de la cuenta de MEGA. Abre la consola de cmd de mega y ejecuta el comando para crear/registar una cuenta
        run(["ActiveLinkAccountsMega.exe", str(GetLinkConfirm()),str(contraseniaCuentaMega)]) # ejecuto etapa 2 y 3, leeo buzon para extraer el link de confirmacion luego activo cuenta de mega                                                                             
        f_cuentasMEGA.writelines(str(listGmail[i])+';'+str(contraseniaCuentaMega)+"\n") # Escribo Gmail y contraseña de la cuenta generada en un archivo para guardar registro
        print("Cuenta numero: ",i+1," | Gmail: ",str(listGmail[i])," | Completada | Tiempo: ",time()-inicio) # Muestro el tiempo que le llevo completar el registro de una cuenta
        i += 1
    f_cuentasMEGA.close()
    print("Completado Todo \n Dando por finalizado !!")
    sleep(10)
    
    
def GeneratingMallaGmails(lgmail): # Creo lista de Gmail con sus combinaciones posibles
    print("Creando lista de combinaciones de Gmail")
    lgmail = lgmail.split('@')[0] # Divido el gmail desde el @ y me quedo con la parte de la isquierda
    lgmail = lgmail.replace('.', '') # Remplazo todo caracter de "." que pueda haber en el nombre
    malla = list(lgmail) # Convierto en lista el Gmail
    for i in range(len(malla)): # Recorro generando los caracteres posibles de combinaciones
        malla[i] = [malla[i],"."+str(malla[i])]
    malla[len(list(lgmail))-1].append(str(malla[len(list(lgmail))-1][0])+".") # Agrego a la ultima conbinacion de la lista un caracter mas de posibilidad
    mallaPre = list(product(*malla)) # Genero una lista con todas las combinaciones posibles
    for i in range(len(mallaPre)): # Recoro malla de Gmail(lista de gmail pre conbinadas el anexo de "@gmail.com" del Gmail)
        mallaPre[i] = (''.join(mallaPre[i]))+'@gmail.com' # Anexo respectiva identidad a cada combinacion de la lista de gmail
    print("Lista de combinaciones posibles completada")
    return mallaPre # retorno la lista de gmail posibles ya final
    
    
def GetLinkConfirm(): # modulo que lee el buzon del gmail y filtra hasta extraer el link de activacion de mega
    f_cunataPassApp = open("key_of_application_software.dat","r")
    mailbox = MailBox('imap.gmail.com')
    mailbox.login(gmail,f_cunataPassApp.readline())
    f_cunataPassApp.close()
    # Obtengo Todos los mensajes del buzon
    mensaje=""
    for m in mailbox.fetch():
        subject = m.subject
        # Filtro para obtener solo los de MEGA
        if re.search(r'MEGA',subject,re.I):  # Aquí se hace un pequeño filtro en el asunto
            mensaje= m.text
    # Filtro hasta dejar el ultimo mensaje de mega y su enlace de confirmacion de email
    confirm=""
    for item in mensaje.split("\n"):
        if "confirm" in item:
            confirm=item.strip()  
    mailbox.logout()
    return confirm    


def ContinuingCreatingAccounts():
    print("ContinuingCreatingAccounts()")
    with open("cuentas_mega.dat","r") as f:
        ultimoGmailReg = f.readlines()[-1]
        f.close()
    cunatasMEGA = open("cuentas_mega.dat","a+")
    mallaGmails = GeneratingMallaGmails(gmail)
    ultimoGmailReg = ultimoGmailReg.split('@')[0]
    L_posicionGmail=0
    print("ultimo Gmail Registrado = ",ultimoGmailReg)
    for i in range(len(mallaGmails)):
        if ultimoGmailReg in str(mallaGmails[i]):
            print("Gmail coinsidente[]= ",str(mallaGmails[i]).split('@')[0])
            L_posicionGmail=i
            break
    sleep(4)
    system("cls")
    numeroCuentasPosibles = (2**(len(gmail.split('@')[0])-1))*3-L_posicionGmail
    print("Cantidad de cuentas de Mega Restantes: ",numeroCuentasPosibles)
    print("Cuantas cuentas de MEGA decea crear ?")
    print("Minimo = 1   |   Maximo = ",numeroCuentasPosibles)
    numeroCuentasCrear = input("Ingrece cantidad: ")
    system("cls")
    print("Pasando a ejecutar Script de creacion de cuentas ..")
    print('* ANTENCION !! a partir de aky evite manipular los componentes como el Mouse y el Teclado')
    sleep(6)
    system("cls")
    i=0
    while i < int(numeroCuentasCrear): # Creo la cantidad de cuentas de mega espesificada
        inicio = time() # Establesco el tiempo para medir el tiempo que le toma ejecutar la accion
        if opcionDeContrasenia == 'Random': # Establesco la contraseña de la cuenta de MEGA
            contraseniaCuentaMega = random.randrange(100000, 1000000) # genero un numero aleatorio
        else:
            contraseniaCuentaMega = opcionDeContrasenia # Establesco como contraseña la ingrezada por el usuario
        run(["RegGmail.exe", str(listGmail[i]),str(contraseniaCuentaMega)]) # ejecuta la primer etapa de la creacion de la cuenta de MEGA. Abre la consola de cmd de mega y ejecuta el comando para crear/registar una cuenta
        run(["ActiveLinkAccountsMega.exe", str(GetLinkConfirm()),str(contraseniaCuentaMega)]) # ejecuto etapa 2 y 3, leeo buzon para extraer el link de confirmacion luego activo cuenta de mega                                                                             
        cunatasMEGA.writelines(str(listGmail[i])+';'+str(contraseniaCuentaMega)+"\n") # Escribo Gmail y contraseña de la cuenta generada en un archivo para guardar registro
        print("Cuenta numero: ",i+1," | Gmail: ",str(listGmail[i])," | Completada | Tiempo: ",time()-inicio) # Muestro el tiempo que le llevo completar el registro de una cuenta
        i += 1
    cunatasMEGA.close()
    print("Completado Todo \n Dando por finalizado !!")
    sleep(10)

# Fin Funciones ----------------------


# ++++++++++++ START ++++++++++++++++
printLogo() # Imprimo Logo
print('v3') # Imprimo Version
sleep(5) # Timepo de espera 5 seg
system("cls") # Limpio la consola

global gmail # declaro variable como global
global numeroCuentasPosibles # declaro variable como global
global opcionDeContrasenia # declaro variable como global

 # Le pido al usuario que ingrece Gmail
gmail = input("Ingrece Gmail a utilizar: ")
system("cls") # Limpio la consola
print("Quiere utilizar contraseñas aleatorias o definir una para todas las cuentas ?")
print('[1] Generar Aleatorias')
print('[2] Quiero definir una')
if (int(input()) == 1):
    opcionDeContrasenia = "Random"
else:
    opcionDeContrasenia = input('Ingrece contraseña: ')

numeroCuentasPosibles = (2**(len(gmail.split('@')[0].replace('.', ''))-1))*3 # Calculo el numero de cuentas posibles para crear


if(AreThereCreatedAccounts(gmail)): # verifico si ya hay cuentas creadas para continuarlas, retorna True/False
    ContinuingCreatingAccounts() # Continuo creando cuentas
else:
    CreatingAccounts() # Inicio crear cuentas desencadenador

