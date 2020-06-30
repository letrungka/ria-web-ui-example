from flask import Flask
from flask import render_template, request, jsonify
import requests
import json
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('app.html')


@app.route('/intents',methods = ['POST'])

def post_intent():
    if request.method == 'POST':

        data = request.json

        inputText = data['inputText']
        userId = data['userId']

        print("Posting: ",inputText  + " with userID : "+ userId + " to API GW"  )

        url = ''
        headers={"x-api-key" : ""}
        payload = {
            'userId': int(userId),
            'inputText': inputText
        }

        r = requests.post(url, data = json.dumps(payload), headers = headers )
        print("r: ",r)
        return (r.text)

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)