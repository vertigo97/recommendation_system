import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('updated_restaurants1.csv')

plt.hist(data['Review'], bins=10, edgecolor='black')
plt.xlabel('Review Rating')
plt.ylabel('Count')
plt.title('Distribution of Restaurant Reviews')
plt.show()
