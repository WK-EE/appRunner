"""
Created on Wed Jun 24 23:48:51 2020

@author: Wael
"""

# Below, we are mporting all the necessary modules for this GUI app to function properly
import tkinter as tk
from tkinter import filedialog, Text
import subprocess, sys
import os.path
from os import path

# The root variable holds the app structure
root = tk.Tk()

# The apps variable will contain a list of the application names (and their directories)
apps = []

# The textfile_path variable holds the path where you want the text file to be created on your machine
textfile_path = "/XXXX/XXXX/XXXXX/save.txt"

# The section below checks if the text file exists, and if it exists,
# then it opens to check what the previously saved preferences are 
if path.exists(textfile_path):
    with open(textfile_path, 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split('\n')
        apps = [x for x in tempApps if x.strip()]
        print(apps)
##########################################################################

# The addApp function allows the user to choose the applications that will run the next time the user utilizes this GUI
def addApp():    
    # Destroy old settings, and push updated to the screen
    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select File", 
                                          filetypes = (("applications", "*.app"),("all files","*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text = app, bg = "gray")
        label.pack()
#######################################################################################################################

# The clearFrame() function will be used to refresh the new preferences on the GUI frame whenever an application is removed
def clearFrame():
    # destroy all widgets from frame
    for widget in frame.winfo_children():
       widget.destroy()

    # this will clear frame and frame will be empty
    # if you want to hide the empty panel then
    frame.pack_forget()
##########################################################################################################

# The runApp function will run the applications chosen by the user
def runApp():
    for app in apps:
        opener = "open" 
        subprocess.call([opener, app])
##################################################################

# The removeApps function allows the user to remove an application that was added to the list, and will refresh the display 
def removeApps():
    
    if apps: 
        del apps[-1]
        clearFrame()
        for app in apps:
            label = tk.Label(frame, text = app, bg = "gray")
            label.pack()

    print(len(apps))
############################################################################################################################

# The section below builds the canvas of our Python GUI
canvas = tk.Canvas(root, height = 650, width = 700, bg = "#263D42")
canvas.pack()

frame = tk.Frame(root, bg = "white")
frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely=0.1)

openFile = tk.Button(root, text = "Open File", padx = 10, pady=5, fg="white", bg = "#000000", command = addApp)
openFile.pack()

runApps = tk.Button(root, text = "Run Apps", padx = 10, pady=5, fg="white", bg = "#263D42", command = runApp)
runApps.pack()

removeApp = tk.Button(root, text = "Remove Last App", padx = 9, pady=5, fg = "white", bg = "#263D42", command = removeApps)
removeApp.pack()

for app in apps:
    label = tk.Label(frame, text = app)
    label.pack()
########################################################    

# The line below will run the GUI application 
root.mainloop()

# The section below will append the txt file with the applications chosen by the user
with open(textfile_path, 'w') as f:
    for app in apps:
        f.write(app + '\n')
###################################################################################
