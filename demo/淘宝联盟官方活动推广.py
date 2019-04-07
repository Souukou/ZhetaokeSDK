from ztk.api import TbkScActivitylinkToolgetRequest
from ztk import appinfo
from config import APPKEY, SID


req = TbkScActivitylinkToolgetRequest()
req.set_app_info(appinfo(APPKEY, SID)) # 设置appkey和sid
req.site_id = 95850046 # 推广位id，mm_xx_xx_xx pid三段式中的第二段
req.adzone_id = 63294350347 # 推广位id，mm_xx_xx_xx pid三段式中的第三段
req.promotion_scene_id = 1552400826973 # 官方活动ID，从官方活动页获取[联盟产品]->[主题活动]->[官方活动推广]

result = req.get_response()
print(result)


