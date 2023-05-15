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

name = "Richard"

if name == "Vincent":
    print("Vincent is one of the instructors of the Python Masterclass")
elif name == "Anushree":
    print("Anushree is the AWS support person during the Python Masterclass")
elif name == "Richard":
    print("Richard is a Hydrologist with DES")
else:
    print("Name is unknown, not sure what to print about this person.")

# 2nd test comment for github upload issue

# Homework 2: Classes
# import class
import well_classes as wc

# instantiate wells
well1 = wc.well(x=0, y=0, exrate=0.3, cas_rad=0.5)
well2 = wc.well(x=8, y=5, exrate=10, cas_rad=3)

# instantiate well field
wfield = wc.wellField("Dutton Park")
# add wells to field
wfield.addWell(well1)
wfield.addWell(well2)


print(f"Well field {wfield.name} contains {str(wfield.well_cnt)} wells:\n")
print(wfield.listWells())

