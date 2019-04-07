from ztk.api.base import RestApi


class ZtkAuthorizeRequest(RestApi):
	def __init__(self, domain='api.zhetaoke.com', port=10001):
		super().__init__(domain, port)
		self._RestApi__name = "/api/open_taokeshouquan.ashx"
		self.backurl = None
		self.type = None

	def getapiname(self):
		return 'zhetaoke.authorize.request'
