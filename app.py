import requests
def fetch_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    joke = response.json()
    return joke
    
joke = fetch_joke()
print(joke)