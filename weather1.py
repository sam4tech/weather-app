# import required modules
import requests, json
from configparser import ConfigParser
from sys import argv

# Enter your API key here
#api_key="8198913108c112f50ff34a9feeafe3b9"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"


def _get_api_key():
    """Fetch the API key from your configuration file.

    Expects a configuration file named "secrets.ini" with structure:

        [openweather]
        api_key=<YOUR-OPENWEATHER-API-KEY>
    """
    config = ConfigParser()
    config.read("secrets.ini")
    return config["openweather"]["api_key"]

api_key = _get_api_key()

# Give city name
def weather_report(city):
    # complete_url variable to store
    # complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric"

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
        current_temperature = y["temp"]

        # print values
        #print(complete_url)
        
        #print(f'City:^20' " Temperature (in Celcius) = " + str(current_temperature))
        print(f'{city:^20}' + "|" + f'{str(current_temperature):^20}')

        return 0
    else:
        print(" City Not Found ")
        

#city_name = input("Enter city name : ")
#city_list = ['Prague', 'Milan', 'Paris']
# iterate a list using range()
#for i in range(len(city_list)):
#    print(weather_report(city_list[i]))

print("\t"+ "CITY " + "\t    |" + "\t TEMPERATURE (in Celcius) " + "\n")


#weather_report("Prague")
#weather_report("Milan")
#weather_report("Paris")
#print(weather_report(city_list[i]))
for i in range(len(argv)):
    if i>0 :
        final_temperature = weather_report(argv[i])
        print(final_temperature)
   
#print(argv[2])