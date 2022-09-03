import requests

endpoint = "http://localhost:8000/api/"

# endpoint = "https://httpbin.org/anything"
# get_response = requests.get(endpoint)

get_response = requests.get(endpoint, json={'query': 'hello world'})
# get_response = requests.get(endpoint, data={'query': 'hello world'})

print(get_response.text)
print(type(get_response.text))

print(get_response.json())
print(type(get_response.json()))

print(get_response.json()['message'])
print(get_response.status_code)