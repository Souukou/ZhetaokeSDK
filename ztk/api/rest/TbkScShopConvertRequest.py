from ztk.api.base import RestApi


class TbkScShopConvertRequest(RestApi):
	'''__init__(self, site_id, fields, user_ids, adzone_id, platform=None, unid=None, signurl=2, domain='api.zhetaoke.com', port=10001):

		site_id    备案的网站id, mm_xx_xx_xx pid三段式中的第二段

		fields     需返回的字段列表，如：user_id,click_url

		user_ids   卖家ID串，用','分割，可通过全网商品详情API接口获得,seller_id字段

		adzone_id  广告位ID，区分效果位置

		platform   链接形式：1：PC，2：无线，默认：1

		unid       自定义输入串，英文和数字组成，长度不能大于12个字符，区分不同的推广渠道

		signurl    1: 使用淘宝联盟的http链接   2: 使用淘宝联盟的https链接

		Reference: https://www.zhetaoke.com/user/open/open_shop_convert.aspx
	'''
	def __init__(self, site_id, fields, user_ids, adzone_id, platform=None, unid=None, signurl=2, domain='api.zhetaoke.com', port=10001):
		super().__init__(domain, port)
		self._RestApi__name = "/api/open_shop_convert.ashx"
		self.site_id = site_id
		self.fields = fields
		self.user_ids = user_ids
		self.adzone_id = adzone_id
		self.platform = platform
		self.unid = unid
		self.signurl = signurl

	def getapiname(self):
		return 'taobao.tbk.sc.shop.convert'
