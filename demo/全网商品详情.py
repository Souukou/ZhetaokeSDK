from ztk.api import TbkItemInfoGetRequest
from ztk import appinfo
from config import APPKEY, SID


req = TbkItemInfoGetRequest(567454541087)
req.set_app_info(appinfo(APPKEY, SID)) # 设置appkey和sid

result = req.get_response()
print(result)


