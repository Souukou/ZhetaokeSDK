from ztk.api import TbkSpreadGetRequest
from ztk import appinfo
from config import APPKEY, SID


req = TbkSpreadGetRequest(content="https://uland.taobao.com/coupon/edetail?e=cbONVoUO0PIGQASttHIRqc34nTBD93iS19C3HluYXIaDiceX8kU%2FfOLSsSLFQH3krf8ORUxzjrEcW%2Bw8nO5GLK0TeAL%2BmcF1UkpftntGQobk6rR0xQn7rFZrtTOLgXkcjDppvlX%2Bob%2F%2BTosbFmliBzQxd0%2F7s8Sy8%2B1UQ0U%2BCWuQzbQRBC%2Bhrh3Rj1YjsbrTXpcOvaPmn5A%3D&traceId=0b14d5fe15546221986247542e&union_lens=lensId:0b150f1b_0bab_169f6b43392_a541&xId=4iQXlGpHZPHDKIn4Pv2QH6WwijRDDK9SUkMbUMQhaF8DOu4fre3Y1CrurgoNESv2P2fYnkzFM6oSKvGTweVbxJ")
req.set_app_info(appinfo(APPKEY, SID)) # 设置appkey和sid

result = req.get_response()
print(result)



