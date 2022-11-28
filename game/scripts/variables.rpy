#
# Filename: variables.rpy
# Author: ArcherZenmi
#
# Description:
#   variables.rpy is in charge of all variables used in this project.
#   This is to organize all the variables in the project and avoid future spaghetti code.
#   (The philosophy is to have 1 this spaghetti file rather than have all the files be spaghetti)

init python:
    presents: int = 0
    quiz_reached: bool =  False
