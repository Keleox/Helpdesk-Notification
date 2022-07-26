#Import libraries
import sys
from freshpy import FreshPy
from playsound import playsound
from time import sleep
from tendo import singleton

#Define Variable(s)
ticketUpdate = True

#Get API key and sound file name from variables.txt
try:
    with open('data\\variables.txt', 'r') as variableFile:
        global apiValue
        global soundFile
        apiValue = variableFile.readline()
        apiValue = apiValue.strip()
        soundFile = variableFile.readline()
        soundFile = soundFile.strip()
        variableFile.close()
except:
    print("Error: Error getting API key or sound file name")
    input()
    sys.exit()

#Connect to the FreshService API with Freshpy
fresh = FreshPy(domain='farnsworthgroup.freshservice.com', api_key = apiValue)

#Prevents duplicate instances of the program from running.
try:
    me = singleton.SingleInstance()
except:
    sys.exit()

#checkTicket function
def checkTicket():
        try:
            with open('data\\latestTicket.txt', 'r+') as latestTicket:
                ticketValue = int(latestTicket.readline())
                latestTicket.close()
            ticket_data = fresh.tickets.get_ticket(ticket_number = ticketValue)
            with open('data\\latestTicket.txt', 'w+') as latestTicket:
                latestTicket.write(str(ticketValue+1))
                latestTicket.close()
            return True
        except:
            return False

if checkTicket() == True:
    playsound('data\\'+soundFile)
    sleep(.5)
    while checkTicket() == True:
        pass
