#
# Filename: script.rpy
# Author: ArcherZenmi
#
# Description:
#   script.rpy is, by convention, the starting place of the projects story/script.
#

label start:

    $ persistent.game_not_started = False
    $ persistent.game_counter += 1

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
    f "KYA!!"
    menu:
        "Hi there!":
            pass

    jump event1_start
