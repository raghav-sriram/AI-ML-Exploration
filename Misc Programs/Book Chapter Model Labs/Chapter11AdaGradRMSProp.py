# Raghav Sriram
# Period 6 ML Gabor
# Chapter 11

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("jobs_in_data.csv")

# Using 'work_year' as a feature to predict 'salary_in_usd'
X = df[['work_year']].values
y = df['salary_in_usd'].values
X = (X - X.mean()) / X.std()
X = np.c_[np.ones(X.shape[0]), X] # bias

# AdaGrad optimization algorithm for linear regression
def adagrad(X, y, theta, learning_rate, epsilon, iterations):
    m = len(y)
    cost_history = []
    G = np.zeros(theta.shape)
    
    for it in range(iterations):
        prediction = np.dot(X, theta)
        error = prediction - y
        cost = (1/(2*m)) * np.dot(error.T, error)
        cost_history.append(cost)
        
        gradient = (1/m) * np.dot(X.T, error)
        G += gradient ** 2
        theta -= (learning_rate / (np.sqrt(G) + epsilon)) * gradient
        
    return theta, cost_history

# RMSProp optimization algorithm for linear regression
def rmsprop(X, y, theta, learning_rate, epsilon, gamma, iterations):
    m = len(y)
    cost_history = []
    G = np.zeros(theta.shape)
    
    for it in range(iterations):
        prediction = np.dot(X, theta)
        error = prediction - y
        cost = (1/(2*m)) * np.dot(error.T, error)
        cost_history.append(cost)
        
        gradient = (1/m) * np.dot(X.T, error)
        G = gamma * G + (1 - gamma) * (gradient ** 2)
        theta -= (learning_rate / (np.sqrt(G) + epsilon)) * gradient
        
    return theta, cost_history

theta = np.zeros(X.shape[1])
learning_rate = 0.1
epsilon = 1e-8
gamma = 0.9
iterations = 100

# Running AdaGrad
theta_adagrad, cost_history_adagrad = adagrad(X, y, theta, learning_rate, epsilon, iterations)

# Running RMSProp
theta_rmsprop, cost_history_rmsprop = rmsprop(X, y, theta, learning_rate, epsilon, gamma, iterations)

print("AdaGrad Final Parameters:", theta_adagrad)
print("AdaGrad Final Cost:", cost_history_adagrad[-1])
print("RMSProp Final Parameters:", theta_rmsprop)
print("RMSProp Final Cost:", cost_history_rmsprop[-1])

# Plotting the cost history for comparison
plt.figure(figsize=(10, 6))
plt.plot(cost_history_adagrad, label='AdaGrad')
plt.plot(cost_history_rmsprop, label='RMSProp')
plt.xlabel('Iteration')
plt.ylabel('Cost')
plt.title('Cost History - AdaGrad vs RMSProp')
plt.legend()
plt.show()
