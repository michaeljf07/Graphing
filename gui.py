import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt 

window = tk.Tk()
window.title("Linear Equation Grapher")
window.geometry('500x600+50+50')

# Text
ymxb = ttk.Label(text="y=mx+b", font="arial").place(x=230,y=10)

global slope
global y_intercept
slope = ttk.Label(text="Slope").place(x=70,y=70)
y_intercept = ttk.Label(text="Y Intercept").place(x=40,y=120)

m = ttk.Entry(window)
b = ttk.Entry(window)

b.place(x=120, y=120)
m.place(x=120, y=70)

global got_inputs
got_inputs = False

def get_inputs():
    global got_inputs
    global slope2
    global y_intercept2
    y_intercept2 = b.get()
    slope2 = m.get()
    print(slope2, y_intercept2)
    got_inputs = True

    return y_intercept2, slope2
 

def graph():
    global slope2
    global y_intercept2
    slope2 = float(slope2)
    y_intercept2 = float(y_intercept2)
    
    x = np.linspace(-5,5,100) # Density of numbers in between
    y = slope2*x+y_intercept2 # Equation
    plt.plot(x, y, '-r', label='y=2x+1')
    plt.title('Graph of y=2x+1')
    plt.xlabel('x', color='#1C2833')
    plt.ylabel('y', color='#1C2833')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()

go = ttk.Button(window, text="Enter", command=get_inputs).place(x=220,y=175)

window.mainloop()

while 1:
    if got_inputs == True:
        graph()
        break