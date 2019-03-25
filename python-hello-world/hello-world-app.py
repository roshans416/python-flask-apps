from flask import Flask,jsonify

#Defining Flask app
app = Flask(__name__)
@app.route('/')

#Preparing the response data in JSON format
def json_data():
    return jsonify(
        id=1,
        message="Hello World"
    )

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
