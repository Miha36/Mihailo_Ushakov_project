import json
import os
from datetime import datetime

import requests
HISTORY_FILE = "history.json"

WEATHER_CODES = {
    0: "Clear sky",
    1: "Mostly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Icy fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Heavy drizzle",
    61: "Light rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Light snow",
    73: "Moderate snow",
    75: "Heavy snow",
    80: "Rain showers",
    95: "Thunderstorm",
}
def get_weather(city_name):
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_params = {"name": city_name, "count": 1}
    geo_response = requests.get(geo_url, params=geo_params, timeout=10)
    geo_response.raise_for_status()
    geo_data = geo_response.json()
    results = geo_data.get("results")
    if not results:
        return None
    place = results[0]
    latitude = place["latitude"]
    longitude = place["longitude"]
    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
        "timezone": "auto",
    }
    weather_response = requests.get(weather_url, params=weather_params, timeout=10)
    weather_response.raise_for_status()
    current = weather_response.json()["current"]
    code = current.get("weather_code", -1)
    description = WEATHER_CODES.get(code, "Unknown")
    return {
        "city": place["name"],
        "country": place.get("country", ""),
        "temperature": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "wind_speed": current["wind_speed_10m"],
        "description": description,
    }
def get_exchange_rate(base_currency, target_currency):
    url = f"https://open.er-api.com/v6/latest/{base_currency}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    if data.get("result") != "success":
        return None
    rates = data.get("rates", {})
    return rates.get(target_currency)
def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []
def save_to_history(entry_type, summary):
    history = load_history()
    history.append(
        {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": entry_type,
            "summary": summary,
        }
    )
    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, ensure_ascii=False, indent=2)
def show_history():
    history = load_history()
    if not history:
        print("History is empty.")
        return
    print("\n--- Search History ---")
    for index, entry in enumerate(history, start=1):
        print(f"{index}. [{entry['timestamp']}] ({entry['type']}) {entry['summary']}")
    print("-----------------------\n")
def handle_weather_choice():
    city_name = input("Enter city name: ").strip()
    if not city_name:
        print("City name cannot be empty.")
        return
    try:
        weather = get_weather(city_name)
    except requests.RequestException:
        print("Could not connect to the weather server. Check your internet connection.")
        return
    if weather is None:
        print(f"City '{city_name}' was not found. Check the spelling.")
        return
    print(f"\nWeather in {weather['city']}, {weather['country']}:")
    print(f"  Temperature: {weather['temperature']} C")
    print(f"  Humidity: {weather['humidity']}%")
    print(f"  Wind speed: {weather['wind_speed']} km/h")
    print(f"  Conditions: {weather['description']}")
    summary = f"{weather['city']}, {weather['country']}: {weather['temperature']} C, {weather['description']}"
    save_to_history("weather", summary)
def handle_currency_choice():
    amount_text = input("Enter amount: ").strip()
    try:
        amount = float(amount_text)
    except ValueError:
        print("Amount must be a number, for example: 100 or 99.5")
        return
    base_currency = input("From currency (e.g. USD): ").strip().upper()
    target_currency = input("To currency (e.g. EUR): ").strip().upper()
    if not base_currency or not target_currency:
        print("Currency code cannot be empty.")
        return
    try:
        rate = get_exchange_rate(base_currency, target_currency)
    except requests.RequestException:
        print("Could not connect to the currency server. Check your internet connection.")
        return
    if rate is None:
        print("One of the currency codes was not found. Try codes like USD, EUR, GBP.")
        return
    converted_amount = round(amount * rate, 2)
    print(f"\n{amount} {base_currency} = {converted_amount} {target_currency}")
    print(f"(rate: 1 {base_currency} = {rate} {target_currency})")
    summary = f"{amount} {base_currency} -> {converted_amount} {target_currency}"
    save_to_history("currency", summary)
def show_menu():
    print("\n=== Weather and Currency Checker ===")
    print("1. Check weather in a city")
    print("2. Convert currency")
    print("3. Show search history")
    print("4. Exit")
def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            handle_weather_choice()
        elif choice == "2":
            handle_currency_choice()
        elif choice == "3":
            show_history()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    main()