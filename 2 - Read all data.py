import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("a5_ENERGIA.csv")

x = dataframe.Ano
y = dataframe.Energia

plt.plot(x, y)
# plt.savefig("img/2.png")
plt.show()