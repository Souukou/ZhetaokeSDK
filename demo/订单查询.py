from ztk.api import TbkScOrderGetRequest
from ztk import appinfo
from config import APPKEY, SID


req = TbkScOrderGetRequest(
    start_time = "2020-04-05 19:30:13",
    end_time = "2020-04-05 22:30:13",
    page_size = 100
)
req.set_app_info(appinfo(APPKEY, SID)) # 设置appkey和sid

result = req.get_response()
print(result)


