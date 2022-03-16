import matplotlib.pyplot as plt
import numpy as np

# create a dataset
boys = [3, 12, 5, 18, 45]
girls = [1, 4, 7, 11, 33]
year = ('A', 'B', 'C', 'D', 'E')
x_pos = np.arange(len(year))

# Create bars
plt.bar(x_pos-0.2, boys, color='red', width=0.4, label='boys')
plt.bar(x_pos+0.2, girls, color='blue', width=0.4, label='girls')

# Create names on the x-axis
plt.xticks(x_pos, year)

plt.xlabel('Year', fontsize=14)
plt.ylabel('Number', fontsize=14)
plt.title('girls v. boys results')
plt.legend()
plt.show()