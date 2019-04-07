from ztk.api import ZtkBaiduShorturlGetRequest
from ztk import appinfo
from config import APPKEY, SID


req = ZtkBaiduShorturlGetRequest()
req.set_app_info(appinfo(APPKEY, SID)) # 设置appkey和sid
req.content = "https://www.sina.com.cn" # 要缩短的链接

result = req.get_response()
print(result)


