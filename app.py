from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

messages = []

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', messages=messages)

@app.route('/message', methods=['POST'])
def new_message():
    message = request.form['message']
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    new_message = {'message': message, 'ts': now}
    messages.append(new_message)
    return 'success'

app.run(port=3000, debug=True, host='0.0.0.0')
