from ztk.api import TbkScActivitylinkToolgetRequest
from ztk import appinfo
from config import APPKEY, SID, PID


req = TbkScActivitylinkToolgetRequest(
    adzone_id = PID.split('_')[-1],        # 推广位id，mm_xx_xx_xx pid三段式中的第三段
    site_id = PID.split('_')[-2],          # 推广位id，mm_xx_xx_xx pid三段式中的第二段
    promotion_scene_id = 20150318019998257 # 官方活动ID，从官方活动页获取
)
req.set_app_info(appinfo(APPKEY, SID)) # 设置appkey和sid

result = req.get_response()
print(result)


