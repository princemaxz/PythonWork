import requests
from dotenv import load_dotenv
from pprint import pprint
import os

load_dotenv()


def get_current_weather():
    print("\n****Get Current Weather Condition****\n")

    city = input("\nPlease Enter a City Name:\n")

    request_url = f"https://api.openweathermap.org/data/3.0/onecall?appid={os.getenv('API_KEY')}&q={city}&units=imperial"

    # print(request_url)

    weather_data = requests.get(request_url).json()
    # pprint(weather_data)

    print(f"\nThe current Weather for {weather_data['name']}")
    print(f"\nThe current Temp {weather_data['main']['temp']}")
    print(
        f"\nFeels like {weather_data['main']['feels_like']} and {weather_data['weather'][0]['description']}."
    )


if __name__ == "__main__":
    get_current_weather()
