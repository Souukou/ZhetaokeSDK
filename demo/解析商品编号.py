from ztk.api import ZtkItemIdConvertRequest
from ztk import appinfo
from config import APPKEY, SID


msg = '''fu致这行话₤x33I1JY3leo₤打開淘宝或點击链街https://m.tb.cn/h.VlHDOB1?sm=6235d9 至瀏lan嘂..【Intel/英特尔 酷睿i3-9100F盒装CPU 1151针脚台式机在线教育授课网课电脑处理器】'''

# 解析商品编号API为折淘客自有API，转链结果与官方不一定相同，可能漏券
req = ZtkItemIdConvertRequest(
    content = msg,  # 支持淘口令、二合一链接、长链、短链、喵口令
    type = 1        #如果有券是否返回优惠券信息
    )
req.set_app_info(appinfo(APPKEY, SID)) # 设置appkey和sid

result = req.get_response()
print(result)
