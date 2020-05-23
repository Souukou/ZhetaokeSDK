from ztk.api.base import RestApi2


class TbkTpwdConvertRequest(RestApi2):
	'''__init__(self, pid, tkl, relation_id=None, signurl=2, domain="api.zhetaoke.com", port=10001)
	
	pid      淘客PID，mm_xxx_xxx_xxx,三段格式，必须与授权的账户相同，否则出错 

	tkl      淘口令文案或者二合一链接或者长链接或者短链接或者喵口令

	relation_id  渠道关系ID，仅适用于渠道推广场景。

	signurl  1: 使用淘宝联盟的http链接   2: 使用淘宝联盟的https链接

	Reference: https://www.zhetaoke.com/user/open/open_gaoyongzhuanlian.aspx
	'''
	def __init__(self, pid, tkl, relation_id=None, signurl=2, domain="api.zhetaoke.com", port=10001):
		super().__init__(domain, port)
		self._RestApi__name = "/api/open_gaoyongzhuanlian_tkl.ashx"
		self.pid = pid
		self.tkl = tkl
		self.relation_id = relation_id
		self.signurl = signurl
	
	def getapiname(self):
		return 'taobao.tbk.tpwd.convert'
