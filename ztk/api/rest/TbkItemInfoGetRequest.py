from ztk.api.base import RestApi


class TbkItemInfoGetRequest(RestApi):
	def __init__(self, domain='api.zhetaoke.com', port=10001):
		super().__init__(domain, port)
		self._RestApi__name = "/api/open_item_info.ashx"
		self.num_iids = None


	def getapiname(self):
		return 'taobao.tbk.item.info.get'
