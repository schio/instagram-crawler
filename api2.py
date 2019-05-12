from flask import Flask, jsonify, request
from multiprocessing import Value
import menew_crawling_info
import dbWriter
import json
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={
  r"/v1/*": {"origin": "*"},
  r"/api/*": {"origin": "*"},
  r"/getFoodImg/*": {"origin": "*"},
  r"/reView/*": {"origin": "*"}
})
@app.route('/getFoodImg', methods=['PUT'])
def update():
    food_names_dict = request.json
    url = {}
    sourceFoodName = food_names_dict['sourceFoodName']
       
    urls = menew_crawling_info.getFoodImgAtInstagram(sourceFoodName)

    food_names_dict['summary1'] = "temp1"
    food_names_dict['about'] = "temp2"
    food_names_dict['summary2'] = "temp3"
    food_names_dict['urls'] = urls
    
    url = json.loads(urls)
    dbWriter.food(food_names_dict)
    # url = json.loads(url)
    return jsonify(url)

# @app.route('/reView/<string:body>', methods=['POST'])
# def update():
#     # review = request.json

#     print('-----------')
#     print(type(body))
#     print(len(body))
#     print(body)
#     print('-----------')
#     # urls = menew_crawling_info.getFoodImgAtInstagram(sourceFoodName)

#     # food_names_dict['summary1'] = "temp1"
#     # food_names_dict['about'] = "temp2"
#     # food_names_dict['summary2'] = "temp3"
#     # food_names_dict['urls'] = urls
    
#     # url['urls'] = urls
#     # dbWriter.food(food_names_dict)

#     return jsonify(url)


if __name__ == '__main__':
    print('app run')
    app.run(host='0.0.0.0',debug=True)