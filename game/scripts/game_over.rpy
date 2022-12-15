#
# Filename: game_over.rpy
# Author: ArcherZenmi
#
# Description:
#   game_over.rpy specifies the behavior that'll occur when the player game over's.
#       This will give the player a menu to retry from the beginning, from the quiz, or simply give up.
#

label game_over(punch=True):
    if(punch):
        call jolteon_hit from _call_jolteon_hit
        play sound "audio/effects/punch.wav"

    scene black
    stop music

    call screen game_over


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
    vbox:
        xalign 0.5 yalign 0.7
        spacing 30

        textbutton "Retry":
            xalign 0.5
            action [Hide(), Jump("start")]
        textbutton "Story Chart":
            xalign 0.5
            action [Hide(), Show("story_chart")]
        if(persistent.event_3_reached):
            textbutton "Redo Quiz":
                xalign 0.5
                action [Hide(), Jump("quiz_retry")]