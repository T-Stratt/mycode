#!/usr/bin/env python3

# Asks the user the weather in there area.
weather = input("What is the weather in your area today?")

# Asks the user the temperature and creates it as an integer.
temp = int(input("What is the temperature in your area today?"))

# Message reads the user input of 'weather' + appended variables.
message = "Today the weather is " + weather + ". We recommend"

# If input value is set of variables or integers then set result.
if weather.lower() == "sunny" and temp >= 70:
    message = message + ' going to the beach!'
elif weather.lower() == "partly cloudy" and temp >= 60:
    message = message + ' go out for a nice drive.'
elif weather.lower() == "rainy" and temp >= 50:
    message = message + ' grab an umbrella.'
elif weather.lower() == "cold" and temp >= 40:
    message = message + ' cuddle in bed with your loved one.'
elif weather.lower() == "snowy" and temp <= 32:
    message = message + ' go out and make a snowman.'
else:
    message = message + ' make the best of the the day.'
print(message)

