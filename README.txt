Installation instructions:

1. Download Python (https://www.python.org/)

2. Open cmd and run the following commands (These are three libraries used by the program)
    py -m pip install freshpy
    py -m pip install playsound==1.2.2
    py -m pip install tendo

3. Download the folder and put it in a location where the file name doesn't have any spaces (i.e. somewhere not backed up by OneDrive. I use my "Downloads" folder).

4. In the “data.json” file, you can put the name of the sound file you want to use (if my weeb one isn’t good enough for you) and your API key. The API key can be found on the right side of the “Profile Settings” page on the helpdesk website. Also, if you use an alternate sound file, it should also be placed in the "data" folder so the program can find it.

5. To setup the program, go to Windows' Task Scheduler, then "Create Task..."
  5.1 Under General, name the task.
  5.2 Under Trigger, create a new trigger with the following settings:
    "Begin the task" -> "On a schedule"
    "Advanced settings" -> "Repeat task every:" -> type in "1 minute" to the box
    "Advanced settings" -> "for a duration of:" -> "Indefinitely"
  5.3 Under Actions, create a new action with the following settings:
    "Program/script:" -> put select the "Pythonw.exe"
    "Add arguments (optional):" - > Select the "APIVersion.pyw" script
    "Start in (optional):" -> Put the path to the directory with "APIVersion.pyw". With the current file structure, it should end with "...\HelpdeskCheck"

6. If the program plays the sound file after you're done setting up, it's working properly.

Common Troubleshooting Problems:
-The dialogue box to ask what program you want to run the script with comes up: Check step 5.3. The Program/script line should only have the program name, not the path.
-The sound file is playing every minute: Check that you put in your API key and removed the brackets. If the Latest Ticket value is super high, the program might just be catching the Latest Ticket value up. You can manually update the value to speed the process up.
