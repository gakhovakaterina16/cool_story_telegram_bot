import requests
url = 'http://numbersapi.com/'
params = {
    'number': 5,
    'type': 'trivia',
}
result = requests.get(url, params=params)
print(result)
