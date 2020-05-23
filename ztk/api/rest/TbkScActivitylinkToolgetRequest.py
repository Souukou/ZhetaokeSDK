from ztk.api.base import RestApi


class TbkScActivitylinkToolgetRequest(RestApi):
	'''__init__(self, adzone_id, site_id, promotion_scene_id, platform=1, union_id=None, relation_id=None, type=0, domain='api.zhetaoke.com', port=10001)

		adzone_id           推广位id，mm_xx_xx_xx pid三段式中的第三段

		site_id	int         推广位id，mm_xx_xx_xx pid三段式中的第二段

		promotion_scene_id  官方活动ID，从官方活动页获取。饿了么:1571715733668, 口碑主会场:1583739244161, 生活服务分会场:1583739244162

		注意：口碑主会场活动和生活服务分会场，是调用的另外一个官方接口，调用接口后，返回的json格式和字段不同，请大家自行匹配。

		platform            1：PC，2：无线，默认：１

		union_id            自定义输入串，英文和数字组成，长度不能大于12个字符，区分不同的推广渠道

		relation_id         渠道关系ID，仅适用于渠道推广场景

		type                0:返回推广长链接，1：返回微信小程序地址（仅限饿了么、口碑两个活动），默认0

		Reference: http://www.zhetaoke.com/user/open/open_activitylink_get.aspx
	
	'''
	def __init__(self, adzone_id, site_id, promotion_scene_id, platform=1, union_id=None, relation_id=None, type=0, domain='api.zhetaoke.com', port=10001):
		super().__init__(domain, port)
		self._RestApi__name = "/api/open_activitylink_get.ashx"
		self.adzone_id = adzone_id
		self.site_id = site_id
		self.promotion_scene_id = promotion_scene_id
		self.platform = platform
		self.union_id = union_id
		self.relation_id = relation_id
		self.type = type
		

	def getapiname(self):
		return 'taobao.tbk.sc.activitylink.toolget'
