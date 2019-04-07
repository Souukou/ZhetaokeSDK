from ztk.api.base import RestApi2


class TbkScOrderGetRequest(RestApi2):
	def __init__(self, domain='api.zhetaoke.com', port=10001):
		super().__init__(domain, port)
		self._RestApi__name = "/api/open_dingdanchaxun.ashx"
		
		self.fields = None  # 订单字段,默认全部字段
		self.start_time = None  # 订单查询开始时间
		self.span = None  # 订单查询时间范围,单位:秒,最小60,最大600,默认60
		self.page_no = None # 第几页
		self.page_size = None # 每页大小
		self.order_query_type = None  # 订单查询类型，创建时间“create_time”，或结算时间“settle_time”
		self.tk_status = None  # 非必须，订单状态，1: 全部订单，3：订单结算，12：订单付款， 13：订单失效，14：订单成功； 订单查询类型为‘结算时间’时，只能查订单结算状态
		self.order_scene = None #  	订单场景类型，1:常规订单，2:渠道订单，3:会员运营订单，默认为1，常规订单包含淘宝客所有的订单数据，含渠道，及会员运营订单，但不包含3方分成，及维权订单 
		self.order_count_type = None
		self.signurl = 1

	def getapiname(self):
		return 'taobao.sc.tbk.order.get'
