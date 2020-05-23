from ztk.api import TbkTpwdCreateRequest
from ztk import appinfo
from config import APPKEY, SID


req = TbkTpwdCreateRequest(
    text = "925纯银四叶草颈链项圈choker性感黑色女锁骨颈饰带脖子饰品韩国", # 口令弹框内容
    url = 'https://uland.taobao.com/coupon/edetail?e=FiP1ldN9itIGQASttHIRqc34nTBD93iS19C3HluYXIaDiceX8kU/fOLSsSLFQH3krf8ORUxzjrG2BhiNCCAkEW02/1k20DLuUkpftntGQobk6rR0xQn7rBemP0hpIIPvjDppvlX+ob8NlNJBuapvQ2MDg9t1zp0RkWxbw+5/SdwBp9L8ern9u0MuxoRQ3C+H3lkSaBjHFZuie/pBy9wBFg==&traceId=0b5218ce15902476208978285e1e74&union_lens=lensId:TAPI@1590247620@0b581b6f_0d83_17242250166_976d@01&xId=2u4qsyQLAFNgr5fYpd8KfpSXzBDZFqLNOyvH3IQhT4VgGXpq1WmtgHFwM9Nej6IjPOF9OAmneirV4u2r484kjNf3IYvT1GVYvXdfmu61vK3O', # 口令跳转目标页
    logo = 'https://img.alicdn.com/i4/2065331662/TB2FRndk7OWBuNjSsppXXXPgpXa_!!2065331662.jpg' # 口令弹框Logo
)
req.set_app_info(appinfo(APPKEY, SID)) # 设置appkey和sid

result = req.get_response()
print(result)


