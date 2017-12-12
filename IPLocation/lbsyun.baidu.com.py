#coding:utf-8
import urllib2
import urllib
import hashlib
import json

WEB_API_AK = "1eElrf6apE4kEmSujp5rkQmjHdolGCU8"
WEB_API_SK = "EypHDmiefFORQ5Gr6BezA2ggHvhpcB42"

def baiduLocation(ip):
	host = "http://api.map.baidu.com"
	sn = calSN(ip)
	whole_url = "%s/location/ip?ip=%s&ak=%s&sn=%s" % (host, ip, WEB_API_AK, sn)
	response = urllib2.urlopen(whole_url)
	return response.read()

def calSN(ip):
	query_url = "/location/ip?ip=%s&ak=%s" % (ip, WEB_API_AK)
	encoded_url = urllib.quote(query_url, safe="/:=&?#+!$,;'@()*[]")
	raw_url = encoded_url + WEB_API_SK
	return hashlib.md5(urllib.quote_plus(raw_url)).hexdigest()

def loadIPs():
	lIP = []
	fo = open("IPs.txt", "r")
	for line in fo.readlines():
		lIP.append(line.strip())
	return lIP

# 淘宝公开接口会限制访问速度，不能频繁使用
def taobaoLocation(ip):
	whole_url = "http://ip.taobao.com/service/getIpInfo.php?ip=%s" % (ip)
	response = urllib2.urlopen(whole_url)
	return response.read()

def localLocation(ip):
	whole_url = "http://localhost/api/ipinfo/find?ip=%s" % (ip)
	response = urllib2.urlopen(whole_url)
	return response.read()

def main():
	lIP = loadIPs()
	for idx, ip in enumerate(lIP):
		# dLocation = json.loads(localLocation(ip))
		# if dLocation.get("country") != u"中国":
		# 	print("[%d] %s" % (idx, ip))
		# 	print(dLocation.get("country", "Unknown"))
		dLocation = json.loads(baiduLocation(ip))
		address = dLocation.get("address", "Unknown")
		if address.find("CN") == -1:
			dLocation = json.loads(taobaoLocation(ip))
			print("[%d] %s" % (idx, ip))
			print(dLocation["data"].get("country", "Unknown"))
		else:
			# print("[%d] %s" % (idx, ip))
			pass

if __name__ == '__main__':
	main()