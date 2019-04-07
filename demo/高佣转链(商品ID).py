from ztk.api import TbkPrivilegeGetRequest
from ztk import appinfo
from config import APPKEY, SID, PID


req = TbkPrivilegeGetRequest()
req.set_app_info(appinfo(APPKEY, SID)) # 设置appkey和sid
req.num_iid = 567454541087 # 设置商品id
req.pid = PID # 推广位PID

result = req.get_response()
print(result)


