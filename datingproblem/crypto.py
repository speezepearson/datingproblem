import rsa.common
import rsa.key
import rsa.prime

def new_pqed():
  p, q = rsa.key.find_p_q(512)
  e, d = new_ed_from_pq(p, q)
  return (p,q,e,d)

def new_ed_from_pq(p, q):
  e = rsa.prime.getprime(512)
  assert rsa.common.extended_gcd(e, (p-1)*(q-1))[0] == 1
  d = rsa.common.inverse(e, (p-1)*(q-1))
  return (e, d)
