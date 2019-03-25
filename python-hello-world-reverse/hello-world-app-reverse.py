import sys, requests, json
from flask import Flask,jsonify

#Constructing the URL from arguments
url = "http://" + sys.argv[1] + ":" + sys.argv[2]

#Getting response from the URL
response = requests.get(url)

#Reversing the string through slicing
mesg_in_rev = json.loads(response.content)['message'][::-1]

#Defining the Flask app

app = Flask(__name__)
@app.route('/')
def json_rev_data():
    return jsonify(
        id=1,
        message=mesg_in_rev
    )

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
