#
# Filename: ending screens.rpy
# Author: ArcherZenmi
#
# Description:
#   ending screens.rpy specifies... well, the screens displayed for each ending type! (including game overs)
#

screen ending(ending_num):
    if ending_num == 1:
        $ ending_text = "Ending 1/3: Materialistic"
    elif ending_num == 2:
        $ ending_text = "Ending 2/3: Just Friends"
    elif ending_num == 3:
        $ ending_text = "Ending 3/3: I WUV YOU!!"
    else:
        $ ending_text = "Ending ?/3: Whoops! Unhandled Exception"

    add "black"

    text ending_text:
        size 60
        color "#ffffff"
        xalign 0.5 yalign 0.4
    
    # Insert small image/art

    textbutton "Main Menu":
        xalign 0.5 yalign 0.65
        action MainMenu(False)

screen game_over():
    add "black"

    text "Game Over":
        size 60
        color "#ffffff"
        xalign 0.5 yalign 0.4

    textbutton "Retry":
        xalign 0.5 yalign 0.6
        action Jump("start")
    if quiz_reached:
        textbutton "Redo Quiz":
            xalign 0.5 yalign 0.7
            action Jump("event3_quiz")