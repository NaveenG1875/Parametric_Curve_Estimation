import numpy as np
import pandas as pd
from scipy.optimize import differential_evolution 
import matplotlib.pyplot as plt
from scipy.spatial import cKDTree

data = pd.read_csv("flam.csv")
x_data = data["x"].values
y_data = data["y"].values

t = np.linspace(6, 60, len(x_data))

def curve(t, theta_deg, M, X):
    theta = np.radians(theta_deg)
    x = (t * np.cos(theta)- np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.sin(theta) + X)
    y = (42 + t * np.sin(theta) + np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.cos(theta))
    return x,y


def objective(params):
    theta, M, X = params
    pred_x, pred_y = curve(t, theta, M, X)

    predicted_points = np.column_stack((pred_x, pred_y))
    tree = cKDTree(predicted_points)

    data_points = np.column_stack((x_data, y_data))
    _, indices = tree.query(data_points, p=1)

    nearest_x = pred_x[indices]
    nearest_y = pred_y[indices]

    error = np.sum(np.abs(x_data - nearest_x) + np.abs(y_data - nearest_y))
    return error

bounds = [(0, 50), (-0.05, 0.05), (0, 100)]

result = differential_evolution(objective, bounds, seed=42, tol=1e-10)

theta, M, X = result.x

print("theta =", theta)
print("M =", M)
print("X =", X)
print("L1 Error =", result.fun)

pred_x, pred_y = curve(t, theta, M, X)

plt.figure(figsize=(10, 6))

plt.scatter(x_data, y_data, s=5, label="CSV data")
plt.plot(pred_x, pred_y, linewidth=2, label="Predicted curve")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

