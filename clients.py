

class Clients():
        def validarDNI(dni):
            try:
                tabla = 'TRWAGKYFPDXBNJZSQVHLCKE' #letras dni
                dig_ext= 'XYZ' #tabla letras extranjero
                reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'} #letras que identifican extranjero cambiadas por nº
                numeros = '1234567890'
                dni = dni.upper() #conver letra a mayús
                if len(dni) == 9: #el dni debe tener 9 caracteres
                    dig_control = dni[8]    #tomo la letra
                    dni = dni[:8]
                    if dni[0] in dig_ext:
                        dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                    return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control
                        #devuelve true si se dan las 2 condiciones y sale del módulo o sino false y sale del módulo
                return False #sino delvuelve falso
            except:
                print('error en la aplicación')
                return None