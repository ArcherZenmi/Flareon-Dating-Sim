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
    "Characters/Flareon/Flareon Normal.png"
    asset_scale
image flareon neutral:
    "Characters/Flareon/Flareon Neutral.png"
    asset_scale
image flareon happy:
    "Characters/Flareon/Flareon Happy.png"
    asset_scale
image flareon sad:
    "Characters/Flareon/Flareon Sad.png"
    asset_scale
image flareon angry:
    "Characters/Flareon/Flareon Angry.png"
    asset_scale
image flareon scared:
    "Characters/Flareon/Flareon Scared.png"
    asset_scale
image flareon surprised:
    "Characters/Flareon/Flareon Surprised.png"
    asset_scale
image flareon flustered:
    "Characters/Flareon/Flareon Flustered.png"
    asset_scale

# Jolteon's Expressions
image jolteon tpose:
    "Characters/Jolteon/Jolteon Tpose.png"
    asset_scale

# Umbreon
image umbreon head:
    "Characters/Umbreon/Umbreon Head.png"
    asset_scale

image umbreon button idle:
    "umbreon head"
    zoom 0.2

image umbreon button hover:
    "umbreon head"
    zoom 0.2
    matrixcolor TintMatrix("cc0066")

image umbreon button click:
    "umbreon head"
    zoom 0.2
    matrixcolor TintMatrix("ffffff")


# Solid Colors
image black = Solid("#000000")
image red = Solid("#ff0000")

# Backgrounds
image bg:
    "Backgrounds/Background.png"
    asset_scale

# Affection Meter
image affection meter empty:
    "Affection Meter/Affection Meter Empty.png"
    asset_scale

image affection meter full:
    "Affection Meter/Affection Meter Full.png"
    asset_scale

# Story chart
image story chart bg:
    "Story Chart/Story Chart Background.png"
    asset_scale

image heart icon 1:
    "Story Chart/Heart Icon 1.png"
    asset_scale

image heart icon 2:
    "Story Chart/Heart Icon 2.png"
    asset_scale

image heart icon 3:
    "Story Chart/Heart Icon 3.png"
    asset_scale

image heart icon empty:
    "Story Chart/Heart Icon Empty.png"
    asset_scale

image event locked:
    "Story Chart/Event Locked.png"
    asset_scale

image retry button idle:
    "Story Chart/Retry Button Idle.png"
    asset_scale

image retry button hover:
    "Story Chart/Retry Button Hover.png"
    asset_scale

image restart button idle:
    "Story Chart/Restart Button Idle.png"
    asset_scale

image restart button hover:
    "Story Chart/Restart Button Hover.png"
    asset_scale

# Images supporting 9slice
image 9Slice blue:
    "9Slice/Blue.png"
    zoom 0.33

image 9Slice blue dark:
    "9Slice/Blue Dark.png"
    zoom 0.33

image 9Slice orange:
    "9Slice/Orange.png"
    zoom 0.33
    
image 9Slice orange light:
    "9Slice/Orange Light.png"
    zoom 0.33