#
# Filename: animation.rpy
# Author: ArcherZenmi
#
# Description:
#   animation.rpy specifies general animations/transformations used throughout the project.
#

# Teleport (called via function)
transform jolteon_teleport_in:
    anchor (0.7, 0.5) pos (0.7, 0.5) xzoom 0.0 yzoom 1.5
    easeout 0.2 xzoom 1.4 yzoom 0.05
    ease 0.14 xzoom 1.0 yzoom 1.0

init python:
    def jolteon_teleport_func():
        renpy.show("jolteon tpose", at_list = [jolteon_teleport_in])
        renpy.pause(0.34, hard=True)

# Jolteon hits you (called via label)
label jolteon_hit(punch=True):
    window hide
    show jolteon tpose:
        anchor (0.7, 0.5) pos (0.7, 0.5)
        easeout 0.2 xpos 0.5 zoom 1.5
    pause 0.2
    window auto

    return

# Affection meter fills up
label fill_affection_meter:
    play sound "audio/effects/shiny.wav"

    show affection meter empty:
        anchor (0.5, 0.5) xpos 1620 ypos 180 rotate 0
        matrixcolor BrightnessMatrix(0.0)
        linear 0.5 matrixcolor BrightnessMatrix(1.0)
    show affection meter full:
        matrixcolor BrightnessMatrix(1.0)
        linear 0.5 matrixcolor BrightnessMatrix(0.0)
    
    pause 1.0