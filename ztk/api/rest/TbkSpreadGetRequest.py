from ztk.api.base import RestApi


class TbkSpreadGetRequest(RestApi):
	'''__init__(self, content, domain='api.zhetaoke.com', port=10001)

		content  输入原始url，转换得到淘宝短链接。要转短链接的网址，需要进行Urlencode编码，只支持uland.taobao.com，s.click.taobao.com， ai.taobao.com，temai.taobao.com的域名转换，否则判错。

		Reference: https://www.zhetaoke.com/user/open/open_shorturl_taobao_get.aspx
	'''
	def __init__(self, content, domain='api.zhetaoke.com', port=10001):
		super().__init__(domain, port)
		self._RestApi__name = "/api/open_shorturl_taobao_get.ashx"
		self.content = content

	def getapiname(self):
		return 'taobao.tbk.spread.get'
