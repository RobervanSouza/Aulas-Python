import requests
url = "terra.com.br/"
file = open('sub.txt')
for linha in file:
    linha = linha.strip()  # tira o espaço entre as linha
    sub_check = f"https://{linha}.{url}"
    try:
        r = requests.get(sub_check)
        print('sucesso')
        print(sub_check)
        print('################')
    except:
        continue












