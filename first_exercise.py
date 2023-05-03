"""
This file is a basic Python program that displays a message on the screen.
The contents of the message vary depending on the name provided.

For Masterclass attendees: First clone the main branch of the 
PythonMasterclass repository to a branch that you call develop_xyz, where
xyz can be the initials of your name or any name you feel is appropriate (as
long as the branch does not yet exist in the repository). After you created
the repository, select it and modify this file by adding your own name
to the conditionals list below and adding a message to be printed to the 
screen. 
"""

name = "YourName"

if name == "Vincent":
    print("Vincent is one of the instructors of the Python Masterclass")
elif name == "Anushree":
    print("Anushree is the AWS support person during the Python Masterclass")
else:
    print("Name is unknown, not sure what message to print for this person.")
    