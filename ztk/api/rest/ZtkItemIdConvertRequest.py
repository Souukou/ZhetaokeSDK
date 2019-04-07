from ztk.api.base import RestApi


class ZtkItemIdConvertRequest(RestApi):
	def __init__(self, domain='api.zhetaoke.com', port=10001):
		super().__init__(domain, port)
		self._RestApi__name = "/api/open_shangpin_id.ashx"
		self.content = None
		self.type  = 1


	def getapiname(self):
		return 'zhetaoke.item.id.convert'
