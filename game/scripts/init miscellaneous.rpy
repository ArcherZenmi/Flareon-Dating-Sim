#
# Filename: init.rpy
# Author: ArcherZenmi
#
# Description:
#   init.rpy specifies any initializations that don't readily fit into other files.
#

# Change what layers exist in this project
init python:
    config.layers = ["master", "transient", "screens", "foreground", "overlay"] 


# Change what font is used for English
translate None style default:
    font "fonts/Mochiy_Pop_One/MochiyPopOne-Regular.ttf"

translate None python:
    # The main fonts
    gui.text_font = "fonts/Mochiy_Pop_One/MochiyPopOne-Regular.ttf"
    gui.name_text_font = "fonts/Mochiy_Pop_One/MochiyPopOne-Regular.ttf"
    gui.interface_text_font = "fonts/Mochiy_Pop_One/MochiyPopOne-Regular.ttf"

    # Extra fonts that Ren'Py refuses to update
    gui.button_text_font = "fonts/Mochiy_Pop_One/MochiyPopOne-Regular.ttf"
    gui.choice_button_text_font = "fonts/Mochiy_Pop_One/MochiyPopOne-Regular.ttf"


# Change what font is used for Japanese
translate japanese style default:
    font "fonts/Mochiy_Pop_One/MochiyPopOne-Regular.ttf"

translate japanese python:
    # The main fonts
    gui.text_font = "fonts/Mochiy_Pop_One/MochiyPopOne-Regular.ttf"
    gui.name_text_font = "fonts/Mochiy_Pop_One/MochiyPopOne-Regular.ttf"
    gui.interface_text_font = "fonts/Mochiy_Pop_One/MochiyPopOne-Regular.ttf"

    # Extra fonts that Ren'Py refuses to update
    gui.button_text_font = "fonts/Mochiy_Pop_One/MochiyPopOne-Regular.ttf"
    gui.choice_button_text_font = "fonts/Mochiy_Pop_One/MochiyPopOne-Regular.ttf"
    
