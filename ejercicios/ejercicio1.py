from errores.error import ValueNegativeError

def factorial(n):
  if n < 0:
    raise ValueNegativeError("Valor negativo no permitido")
  if n == 0 or n == 1:
    return 1
  return n * factorial(n-1)