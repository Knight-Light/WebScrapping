import requests
import urllib3
urllib3.disable_warnings()

def fetch(a, path):
    r = requests.get(a, verify=False)
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)
        f.close()

url = "https://main.sci.gov.in/causelist"

fetch(url, "DataCollected.html")
