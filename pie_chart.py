import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('updated_restaurants1.csv')
cuisine_counts = data['Cuisine'].value_counts().head(10)

plt.pie(cuisine_counts.values, labels=cuisine_counts.index, autopct='%1.1f%%')
plt.title('Top 10 Cuisine Types')
plt.axis('equal')
plt.show()
