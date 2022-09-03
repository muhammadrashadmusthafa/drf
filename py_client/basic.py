import requests

endpoint = "https://httpbin.org"

# endpoint = "https://httpbin.org/anything"
get_response = requests.get(endpoint)

# get_response = requests.get(endpoint, json={'query': 'hello world'})
# get_response = requests.get(endpoint, data={'query': 'hello world'})

print(get_response.text)
# print(get_response.json())
print(get_response.status_code)