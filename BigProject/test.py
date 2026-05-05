## test.py
## Author Cathal Redmond
## Data 05 May 2026

# This test file will be used to develop the code for the big project for Web services and Applications coursework. 
# It will be used to test the functionality of the code as it is developed.

# imports
from urllib import response

import requests

# define the functions for the test file
class BookDAO:
    # This class will be used to test the data access object for the books in the REST API
    def __init__(self):
        self.base_url = 'http://localhost:5000/api/data'

    def getall(self):
        # This function will be used to test the GET request to the REST API
        response = requests.get(self.base_url)
        print("GET response:", response.json())

    def findbyid(self, id):
        # This function will be used to test the GET request to the REST API with an ID parameter
        response = requests.get(f'http://localhost:5000/api/data/{id}')
        print("GET by ID response:", response.json())

    def create(self, book):
        # This function will be used to test the POST request to the REST API to create a new book
        response = requests.post(self.base_url, json=book)
        print("POST response:", response.json())

    def update(self, id, book):
        # This function will be used to test the PUT request to the REST API to update a book by ID
        response = requests.put(f'http://localhost:5000/api/data/{id}', json=book)
        print("PUT response:", response.json())

    def delete(self, id):
        # This function will be used to test the DELETE request to the REST API to delete a book by ID
        response = requests.delete(f'http://localhost:5000/api/data/{id}')
        print("DELETE response:", response.json()) 

