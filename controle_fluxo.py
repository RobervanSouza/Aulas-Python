# def check_email(username):
#     admin = 'robervan'
#     if username == admin:
#         msn = username + ' é admin'
#     else:
#       if username == 'auriene':
#          msn = username + ' não é admin, mas tem permissão'
#       else:
#             msn = username + ' não é admin'
#     return msn


# def check_email(username):
#     admin = 'robervan'
#     if username == admin:
#         msn = username + ' é admin'
#     elif username == 'auriene':
#         msn = username + ' não é admin, mas tem permissão'
#     else:
#          msn = username + ' não é admin'
#     return msn


def check_email(username):
    admin = 'robervan'
    if username == admin or username == 'auriene':
  #  if username == admin and username == 'auriene': # OBRIGA PARA OS DOIS SER VERDADEIROS
        msn = username + ' é admin'
    else:
        msn = username + ' não é admin'
    return msn

print(check_email('teste'))
print(check_email('robervan'))
print(check_email('auriene'))
