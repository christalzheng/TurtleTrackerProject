#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: John Fay (john.fay@duke.edu)
# Date:   Fall 2023
#--------------------------------------------------------------

# Ask the user for a date, specifying the format
user_date = input("Enter a date (M/D/YYYY):")
#user_date = "7/3/2003"
#Create a variable pointing to the data file
file_name = './data/raw/sara.txt'

#Create a file object from the file
file_object = open(file_name,'r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()

#Pretend we read one line of data from the file
date_dict={}
location_dict = {}
for lineString in line_list:
    # Check if line is a data line
    if lineString[0] in ("#","u"):
        continue

    #Split the string into a list of data items
    lineData = lineString.split()

    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]

    if obs_lc in ("1","2","3"):
        date_dict[record_id] = obs_date
        location_dict[record_id] = (obs_lat,obs_lon)

        #Print the location of sara
        print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")

# list(location_dict.keys())[0]
# print (location_dict['20616'])
# print(date_dict['24719'])
# print(len(date_dict))
# Loop through all key, value pairs in the date_dictionary
keys = []
for key, value in date_dict.items():
    #See if the date (the value) matches the user date
    if value == user_date:
        keys.append(key)

# Report whether no keys were found
if len(keys) == 0:
    print(f"Sara was not located on {user_date}")
else:
    #Reveal locations for each key in matching_keys
    for key in keys:
        lat, lng = location_dict[key]
        print(f"On {user_date}, Sara the the turtle was seen at {lat}d Lat, {lng}d Lng.")

       