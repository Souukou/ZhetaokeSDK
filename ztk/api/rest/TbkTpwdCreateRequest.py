from ztk.api.base import RestApi


class TbkTpwdCreateRequest(RestApi):
	def __init__(self, domain='api.zhetaoke.com', port=10001):
		super().__init__(domain, port)
		self._RestApi__name = "/api/open_tkl_create.ashx"
		self.text = None
		self.url = None
		self.logo = None

	def getapiname(self):
		return 'taobao.tbk.tpwd.create'
