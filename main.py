from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Hellocall(Resource):
    def get(self,name,number):
        return({'Name':name,'Age':number})

api.add_resource(Hellocall,"/Helloworld/<string:name>/<int:number>")

if __name__ == "__main__":
    app.run(debug=True)




