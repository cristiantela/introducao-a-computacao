import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("a5_ENERGIA.csv").head(30)

x = dataframe.Ano
y = dataframe.Energia


plt.plot(x, y)

plt.xlabel('Mes')
plt.xticks(x, x, rotation='vertical')
plt.ylabel('Consumo de energia eletrica')
plt.title('Valores mensais do consumo de energia eletrica no estado do Espirito Santo')
plt.grid(True)

plt.show()