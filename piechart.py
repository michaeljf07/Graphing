import matplotlib.pyplot as plt

y = [35, 25, 25, 15]
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels=mylabels)
plt.legend(loc='upper right')
plt.show() 