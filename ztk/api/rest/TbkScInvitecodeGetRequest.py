from ztk.api.base import RestApi


class TbkScInvitecodeGetRequest(RestApi):
	def __init__(self, domain='api.zhetaoke.com', port=10001):
		super().__init__(domain, port)
		self._RestApi__name = "/api/open_sc_invitecode_get.ashx"
		self.relation_app = None
		self.code_type = None
		self.relation_id = None


	def getapiname(self):
		return 'taobao.tbk.sc.invitecode.get'
