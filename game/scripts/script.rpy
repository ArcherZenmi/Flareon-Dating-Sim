#
# Filename: script.rpy
# Author: ArcherZenmi
#
# Description:
#   script.rpy is, by convention, the starting place of the projects story/script.
#

label start:

    $ persistent.game_not_started = False

    scene black

    play sound "audio/door/door.wav"
    pause 5.5
    
    play music "audio/music/dating-start.mp3"
    scene bg
    show flareon surprised:
        xalign 0.5 yalign 0.5
        easein 0.1 ypos 0.35
        easeout 0.1 ypos 0.5
    pause 0.75
    show affection meter:
        anchor (0.5, 0.5) xpos 1620 ypos 130
    f "KYA!!"
    show affection meter:
        anchor (0.5, 0.5) xpos 1620 ypos 130 rotate 0
        parallel:
            linear 0.5 xpos 1820 rotate 45
        parallel:
            easein_quad 0.1 ypos 80
            easeout_quad 0.4 ypos 1600
    menu:
        "Hi there!":
            pass

    jump event1_start
