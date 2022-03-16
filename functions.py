import matplotlib.pyplot as plt
import numpy as np

m = int(input("What is the slope of the line? "))
b = int(input("What is the y intercept of the line? "))

x = np.linspace(-5,5,100) # Density of numbers in between
y = m*x+b # Equation

plt.plot(x, y, '-r', label='y=2x+1')
plt.title('Graph of y=2x+1')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.legend(loc='upper left')
plt.grid()
plt.show()