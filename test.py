import string
import random
import threading
import datingproblem

people = ['a', 'b', 'c', 'd']

interests = {(alice,bob): random.random()<0.5 for alice in people for bob in people if alice!=bob}

expected_handshake_results = {(alice,bob): interests[alice,bob] and interests[bob,alice] for alice in people for bob in people if alice!=bob}
handshake_results = {}

threads = set()
for alice in people:
  for bob in people:
    if alice==bob: continue
    if hash(alice) < hash(bob): # TODO
      def f(alice=alice, bob=bob):
        p,q,e,d = datingproblem.crypto.new_pqed()
        handshake_results[alice,bob] = datingproblem.handshakes.do_initiator_handshake(
          matchmaker=datingproblem.Matchmaker('localhost:8080', alice, bob),
          interested=interests[alice,bob],
          p=p, q=q, e=e, d=d)
    else:
      def f(alice=alice, bob=bob):
        handshake_results[alice,bob] = datingproblem.handshakes.do_responder_handshake(
          matchmaker=datingproblem.Matchmaker('localhost:8080', bob, alice),
          interested=interests[alice,bob])

    threads.add(threading.Thread(target=f))

for thread in threads:
  thread.start()

for thread in threads:
  thread.join()

assert expected_handshake_results == handshake_results
