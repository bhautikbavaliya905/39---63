import requests

url = input("Enter web page URL: ")

response = requests.get(url)

print(response.text)
