#!/usr/bin/env python

import pywapi

google_result = pywapi.get_weather_from_google('10001')
yahoo_result = pywapi.get_weather_from_yahoo('10001')
noaa_result = pywapi.get_weather_from_noaa('KJFK')

print("Google says: It is " + google_result['current_conditions']['condition'].lower() + " and " + google_result['current_conditions']['temp_c'] + "C now in New York.")

print("Yahoo says: It is " + yahoo_result['condition']['text'].lower() + " and " + yahoo_result['condition']['temp'] + "C now in New York.")

print("NOAA says: It is " + noaa_result['weather'].lower() + " and " + noaa_result['temp_c'] + "C now in New York.")
