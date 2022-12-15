#
# Filename: variables.rpy
# Author: ArcherZenmi
#
# Description:
#   variables.rpy is in charge of all variables used in this project.
#   This is to organize all the variables in the project and avoid future spaghetti code.
#   (The philosophy is to have this 1 spaghetti file rather than have all the files be spaghetti)
#

init:
    # Used to dictate whether the player has previously opened the game before.
    default persistent.game_not_started = True

    # How many times the player has played the game.
    default persistent.game_counter = 0

    # How many "presents" the player has offerred Flareon.
    # Used to dictate which events to show
    default persistent.presents = 0

    # Represents which events the player has reached (and can restart at)
    default persistent.event1_reached = False
    default persistent.event2_reached = False
    default persistent.event3_reached = False

    # Represents which endings the player has reached
    default persistent.ending_0_reached = False
    default persistent.ending_1_reached = False
    default persistent.ending_2_reached = False
    default persistent.ending_3_reached = False
