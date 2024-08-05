import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,  
        'appid': api_key,
        'units': 'metric'  
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if data['cod'] != 200:
        return f"Error: {data['message']}"

    weather_info = {
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed'],
        'description': data['weather'][0]['description']
    }

    return weather_info

def display_weather(weather_info):
    if isinstance(weather_info, str):
        print(weather_info)
    else:
        print(f"Temperature: {weather_info['temperature']}°C")
        print(f"Humidity: {weather_info['humidity']}%")
        print(f"Wind Speed: {weather_info['wind_speed']} m/s")
        print(f"Description: {weather_info['description'].capitalize()}")

def main():
    api_key = "afd534a32da85d74611ed3dc6691e3f0"  
    location = input("Enter city name or zip code: ")
    weather_info = get_weather(api_key, location)
    display_weather(weather_info)

if __name__ == "__main__":
    main()
