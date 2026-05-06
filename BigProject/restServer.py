## restServer.py
## Author Cathal Redmond
## Data 05 May 2026
# This is the main REST server file for the big project for Web services and Applications coursework.

# imports
from flask import Flask, request, jsonify
from bookDAO import BookDAO

# create the Flask app
app = Flask(__name__)
book_dao = BookDAO()

# define the route for the REST API
@app.route('/api/data', methods=['POST'])


# Welcome Message
@app.route('/')
def index():
    return "Welcome to the REST API for the Big Project!"


# getall
# curl http://127.0.0.1:5000/books
@app.route('/books', methods=['GET'])
def getall():
    return jsonify(book_dao.getAll())

# find by ID
# curl http://127.0.0.1:5000/books/1

@app.route('/books/<int:id>', methods=['GET'])
def findby(id):
    book = BookDAO.findByID(id)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

# create
# curl -X POST -H "Content-Type: application/json" -d '{"title": "New Book", "author": "Author Name"}' http://127.0.0.1:5000/books

@app.route('/books', methods=['POST'])
def create():
    # get the JSON data from the request
    jsonstring = request.json()
    book = {}
    book["title"] = jsonstring["title"]
    book["author"] = jsonstring["author"]
    book["price"] = jsonstring["price"]
    book["isbn"] = jsonstring["isbn"]
    bookDAO.create(jsonstring)

    # print the received data to the console for testing
    print("Received data:", jsonstring)
    # return a response to the client
    return jsonify({"message": "Data received successfully!"}), 200 


# run the Flask app
if __name__ == '__main__':
    app.run(debug=True) 


