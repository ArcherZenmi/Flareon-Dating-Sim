#
# Filename: characters.rpy
# Author: ArcherZenmi
#
# Description:
#   characters.rpy is a file containing any and all information
#   pertaining to initializing the characters in this project.

# Define the voice callback
init python:
    def voiceCallback(event, name, **kwargs):
        if event == "show":
            renpy.sound.play(f"audio/voice/{name}.wav", channel="sound", loop=True)
        elif event == "slow_done":
            renpy.sound.play(f"audio/voice/{name}.wav", channel="sound")
            renpy.sound.stop(channel="voice")

# Define characters
define f = Character("Flareon", color="#ee7b46", callback=voiceCallback, cb_name="Flareon")
define j = Character("Jolteon", color="#fccc4a", callback=voiceCallback, cb_name="Jolteon")
define u = Character("", what_color="#ffffff", window_background="gui/textbox renpy.png")

define f_silent = Character("Flareon", color="#ee7b46", cb_name="Flareon")
