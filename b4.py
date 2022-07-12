import requests
from bs4 import BeautifulSoup

url = "https://www.goszakup.gov.kz/ru/registry/rqc"

r = requests.get(url=url, verify=False)
print(r.text)