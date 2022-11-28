#
# Filename: main menu.rpy
# Author: ArcherZenmi
#
# Description:
#   main menu.rpy specifies the behavior of the main menu. Hopefully the code is self explanatory.
#

label main_menu:
    if persistent.game_not_started:
        return

    call screen main_menu