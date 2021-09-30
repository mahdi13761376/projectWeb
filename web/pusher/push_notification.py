from pusher import Pusher


def send_notification(message):
    pusher = Pusher(app_id=u'823552', key=u'0637c27faa22b112d96c', secret=u'2b5eaec74eb1b58908b3', cluster=u'ap2')
    pusher.trigger(u'test', u'test', message)
    return True


def open_door(device_id):
    pusher = Pusher(app_id=u'823552', key=u'0637c27faa22b112d96c', secret=u'2b5eaec74eb1b58908b3', cluster=u'ap2')
    pusher.trigger(device_id, u'test', 'open the door')
    return True
