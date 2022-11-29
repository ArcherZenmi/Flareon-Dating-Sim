#
# Filename: images.rpy
# Author: ArcherZenmi
#
# Description:
#   images.rpy creates any animations/images in this project.
#       This file is meant to specify "as-is" images.
#       Alterations may be made to preserve "as-is"-ness of images.
#       However, animations & complex visuals should be specified elsewhere.
#

# Transform to fix to screen
transform asset_scale:
    zoom (2.0 / 3)

# Flareon's Expressions
image flareon normal:
    "Flareon Normal.png"
    asset_scale
image flareon neutral:
    "Flareon Neutral.png"
    asset_scale
image flareon happy:
    "Flareon Happy.png"
    asset_scale
image flareon sad:
    "Flareon Sad.png"
    asset_scale
image flareon angry:
    "Flareon Angry.png"
    asset_scale
image flareon scared:
    "Flareon Scared.png"
    asset_scale
image flareon surprised:
    "Flareon Surprised.png"
    asset_scale
image flareon flustered:
    "Flareon Flustered.png"
    asset_scale

# Jolteon's Expressions
image jolteon tpose:
    "Jolteon Tpose.png"
    asset_scale
image jolteon normal:
    "Jolteon Normal.png"
    asset_scale

# Solid Colors
image black = Solid("#000000")

# Backgrounds
image bg:
    "Background.png"
    asset_scale

# Affection Meter
image affection meter empty:
    "Affection Meter Empty.png"
    asset_scale

image affection meter full:
    "Affection Meter Full.png"
    asset_scale