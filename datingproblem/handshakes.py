import os
import random
import requests
import rsa.core
from . import crypto

def secure_randrange(limit):
  random.seed(os.urandom(256))
  return random.randrange(limit)

def do_initiator_handshake(matchmaker, interested, p, q, e, d):
  msg_no_plaintext = 2*secure_randrange(2**510)
  msg_true_plaintext = 2*secure_randrange(2**510) + (1 if interested else 0)
  msg_no = rsa.core.encrypt_int(message=msg_no_plaintext, ekey=e, n=p*q)
  msg_true = rsa.core.encrypt_int(message=msg_true_plaintext, ekey=e, n=p*q)
  matchmaker.set_p_q_msg_no_msg_true(p, q, msg_no, msg_true)

  msg_doubleencrypted = matchmaker.get_msg_doubleencrypted()
  msg_unlocked = rsa.core.decrypt_int(cyphertext=msg_doubleencrypted, dkey=d, n=p*q)
  matchmaker.set_msg_unlocked(msg_unlocked)

  msg_result = int(matchmaker.get_msg_result())

  if msg_result == msg_no_plaintext:
    return False
  elif msg_result == msg_true_plaintext:
    return interested
  else:
    raise RuntimeError('decrypted message is neither original message; somebody is a DIRTY CHEATER')

def do_responder_handshake(matchmaker, interested):
  p, q, msg_no, msg_true = matchmaker.get_p_q_msg_no_msg_true()
  e, d = crypto.new_ed_from_pq(p, q)

  msg_doubleencrypted = rsa.core.encrypt_int(message=(msg_true if interested else msg_no), ekey=e, n=p*q)
  matchmaker.set_msg_doubleencrypted(msg_doubleencrypted)

  msg_unlocked = matchmaker.get_msg_unlocked()
  msg_result = rsa.core.decrypt_int(cyphertext=msg_unlocked, dkey=d, n=p*q)
  matchmaker.set_msg_result(msg_result)

  match = (msg_result%2 == 1)
  return match
