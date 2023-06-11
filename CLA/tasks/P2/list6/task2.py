import alc
from math import sin, cos
import matplotlib.pyplot as plt
import seaborn as sns

def function(t, y, z):
  return -z/5 -y + 2 * sin(t/2) + sin(t) + cos(3*t/2)

for delta in [10, 5, 1, 0.5, 0.1, 0.05, 0.01]:                       #methods: 'taylor_series','runge_kutta_nystron'
  ts, xs = alc.solve_second_order_ode(function, 0, 100, delta, 0, 0, method='taylor_series')

  sns.set_style('whitegrid')
  plt.rcParams['font.family'] = 'serif'
  plt.rcParams['font.size'] = 12

  fig, ax = plt.subplots(figsize=(8, 6))
  ax.plot(ts, xs, color='red')

  ax.set_title(r"Taylor Series Expansion Method $\Delta={}$".format(delta), fontsize=16, fontweight='bold')
  ax.set_xlabel("t", fontsize=14)
  ax.set_ylabel("y''(t)", fontsize=14)

  ax.tick_params(axis='both', which='major', labelsize=12)
  ax.grid(True, linestyle='--', linewidth=0.5)

  plt.show()

  ts, xs = alc.solve_second_order_ode(function, 0, 100, delta, 0, 0, method='runge_kutta_nystron')

  sns.set_style('whitegrid')
  plt.rcParams['font.family'] = 'serif'
  plt.rcParams['font.size'] = 12

  fig, ax = plt.subplots(figsize=(8, 6))
  ax.plot(ts, xs, color='red')

  ax.set_title(r"Runge-Kutta-Nystron (RKN) Method $\Delta={}$".format(delta), fontsize=16, fontweight='bold')
  ax.set_xlabel("t", fontsize=14)
  ax.set_ylabel("y''(t)", fontsize=14)

  ax.tick_params(axis='both', which='major', labelsize=12)
  ax.grid(True, linestyle='--', linewidth=0.5)

  plt.show()
