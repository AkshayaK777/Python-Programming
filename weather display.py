def display_weather(city_data):
    print(f"\n--- Weather Report: {city_data['name']} ---")
    print(f"Condition: {city_data['sky']}")
    print(f"Temperature: {city_data['temp']}°C")
    print(f"Humidity: {city_data['humidity']}%")
    print("-" * 30)

def main():
    mock_database = {
        "london": {"name": "London", "sky": "Cloudy", "temp": 15, "humidity": 80},
        "new york": {"name": "New York", "sky": "Sunny", "temp": 22, "humidity": 45},
        "mumbai": {"name": "Mumbai", "sky": "Humid", "temp": 32, "humidity": 90}
    }

    city = input("Enter city name (London/New York/Mumbai): ").lower()
    
    if city in mock_database:
        display_weather(mock_database[city])
    else:
        print("City not found in local database.")

if __name__ == "__main__":
    main()