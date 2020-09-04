import matplotlib.pyplot as plt
import numpy as np
def compute():
    inp = input("enter your function: ")
    x = np.linspace(-2, 2, 100) 
    expr = inp.replace("^","**")

    y= eval(expr)

    plt.plot(y)
    plt.show()

compute()