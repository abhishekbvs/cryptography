from Crypto.Util.number import *

# creating encryption oracle such that its vulnerable to cube root attack

p = getPrime(512)
q = getPrime(512)
n = p*q
e = 3
m = bytes_to_long("youGotMe")
ct = pow(m,e,n)
print m**3 < n
print (ct,n)