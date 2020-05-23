from ztk.api.base import RestApi


class ZtkAlipayAgentPayRequest(RestApi):
	def __init__(self, password, alipay_account, alipay_name, money, remark, domain='api.zhetaoke.com', port=10001):
		super().__init__(domain, port)
		self._RestApi__name = "/api/open_agent_alipay_money.ashx"
		self.password = password
		self.alipay_account = alipay_account
		self.alipay_name = alipay_name
		self.money = money
		self.remark = remark


	def getapiname(self):
		return 'zhetaoke.alipay.agent.pay'
