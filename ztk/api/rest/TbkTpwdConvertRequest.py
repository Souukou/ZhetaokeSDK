from ztk.api.base import RestApi2


class TbkTpwdConvertRequest(RestApi2):
	def __init__(self, domain="api.zhetaoke.com", port=10001):
		super().__init__(domain, port)
		self._RestApi__name = "/api/open_gaoyongzhuanlian_tkl.ashx"
		self.pid = None
		self.tkl = None
		self.relation_id = None
		self.signurl = 1
	
	def getapiname(self):
		return 'taobao.tbk.tpwd.convert'
