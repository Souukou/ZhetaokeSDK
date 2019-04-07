# 折淘客 Python3 SDK
淘宝联盟-折淘客(www.zhetaoke.com)-Python3 SDK （非官方）
阿里妈妈已经无法申请到转链、订单等API权限，但可以用第三方接口使用到这些权限。
本SDK基于官方SDK修改得到的，提供折淘客的所有API功能，使用方法可见demo目录。

API列表
| 折淘客API | 类名 |
| ------ | ------ |
| 高佣转链（商品ID）| TbkPrivilegeGetRequest |
| 高佣转链（淘口令）| TbkTpwdConvertRequest |
| 订单查询 | TbkScOrderGetRequest |
| 解析商品编号 | ZtkItemIdConvertRequest |
| 淘客账号授权 | ZtkAuthorizeRequest |
| 获取账户授权列表 | ZtkAuthorisationGetRequest |
| 淘宝短链转换 | TbkSpreadGetRequest |
| 新浪短链转换 | ZtkSinaShorturlGetRequest |
| 百度短链转换 | ZtkBaiduShorturlGetRequest |
| 淘口令生成 | TbkTpwdCreateRequest |
| 淘宝客邀请码生成 | TbkScInvitecodeGetRequest |
| 淘宝客渠道备案 | TbkScPublisherInfoSave |
| 淘宝客渠道信息查询 | TbkScPublisherInfoGet |
| 全网商品详情 | TbkItemInfoGetRequest |
| 淘宝联盟官方活动推广 | TbkScActivitylinkToolgetRequest |
| 支付宝代付 | ZtkAlipayAgentPayRequest |
