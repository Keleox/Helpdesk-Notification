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
        variableFile.close()
except:
    print("Error: Error getting API key or sound file name")
    sys.exit()

playsound(soundFile)
#Connect to the FreshService API with Freshpy
fresh = FreshPy(domain='farnsworthgroup.freshservice.com', api_key = apiValue)

#Prevents duplicate instances of the program from running.
try:
    me = singleton.SingleInstance()
except:
    sys.exit()

#Checks to see if the server can be accessed. If it errors out, it is most likely due to the API key not being correct
try:
    with open('latestTicket.txt', 'r+') as latestTicket:
        ticketValue = int(latestTicket.readline())
        latestTicket.close()
    ticket_data = fresh.tickets.get_ticket(ticket_number = ticketValue-1)
    if ticket_data.get('code') == 'access_denied':
        raise Exception
except:
    print("Access Denied")
    sys.exit()

#General logic of the program: It checks to see if a ticket with the value 1+ of the current highest ticket number exists.
#If it does, the program will update the text file and run again. If it errors, then the program is up to date.
while ticketUpdate == True:
    try:
        with open('latestTicket.txt', 'r+') as latestTicket:
            ticketValue = int(latestTicket.readline())
            latestTicket.close()
        ticket_data = fresh.tickets.get_ticket(ticket_number = ticketValue)
        with open('latestTicket.txt', 'w+') as latestTicket:
            latestTicket.write(str(ticketValue+1))
            latestTicket.close()
    except:
        ticketUpdate = False

#Same logic as before, but this time it checks once every minute. If a new ticket is found, it updates the text file and plays the notification sound.
#This is an infinite loop
while True:
    try:
        with open('latestTicket.txt', 'r+') as latestTicket:
            ticketValue = int(latestTicket.readline())
            latestTicket.close()
        ticket_data = fresh.tickets.get_ticket(ticket_number = ticketValue)
        playsound("data\\"+soundFile)
        with open('latestTicket.txt', 'w+') as latestTicket:
            latestTicket.write(str(ticketValue+1))
            latestTicket.close()
    except:
        pass
    sleep(60)
