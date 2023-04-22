import re

reg_ex_email = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def email_valido(email):
  if re.fullmatch(reg_ex_email, email):
    return True
  else:
    return False
  
def valor_vacio(texto):
  if len(texto) <= 0:
    return False
  else:
    return True

def contrasena_mayor_a(text, num):
  if len(text) >= num:
    return True
  else:
    return False