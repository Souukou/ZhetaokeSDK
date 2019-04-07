from ztk.api import ZtkSinaShorturlGetRequest
from ztk import appinfo
from config import APPKEY, SID


req = ZtkSinaShorturlGetRequest()
req.set_app_info(appinfo(APPKEY, SID)) # 设置appkey和sid
req.content = "https://baidu.com" # 要缩短的链接

result = req.get_response()
print(result)


