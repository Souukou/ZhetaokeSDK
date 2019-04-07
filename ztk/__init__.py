class appinfo(object):
	def __init__(self, appkey, sid=None):
		self.appkey = appkey
		self.sid = sid


def get_default_app_info():
	pass


def set_default_app_info(appkey, sid = None):
	default = appinfo(appkey, sid)
	global get_default_app_info
	get_default_app_info = lambda: default
