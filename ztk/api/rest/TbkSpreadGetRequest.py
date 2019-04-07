from ztk.api.base import RestApi


class TbkSpreadGetRequest(RestApi):
	def __init__(self, domain='api.zhetaoke.com', port=10001):
		super().__init__(domain, port)
		self._RestApi__name = "/api/open_shorturl_taobao_get.ashx"
		self.content = None

	def getapiname(self):
		return 'taobao.tbk.spread.get'
