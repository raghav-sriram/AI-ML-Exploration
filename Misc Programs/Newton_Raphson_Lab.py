# Raghav Sriram
# Wednesday, August 23rd, 2023
# Machine Learning 1 Gabor
# Newton Raphson Lab

import numpy as np
import math
from math import e

# ======================== Limit Definitions ======================== #

def lim_deriv(f, h=1e-7):
    def deriv(x):
        return (f(x + h)- f(x)) / h
    
    return deriv

def lim_second_deriv(f, h=1e-7):
    df = lim_deriv(f, h)
    
    def second_deriv(x):
        return (df(x + h)- df(x)) / h
    
    return second_deriv

def lim_gradient(f, h=1e-7):
    def gradient(x):
        df_dx = (f([x[0] + h, x[1]]) - f(x)) / h
        df_dy = (f([x[0], x[1] + h]) - f(x)) / h
        return np.array([df_dx, df_dy])
    
    return gradient

def lim_hessian(f, h=1e-7):
    grad = lim_gradient(f, h)
    
    def hessian(x):
        d2f_dx2 = (grad([x[0] + h, x[1]])[0] - grad(x)[0]) / h
        d2f_dy2 = (grad([x[0], x[1] + h])[1] - grad(x)[1]) / h
        d2f_dxdy = (grad([x[0] + h, x[1]])[1] - grad(x)[1]) / h
        return np.array([[d2f_dx2, d2f_dxdy], [d2f_dxdy, d2f_dy2]])
    
    return hessian

def lim_jacobian(f, h=1e-7):
    def jacobian(x):
        df1_dx = (f([x[0] + h, x[1]])[0] - f(x)[0]) / h
        df1_dy = (f([x[0], x[1] + h])[0] - f(x)[0]) / h
        df2_dx = (f([x[0] + h, x[1]])[1] - f(x)[1]) / h
        df2_dy = (f([x[0], x[1] + h])[1] - f(x)[1]) / h
        return np.array([[df1_dx, df1_dy], [df2_dx, df2_dy]])
    
    return jacobian

# ======================== Part 1 ======================== #

def estimate(f, df, x0, error, n):

    x = x0
    for i in range (n):
        x_n = x - f(x) / df(x)
        if abs(f(x)) < error or abs(x_n-x) < error:
            return x_n
        x = x_n
        
    return x

# ADD THE VALUE ERROR TEST CASE STUFF AND EXAMPLES

def rel_minmax(f, df, d2f, x0, error, n):

    x = x0
    for i in range (n):
        if abs(d2f(x)) < error: return x
        x_n = x - df(x)/d2f(x)
        if error > abs(x-x_n): return x_n
        x = x_n

    return x_n

# f(x) = x**4 - 7*x**3 + 16*x**2 - 17*x + 6
# g(x) = 2*x**5 - 11*x**4 + 29*x**3 - 38*x**2 + 22*x - 6
# h(x) = x**3 + 5*x**2 - 14*x + 8
# i(x) = -x**4 + 6*x**3 - 8*x**2 + 3*x - 1
# j(x) = 3*x**5 - 5*x**4 + 2*x**3 + x**2 - 5*x + 1
# k(x) = x**2 - 3*x + 2
# l(x) = -2*x**4 + 9*x**3 - 11*x**2 + 5*x - 1
# m(x) = 4*x**3 - 12*x**2 + 11*x - 3
# n(x) = -x**5 + 10*x**4 - 35*x**3 + 50*x**2 - 25*x + 5
# o(x) = 3*x**4 - 4*x**3 + x**2 - 6*x + 2


f_x = lambda x: 2*x**3 - 7*x**2 + 5*x - 9
df_x = lim_deriv(f_x)
d2f_x = lim_second_deriv(f_x)

print("Roots", estimate(f_x, df_x, 1, 0.001, 100))
print("Relative Extrema", rel_minmax(f_x, df_x, d2f_x, 1, 0.001, 100))

f_1 = lambda x: (x-1)**3 - 8*x**2 + 5*x -2
df_1 = lim_deriv(f_1)
d2f_1 = lim_second_deriv(f_1)

print("Roots 1", estimate(f_1, df_1, 1, 0.001, 100))
print("Relative Extrema", rel_minmax(f_1, df_1, d2f_1, 1, 0.001, 100))

f_2 = lambda x: x * (1+e**-x)**-1
df_2 = lim_deriv(f_2)
d2f_2 = lim_second_deriv(f_2)

print("Roots 2", estimate(f_2, df_2, 1, 0.001, 100))
print("Relative Extrema", rel_minmax(f_2, df_2, d2f_2, 1, 0.001, 100))

