# ###### Weather App ######

# =================================
# Importing modules
import json
import requests
import tkinter as tk
# =================================
# Configuring our window

root = tk.Tk()
root.title("Weather App")
root.geometry("600x100")
# =================================


def zip_lookup():

    try:
        api_key = "Put your api here"
        api_request = requests.get(f"http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zip_entry.get()}&distance=25&API_KEY={api_key}")
        api = json.loads(api_request.content)

        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == "USG":
            weather_color = "#ff9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"

        label = tk.Label(root, text=f"{city} air quality {quality} {category}", font=("Helvetica", 20), background=weather_color)
        label.grid(row=1, column=0, columnspan=2)
        root.configure(background=weather_color)
    except Exception as e:
        api = "Error..."


zip_entry = tk.Entry(root)
zip_entry.grid(row=0, column=0, sticky=tk.W + tk.E + tk.N + tk.S)

zip_button = tk.Button(root, text="Lookup Zipcode", command=zip_lookup)
zip_button.grid(row=0, column=1, sticky=tk.W + tk.E + tk.N + tk.S)
# =================================
root.mainloop()
