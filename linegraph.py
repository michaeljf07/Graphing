import matplotlib.pyplot as plt
   
Year = [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010]
Unemployment_Rate = [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
Single_Motherhood = [4,5,8.2,6,5.5,3.7,4,9.7,3,6.9]

# 1st  line
plt.plot(Year, Unemployment_Rate, color='red', marker='o', label='Unemployement Rate')
# 2nd line
plt.plot(Year, Single_Motherhood, color='blue', marker='o', label='Single Motherhood')

plt.title('Unemployment Rate and Single Motherhood', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Rate', fontsize=14)
plt.grid(True)
plt.legend()
plt.show()