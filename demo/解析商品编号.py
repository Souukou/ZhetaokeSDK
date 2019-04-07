from ztk.api import ZtkItemIdConvertRequest
from ztk import appinfo
from config import APPKEY, SID


msg = '''【这个#聚划算团购#宝贝不错:925银四叶草颈链项圈choker性感黑色项链女锁骨颈带脖子饰品韩国(分享自@手机淘宝android客户端)】https://m.tb.cn/h.eZZzdfm?sm=a9cc61 点击链接，再选择浏览器咑閞；或復·制这段描述￥OzXfbztYWUw￥后到👉淘♂寳♀👈'''

# 解析商品编号API为折淘客自有API，转链结果与官方不一定相同，可能漏券
req = ZtkItemIdConvertRequest()
req.set_app_info(appinfo(APPKEY, SID)) # 设置appkey和sid
req.content = msg # 支持淘口令、二合一链接、长链、短链、喵口令
req.type = 1 #如果有券是否返回优惠券信息

result = req.get_response()
print(result)


