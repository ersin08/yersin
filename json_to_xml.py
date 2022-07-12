from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson

# get the xml from a json string

# json-ды xml-ге конвертация жасайтын функция
def j_2_xml(json_: str):
    data = readfromstring(json_)
    return json2xml.Json2xml(data).to_xml()