f_3 = lambda x: math.sin(x)
df_3 = lim_deriv(f_3)
d2f_3 = lim_second_deriv(f_3)

print("Roots 3", estimate(f_3, df_3, 1, 0.001, 100))
print("Relative Extrema", rel_minmax(f_3, df_3, d2f_3, 1, 0.001, 100))

# df_x = lambda x: 24 * x**2
# d2f_x = lambda x: 48 * x

# ======================== Part 2 ======================== #

def rel_minmax_2(f, grad, H, x0, error, n):
            
    a = np.array(x0)
    for i in range(n):
        v = a - np.linalg.inv(H(a)) @ (grad(a))
        if abs(np.linalg.norm(v-a)) < error:
            return v
        a = v
    return v 

def zeros(F, J, x0, error, n):
    a = np.array(x0)
    for i in range(n):
        v = a - np.linalg.inv(J(a)).dot(F(a))
        if np.linalg.norm(F(a)) < error:
            return v
    a = v
    return v



# x[0]**2 + 3*(x[1]+7)**2 + 7

F_x = lambda x: x[0]**2 + 3*(x[1]+7)**2 + 7
# grad_F = lim_gradient(F_x)
# hessian_F = lim_hessian(F_x)

# jacobian_F = lim_jacobian(F_x)
# F_x = lambda x: np.array([x[0]**2 - x[1], x[0] - x[1]**2])

grad_F = lambda x: np.array([2*x[0], 6*x[1]+42])
hessian_F = lambda x: np.array([[2,0],[0,6]])


# jacobian_F = lambda x: np.array([[2*x[0],-1],[1, -2*x[1]]])

print("Relative Extrema (Multi Variable)", rel_minmax_2(F_x, grad_F, hessian_F, (1,1), 0.001, 100))
# print("Zeros (Multi Variable)", zeros(F_x, jacobian_F, (1,1), 0.001, 100))





# x[0]**2 + 3*(x[1]+7)**2 + 7

F_x = lambda x: x[0]**2 + 3*(x[1]+7)**2 + 7

grad_F = lambda x: np.array([2*x[0], 6*x[1]+42])
hessian_F = lambda x: np.array([[2,0],[0,6]])


F_xx = lambda x: np.array([x[0]**2 - x[1], x[0] - x[1]**2])
jacobian_F = lambda x: np.array([[2*x[0],-1],[1, -2*x[1]]]) 

print("Relative Extrema (Multi Variable)", rel_minmax_2(F_x, grad_F, hessian_F, (1,1), 0.001, 100))
print("Zeros (Multi Variable)", zeros(F_xx, jacobian_F, (1,1), 0.001, 100))


print("# ======================== Testing ======================== #")

# ======================== Testing ======================== #

F_1 = lambda x: x[0]**3 + 2*x[1]**2 + 3*x[0]*x[1]

grad_F_1 = lambda x: np.array([3*x[0]**2 + 3*x[1], 4*x[1] + 3*x[0]])
hessian_F_1 = lambda x: np.array([[6*x[0], 3], [3, 4]])

F_2 = lambda x: 4*x[0]**2 - 3*x[0]*x[1] + 5*x[1]**3

grad_F_2 = lambda x: np.array([8*x[0] - 3*x[1], -3*x[0] + 15*x[1]**2])
hessian_F_2 = lambda x: np.array([[8, -3], [-3, 30*x[1]]])

F_3 = lambda x: x[0]**2 + x[1]**2 + x[0]*x[1]

grad_F_3 = lambda x: np.array([2*x[0] + x[1], 2*x[1] + x[0]])
hessian_F_3 = lambda x: np.array([[2, 1], [1, 2]])

F_4 = lambda x: 3*x[0]**2*x[1] - 4*x[1]**3 + 2*x[0]

grad_F_4 = lambda x: np.array([6*x[0]*x[1] + 2, 3*x[0]**2 - 12*x[1]**2])
hessian_F_4 = lambda x: np.array([[6*x[1], 6*x[0]], [6*x[0], -24*x[1]]])

print("Relative Extrema (Multi Variable)", rel_minmax_2(F_1, grad_F_1, hessian_F_1, (1,1), 0.001, 100))
print("Relative Extrema (Multi Variable)", rel_minmax_2(F_2, grad_F_2, hessian_F_2, (1,1), 0.001, 100))
print("Relative Extrema (Multi Variable)", rel_minmax_2(F_3, grad_F_3, hessian_F_3, (1,1), 0.001, 100))
print("Relative Extrema (Multi Variable)", rel_minmax_2(F_4, grad_F_4, hessian_F_4, (1,1), 0.001, 100))