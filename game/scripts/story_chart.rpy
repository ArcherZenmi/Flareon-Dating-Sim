#
# Filename: story_chart.rpy
# Author: ArcherZenmi
#
# Description:
#   story_chart.rpy specifies the story_chart screen.
#

screen story_chart():
    # Add the background
    add "story chart bg"

    # 1st Event
    if(persistent.event1_reached):
        text "{}/{}".format(event1_fail_count(), len(persistent.event1_game_overs)):
            xalign 0.15 yalign 0.4
            size 100
        if(event1_fail_count() == len(persistent.event1_game_overs)):
            text "COMPLETE!!":
                xalign 0.1 yalign 0.5
                size 80
        textbutton "Retry":
            xalign 0.15 yalign 0.68
            text_size 60
            action [Hide(), Jump("event1_restart")]

    # 2nd Event
    if(persistent.event2_reached):
        text "{}/{}".format(event2_fail_count(), len(persistent.event2_game_overs)):
            xalign 0.5 yalign 0.4
            size 100
        textbutton "Retry":
            xalign 0.5 yalign 0.68
            text_size 60
            action [Hide(), Jump("event2_restart")]

    #3rd Event
    if(persistent.event3_reached):
        text "{}/{}".format(event3_fail_count(), len(persistent.event3_game_overs)):
            xalign 0.85 yalign 0.4
            size 100
        textbutton "Retry":
            xalign 0.86 yalign 0.68
            text_size 60
            action [Hide(), Jump("event3_restart")]

    # Restart Game
    textbutton "Start From Beginning":
        anchor (0.0, 1.0)
        xpos 0.05 ypos 0.95
        text_size 60
        action [Hide(), Jump("start")]

    # Finished Endings
    text "Endings:":
        anchor (0.5, 1.0) xpos 0.62 ypos 0.97
        size 100
    hbox:
        anchor (0.5, 1.0) xpos 0.86 ypos 1.02
        spacing 5

        # Ending 1
        if(persistent.ending_1_reached):
            add "heart icon 1":
                anchor (0.5, 0.5) zoom 0.8
        else:
            add "heart icon 1":
                anchor (0.5, 0.5) zoom 0.8
                matrixcolor BrightnessMatrix(-1)
        # Ending 2
        if(persistent.ending_2_reached):
            add "heart icon 2":
                anchor (0.5, 0.5) zoom 0.8
        else:
            add "heart icon 2":
                anchor (0.5, 0.5) zoom 0.8
                matrixcolor BrightnessMatrix(-1)
        # Ending 3
        if(persistent.ending_3_reached):
            add "heart icon 3":
                anchor (0.5, 0.5) zoom 0.8
        else:
            add "heart icon 3":
                anchor (0.5, 0.5) zoom 0.8
                matrixcolor BrightnessMatrix(-1)

    # Ending 0
    if(persistent.ending_0_reached):
        add "umbreon head":
            anchor (0.6, 0.6) xpos 0.96 ypos 0.9 zoom 0.15