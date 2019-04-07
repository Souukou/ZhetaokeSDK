from ztk.api.base import RestApi


class ZtkAuthorisationGetRequest(RestApi):
	def __init__(self, domain='api.zhetaoke.com', port=10001):
		super().__init__(domain, port)
		self._RestApi__name = "/api/open_taokeshouquaninfo.ashx"
		self.page  = None


	def getapiname(self):
		return 'zhetaoke.authorisation.get'
