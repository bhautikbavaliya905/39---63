import requests

url = input("Enter web page URL: ")

response = requests.get(url)

with open("webpage.html", "w", encoding="utf-8") as file:
    file.write(response.text)

print("Web page downloaded successfully.")
