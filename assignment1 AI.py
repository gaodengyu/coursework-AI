import numpy as np
import matplotlib.pyplot as plt

def galton_board(num_balls, num_levels):
    slots = np.zeros(num_levels + 1)
    
    for _ in range(num_balls):
        position = 0
        for _ in range(num_levels):
            position += np.random.choice([0, 1]) 
        slots[position] += 1
    
    return slots

num_balls = 100000  
num_levels = 200   

slots = galton_board(num_balls, num_levels)

x = np.arange(len(slots))
plt.bar(x, slots, width=0.8, color='blue', alpha=0.7)
plt.xlabel('Slots')
plt.ylabel('Number of Balls')
plt.title('Galton Board Simulation Result')
plt.show()

mu = num_levels / 2
sigma = np.sqrt(num_levels / 4)
x_values = np.linspace(0, num_levels, 100)
y_values = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_values - mu) / sigma) ** 2)
plt.plot(x_values, y_values * num_balls * (x_values[1] - x_values[0]), color='red')
plt.hist(np.random.normal(mu, sigma, num_balls), bins=num_levels, alpha=0.3, density=True, color='gray')
plt.title('Gaussian Distribution vs Galton Board')
plt.show()
