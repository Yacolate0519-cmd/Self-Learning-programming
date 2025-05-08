import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0 , 2 * np.pi , 100)

fig , ax = plt.subplots()

ax.set_xlim(0 , 2 * np.pi)

ax.set_ylim(-1 , 1)

sin_line, = ax.plot(x , np.sin(x) , color = 'blue' , label = 'sin')
cos_line, = ax.plot(x , np.cos(x) , color = 'red' , label = 'cos')
sum_line, = ax.plot(x , np.sin(x) + np.cos(x) , color = 'black' , label = 'sum')

ax.legend()

while True:
    sin_data = np.sin(x)
    cos_data = np.cos(x - 4.575)
    sum_data = sin_data + cos_data
    
    sin_line.set_ydata(sin_data)
    cos_line.set_ydata(cos_data)
    sum_line.set_ydata(sin_data + cos_data)
    
    fig.canvas.draw()
    
    plt.pause(0.1)

    x += 0.1
        