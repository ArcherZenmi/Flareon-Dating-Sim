#
# Filename: ending screens.rpy
# Author: ArcherZenmi
#
# Description:
#   ending screens.rpy specifies... well, the screens displayed for each ending type!
#

screen ending(ending_num):
    # Decide what ending to display
    if ending_num == 1:
        $ ending_text = _("Ending 1/3: You Bought Yourself A Date!")
    elif ending_num == 2:
        $ ending_text = _("Ending 2/3: Just Friends")
    elif ending_num == 3:
        $ ending_text = _("Ending 3/3: I WUV YOU!!")
    else:
        $ ending_text = _("Ending ?/3: Whoops, You Got Banned From Reality!")

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
    if(ending_num == 0):
        imagebutton:
            xalign 0.49 yalign 0.65
            action MainMenu(False)
            auto "umbreon button %s"
    else:
        textbutton _("Main Menu"):
            xalign 0.5 yalign 0.65
            action MainMenu(False)
