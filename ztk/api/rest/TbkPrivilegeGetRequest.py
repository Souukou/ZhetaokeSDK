from ztk.api.base import RestApi2


class TbkPrivilegeGetRequest(RestApi2):
	'''__init__(self, pid, num_iid=None, me=None, relation_id=None, signurl=2, domain='api.zhetaoke.com', port=10001)

	pid      淘客PID，mm_xxx_xxx_xxx,三段格式，必须与授权的账户相同，否则出错 

	num_iid  商品ID,商品ID或me必须填一个 

	me       二合一的me参数，大多数是e后面的那个参数

	relation_id  渠道关系ID，仅适用于渠道推广场景。

	signurl  1: 使用淘宝联盟的http链接   2: 使用淘宝联盟的https链接

	Reference: https://www.zhetaoke.com/user/open/open_gaoyongzhuanlian.aspx
	
	'''
	def __init__(self, pid, num_iid=None, me=None, relation_id=None, signurl=2, domain='api.zhetaoke.com', port=10001):
		super().__init__(domain, port)
		self._RestApi__name = "/api/open_gaoyongzhuanlian.ashx"
		self.pid = pid
		self.num_iid = num_iid
		self.me = me
		self.relation_id = relation_id
		self.signurl = signurl

	def getapiname(self):
		return 'taobao.tbk.privilege.get'
