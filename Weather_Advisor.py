#!/usr/bin/env python3

# Asks the user the weather.
weather = input("What is the weather in your area today?")

# Asks the user the temperature and creates it as an integer.
temp = int(input("What is the temperature in your area today?"))

# Message reads the user input of 'weather' + appended variables.
message = "Today the weather is " + weather + ". We recommend"

# Allows input of either upper or lower case and appends new message based on the previous parameters in place.

if weather.lower() == "sunny" and temp >= 100:
    message = message + ' drink water and put on sunscreen.'
elif weather.lower() == "sunny" and temp >= 70 and temp <= 99:
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

# Will print complete message with all variables, integers, and appendages in place.

print(message)

