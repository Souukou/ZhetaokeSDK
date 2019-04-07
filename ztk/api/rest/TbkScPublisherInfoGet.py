from ztk.api.base import RestApi


class TbkScPublisherInfoGet(RestApi):
	def __init__(self, domain='api.zhetaoke.com', port=10001):
		super().__init__(domain, port)
		self._RestApi__name = "/api/open_sc_publisher_get.ashx"
		self.relation_app = None
		self.info_type = None
		self.relation_id = None
		self.page_no = None
		self.page_size = None


	def getapiname(self):
		return 'taobao.tbk.sc.publisher.info.get'
