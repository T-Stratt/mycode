#!/usr/bin/env python3

# Input what the wind speed is.
windspeed = int(input("What is the wind speed?"))
 
# Outputs the wind speed and category of the storm.
message = print("The speed is" + wind speed + " mph.The storm is a Cat")

# Outputs message for if not within any other parameters.
warning = "High winds and possible flooding."

if windspeed >= 157:
    message = message + ' 5.Catastrophic damage will occur.'
elif windspeed  <= 156 and >= 130:
    message = message + ' 4.Catastrophic damage will occur.'
elif windspeed <= 129 and >= 111:
    message = message + ' 3.Devastating damage will occur.'
elif windspeed <= 110 and >= 96:
    message = message + ' 2.Extremely dangerous winds will cause extensive damage.'
elif windspeed <= 95 and >= 74:
    message = message + ' 1.Very dangerous winds will produce some damage.'
else:
    warning = 'High winds and possible flooding.'
print(message)

