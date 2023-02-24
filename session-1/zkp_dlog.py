import random

'''
This function calculates pow(x, n) (mod p)
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
https://people.eecs.berkeley.edu/~jfc/cs174/lecs/lec24/lec24.pdf
h is A^r(mod p)
s is (r + bx)(mod (p - 1))
'''
def dlog_proof(x, g, p, b):
  r = random.randint(1, p-1)
  h = power_module(g, r, p)
  s = (r + b * x) % (p - 1)
  return h, s

'''
y = (g ^ r) (mod p)
h = (g ^ x) (mod p)
pf is proof
'''  
def verify(y, g, p, h, s, b):
  lhs = power_module(g, s, p)
  rhs = h % p if b == 0 else (h * y) % p
  return lhs == rhs