import requests
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox

# OpenWeatherMap API Key
API_KEY = "your_openweathermap_api_key"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    """
    Fetches weather data from OpenWeatherMap API.
    :param city_name: Name of the city to fetch weather for.
    :return: Dictionary containing weather details or None if an error occurs.
    """
    try:
        params = {
            "q": city_name,
            "appid": API_KEY,
            "units": "metric"  # Celsius
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_data = {
                "City": data["name"],
                "Temperature": f"{data['main']['temp']} °C",
                "Humidity": f"{data['main']['humidity']}%",
                "Wind Speed": f"{data['wind']['speed']} m/s",
                "Weather": data["weather"][0]["description"].capitalize()
            }
            return weather_data
        else:
            messagebox.showerror("Error", f"City not found: {data.get('message', 'Unknown error')}")
            return None
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch data: {str(e)}")
        return None

def display_weather():
    """
    Displays the weather information on the GUI.
    """
    city = city_var.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name!")
        return

    weather = get_weather(city)
    if weather:
        result_var.set(
            f"City: {weather['City']}\n"
            f"Temperature: {weather['Temperature']}\n"
            f"Humidity: {weather['Humidity']}\n"
            f"Wind Speed: {weather['Wind Speed']}\n"
            f"Weather: {weather['Weather']}"
        )

# GUI Setup
root = Tk()
root.title("Weather Information Application")
root.geometry("400x300")

# Input Section
Label(root, text="Enter City Name:", font=("Arial", 12)).pack(pady=10)
city_var = StringVar()
Entry(root, textvariable=city_var, width=30, font=("Arial", 12)).pack()

# Search Button
Button(root, text="Get Weather", command=display_weather, font=("Arial", 12), bg="blue", fg="white").pack(pady=10)

# Result Display
result_var = StringVar()
Label(root, textvariable=result_var, font=("Arial", 12), justify="left", wraplength=300).pack(pady=20)

# Main Loop
root.mainloop()
