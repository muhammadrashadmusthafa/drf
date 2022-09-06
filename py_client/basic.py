import requests

endpoint = "http://localhost:8000/api/"

# endpoint = "https://httpbin.org/anything"
# get_response = requests.get(endpoint)

get_response = requests.get(endpoint, json={"product_id": 123 }, params= {'abc': 123}) # HTTP Request
# print(get_response.text) # print raw text response
# print(get_response.status_code)

print(get_response.json())
