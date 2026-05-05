## test.py
## Author Cathal Redmond
## Data 05 May 2026

# This test file will be used to develop the code for the big project for Web services and Applications coursework. 
# It will be used to test the functionality of the code as it is developed.

# imports
import requests

# define the functions for the test file

def getall():
    # This function will be used to test the GET request to the REST API
    response = requests.get('http://localhost:5000/api/data')
    print("GET response:", response.json())

def findbyid(id):
    # This function will be used to test the GET request to the REST API with an ID parameter
    response = requests.get(f'http://localhost:5000/api/data/{id}')
    print("GET by ID response:", response.json())

def create(book):
    # This function will be used to test the POST request to the REST API to create a new book
    response = requests.post('http://localhost:5000/api/data', json=book)
    print("POST response:", response.json())

def update(id, book):
    # This function will be used to test the PUT request to the REST API to update a book by ID
    response = requests.put(f'http://localhost:5000/api/data/{id}', json=book)
    print("PUT response:", response.json())

def delete(id):
    # This function will be used to test the DELETE request to the REST API to delete a book by ID
    response = requests.delete(f'http://localhost:5000/api/data/{id}')
    print("DELETE response:", response.json()) 

