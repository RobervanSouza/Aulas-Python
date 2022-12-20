# ######  AULA DE FUNÇÃO E DICIONARIO

alvos = [{'ip': '127.0.4.1', 'port': [32, 32, 23, 22], 'ativo': True, 'so': 'linux'},
         {'ip': '127.0.0.1', 'port': [50, 55, 33, 22], 'ativo': False, 'so': 'windows'},
         {'ip': '127.0.5.1', 'port': [30, 35, 33, 32], 'ativo': True, 'so': 'windows'},
         {'ip': '127.0.6.1', 'port': [40, 45, 43, 42], 'ativo': False, 'so': 'linux'},
         {'ip': '127.0.7.1', 'port': [50, 55, 53, 52], 'ativo': True, 'so': 'windows'}]
############################################################################################
# for t in alvos:   MOSTRA SEPARADO CADA LINHA  MODO DE PESQUISA TIPO DICIONARIOS
# print(t['ip'])
# print(t['ativo'])
# print(t['so'])
# print('##################')
# print('atacando o alvo =>' + t['ip'])
##########################################################################
# for alvo in alvos: # como se fosse fazer pesquisa em um dicionario
#     if alvo['so'] == 'linux':  # se o alvo for linux
#
#         print('atacando linux -> ' + str(alvo['port']))  # se o alvo for linux mostra a porta para atacar
#          for porta in alvo['port']:
# #             print('atacando a porta -> ' + str(
# #                 porta))  # se encontrar alvo em porta, então, mosta porta>> STR(transforma em strig)
# #        print('################')
# else:
#  print('atacando windows')
#   print(alvo['ip'])
#  print('################')

# def encontra_linux(alvos):
#     for alvo in alvos:
#         if alvo['so'] == 'linux':
#             print('encontra_linux -> ' + str(alvo['ativo']), alvo['port']) # MOSTRA O LINUX QUE ENCONTROU E SE ESTA ATIVO E A PORTA
#             break
#
# encontra_linux(alvos)
##############################################################################33
# BREAK E CONTINUE
for alvo in alvos:
    if alvo['so'] == 'linux':
        print('Não ataquei porque e linux>>> ' )
        continue
    print('Agora encontrei o linux' + str(alvo['ip']))
