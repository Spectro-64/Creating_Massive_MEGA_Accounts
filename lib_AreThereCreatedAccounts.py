import os # modulo para ejecutar comandos del systema

def AreThereCreatedAccounts(l_cuentaGmail): # Defino modulo para Verificar si existen cuentas del gmail ingrezado en "cuentas_mega.dat", retorna True/False
    result_CreatingAcount=False
    
    if(os.stat('cuentas_mega.dat').st_size == 0):# Verifico si el tamaño del archivo es distinto de 0
        result_CreatingAcount=False # significa que el archivo esta vacío, retornando false
    else:
        with open("cuentas_mega.dat","r") as f: # Abro el archivo de cuentas de mega
            last_line_cuentas = f.readlines()[-1] # Extraigo la ultima linea que contiene el ultimo gmail generado
            f.close()
   
        if('@' in last_line_cuentas):
            last_line_cuentas_short = last_line_cuentas.split('@')[0].replace('.', '') # Limpio el Gmail quitandole el @gmail.com y cualquier "." que tenga
            if(l_cuentaGmail.split('@')[0].replace('.', '') == last_line_cuentas_short): # Comparo Gmail ingrezado con el del registro de cuentas de mega
                result_CreatingAcount=True # Significa que son iguales, retornando true
        else:
            result_CreatingAcount=False # Significa que no son iguales, retornando false
    return result_CreatingAcount