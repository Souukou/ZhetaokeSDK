from ztk.api import TbkPrivilegeGetRequest
from ztk import appinfo
from config import APPKEY, SID, PID


req = TbkPrivilegeGetRequest(
    pid = PID,             # 推广位PID
    num_iid = 567454541087 # 商品ID
)
req.set_app_info(appinfo(APPKEY, SID)) # 设置appkey和sid
result = req.get_response()
print(result)


