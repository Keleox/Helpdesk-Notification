Installation instructions:

1.	Download Python (https://www.python.org/)

2.	Open cmd and run the following commands (These are three libraries used by the program)
  a.	py -m pip install freshpy
  b.	py -m pip install playsound==1.2.2
  c.	py -m pip install tendo

3. Download the folder and put it in a location where the file name doesn't have any spaces (i.e. somewhere not backed up by OneDrive. I use my "Downloads" folder).

4.	In the “data.json” file, you can put the name of the sound file you want to use (if my weeb one isn’t good enough for you) and for your API key. The API key can be found by going to the “Profile Settings” page on the helpdesk website. An alternate sound file should also be placed in the "data" folder, so the program can find it.

5.	To setup the program, go to Windows' Task Scheduler, then "Create Task..."
  5.1 Under General, name the task.
  5.2 Under Trigger, create a new trigger with the following settings:
    "Begin the task" -> "On a schedule"
    "Advanced settings" -> "Repeat task every:" -> type in "1 minute" to the box
    "Advanced settings" -> "for a duration of:" -> "Indefinitely"
  5.3 Under Actions, create a new action with the following settings:
    "Program/script:" -> "JsonVersion.pyw"
    "Start in (optional):" -> Put the path to the directory with "JsonVersion.pyw". With the current file structure, it should end with "...\Helpdesk-Notification-main\v1.0\"

6. If the program plays the sound file after you're done setting up, it's working properly.
