from ztk.api.base import RestApi


class TbkItemInfoGetRequest(RestApi):
	'''
	__init__(self, num_iids, domain='api.zhetaoke.com', port=10001)

	num_iids    商品ID串，用,分割，最大40个

	Reference: https://www.zhetaoke.com/user/open/open_item_info.aspx
	'''
	def __init__(self, num_iids, domain='api.zhetaoke.com', port=10001):
		super().__init__(domain, port)
		self._RestApi__name = "/api/open_item_info.ashx"
		self.num_iids = num_iids


	def getapiname(self):
		return 'taobao.tbk.item.info.get'
