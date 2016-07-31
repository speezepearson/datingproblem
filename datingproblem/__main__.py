#!/usr/bin/python3

'''
A solution to the dating problem (secure multiparty computation of A&B).

The dating problem:
- Alice and Bob may each have a crush on the other.
- Alice constructs two messages:
  the first is "I'm not interested; {random garbage}",
  and the second is either "I'm interested" or "I'm not interested" (whichever is true).
  She encrypts each with a commutative cipher and sends them to Bob.
- Bob selects one of the messages (the first if he's not interested, the second if he is);
  encrypts it with the same commutative cipher;
  and sends it back to Alice.
- Alice ...
'''

import argparse
import requests
import datingproblem

parser = argparse.ArgumentParser()
parser.add_argument('--initiate', action='store_true')
parser.add_argument('--serve', action='store_true')
parser.add_argument('initiator_name')
parser.add_argument('responder_name')
args = parser.parse_args()

if args.serve:
  datingproblem.server.serve()
else:
  interested = (input('Are you interested in {}? [y/n] '.format(args.responder_name)) == 'y')

  matchmaker = datingproblem.Matchmaker(
    host='localhost:8080',
    initiator_name=args.initiator_name,
    responder_name=args.responder_name)

  if args.initiate:
    p, q, e, d = datingproblem.crypto.new_pqed()
    match = datingproblem.handshakes.do_initiator_handshake(
      matchmaker=matchmaker,
      interested=interested,
      p=p, q=q, e=e, d=d)
  else:
    match = datingproblem.handshakes.do_responder_handshake(
      matchmaker=matchmaker,
      interested=interested)

  print('Match!' if match else 'No match.')
