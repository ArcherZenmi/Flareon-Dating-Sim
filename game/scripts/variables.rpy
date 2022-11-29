#
# Filename: variables.rpy
# Author: ArcherZenmi
#
# Description:
#   variables.rpy is in charge of all variables used in this project.
#   This is to organize all the variables in the project and avoid future spaghetti code.
#   (The philosophy is to have 1 this spaghetti file rather than have all the files be spaghetti)

init:
    default persistent.game_not_started = True
    default persistent.game_counter = 0

init python:
    presents: int = 0
    quiz_reached: bool = False
