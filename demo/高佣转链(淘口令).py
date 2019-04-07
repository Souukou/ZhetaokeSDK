from ztk.api import TbkTpwdConvertRequest
from ztk import appinfo
from config import APPKEY, SID, PID


msg = '''【这个聚划算团购宝贝不错:925银四叶草颈链项圈choker性感黑色项链女锁骨颈带脖子饰品韩国(分享自@手机淘宝android客户端)】https://m.tb.cn/h.eZZzdfm?sm=a9cc61 点击链接，再选择浏览器咑閞；或復·制这段描述￥OzXfbztYWUw￥后到👉淘♂寳♀👈'''

req = TbkTpwdConvertRequest()
req.set_app_info(appinfo(APPKEY, SID)) # 设置appkey和sid
req.tkl = msg # 包含淘口令的文本
req.pid = PID # 推广位PID

result = req.get_response()
print(result)


