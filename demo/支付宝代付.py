from ztk.api import ZtkAlipayAgentPayRequest
from ztk import appinfo
from config import APPKEY, SID, ALIPAY_KEY


req = ZtkAlipayAgentPayRequest()
req.set_app_info(appinfo(APPKEY, SID)) # 设置appkey和sid
req.password = ALIPAY_KEY # 代付安全密匙
req.alipay_account = "130xxxxxxxx" # 支付宝账号
req.alipay_name = "xxx" # 支付宝真实姓名 
req.money = 2.33 # 代付金额，单位：元，最少0.1元/笔，只支持2位小数
req.remark = "你的返利已到账，请查收" # 代付备注，用户可见

result = req.get_response()
print(result)


