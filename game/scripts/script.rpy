#
# Filename: script.rpy
# Author: ArcherZenmi
#
# Description:
#   script.rpy is, by convention, the starting place of the projects story/script..

label start:

    scene bg
    
    j "I can APPARATE!"
    $ jolteon_teleport_func()
    j "Harry Potter to the right!"
    
    show flareon surprised
    f "KYA!!"
    menu:
        "Hi there!":
            pass

    jump event1_start
