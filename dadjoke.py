import requests
import json

def randjoke():
    dadurl = "https://icanhazdadjoke.com/"
    headers = {
        'Accept': 'application/json',
    }
    newjoke = requests.get(dadurl, headers=headers)
    # print(newjoke.text)
    jsondata = newjoke.json()
    print(jsondata['joke'])

def searchjoke(query): 
    headers = {
        'Accept': 'application/json',
    }
    params = {
        'term':  query,
        'limit': 20, 
    }
    search_joke=requests.get("https://icanhazdadjoke.com/search", headers=headers, params=params)
    jsondata2 = search_joke.json()
    if jsondata2["total_jokes"] > 0:
        jokes_dict = jsondata2['results']
        
        for x in range(len(jokes_dict)):
            dict = jokes_dict[x]
            print(dict['joke'])
    else:
        print("I guess there was no match for the subject you chose, please enter a different subject.")
        dadjoke()

def dadjoke():
    response = input("Please tell me what joke subject you are looking for. \nPressing Enter will give you a random joke:  ")
    print()
    if len(response) == 0:
        randjoke()
    else:
        searchjoke(response)

dadjoke()