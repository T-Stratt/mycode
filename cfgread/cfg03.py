#!/usr/bin/env python3
## create file object in "r"ead mode
configfile= open("/home/student/mycode/cfgread/vlanconfig.cfg", "r")

    ## readlines() creates a list by reading target
    ## file line by line

configlist = configfile.readlines()
    
print(configlist)

Counter = 0

# Reading from file 

for i in configlist:
     Counter += 1

print("This is the number of lines in the file")
print(Counter)

configfile.close()
