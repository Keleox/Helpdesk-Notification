#Import libraries
import sys
import json
from freshpy import FreshPy
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

#Connect to the FreshService API with Freshpy
fresh = FreshPy(domain='farnsworthgroup.freshservice.com', api_key = apiValue)

#checkTicket function - Checks for new tickets
def checkTicket():
        try:
            ticket_data = fresh.tickets.get_ticket(ticket_number = jsonData['Latest Ticket'])
            jsonData['Latest Ticket'] = jsonData['Latest Ticket']+1
            with open( "data\\data.json" , "w" ) as write:
                json.dump( jsonData , write)
            return True
        except:
            return False

#If multiple tickets have come in in the past minute, updates values to include those
if checkTicket() == True:
    playsound('data\\'+soundFile)
    sleep(.5)
    while checkTicket() == True:
        pass
