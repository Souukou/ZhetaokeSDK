from ztk.api.base import RestApi


class TbkScInvitecodeGetRequest(RestApi):
	'''__init__(self, relation_app, code_type, relation_id=None, domain='api.zhetaoke.com', port=10001)

	relation_app   渠道推广的物料类型，示例值：common

 	code_type      邀请码类型，1 - 渠道邀请，2 - 渠道裂变，3 -会员邀请

 	relation_id    渠道关系ID

	Reference: https://www.zhetaoke.com/user/open/open_sc_invitecode_get.aspx
	'''
	def __init__(self, relation_app, code_type, relation_id=None, domain='api.zhetaoke.com', port=10001):
		super().__init__(domain, port)
		self._RestApi__name = "/api/open_sc_invitecode_get.ashx"
		self.relation_app = relation_app
		self.code_type = code_type
		self.relation_id = relation_id


	def getapiname(self):
		return 'taobao.tbk.sc.invitecode.get'
