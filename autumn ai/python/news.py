import requests 
from ss import *

api_address="https://newsapi.org/v2/top-headlines?country=in&apiKey=b8348b6c977f48bc85277ecfddeb277a"
json_data = requests.get(api_address).json()

ar=[]

def news():
    for i in range(2):
        ar.append("Number"+ str(i+1) + ", " + json_data["articles"][i]["title"]+".")

    return ar

arr = news()