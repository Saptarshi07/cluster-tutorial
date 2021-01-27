import math 
import sys

filename = sys.argv[1]

with open(filename, "r") as file:
    f_list = [float(i) for line in file for i in line.split(' ') if i.strip()]



x, K, beta, x0 = f_list[0], f_list[1], f_list[2], f_list[3]




def sigmoid(x, K, beta, x0):
    r"""
    Computes the sigmoid with the parameters at float point x.

    Sigmoid with parameters K, beta, x0:

    \frac{K}{1+e^{\beta(x - x_0)}}

    Parameters
    ----------
    K: float
        maximum height
    beta: float
        elasticity
    x0: half-height point
        

    Returns
    -------
    euclidean : float double
        Sigmoid function with parameters K, beta and x0 at point x.
    """

    return 1/(1 + math.exp(-beta*(x - x0)))


result = sigmoid(x, K, beta, x0)

print('The sigmoid value with parameters ' + 'K = %.2f,'%K + ' beta = %.2f,'%beta + ' x0 = %.2f'%x0 + ' at ' + 'x= %.2f'%x + ' is ' + '%.4f'%result)



