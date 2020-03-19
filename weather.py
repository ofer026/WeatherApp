import pyautogui
import requests, json
import time
import math


api_key = "0c087fcad3f167b67ee4c61e9792e82e"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

def set_app():
    # Give city name
    #city_name = input("Enter city name : ")
    global city_name
    city_name = pyautogui.prompt(title='Enter City', text='Enter a city name or a postal code that you want to get '
                                                          'weather reports about')
    while True:
        try:
            global delay
            delay = int(pyautogui.prompt(text='Enter the delay that you want to be between the reports (In minutes)', default=60))
            break
        except ValueError: # for stings and floats as on (not that good)  TODO look if you can maybe keep it as one
            # TODO expcept and sperate between strings and floats in the except
            pyautogui.alert(text='Please enter a whole number')
        # except "ValueError: invalid literal for int() with base 10:" + delay: # not good
            # pyautogui.alert(text='Please enter a whole number') # not good
            # TODO Fix this (good excpet) and one excpet for folat and one for strings and maybe one for none
    delay = delay * 60
set_app()
# complete_url variable to store
# complete url address
# complete_url = base_url + "appid=" + api_key + "&q=" + city_name
while True:
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key
    # print(complete_url)
    # get method of requests module
    # return response object
    response = requests.get(complete_url)

    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()

    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":

        # store the value of "main"
        # key in variable y
        y = x["main"]


        # store the value corresponding
        # to the "temp" key of y
        current_temperature = float(y["temp"])
        current_temperature = math.floor(current_temperature - 273.15)# TODO decide how to make this show up
        str(current_temperature)

        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]

        # store the value corresponding
        # to the "humidity" key of y
        current_humidiy = y["humidity"]

        # store the value of "weather"
        # key in variable z
        z = x["weather"]

        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]
        ans = pyautogui.confirm(text=" Temperature = " +
          str(current_temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
          str(current_pressure) +
          "\n humidity (in percentage) = " +
          str(current_humidiy) +
          "\n description = " +
          str(weather_description), buttons=['Change City', 'OK'])
        if ans == 'Change City':
            set_app()

    else:
        pyautogui.alert(text='City Not Found!')
    time.sleep(delay)
