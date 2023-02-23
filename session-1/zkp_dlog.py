import random

'''
pow(x, n) (mod p)
'''
def power_module(x, n, p):
  y = 1
  while n > 0:
    if n % 2 == 1:
      y *= x
    x *= x
    n //= 2
    y %= p
  return y

'''
x is secret
(g ^ x) (mod p)
'''
def dlog_proof(x, g, p, b):
  r = random.randint(1, p-1)
  h = power_module(g, x, p)
  pf = (r + b * x) % (p - 1)
  return h, pf

'''
y = (g ^ r) (mod p)
h = (g ^ x) (mod p)
pf is proof
'''  
def verify(y, g, p, h, pf, b):
  lhs = power_module(g, pf, p)
  rhs = h % p if b == 0 else (h * y) % p
  return lhs == rhs