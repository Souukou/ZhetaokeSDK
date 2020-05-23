from ztk.api.base import RestApi


class TbkScPublisherInfoSave(RestApi):
	'''
	(未测试)
	__init__(self, backurl, inviter_code, inviter_code_s=None, s_note=None, type=1, domain='api.zhetaoke.com', port=10001)

	
 	inviter_code    淘宝客邀请渠道的邀请码

 	inviter_code_s  淘宝客邀请会员的邀请码

 	backurl         代理授权，并登记备案后，返回渠道信息至回调地址。

 	s_note          渠道备注，此内容建议填写用户唯一标识（比如用户编号，账号等唯一字段），跟返回的relation_id字段做关联。

 	type            淘客授权页面类型，1：电脑版授权页面，0：手机版授权页面，默认值1

	Reference: https://www.zhetaoke.com/user/open/open_sc_publisher_save.aspx
	'''
	def __init__(self, backurl, inviter_code, inviter_code_s=None, s_note=None, type=1, domain='api.zhetaoke.com', port=10001):
		super().__init__(domain, port)
		self._RestApi__name = "/api/open_sc_publisher_save.ashx"
		self.backurl = backurl
		self.inviter_code = inviter_code
		self.inviter_code_s = inviter_code_s
		self.s_note = s_note
		self.type = type


	def getapiname(self):
		return 'taobao.tbk.sc.publisher.info.save'
