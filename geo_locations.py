import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('updated_restaurants1.csv')

plt.scatter(data['Longitude'], data['Latitude'])
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Geographic Locations of Restaurants')
plt.show()
