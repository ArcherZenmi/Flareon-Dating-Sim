#
# Filename: animation.rpy
# Author: ArcherZenmi
#
# Description:
#   animation.rpy specifies general animations/transformations used throughout the project.
#

# Teleport
transform jolteon_teleport_in:
    anchor (0.7, 0.5) pos (0.7, 0.5) xzoom 0.0 yzoom 1.5
    easeout 0.2 xzoom 1.4 yzoom 0.05
    ease 0.14 xzoom 1.0 yzoom 1.0

init python:
    def jolteon_teleport_func():
        renpy.show("jolteon tpose", at_list = [jolteon_teleport_in])
        renpy.pause(0.34, hard=True)
