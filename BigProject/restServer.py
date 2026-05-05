## restServer.py
## Author Cathal Redmond
## Data 05 May 2026
# This is the main REST server file for the big project for Web services and Applications coursework.

# imports
from flask import Flask, request, jsonify
import requests

# create the Flask app
app = Flask(__name__)
# define the route for the REST API
@app.route('/api/data', methods=['POST'])
def receive_data():
    # get the JSON data from the request
    data = request.get_json()
    # print the received data to the console for testing
    print("Received data:", data)
    # return a response to the client
    return jsonify({"message": "Data received successfully!"}), 200 
# run the Flask app
if __name__ == '__main__':
    app.run(debug=True) 


