from ztk.api.base import RestApi


class TbkScActivitylinkToolgetRequest(RestApi):
	def __init__(self, domain='api.zhetaoke.com', port=10001):
		super().__init__(domain, port)
		self._RestApi__name = "/api/open_activitylink_get.ashx"
		self.adzone_id = None
		self.site_id = None
		self.promotion_scene_id = None
		self.platform = None
		self.union_id = None
		self.relation_id = None
		

	def getapiname(self):
		return 'taobao.tbk.sc.activitylink.toolget'
