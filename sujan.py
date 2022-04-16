import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt


input = pd.read_csv('data.csv')
cor = input.corr()
print(cor)
sb.set(font_scale=4)
sb.set(font_scale=0.7)   # set the font scale at 0.7
sb.heatmap(cor, annot=False, cmap="YlGnBu", cbar=True)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()