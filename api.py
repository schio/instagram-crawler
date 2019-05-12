from flask import Flask, request
from flask_restful import Resource, Api
import menew_crawling_info

app = Flask(__name__)
api = Api(app)

food_names = {}

class GetFoodName(Resource):    
    def put(self):

        food_name = request.form['data']
        urls = menew_crawling_info.getFoodImgAtInstagram(food_name)
        print('---------------------')
        return {'food' : urls}

api.add_resource(GetFoodName, '/foodName')

if __name__ == '__main__':
    print('app run')
    app.run(host='0.0.0.0',debug=True)
