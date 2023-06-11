import alc
from math import sqrt
import matplotlib.pyplot as plt
import seaborn as sns

def function (t, y, z):
  gravity = 9.81 #S.I
  return - gravity - z * sqrt(z ** 2)

ts, xs = alc.solve_second_order_ode(function, 0, 20, 0.1, 0, 0, method='taylor_series')
sns.set_style('whitegrid')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 12
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(ts, xs, color='red')
ax.set_title("Taylor Series Expansion Method", fontsize=16, fontweight='bold')
ax.set_xlabel("t", fontsize=14)
ax.set_ylabel("y''(t)", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=12)
ax.grid(True, linestyle='--', linewidth=0.5)
plt.show()

ts, xs = alc.solve_second_order_ode(function, 0, 20, 0.1, 0, 0, method='runge_kutta_nystron')
sns.set_style('whitegrid')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 12
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(ts, xs, color='red')
ax.set_title("Runge-Kutta-Nystron (RKN) Method", fontsize=16, fontweight='bold')
ax.set_xlabel("t", fontsize=14)
ax.set_ylabel("y''(t)", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=12)
ax.grid(True, linestyle='--', linewidth=0.5)
plt.show()