# 3-е задание
"""
Я использовал фреймворк Flask, чтобы протолкнуть сюда API.
"""


import json
from flask import Flask, request
from json_to_xml import j_2_xml


app = Flask(__name__)

# Обработчик, принимающий метод POST
@app.route('/post_json', methods=['POST'])
def handle():
    json_data = request.json
    data = json.dumps(json_data)
   # здесь мы будем конвертировать из json_to_xml import j_2_xml
    res = j_2_xml(data)
    print(res)
    return res

if __name__ == "__main__":
    app.run(debug=True)
    
