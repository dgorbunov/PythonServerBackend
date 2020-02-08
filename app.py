from pymongo import MongoClient
from flask import Flask, render_template, request
import datetime


app = Flask(__name__)

client = MongoClient("mongodb+srv://admin:admin@cluster0-clvxi.mongodb.net/test?retryWrites=true&w=majority")
db = client['blueprint2020']
messages = db['messages']

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', messages=messages.find({})) #renders all messages

@app.route('/message', methods=['POST'])
def new_message():
    print(request.form)
    message = request.form['message']
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    new_object = {'message':message, 'ts': now}
    messages.insert_one(new_object)
    return 'success'

app.run(port=3000, debug=True, host='0.0.0.0')
