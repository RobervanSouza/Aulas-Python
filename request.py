import requests
url = " http://globo.com/"
lista = ['admin', 'password', 'senha', 'login']
for encontrados in lista:
    check_url = f"https://{encontrados}.{url}"
    try:
        r = requests.get(check_url)
        print(check_url)
        print(r.status_code)
    except:
        print("não encontrado")
    continue