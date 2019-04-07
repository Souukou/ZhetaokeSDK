from ztk.api import TbkItemInfoGetRequest
from ztk import appinfo
from config import APPKEY, SID


req = TbkItemInfoGetRequest()
req.set_app_info(appinfo(APPKEY, SID)) # 设置appkey和sid
req.num_iids = 567454541087 # 设置商品id

result = req.get_response()
print(result)


