from ztk.api.base import RestApi


class ZtkAlipayAgentPayRequest(RestApi):
	'''__init__(self, password, alipay_account, alipay_name, money, remark, domain='api.zhetaoke.com', port=10001)

	password            付安全秘钥代付设置

 	alipay_account  	支付宝账号

 	alipay_name         支付宝真实姓名

 	money               代付金额，单位：元，最少0.1元/笔，只支持2位小数

 	remark              备注，如：佣金发放

	Reference: https://www.zhetaoke.com/user/open/open_agent_alipay_money.aspx
	
	'''
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
