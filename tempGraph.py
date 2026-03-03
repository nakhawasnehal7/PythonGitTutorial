#Author SnehalNakhawa
#Date 24th February 2026
#Description - This program generates random monthly temperatures for
# three cities and plots them using matplotlib


import random
import  matplotlib.pyplot as plt


time = []
for i in range(1, 13):
    time.append(i)

city1 = []
for i in range(12):
    city1.append(random.randint(10, 30))

city2 = []
for i in range(12):
    city2.append(random.randint(10, 30))


city3 = []
for i in range(12):
    city3.append(random.randint(10, 30))


plt.plot(time, city1)
plt.plot(time, city2)
plt.plot(time, city3)

plt.title("Monthly Temperature Comparison")
plt.xlabel("Month")
plt.ylabel("Temperature (Degree Celsius)")

plt.legend(["New York", "Mumbai", "London"])

plt.show()