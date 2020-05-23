# --------------------------------------
# 使用淘口令解析、商品详情、淘口令生成、淘宝短链接转换API，实现转链功能
# --------------------------------------

from ztk.api import TbkTpwdConvertRequest
from ztk.api import TbkItemInfoGetRequest
from ztk.api import TbkTpwdCreateRequest
from ztk.api import TbkSpreadGetRequest
import ztk.api
from config import APPKEY, SID, PID


msg = '''付致这段话€7Gaw1qEVcgx€转移至淘宝或点几链街https://m.tb.cn/h.VlMgLav?sm=15f7e3 至瀏..覽..噐【Sony/索尼 SRS-XB01 无线蓝牙音箱迷你户外防水小钢炮便携式手】'''

# 设置全局appkey和sid
ztk.set_default_app_info(APPKEY, SID) 

# 调用淘口令解析API，以进行转链
req = TbkTpwdConvertRequest(pid=PID, tkl=msg)
# 获取转链结果
result = req.get_response()["tbk_privilege_get_response"]["result"]["data"]
# print(result)

# 根据有无优惠券，选择合适的url
if "coupon_remain_count" in result:
	url = result["coupon_click_url"]
else:
	url = result["item_url"]
# 提取商品ID
id = result["item_id"]

# 调用商品详情API，获取主图url和商品标题
req = TbkItemInfoGetRequest(num_iids=id)
# 获取商品详情
result = req.get_response()["tbk_item_info_get_response"]["results"]["n_tbk_item"][0]
# print(result)

# 提取主图url
pic = result["pict_url"]
# 提取商品标题
texts = result["title"]

# 调用淘口令API，生成淘口令
req = TbkTpwdCreateRequest(text=texts, url=url, logo=pic)
# 获取淘口令
result = req.get_response()
# print(result)

# 提取淘口令
taopasswd = result["tbk_tpwd_create_response"]["data"]["model"]

# 调用淘宝短链API，生成短链接
req = TbkSpreadGetRequest(content=url)
# 获取短连接
result = req.get_response()
# print(result)

# 提取短连接
taourl = result["shorturl"]

print(f"淘口令：{taopasswd}\n链接：{taourl}")


