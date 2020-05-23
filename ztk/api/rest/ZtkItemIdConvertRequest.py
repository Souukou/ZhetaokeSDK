from ztk.api.base import RestApi


class ZtkItemIdConvertRequest(RestApi):

	'''__init__(self, content, type=1, tlj=0, hjs=1, domain='api.zhetaoke.com', port=10001)
		
		解析商品编号API（返回商品ID和券ID）

		content 淘口令文案或者二合一链接或者长链接或者短链接或者喵口令。

		type 是否返回优惠券详细信息，type=1表示返回商品ID和优惠券详细信息，注意，优惠券信息可能为空

		tlj 是否解析淘礼金淘口令，tlj=1表示解析，tlj=0表示不解析，默认tlj=0

		hjs 是否解析火炬手淘口令，hjs=1表示解析，hjs=0表示不解析，默认hjs=1

		返回示例
		{
			"item_id":"524136796550", /*商品ID*/
			"activity_id":"c15af3c5bd7641419142344b214c1aa7", /*优惠券ID*/
			"amount":"20",   /*优惠券面额*/
			"startFee":"50",   /*优惠券满减信息*/
			"effectiveStartTime":"2019-03-21 00:00:00",  /*优惠券开始时间*/
			"effectiveEndTime":"2019-03-22 23:59:59",    /*优惠券结束时间*/
			"shopLogo":"//img.alicdn.com/bao/uploaded//3b/e5/TB1hP2enhWYBuNjy1zkSutGGpXa.jpg",  /*店铺Logo*/
			"shopName":"天猫超市"   /*店铺名称*/
		}
	'''
	
	def __init__(self, content, type=1, tlj=0, hjs=1, domain='api.zhetaoke.com', port=10001):
		super().__init__(domain, port)
		self._RestApi__name = "/api/open_shangpin_id.ashx"
		self.content = content
		self.type  = type
		self.tlj = tlj
		self.hjs = hjs


	def getapiname(self):
		return 'zhetaoke.item.id.convert'
