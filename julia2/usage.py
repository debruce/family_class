
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)

'''
fig, ax = plt.subplots() #figure w/ one axis
ax.plot(x, x, label='linear') 
ax.plot(x, x**2, label='quadratic')  
ax.plot(x, x**3, label='cubic') 
ax.set_xlabel('x label')  
ax.set_ylabel('y label')  
ax.set_title("Simple Plot") 
ax.legend()  
#axis not necessary to define beforehand, can just use plt.plot
'''


def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph

    Parameters
    ----------
    ax : Axes
        The axes to draw to

    data1 : array
       The x data

    data2 : array
       The y data

    param_dict : dict
       Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out : list
        list of artists added
    """
    out = ax.plot(data1, data2, **param_dict)
    return out

data1, data2, data3, data4 = np.random.randn(4, 100)
fig, ax = plt.subplots(1, 1)
my_plotter(ax, data1, data2, {'marker': 'x'})

fig, (ax1, ax2) = plt.subplots(1, 2)
my_plotter(ax1, data1, data2, {'marker': 'x'})
my_plotter(ax2, data3, data4, {'marker': 'o'})

