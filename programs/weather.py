from tkinter import *
from PIL import ImageTk,Image
import requests
import json
import os

def weather_launch():
    sun_icon_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'images', 'sun.ico'))
    print(sun_icon_path)

    weather_window = Toplevel()
    weather_window.title('Weather App')
    weather_window.iconbitmap(sun_icon_path)
    weather_window.geometry("500x500")

    def zipLookup():
        #zip_label.get()
        #zipLabel = Label(weather_window, text=zip_label.get())
        #zipLabel.grid(row=1, column=0, columnspan=2)

        #
        try: 
            #variable for actual api request, DE92BBCF-1882-4BEC-85CD-64E56A2B75B2
            api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip_label.get() + "&distance=25&API_KEY=DE92BBCF-1882-4BEC-85CD-64E56A2B75B2")
            api = json.loads(api_request.content)

            #setting variables to display, pulling off API request
            city = api[0]['ReportingArea']
            quality = api[0]['AQI']
            category = api[0]['Category']['Name']

            #second api 0eb4aece1f694455a9324940211304
            api_request2 = requests.get("http://api.weatherapi.com/v1/current.json?key=0eb4aece1f694455a9324940211304&q=" + zip_label.get() + "&aqi=yes")
            api2 = json.loads(api_request2.content)

            city2 = api2['location']['name']
            quality2 = api2['current']['air_quality']['us-epa-index']
            condition2 = api2['current']['condition']['text']

            api_request3 = requests.get("https://api.weatherbit.io/v2.0/current/airquality?postal_code=" + zip_label.get() + "&key=79a5e0182ecd445aacd908e89d4b1cc0")
            api3 = json.loads(api_request3.content)

            city3 = api3['city_name']
            quality3 = api3['data'][0]['aqi']
            condition3 = api3['data'][0]['pm10']

            #setting hex color schemes
            if category == "Good":
                weather_color = "#0C0"
            elif category == "Moderate":
                weather_color = "#FFFF00"
            elif category == "Unhealthy for Sensitive Groups":
                weather_color = "#ff9900"
            elif category == "Unhealthy":
                weather_color = "#FF0000"
            elif category == "Very Unhealthy":
                weather_color = "#990066"
            elif category == "Hazardous":
                weather_color = "#660000"

            #graphic elements to display info from APIs
            weather_window.configure(background=weather_color)
            api1_label = Label(weather_window, text="City: " + city + "\nAir Quality: " + str(quality) + "\nCategory: " + category + "\n", font=("Helvetica", 20), background=weather_color)
            api2_label = Label(weather_window, text="City: " + city2 + "\nUS EPA Index: " + str(quality2) + "\nCurrent Condition: " + condition2 + "\n", font=("Helvetica", 20), background=weather_color)
            api3_label = Label(weather_window, text="City: " + city3 + "\nAQI: " + str(quality3) + "\npm10: " + str(condition3) + "\n", font=("Helvetica", 20), background=weather_color)

            api1_label.grid(row=2, column=0, columnspan=2, sticky='we')
            api2_label.grid(row=3, column=0, columnspan=2, sticky='we')
            api3_label.grid(row=4, column=0, columnspan=2, sticky='we')

        except Exception as e:
            api = "Error..."

    #graphic elements for ZIP entry
    display_label = Label(weather_window, text="Enter ZIP Below:")
    display_label.grid(row=0, column=0, sticky='we')
    #lookup ui variables / elements
    zip_label = Entry(weather_window)
    #needs sticky otherwise will leave remnants between switches
    zip_label.grid(row=1, column=0, sticky=W+E+N+S)

    zip_button = Button(weather_window, text="Submit", command=zipLookup)
    zip_button.grid(row=1, column=1, sticky=W+E+N+S)