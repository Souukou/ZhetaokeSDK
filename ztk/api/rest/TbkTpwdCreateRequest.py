from ztk.api.base import RestApi2


class TbkTpwdCreateRequest(RestApi2):
	'''__init__(self, text, url, logo=None, signurl=2, domain='api.zhetaoke.com', port=10001)

	text     口令弹框内容，长度大于5个字符，如：美美小编精心推荐。尽量不要带特殊符号或特殊词，否则生成的淘口令手淘里可能打不开。

 	url      口令跳转目标页，如：https://uland.taobao.com/，必须以https开头，可以是二合一链接、长链接、短链接等各种淘宝高佣链接；支持渠道备案链接

 	logo     口令弹框logoURL，如：https://img.alicdn.com/bao/uploaded/i2.jpg_200x200.jpg

 	signurl  1: 使用淘宝联盟的http链接   2: 使用淘宝联盟的https链接
	'''
	def __init__(self, text, url, logo=None, signurl=2, domain='api.zhetaoke.com', port=10001):
		super().__init__(domain, port)
		self._RestApi__name = "/api/open_tkl_create.ashx"
		self.text = text
		self.url = url
		self.logo = logo
		self.signurl = signurl

	def getapiname(self):
		return 'taobao.tbk.tpwd.create'
