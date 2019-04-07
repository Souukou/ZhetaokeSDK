from ztk.api import TbkScOrderGetRequest
from ztk import appinfo
from config import APPKEY, SID


req = TbkScOrderGetRequest()
req.set_app_info(appinfo(APPKEY, SID)) # 设置appkey和sid
req.start_time = "2019-04-05 19:30:13" # 起始时间
req.span = 1200 # 时间范围,单位:秒

result = req.get_response()
print(result)


