from flask import Flask
from flask_restplus import Api, Resource


# something
app = Flask(__name__)
api = Api(app)

@api.route("/hello")
class HelloWorld(Resource):
    def get(self):
        return {'hello' : 'world1'}

# some comment added
if __name__ == '__main__':
    # app.config()
    app.run(debug=True)

