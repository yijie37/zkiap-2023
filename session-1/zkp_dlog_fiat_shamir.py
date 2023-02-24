import random
import hashlib

nn = 64

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

def bits(msg):
    # here we use md5 as a hash function
    code = int(hashlib.md5(msg.encode()).hexdigest(), 16)
    return [1 if 1 << i & code != 0 else 0 for i in range(nn)]

'''
x is secret
https://people.eecs.berkeley.edu/~jfc/cs174/lecs/lec24/lec24.pdf
h is A^r(mod p)
s is (r + bx)(mod (p - 1))
'''
def dlog_proof(x, g, p):
  rs = [random.randint(1, p-1) for _ in range(nn)]
  hs = [power_module(g, r, p) for r in rs]
  bits = bits(''.join([str(h) for h in hs]))
  ss = [(r + b * x) % (p - 1) for (r, b) in rs.zip(btis)]
  return hs, ss

'''
y = (g ^ r) (mod p)
h = (g ^ x) (mod p)
pf is proof
'''
def verify(y, g, p, hs, ss):
  bits = bits(''.join([str(h) for h in hs]))
  lhs = [power_module(g, s, p) for s in ss]
  rhs = [h % p if b == 0 else (h * y) % p for h, b in hs.zip(bits)]
  return lhs == rhs