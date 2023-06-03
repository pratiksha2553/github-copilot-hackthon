import requests

def get_weather(city):
    api_key = '46521d923283f2f31875eda70c26fefe'  # Replace with your OpenWeatherMap API key
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for unsuccessful requests
        weather_data = response.json()

        # Use Copilot suggestions for parsing and extracting relevant information
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']

        # Display the weather information
        print(f"Current weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description}")
    except requests.exceptions.RequestException as e:
        # Handle API request errors
        print(f"Error fetching weather data: {e}")

def gen_report(city):
    url = f'https://wttr.in/{city}'
    try:
        data = requests.get(url)
        report = data.text
    except:
        report = "Error occurred while generating report."
    print(report)

def main():
    print("\t\tWelcome to the Weather Forecaster!\n")
    print("Just enter the city you want the weather report for and click on the button! It's that simple!\n")

    city_name = input("Enter the name of the city: ")
    print("\n")

    get_weather(city_name)
    gen_report(city_name)

if __name__ == '__main__':
    main()
