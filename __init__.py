from flask import Flask
from flask_restful import Api, Resource
from flask import send_file
from handleColor import *
from makeGraph import makeGraph

app = Flask(__name__)
api = Api(app)


class RequestColor(Resource):
    def get(self):
        return {"color": requestColor()}

class GetBestFit(Resource):
    def get(self, r, g, b):
        return {"color": requestBestFit((r, g, b))}

class LearnColor(Resource):
    def post(self, r, g, b, color):
        learnColor(color, (r, g, b))
        return {"response": 200}

class GetGraph(Resource):
    def get(self):
        makeGraph()
        return send_file("graph.png")


api.add_resource(RequestColor, "/requestColor")
api.add_resource(GetGraph, "/graph.png")
api.add_resource(GetBestFit, "/getBestFit/<int:r>/<int:g>/<int:b>")
api.add_resource(LearnColor, "/learnColor/<int:r>/<int:g>/<int:b>/<string:color>")
if __name__ == "__main__":
    app.run(debug=False)