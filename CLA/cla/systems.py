__all__ = [
  "solve",
  "equations"
]
from sympy import *
from sympy import Symbol, Matrix, zeros, Array
from sympy import Function, Symbol
import numpy as np
from cla.Array import Array
from cla.exceptions import ExpressionError
from cla.constants import constants
from cla.gauss import gauss_elimination, gauss_jordan_elimination
from cla.utils import zeros
from cla.jacobi import jacobi
from cla.gauss_seidel import gauss_seidel
from cla.decomposition import lu_decomposition, cholesky_decomposition


# Backward substitution algorithm
def retrosub (A, B):
  # Initialize x
  x = zeros((A.shape[0], B.shape[1]))
  n = A.shape[0]
  # Retro-substitution
  x[n-1] = [B[n-1][0]/A[n-1][n-1]]
  for i in range(n-2, -1, -1):
    x[i][0] = B[i][0]
    for j in range(i+1, n):
      x[i][0] -= A[i][j]*x[j][0]
    x[i][0] /= A[i][i]
  return x

# Forward substitution algorithm
def forwardsub (L, B):
  # Initialize y
  y = zeros((L.shape[0], B.shape[1]))
  n = L.shape[0]
  # Forward sub
  y[0][0] = B[0][0] / L[0][0]
  for i in range(1, n):
    y[i][0] = B[i][0]
    for j in range(0, i):
      y[i][0] -= L[i][j]*y[j][0]
    y[i][0] /= L[i][i]
  return y

def solve (A, B, method='gauss', threshold=constants.epsilon):
  if method == "gauss":
    # Turn A into an upper triangular matrix
    A, intermediates = gauss_elimination (A, return_intermediates=True, show_steps=False, return_pivots=False)
    # To keep it an equation, apply transformations to B as well
    for m in intermediates:
      B = m * B
    x = retrosub(A, B)
    return x
  elif method == "gauss_jordan":
    # Turn A into an upper triangular matrix
    A, intermediates = gauss_elimination (A, return_intermediates=True, show_steps=False, return_pivots=False)
    # To keep it an equation, apply transformations to B as well
    for m in intermediates:
      B = m * B
    # Turn A into diagonal matrix
    A, intermediates = gauss_jordan_elimination (A, return_intermediates=True, show_steps=False)
    # Apply transformations to B as well
    for m in intermediates:
      B = m * B
    # Initialize x
    x = zeros((A.shape[0], B.shape[1]))
    # Computing x
    for i in range(A.shape[0]):
      x[i][0] = B[i][0]/A[i][i]
    return x
  elif method == "jacobi":
    x = jacobi(A, B, threshold=threshold)
    return x
  elif method == "gauss_seidel":
    x = gauss_seidel(A, B, threshold=threshold)
    return x
  elif method == "lu":
    L, U = lu_decomposition (A, return_det=False)
    y = forwardsub(L, B)
    x = retrosub(U, y)
    return x
  elif method == "cholesky":
    try:
      L, Lt = cholesky_decomposition(A)
      y = forwardsub(L, B)
      x = retrosub(Lt, y)
      return x
    except ValueError as e:
      raise e
  else:
    raise NameError("Solving method not allowed!")

def equations(eq_list, symbols, x0, threshold=1e-4, max_iter=7, method='newton'):
    n = len(symbols)
    
    # Criar os símbolos das variáveis
    func_vars = []
    for symbol in symbols:
        exec("{0} = Symbol('{0}')".format(symbol))
        exec("func_vars.append({})".format(symbol))
    
    # Avaliar as expressões das equações
    eqs = []
    for eq in eq_list:
        try:
            eqs.append(eval(eq))
        except:
            raise ValueError("Falhou ao executar a seguinte função: {}. Favor verificar a expressão.".format(eq))
    
    # Construir a matriz das equações
    F = Matrix(eqs)
    Y = Matrix(func_vars)
    J = F.jacobian(Y)
    
    xk1 = Matrix(x0)
    if method == 'newton':
        for k in range(max_iter):
            j = J
            f = F
            for i, var in enumerate(func_vars):
                j = j.limit(var, xk1[i])
                f = f.limit(var, xk1[i])
            j = j.n()
            f = f.n()
            delta_x = - j.inv() * f
            xk = xk1 + delta_x
            xk1 = xk
            tol = delta_x.norm() / xk.norm()
            if tol <= threshold:
                return xk
        raise ValueError("Método de Newton não convergiu (threshold={:e}, max_iter={}).".format(threshold, max_iter))
    
    elif method == 'broyden':
        bk1 = J
        f = F
        for i, var in enumerate(func_vars):
            bk1 = bk1.limit(var, xk1[i])
            f = f.limit(var, xk1[i])
        bk1 = bk1.n()
        f = f.n()
        for k in range(max_iter):
            j = bk1
            delta_x = - j.inv() * f
            xk = xk1 + delta_x
            fxk = F
            for i, var in enumerate(func_vars):
                fxk = fxk.limit(var, xk[i])
            fxk = fxk.n()
            yk = fxk - f
            tol = delta_x.norm().n() / xk.norm().n()
            if tol <= threshold:
                return xk
            bk = bk1 + (yk - bk1 * delta_x) * delta_x.transpose() / (delta_x.transpose() * delta_x).n()[0]
            xk1 = xk.n()
            bk1 = bk
            f = fxk
    else:
        raise NameError("Solving method {} not allowed!".format(method))