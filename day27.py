import requests

api_key = "YOUR_API_KEY"
city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]

    print(f"Weather in {city}:")
    print("Temperature:", temperature, "°C")
    print("Condition:", description)
else:
    print("City not found ❌")
