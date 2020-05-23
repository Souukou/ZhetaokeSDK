from ztk.api.base import RestApi2


class TbkScOrderGetRequest(RestApi2):
	'''__init__(
		self, 
		start_time, 
		end_time, 
		query_type=None, 
		position_index=None, 
		page_size=None, 
		member_type=None, 
		tk_status=None, 
		jump_type=None, 
		page_no=None, 
		order_scene=None, 
		signurl=2, 
		domain='api.zhetaoke.com', 
		port=10001):

		start_time      订单查询开始时间，2019-04-05 12:18:22
 		end_time        订单查询结束时间，2019-04-25 15:18:22，目前最大可查3个小时内的数据
		query_type      查询时间类型，1：按照订单淘客创建时间查询，2:按照订单淘客付款时间查询，3:按照订单淘客结算时间查询
		position_index  位点，除第一页之外，都需要传递；前端原样返回。注意：从第二页开始，位点必须传递前一页返回的值，否则翻页无效。
		page_size       页大小，默认20，1~100
		member_type     推广者角色类型,2:二方，3:三方，不传，表示所有角色
		tk_status       淘客订单状态，12-付款，13-关闭，14-确认收货（暂时无法结算佣金），3-结算成功; 不传，表示所有状态
		jump_type       跳转类型，当向前或者向后翻页必须提供,-1: 向前翻页,1：向后翻页
		page_no	string  第几页，默认1，1~100
		order_scene     场景订单场景类型，1:常规订单，2:渠道订单，3:会员运营订单，默认为1
		signurl         1:使用淘宝联盟的http链接  2:使用淘宝联盟的https链接

		Reference: https://www.zhetaoke.com/user/open/open_dingdanchaxun2.aspx
	
	'''
	def __init__(
		self, 
		start_time, 
		end_time, 
		query_type=None, 
		position_index=None, 
		page_size=None, 
		member_type=None, 
		tk_status=None, 
		jump_type=None, 
		page_no=None, 
		order_scene=None, 
		signurl=2, 
		domain='api.zhetaoke.com', 
		port=10001):
		super().__init__(domain, port)
		self._RestApi__name = "/api/open_dingdanchaxun2.ashx"
		self.start_time = start_time  
		self.end_time = end_time
		self.query_type = query_type  
		self.position_index = position_index
		self.page_size = page_size
		self.member_type = member_type
		self.tk_status = tk_status  # 非必须，订单状态，1: 全部订单，3：订单结算，12：订单付款， 13：订单失效，14：订单成功； 订单查询类型为‘结算时间’时，只能查订单结算状态
		self.jump_type = jump_type #  	订单场景类型，1:常规订单，2:渠道订单，3:会员运营订单，默认为1，常规订单包含淘宝客所有的订单数据，含渠道，及会员运营订单，但不包含3方分成，及维权订单 
		self.page_no = page_no
		self.order_scene = order_scene
		self.signurl = signurl

	def getapiname(self):
		return 'taobao.sc.tbk.order.get'
