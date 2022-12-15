#
# Filename: event1.rpy
# Author: ArcherZenmi
#
# Description:
#   game_over.rpy specifies the behavior that'll occur when the player game over's.
#       This will give the player a menu to retry from the beginning, from the quiz, or simply give up.
#

label game_over(punch=True):
    if(punch):
        call jolteon_hit
        play sound "audio/effects/punch.wav"

    scene black
    stop music

    call screen game_over