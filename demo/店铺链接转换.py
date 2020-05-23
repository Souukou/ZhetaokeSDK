from ztk.api import TbkScShopConvertRequest
from ztk import appinfo
from config import APPKEY, SID, PID


req = TbkScShopConvertRequest(
    site_id = PID.split('_')[-2],          # 备案的网站id, mm_xx_xx_xx pid三段式中的第二段
    fields = 'user_id,click_url',           # 需返回的字段列表
    user_ids = 2065331662,                  # 卖家ID串
    adzone_id = PID.split('_')[-1]         # 广告位ID，备案的网站id, mm_xx_xx_xx pid三段式中的第三段
)
req.set_app_info(appinfo(APPKEY, SID)) # 设置appkey和sid

result = req.get_response()
print(result)


