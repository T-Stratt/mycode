#!/usr/bin/env python3

# Input what the wind speed is.
windspeed = int(input("What is the wind speed?")) 
 
# Outputs the wind speed and category of the storm.
message ="The speed is " + str(windspeed) + " mph. "

# Outputs message for if not within any other parameters.
warning = "High winds and possible flooding."

if windspeed >= 157:
    message = message + ' The storm is a Cat 5.Catastrophic damage will occur.'
elif windspeed >= 130:
    message = message + ' The storm is a Cat 4.Catastrophic damage will occur.'
elif windspeed >= 111:
    message = message + ' The storm is a Cat 3.Devastating damage will occur.'
elif windspeed >= 96:
    message = message + ' The storm is a Cat 2.Extremely dangerous winds will cause extensive damage.'
elif windspeed >= 74:
    message = message + ' The storm is a Cat 1.Very dangerous winds will produce some damage.'
else:
    warning = 'High winds and possible flooding.'

print(message + warning)

