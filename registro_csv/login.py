import pandas as pd

df = pd.read_csv('usuarios.csv')

def login():
  email = input('Ingrese su email: ')
  contrasena = input('Ingrese su contraseña: ')
  fila = df.loc[df['email'] == email]
  try:
    if contrasena == str(fila['contrasena'].values[0]):
      print('usuario logueado')
      return fila.to_dict('records')[0]
    else:
      print('La contraseña y el email no coinciden')
      return
  except Exception as e:
    print("Ha ocurrido un error :(. El mail que ingreso no esta registrado")
    print(f'{type(e).__name__}: {e}')
    return

print(login())