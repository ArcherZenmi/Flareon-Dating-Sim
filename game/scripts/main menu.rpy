#
# Filename: main menu.rpy
# Author: ArcherZenmi
#
# Description:
#   main menu.rpy specifies the behavior of the main menu. When first playing the game, the main menu will be skipped.
#   Also, the player gets to choose their language when first playing.
#

label main_menu:
    if persistent.game_not_started:
        call screen language_chooser
        return

    call screen main_menu


# Change the language for the game
screen language_chooser():
    imagebutton:
        xalign 0.2 yalign 0.5
        auto "button us flag %s"
        action [Language(None), Return("N/A")]

    imagebutton:
        auto "button japanese flag %s"
        xalign 0.8 yalign 0.5
        action [Language("japanese"), Return("N/A")]
