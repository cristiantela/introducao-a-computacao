import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("a5_ENERGIA.csv")

dataframe.boxplot()

plt.show()