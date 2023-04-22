import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('usuarios.csv')

df['edad'].hist()

edad_promedio = df['edad'].mean()
plt.axvline(edad_promedio, color='r', linestyle='dashed', linewidth=2)

plt.xlabel('Edad')
plt.ylabel('Cantidad de usuarios')
plt.title('Distribución de edades de los usuarios')

plt.show()