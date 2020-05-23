import urllib
import json
import ztk
import urllib.request 

class RequestException(Exception):
	# 请求连接异常类，用于抛出异常
	pass


class RestApi(object):
	# =====================
	# RestApi 的基础类
	# =====================

	def __init__(self, domain="api.zhetaoke.com", port=10001):
		# 初始化基础类
		# Args @param domain: 请求的域名或者ip
		#      @param port: 请求的端口
		self.__domain = domain
		self.__port = port
		self.__httpmethod = "GET"
		self._RestApi__name = ""
		if (ztk.get_default_app_info()):
			self.__app_key = ztk.get_default_app_info().appkey
			# sid为折淘客中淘客账号授权ID，可在调用API时再填写
			self.sid = ztk.get_default_app_info().sid

	def get_request_header(self):
		return {
			"content-type": "application/x-www-form-urlencoded;charset=UTF-8",
			"Cache-Control": "no-cache",
			"Connection": "Keep-Alive"
		}

	def set_app_info(self, appinfo):
		# 设置请求的app信息
		# @param appinfo: import top
		#                 appinfo top.appinfo(appkey,secret)
		self.__app_key = appinfo.appkey
		self.sid = appinfo.sid

	def getapiname(self):
		return ""

	def getMultipartParas(self):
		return []

	def getTranslateParas(self):
		return {}

	def _check_request(self):
		pass

	def get_response(self, timeout=30):
		#header = self.get_request_header()
		parameters = self.get_aplication_parameters()
		parameters["appkey"] = self.__app_key
		url = f'https://{self.__domain}:{self.__port}{self._RestApi__name}'

		response = urllib.request.urlopen(url, data=urllib.parse.urlencode(parameters).encode('utf-8'))
		
		if response.status is not 200:
			raise RequestException('invalid http status ' + str(response.status) + ',detail body:' + response.read().decode("utf-8"))

		result = response.read()
		
		try:
			jsonobj = json.loads(result)
			return jsonobj
		except:
			raise RequestException("折淘客返回值异常 - " + result.decode("utf-8"))

	def get_aplication_parameters(self):
		application_parameter = {}
		for key, value in self.__dict__.items():
			if not key.startswith("__") and not key.startswith("_RestApi__") and value is not None:
				if (key.startswith("_")):
					application_parameter[key[1:]] = value
				else:
					application_parameter[key] = value
		return application_parameter


class RestApi2(RestApi):
	# =====================
	# 需要进行二次请求的RestApi
	# 首次请求折淘客会返回一个已签名的url，需要再次请求该url
	# =====================
	def get_response(self, timeout=30):
		
		jsonobj = super().get_response()
		url = jsonobj["url"]

		response = urllib.request.urlopen(url)

		if response.status is not 200:
			raise RequestException('invalid http status ' + str(response.status) + ',detail body:' + response.read().decode("utf-8"))
		result = response.read()

		try:
			jsonobj = json.loads(result)
			return jsonobj
		except:
			raise RequestException("淘宝联盟返回值异常 - " + result.decode("utf-8"))