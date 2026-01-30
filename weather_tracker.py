import requests
import time

def get_weather():
    # Coordinates for Jaipur
    lat = 26.91
    lon = 75.78
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=True"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if "current_weather" in data:
            temp = data["current_weather"]["temperature"]
            print(f"Success! The current temperature in Jaipur is {temp}°C")
        else:
            print("Error: Could not find weather data in the response.")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Cloud-Native Weather Tracker started...")
    # This loop keeps the script running indefinitely
    while True:
        get_weather()
        
        # Wait for 30 minutes (1800 seconds) before checking again
        print("Next update in 30 minutes. Sleeping...")
        time.sleep(1800)