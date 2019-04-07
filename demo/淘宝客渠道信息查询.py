from ztk.api import TbkScPublisherInfoGet
from ztk import appinfo
from config import APPKEY, SID


req = TbkScPublisherInfoGet()
req.set_app_info(appinfo(APPKEY, SID)) # 设置appkey和sid
req.relation_app = "common" # 渠道推广的物料类型，通常为common
req.info_type = 1 # 类型，必选 默认为1 

result = req.get_response()
print(result)
