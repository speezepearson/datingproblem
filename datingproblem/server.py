import collections
import json
import bottle
import threading
from .conversation import Conversation

def serve():
  conversations = collections.defaultdict(Conversation)

  @bottle.post('/<initiator>/<responder>/set_p_q_msg_no_msg_true')
  def _(initiator, responder):
    conversations[initiator,responder].set_p_q_msg_no_msg_true(**bottle.request.json)

  @bottle.get('/<initiator>/<responder>/get_p_q_msg_no_msg_true')
  def _(initiator, responder):
    return json.dumps(list(conversations[initiator,responder].get_p_q_msg_no_msg_true()))

  @bottle.post('/<initiator>/<responder>/set_msg_doubleencrypted')
  def _(initiator, responder):
    conversations[initiator,responder].set_msg_doubleencrypted(**bottle.request.json)

  @bottle.get('/<initiator>/<responder>/get_msg_doubleencrypted')
  def _(initiator, responder):
    return json.dumps(conversations[initiator,responder].get_msg_doubleencrypted())

  @bottle.post('/<initiator>/<responder>/set_msg_unlocked')
  def _(initiator, responder):
    conversations[initiator,responder].set_msg_unlocked(**bottle.request.json)

  @bottle.get('/<initiator>/<responder>/get_msg_unlocked')
  def _(initiator, responder):
    return json.dumps(conversations[initiator,responder].get_msg_unlocked())

  @bottle.post('/<initiator>/<responder>/set_msg_result')
  def _(initiator, responder):
    conversations[initiator,responder].set_msg_result(**bottle.request.json)

  @bottle.get('/<initiator>/<responder>/get_msg_result')
  def _(initiator, responder):
    return json.dumps(conversations[initiator,responder].get_msg_result())

  bottle.run(host='localhost', port=8080, server='cherrypy')
