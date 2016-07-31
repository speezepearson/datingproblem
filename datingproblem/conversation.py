import threading

class Conversation:
  def __init__(self):
    self.p = None
    self.q = None
    self.msg_no = None
    self.msg_true = None
    self.msg_doubleencrypted = None
    self.msg_unlocked = None
    self.msg_result = None
    self._p_q_msg_no_msg_true_set = threading.Event()
    self._msg_doubleencrypted_set = threading.Event()
    self._msg_unlocked_set = threading.Event()
    self._msg_result_set = threading.Event()

  def set_p_q_msg_no_msg_true(self, p, q, msg_no, msg_true):
    self.p, self.q, self.msg_no, self.msg_true = p, q, msg_no, msg_true
    self._p_q_msg_no_msg_true_set.set()
  def get_p_q_msg_no_msg_true(self):
    self._p_q_msg_no_msg_true_set.wait()
    return (self.p, self.q, self.msg_no, self.msg_true)

  def set_msg_doubleencrypted(self, msg_doubleencrypted):
    self.msg_doubleencrypted = msg_doubleencrypted
    self._msg_doubleencrypted_set.set()
  def get_msg_doubleencrypted(self):
    self._msg_doubleencrypted_set.wait()
    return self.msg_doubleencrypted

  def set_msg_unlocked(self, msg_unlocked):
    self.msg_unlocked = msg_unlocked
    self._msg_unlocked_set.set()
  def get_msg_unlocked(self):
    self._msg_unlocked_set.wait()
    return self.msg_unlocked

  def set_msg_result(self, msg_result):
    self.msg_result = msg_result
    self._msg_result_set.set()
  def get_msg_result(self):
    self._msg_result_set.wait()
    return self.msg_result
