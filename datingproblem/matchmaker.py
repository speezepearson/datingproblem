import requests
import json

class Matchmaker:
  def __init__(self, host, initiator_name, responder_name):
    self.host = host
    self.initiator_name = initiator_name
    self.responder_name = responder_name

  def set_p_q_msg_no_msg_true(self, p, q, msg_no, msg_true):
    r = requests.post('http://{}/{}/{}/set_p_q_msg_no_msg_true'.format(self.host, self.initiator_name, self.responder_name), json={'p':p, 'q':q, 'msg_no':msg_no, 'msg_true':msg_true})
    if r.status_code != 200:
      raise RuntimeError(r)
  def get_p_q_msg_no_msg_true(self):
    r = requests.get('http://{}/{}/{}/get_p_q_msg_no_msg_true'.format(self.host, self.initiator_name, self.responder_name))
    if r.status_code != 200:
      raise RuntimeError(r)
    return [int(s) for s in r.json()]
  def set_msg_doubleencrypted(self, msg_doubleencrypted):
    r = requests.post('http://{}/{}/{}/set_msg_doubleencrypted'.format(self.host, self.initiator_name, self.responder_name), json={'msg_doubleencrypted':msg_doubleencrypted})
    if r.status_code != 200:
      raise RuntimeError(r)
  def get_msg_doubleencrypted(self):
    r = requests.get('http://{}/{}/{}/get_msg_doubleencrypted'.format(self.host, self.initiator_name, self.responder_name))
    if r.status_code != 200:
      raise RuntimeError(r)
    return int(r.text)
  def set_msg_unlocked(self, msg_unlocked):
    r = requests.post('http://{}/{}/{}/set_msg_unlocked'.format(self.host, self.initiator_name, self.responder_name), json={'msg_unlocked':msg_unlocked})
    if r.status_code != 200:
      raise RuntimeError(r)
  def get_msg_unlocked(self):
    r = requests.get('http://{}/{}/{}/get_msg_unlocked'.format(self.host, self.initiator_name, self.responder_name))
    if r.status_code != 200:
      raise RuntimeError(r)
    return int(r.text)
  def set_msg_result(self, msg_result):
    r = requests.post('http://{}/{}/{}/set_msg_result'.format(self.host, self.initiator_name, self.responder_name), json={'msg_result':msg_result})
    if r.status_code != 200:
      raise RuntimeError(r)
  def get_msg_result(self):
    r = requests.get('http://{}/{}/{}/get_msg_result'.format(self.host, self.initiator_name, self.responder_name))
    return int(r.text)
    if r.status_code != 200:
      raise RuntimeError(r)
