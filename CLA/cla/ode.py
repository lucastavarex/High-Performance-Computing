__all__ = [
  'solve_first_order_ode',
  'solve_second_order_ode'
]

def solve_first_order_ode (function, t0, t, delta, x0, method='euler'):

  xs = [x0]
  ts = [t0]
  result_xs = []
  result_ts = []
  steps = int((t - t0) / (delta))

  for i in range(steps):
    ts.append((i + 1) * delta)

    if (method == 'euler'):
      xs.append(xs[i] + delta * function(ts[i], xs[i]))

    elif(method == 'runge_kutta_second_order'):
      k1 = function(ts[i], xs[i])
      k2 = function(ts[i] + delta, xs[i] + delta * k1)
      xs.append(xs[i] + delta / 2 * (k1 + k2))

    elif(method == 'runge_kutta_fourth_order'):
      k1 = function(ts[i], xs[i])
      k2 = function(ts[i] + delta / 2, xs[i] + delta / 2 * k1)
      k3 = function(ts[i] + delta / 2, xs[i] + delta / 2 * k2)
      k4 = function(ts[i] + delta, xs[i] + delta * k3)
      xs.append(xs[i] + delta / 6 * (k1 + 2 * k2 + 2 * k3 + k4))

    if(i==0 or i == steps):
        continue
    
    result_ts.append(ts[i])
    result_xs.append(xs[i])

  result_ts.append(ts[-1])
  result_xs.append(xs[-1])
  return result_ts, result_xs

def solve_second_order_ode (function, t0, t, delta, x0, x0_prime, method='taylor_series'):

  xs = [x0]
  ts = [t0]
  prime = x0_prime
  steps = int((t - t0) / delta)

  for i in range(steps):
    ts.append((i + 1) * delta)

    if (method == 'taylor_series'):
      tmp = function(ts[i], xs[i], prime) * delta
      xs.append(xs[i] + prime * delta + tmp * delta / 2)
      prime += tmp

    elif (method == 'runge_kutta_nystron'):
      k1 = delta / 2  * function(ts[i], xs[i], prime)
      q = delta / 2 * (prime + k1 / 2)
      k2 = delta / 2 * function(ts[i] + delta / 2, xs[i] + q, prime + k1)
      k3 = delta / 2 * function(ts[i] + delta / 2, xs[i] + q, prime + k2)
      l = delta * (prime + k3)
      k4 = delta/ 2 * function(ts[i] + delta, xs[i] + l, prime + 2*k3)
      xs.append(xs[i] + delta*(prime + (k1 + k2 + k3) / 3))
      prime += (k1 + 2 * k2 + 2 * k3 + k4) / 3

    else:
      raise NameError("Method {} not allowed.".format(method))

  return ts, xs