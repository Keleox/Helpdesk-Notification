import requests
import json
import sys
from playsound import playsound
from time import sleep

#Get data from JSON file
try:
    with open('data\\data.json', 'r') as jsonFile:
        jsonData = json.load(jsonFile)
        global apiValue
        global soundFile
        apiValue = jsonData['API Key']
        soundFile = jsonData['Sound File']
except:
    print("Error getting data from JSON")
    sys.exit()


#Define Variables
headers = {'Content-Type': 'application/json',}



#Check if new ticket has been submitted
def checkTicket():
        try:
            url = 'https://farnsworthgroup.freshservice.com/api/v2/tickets/' + str(jsonData['Latest Ticket'])
            response = requests.get(url, headers=headers, auth=('mJDxpebZFMg69LOicG', 'X'))
            if response.status_code != 200:
                return False
            else:
                jsonData['Latest Ticket'] = jsonData['Latest Ticket']+1
                with open( "data\\data.json" , "w" ) as write:
                    json.dump( jsonData , write)
                return True
        except Exception as e:
            print(e)



#If multiple tickets have come in in the past minute, updates values to include those
if checkTicket() == True:
    playsound('data\\'+soundFile)
    sleep(.5)
    while checkTicket() == True:
        pass
