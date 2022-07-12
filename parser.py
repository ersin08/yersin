import requests
from bs4 import BeautifulSoup 
import certifi
def parse():
    
    URL ='https://www.goszakup.gov.kz/ru/registry/rqc?count_record=2000&page=1'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
        }
    response = requests.get(URL, headers=HEADERS,  verify='goszakup-gov-kz-chain.pem')
    soup=BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div',class_='table-responsive')
    comps = []

    for item in items:
        comps.append({
                'link': item.find('a').get('href')

            })
        for copm in comps:
            print(copm['link'])


parse()
