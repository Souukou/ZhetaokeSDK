from ztk.api.base import RestApi


class TbkScPublisherInfoSave(RestApi):
	def __init__(self, domain='api.zhetaoke.com', port=10001):
		super().__init__(domain, port)
		self._RestApi__name = "/api/open_sc_publisher_save.ashx"
		self.inviter_code = None
		self.inviter_code_s = None
		self.backurl = None
		self.s_note = None
		self.type = None


	def getapiname(self):
		return 'taobao.tbk.sc.publisher.info.save'
