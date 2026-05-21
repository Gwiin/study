# ex12_flask_simple.py

# pip install flask
from flask import Flask

app = Flask(__name__)

# http://127.0.0.1:5000/
@app.route('/') 
def home():
    return "Wow!"

# # http://127.0.0.1:5000/login
# @app.route('/') 
# def home():
#     return "Wow!"

# http://127.0.0.1:5000/light_sensors
@app.route('/light_sensors') 
def light_sensors():
    return "센서1: 100<br>센서2: 90<br>센서3: 105<br>"

if __name__ == "__main__":
    app.run(host = "163.152.213.111", port = 5000)
