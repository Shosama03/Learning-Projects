import requests

API_Key = "bfa205cb96c994adf1093ddff8ff00c7"

city = input("Enter a city: ")
base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}&units=metric"

weather_data = requests.get(base_url).json()

if weather_data.get("cod") != 200:
    print("❌ Error:", weather_data.get("message", "Something went wrong"))
else:
    main = weather_data["main"]
    weather = weather_data["weather"][0]

    print(f"\n✅ Weather Report for {city.capitalize()}")
    print("-" * 35)
    print(f"🌡 Temperature: {main['temp']} °C")
    print(f"🤒 Feels Like: {main['feels_like']} °C")
    print(f"☁️ Condition: {weather['description'].capitalize()}")
    print(f"💧 Humidity: {main['humidity']}%")
    print(f"💨 Pressure: {main['pressure']} hPa")
    print(f"🌍 Country: {weather_data['sys']['country']}")
    print(f"📍 Coordinates: {weather_data['coord']}")