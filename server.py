# 3ші тапсырма
"""
Мен бұл жерде API көтеру үшін Flask фреймворгін қолдандым
"""


import json
from flask import Flask, request
from json_to_xml import j_2_xml


app = Flask(__name__)

# POST методын қабылдайтын хэндлер
@app.route('/post_json', methods=['POST'])
def handle():
    json_data = request.json
    data = json.dumps(json_data)
    # мына жерде from json_to_xml import j_2_xml шықырып конвертация жасаймыз
    res = j_2_xml(data)
    print(res)
    return res

if __name__ == "__main__":
    app.run(debug=True)
    