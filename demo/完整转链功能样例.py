# --------------------------------------
# 使用淘口令解析、商品详情、淘口令生成、淘宝短链接转换API，实现转链功能
# --------------------------------------

from ztk.api import TbkTpwdConvertRequest
from ztk.api import TbkItemInfoGetRequest
from ztk.api import TbkTpwdCreateRequest
from ztk.api import TbkSpreadGetRequest
import ztk.api
from config import APPKEY, SID, PID


msg = '''【这个聚划算团购宝贝不错:925银四叶草颈链项圈choker性感黑色项链女锁骨颈带脖子饰品韩国(分享自@手机淘宝android客户端)】https://m.tb.cn/h.eZZzdfm?sm=a9cc61 点击链接，再选择浏览器咑閞；或復·制这段描述￥OzXfbztYWUw￥后到👉淘♂寳♀👈'''

# 设置全局appkey和sid
ztk.set_default_app_info(APPKEY, SID) 

# 调用淘口令解析API，以进行转链
req = TbkTpwdConvertRequest()
# 包含淘口令的文本
req.tkl = msg
# 推广位PID
req.pid = PID
# 获取转链结果
result = req.get_response()["tbk_privilege_get_response"]["result"]["data"]
#print(result)

# 根据有无优惠券，选择合适的url
if "coupon_remain_count" in result:
	url = result["coupon_click_url"]
else:
	url = result["item_url"]
# 提取商品ID
id = result["item_id"]

# 调用商品详情API，获取主图url和商品标题
req = TbkItemInfoGetRequest()
# 商品ID
req.num_iids = id
# 获取商品详情
result = req.get_response()["tbk_item_info_get_response"]["results"]["n_tbk_item"][0]
#print(result)

# 提取主图url
pic = result["pict_url"]
# 提取商品标题
texts = result["title"]

# 调用淘口令API，生成淘口令
req = TbkTpwdCreateRequest()
# 口令弹框内容
req.text = texts
# 口令弹框内容
req.url = url
# 口令弹框Logo
req.logo = pic
# 获取淘口令
result = req.get_response()
#print(result)

# 提取淘口令
taopasswd = result["model"]

# 调用淘宝短链API，生成短链接
req = TbkSpreadGetRequest()
# 商品URL
req.content = url
# 获取短连接
result = req.get_response()
#print(result)

# 提取短连接
taourl = result["shorturl"]

print(f"淘口令：{taopasswd}\n链接：{taourl}")

'''
输出示例：

淘口令：￥AzQybzGT6IP￥
链接：https://s.click.taobao.com/N2lFqCw
'''


