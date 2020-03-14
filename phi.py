import numpy as np
import matplotlib.pyplot as plt
def function_circle(n):
    x= np.random.uniform(-1,1,n)
    y= np.random.uniform(-1,1,n)

    y_in_circle= (x*x +y*y<1)
    x_in_circle = (x*x +y*y<1)
     
    y_blue= y[y_in_circle]
    x_blue = x[x_in_circle]
    x_red= x[np.invert(x_in_circle)]
    y_red= y[np.invert(y_in_circle)]


    #forma cuadrada
    plt.figure(figsize=(5,5))
    #pintar numeros
    plt.plot(x_blue,y_blue, 'o',color='blue')
    plt.plot(x_red,y_red, 'o',color='red')
    #limite eje x
    plt.xlim(-1,1)
    #limite eje y
    plt.ylim(-1,1)
    plt.show()
    
    return len(x_blue)
    
    n=10000000
dentro = function_circle(n)
print(4*dentro/n)
