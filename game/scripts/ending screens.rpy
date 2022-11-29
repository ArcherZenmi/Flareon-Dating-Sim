#
# Filename: ending screens.rpy
# Author: ArcherZenmi
#
# Description:
#   ending screens.rpy specifies... well, the screens displayed for each ending type! (including game overs)
#

screen ending(ending_num):
    # Decide what ending to display
    if ending_num == 1:
        $ ending_text = "Ending 1/3: You Bought Yourself A Date!"
    elif ending_num == 2:
        $ ending_text = "Ending 2/3: Just Friends"
    elif ending_num == 3:
        $ ending_text = "Ending 3/3: I WUV YOU!!"
    else:
        $ ending_text = "Ending ?/3: Whoops, You Got Banned From Reality!"

    # Black background
    add "black"

    # The title of the ending
    text ending_text:
        size 60
        color "#ffffff"
        xalign 0.5 yalign 0.4
    
    # Some art
    # Insert small image/art

    # Button to return to main menu
    textbutton "Main Menu":
        xalign 0.5 yalign 0.65
        action MainMenu(False)

screen game_over(punch = False):
    # A punch sound effect for extra kick
    #if(punch):
    #    Play("sound", "audio/effects/punch/wav")

    # Black background
    add "black"

    # Gameover title
    text "Game Over":
        size 60
        color "#ffffff"
        xalign 0.5 yalign 0.4

    # Retry/restart buttons
    textbutton "Retry":
        xalign 0.5 yalign 0.6
        action Jump("start")
    if quiz_reached:
        textbutton "Redo Quiz":
            xalign 0.5 yalign 0.7
            action Jump("quiz_retry")