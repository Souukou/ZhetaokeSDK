from ztk.api.base import RestApi


class ZtkAlipayAgentPayRequest(RestApi):
	def __init__(self, domain='api.zhetaoke.com', port=10001):
		super().__init__(domain, port)
		self._RestApi__name = "/api/open_agent_alipay_money.ashx"
		self.password = None
		self.alipay_account = None
		self.alipay_name = None
		self.money = None
		self.remark = None


	def getapiname(self):
		return 'zhetaoke.alipay.agent.pay'
