from ztk.api import TbkTpwdConvertRequest
from ztk import appinfo
from config import APPKEY, SID, PID

msg = '''付致这段话€7Gaw1qEVcgx€转移至淘宝或点几链街https://m.tb.cn/h.VlMgLav?sm=15f7e3 至瀏..覽..噐【Sony/索尼 SRS-XB01 无线蓝牙音箱迷你户外防水小钢炮便携式手】'''

req = TbkTpwdConvertRequest(
    tkl = msg,
    pid = PID
)
req.set_app_info(appinfo(APPKEY, SID)) # 设置appkey和sid

result = req.get_response()
print(result)


