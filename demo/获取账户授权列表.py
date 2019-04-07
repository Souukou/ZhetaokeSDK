from ztk.api import ZtkAuthorisationGetRequest
from ztk import appinfo
from config import APPKEY


req = ZtkAuthorisationGetRequest()
req.set_app_info(appinfo(APPKEY)) # 设置appkey和sid

result = req.get_response()
print(result)


