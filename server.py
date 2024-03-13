import flask
from flask import request, jsonify
import random

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>API</h1>'''


@app.route('/api/resources/rgb', methods=['GET'])
def handleRGB():
    # if request.method == 'GET':
    red = random.randint(0,255)
    blue = random.randint(0,255)
    green = random.randint(0,255)
    return jsonify({"r": red, "g": green, "b": blue})
    
    # elif request.method == 'POST':
    #     params = request.json
    #     # Ensure that all values are present and convert to integers
    #     red = int(params.get('red', red))
    #     blue = int(params.get('blue', blue))
    #     green = int(params.get('green', green))
    #     return "data added to db"
    
    # else:
    #     print("something went horribly wrong!")
    #     return


@app.errorhandler(404)
def page_not_found(e):
    return 404

app.run(debug=True, use_reloader = False)