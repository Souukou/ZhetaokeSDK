from ztk.api.base import RestApi2


class TbkPrivilegeGetRequest(RestApi2):
	def __init__(self, domain='api.zhetaoke.com', port=10001):
		super().__init__(domain, port)
		self._RestApi__name = "/api/open_gaoyongzhuanlian.ashx"
		self.pid = None
		self.num_iid = None
		self.me = None  # 营销计划链接中的me参数
		self.relation_id = None
		self.signurl = 1

	def getapiname(self):
		return 'taobao.tbk.privilege.get'
