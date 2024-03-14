import flask
from flask import request, jsonify

x = 0
y = 0
z = 0
a = 0

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>API</h1>'''


@app.route('/api/resources/rgb', methods=['GET', 'POST'])
def handleRGB():
    global x, y, z, a
    if request.method == 'GET':
        return jsonify({"x": x, "y": y, "z": z, "a": a})
    
    elif request.method == 'POST':
        params = request.json
        x = int(params.get('x'))
        y = int(params.get('y'))
        z = int(params.get('z'))
        a = x + y
        print(f'Response:\n\tx: {x}, y: {y}, z: {z}, a: {a}')
        return "Data received!"
    
    else:
        print("something went horribly wrong!")
        return


@app.errorhandler(404)
def page_not_found(e):
    return 404

app.run(host='0.0.0.0')