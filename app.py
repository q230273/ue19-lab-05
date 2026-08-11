import requests

url = "https://v2.jokeapi.dev/joke/Any"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    if data["type"] == "single":
        print(data["joke"])
    else:
        print(data["setup"])
        print(data["delivery"])
else:
    print("Erreur lors de la récupération de la blague.")
