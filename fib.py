

def fib1(x):
  if (x <= 1):
    return x
  else:
    return fib(x-1) + fib(x-2)

def fib2(x):
  f = [0] * (x+1)
  for i in range(x+1):
    if (i <= 1):
      f[i] = i
    else:
      f[i] = f[i-1] + f[i-2]
  return f[x]



for x in range(100):
  print(x, fib2(x))

