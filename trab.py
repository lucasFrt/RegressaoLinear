import numpy as np
import matplotlib.pyplot as plt


#NOTAS
y = np.array([7, 8, 7, 9, 8, 9, 7, 8, 10, 7, 9, 9, 8, 9, 9, 10, 7, 8, 9, 8, 8, 7, 7.5, 8])
#HORAS SEMANAIS
x = np.array([10, 11, 10, 30, 25, 20, 12, 12, 10, 10, 10, 13, 12, 5, 10, 25, 10, 5, 10, 20, 10, 8, 15, 15])
coeficiente_angular, intercepto = np.polyfit(x, y, 1)

print(f'Coeficiente Angular: {coeficiente_angular}')
print(f'Intercepto: {intercepto}')

y_pred = coeficiente_angular * x + intercepto
print(y_pred)

#PARTE DO GRAFICO 
plt.scatter(x, y, label = 'Dados Originais')
plt.plot(x, y_pred, color = 'yellow', linewidth = 3, label = 'Linha de Regressão')
plt.xlabel('Horas de estudo Semanais:')
plt.ylabel('Notas em Geral:')
plt.legend()
plt.title('Trabalho: Regressão Linear Simples')
plt.grid(True)
plt.show()