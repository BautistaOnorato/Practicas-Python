import pandas as pd
from validaciones import email_valido, valor_vacio, contrasena_mayor_a

info_usuario = {
  'nombre': '',
  'apellido': '',
  'email': '',
  'edad': 0,
  'contrasena': ''
}

def ingresar_nombre():
  while True:
    nombre = input("Nombre: ")
    if valor_vacio(nombre):
      info_usuario["nombre"] = [nombre]
      break
    else:
      print("Minimo un caracter")
    
  
def ingresar_apellido():
  while True:
    apellido = input("Apellido: ")
    if valor_vacio(apellido):
      info_usuario["apellido"] = [apellido]
      break
    else:
      print("Minimo un caracter")
  
def ingresar_edad():
  while True:
    edad = input("Edad: ")
    try:
      edad = int(edad)
      info_usuario["edad"] = [edad]
    except:
      print("Ingrese un número por favor")
    else:
      break
    
  
def ingresar_email():
  while True:
    email = input("Email: ")
    if email_valido(email):
      info_usuario["email"] = [email]
      break
    else:
      print("El email ingresado no es válido")
  

def ingresar_contrasena(num):
  while True:
    contrasena = input("Contrasena: ")
    if contrasena_mayor_a(contrasena, num):
      info_usuario["contrasena"] = [contrasena]
      break
    else:
      print(f"Minimo {num} caracteres")

def registro():
  ingresar_nombre()
  ingresar_apellido()
  ingresar_email()
  ingresar_edad()
  ingresar_contrasena(6)
  try:
    df = pd.DataFrame(info_usuario)
    df.to_csv('usuarios.csv', mode='a', index=False, header=False)
    print("Usuario registrado") 
  except Exception as e:
    print("Ha ocurrido un error :(")
    print(f'{type(e).__name__}: {e}')
    exit()

registro()