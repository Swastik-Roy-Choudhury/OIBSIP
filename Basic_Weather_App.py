import requests

# Function to get weather data for a specified city using the OpenWeatherMap API
def get_weather(city, api_key):
    # OpenWeatherMap API URL
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    # Make the API request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error: Unable to fetch weather data")
        return None

# Function to display weather data
def display_weather(data):
    if data:
        city = data['name']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']

        # Display the weather information
        print(f"\nWeather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {description.capitalize()}")
    else:
        print("Error: No weather data available.")

# Main function to prompt user for city and display weather
def weather_app():
    city = input("Enter the name of the city: ")

    # Provided API key
    api_key = "3bb9ebf8f59f055b1d13b54c394b03fa"

    # Fetch weather data for the specified city
    weather_data = get_weather(city, api_key)

    # Display fetched weather data
    display_weather(weather_data)

# Run the weather app
weather_app()
