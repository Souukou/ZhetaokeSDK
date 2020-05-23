from ztk.api.base import RestApi


class ZtkAuthorisationGetRequest(RestApi):
	'''
	__init__(self, page=None, expire_day=None, domain='api.zhetaoke.com', port=10001):

	page        第几页，每页最多返回100个
 	expire_day  还剩下几天授权过期，取值范围0-7之间的整数，比如值为3，表示获取还剩下3天授权过期淘客账号信息

	Reference: https://www.zhetaoke.com/user/open/open_taokeshouquaninfo.aspx
	'''
	def __init__(self, page=None, expire_day=None, domain='api.zhetaoke.com', port=10001):
		super().__init__(domain, port)
		self._RestApi__name = "/api/open_taokeshouquaninfo.ashx"
		self.page = page
		self.expire_day = expire_day


	def getapiname(self):
		return 'zhetaoke.authorisation.get'
