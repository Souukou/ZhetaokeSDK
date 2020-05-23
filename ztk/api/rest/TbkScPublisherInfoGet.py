from ztk.api.base import RestApi


class TbkScPublisherInfoGet(RestApi):
	'''__init__(self, relation_app, info_type, relation_id=None, page_no=None, page_size=None, domain='api.zhetaoke.com', port=10001)

		relation_app    渠道推广的物料类型，示例值：common

		info_type       邀请码类型，1 - 渠道邀请，2 - 渠道裂变，3 -会员邀请

		relation_id     渠道备案 - 渠道关系ID

		page_no         第几页

		page_size       每页大小

		Reference: https://www.zhetaoke.com/user/open/open_sc_publisher_get.aspx
	'''
	def __init__(self, relation_app, info_type, relation_id=None, page_no=None, page_size=None, domain='api.zhetaoke.com', port=10001):
		super().__init__(domain, port)
		self._RestApi__name = "/api/open_sc_publisher_get.ashx"
		self.relation_app = relation_app
		self.info_type = info_type
		self.relation_id = relation_id
		self.page_no = page_no
		self.page_size = page_size


	def getapiname(self):
		return 'taobao.tbk.sc.publisher.info.get'
