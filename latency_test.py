from flask import Flask
import requests
import time

app = Flask(__name__)

@app.route('/')
def index():
    start_time = time.time()
    response = requests.get('http://192.168.4.36:5000')
    end_time = time.time()
    latency = end_time - start_time
    return f'Latency: {latency} seconds'

if __name__ == '__main__':
    app.run()