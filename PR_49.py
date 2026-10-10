import requests

url = input("Enter image URL: ")

response = requests.get(url)

with open("image.jpg", "wb") as file:
    file.write(response.content)

print("Image downloaded successfully.")

