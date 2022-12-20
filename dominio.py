import requests
import sys  # usuário informa o site
# lista de status online
status_online = [200, 403, 404, 302, 301]
# pega o valor que o usuário informar
site = str(sys.argv[1])
# verifica se tem http em site
if 'http' not in site:
    # se não tem http no site então informa com a mensagem
    print('verifica se você colocou http no site')
else:
    # se tem http no site então informa com a mensagem
    r = requests.get(site)
    if r.status_code in status_online:
        print('site online')
    else:
        print('site offline')
 ##########################################################################################################3
status_online = [200, 403, 404, 302, 301]
site = str(sys.argv[1])
if '.'not in site: # verifica se tem o pontto
    print('dominio invalido')
else:
    if 'http' not in site:  # si tiver  o ponto então verifica se o http esta correto
        site = f"http://{site}" # se não estiver http então adiciona http
        r = requests.get(site)
        if r.status_code in status_online:
            print("online")
        else:
            print("ofline")