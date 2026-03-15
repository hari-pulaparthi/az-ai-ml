# Python Program: Simple Weather API Fetcher 

import requests

def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,  # Replace with your actual API key
        'units': 'metric'
    }

    try:
        reponse = requests.get(base_url, params=params)
        reponse.raise_for_status()  # Check for HTTP errors for bad responses (4XX or 5XX)
        data = reponse.json()
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        print(f"Weather in {city}: {temperature}°C, {description}")
    except requests.exceptions.HTTPError: 
        print("City not found or API error.") 
    except requests.exceptions.RequestException as e: 
        print(f"Network error: {e}") 

if __name__ == "__main__":
    api_key = "86d6b45ffcaa9719eff6c7075f8c97dd"
    city = input("Enter city name: ").strip()
    get_weather(city, api_key)


    
