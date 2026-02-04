## dealCards.py
# Author Cathal Redmond Date 4 Feb 2026
# this assignment is an excercise to cinteract with an API that simulates dealing a deck of cards to players. 

# imports
import requests
import csv

#Create an array called retrieveTags that will store all the names of the tags we want to retrieve.
retrieveTags = ['success', 
                'deck_id',
                'shuffled',  
                'remaining'
                ]

# define the variables
url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
page = requests.get(url)

# read the content of the page and parse its content into variables using a for loop to loop through the retrieveTags array and store the values in a list called dataList.
data = page.json()
dataList = []
for retrieveTag in retrieveTags:
    dataList.append(data[retrieveTag])  

#print the elements of the dataList and retrieve tags as a matched set
#print("Data List:", list(zip(retrieveTags, dataList)))

# return deck_id to use in the next API call
deck_id = data['deck_id']
#print("Deck ID:", deck_id)

# pull 2 cards from the deck using the deck_id and store the values in a list called cardDataList
deckPull = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=2"
cardPage = requests.get(deckPull)
cardData = cardPage.json()
cardDataList = []
for card in cardData['cards']:
    cardDataList.append({
        'code': card['code'],
        'image': card['image'],
        'value': card['value'],
        'suit': card['suit']
    })  

# print suit and card value for each card from the card data list and remaining quantity of cards in the deck
for card in cardDataList:
    print(f"Card: {card['value']} of {card['suit']}")
print("Remaining Cards in Deck:", cardData['remaining'])

# check if the 2 cards are a pair, or same suit, and print the result
if cardDataList[0]['value'] == cardDataList[1]['value']:
    print("The cards are a pair.")
elif cardDataList[0]['suit'] == cardDataList[1]['suit']:
    print("The cards are of the same suit.")
else:
    print("The cards are different in both value and suit.")

