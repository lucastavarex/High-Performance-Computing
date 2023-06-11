import alc

def function (t, y):
  return -2*t*(y**2)
                                                            #methods: 'euler','runge_kutta_second_order', 'runge_kutta_fourth_order'
ts, xs = alc.solve_first_order_ode(function, 0, 10, 0.1, 1, method='runge_kutta_fourth_order')
print("╔═════════════════════════════════╗")
print("║ t_values              x_values  ║ ")
print("╠═════════════════════════════════╣")
for i in range(len(ts)):
  if i != len(ts) - 1:
    print("║ t={:.3f}\t\tx={:.5f} ║".format(ts[i], xs[i]))
    print("╠═════════════════════════════════╣")
  else:
    print("║ t={:.3f}\t\tx={:.5f} ║".format(ts[i], xs[i]))
print("╚═════════════════════════════════╝")

