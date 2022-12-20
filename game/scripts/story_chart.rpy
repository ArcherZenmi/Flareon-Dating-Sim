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
    $ asset_scale = 2.0 / 3
    $ blue_dark = "#003349"

    # 1st Event
    if(persistent.event1_reached):
        text "{}/{}".format(event1_fail_count(), len(persistent.event1_game_overs)):
            color blue_dark
            anchor (.5, .5)
            xpos int(540 * asset_scale) ypos int(738 * asset_scale)
            size int(160 * asset_scale)
        if(event1_fail_count() == len(persistent.event1_game_overs)):
            text _("COMPLETE!!"):
                color blue_dark
                anchor (.5, .5)
                xpos int(540 * asset_scale) ypos int(908 * asset_scale)
                size int(76 * asset_scale)
        imagebutton:
            auto "retry button %s"
            anchor (.5, .5)
            xpos int(540 * asset_scale) ypos int(1131 * asset_scale)
            action [Hide(), Jump("event1_restart")]
        
    else:
        add "event locked":
            anchor (.5, .5) xpos int(540 * asset_scale) ypos int(767 * asset_scale)

    # 2nd Event
    if(persistent.event2_reached):
        text "{}/{}".format(event2_fail_count(), len(persistent.event2_game_overs)):
            color blue_dark
            anchor (.5, .5)
            xpos int(1440 * asset_scale) ypos int(738 * asset_scale)
            size int(160 * asset_scale)
        if(event2_fail_count() == len(persistent.event2_game_overs)):
            text _("COMPLETE!!"):
                color blue_dark
                anchor (.5, .5)
                xpos int(1440 * asset_scale) ypos int(908 * asset_scale)
                size int(76 * asset_scale)
        imagebutton:
            auto "retry button %s"
            anchor (.5, .5)
            xpos int(1440 * asset_scale) ypos int(1131 * asset_scale)
            action [Hide(), Jump("event2_restart")]
    else:
        add "event locked":
            anchor (.5, .5) xpos int(1440 * asset_scale) ypos int(767 * asset_scale)

    #3rd Event
    if(persistent.event3_reached):
        text "{}/{}".format(event3_fail_count(), len(persistent.event3_game_overs)):
            color blue_dark
            anchor (.5, .5)
            xpos int(2340 * asset_scale) ypos int(738 * asset_scale)
            size int(160 * asset_scale)
        if(event3_fail_count() == len(persistent.event3_game_overs)):
            text _("COMPLETE!!"):
                color blue_dark
                anchor (.5, .5)
                xpos int(2340 * asset_scale) ypos int(908 * asset_scale)
                size int(76 * asset_scale)
        imagebutton:
            auto "retry button %s"
            anchor (.5, .5)
            xpos int(2340 * asset_scale) ypos int(1131 * asset_scale)
            action [Hide(), Jump("event3_restart")]
    else:
        add "event locked":
            anchor (.5, .5) xpos int(2340 * asset_scale) ypos int(767 * asset_scale)

    # Restart Game
    imagebutton:
        auto "restart button %s"
        anchor (.0, .5)
        xpos int(35 * asset_scale) ypos int(1485 * asset_scale)
        action [Hide(), Jump("start")]

    # Finished Endings
    # Ending 1
    if persistent.ending_1_reached:
        add "heart icon 1":
            anchor (0.5, 0.5)
            xpos int(2235 * asset_scale) ypos int(1485 * asset_scale)
            zoom 0.66
    else:
        add "heart icon empty":
            anchor (0.5, 0.5)
            xpos int(2235 * asset_scale) ypos int(1485 * asset_scale)
            zoom 0.66
    # Ending 2
    if persistent.ending_2_reached:
        add "heart icon 2":
            anchor (0.5, 0.5)
            xpos int(2395 * asset_scale) ypos int(1485 * asset_scale)
            zoom 0.66
    else:
        add "heart icon empty":
            anchor (0.5, 0.5)
            xpos int(2395 * asset_scale) ypos int(1485 * asset_scale)
            zoom 0.66
    # # Ending 3
    if persistent.ending_3_reached:
        add "heart icon 3":
            anchor (0.5, 0.5)
            xpos int(2555 * asset_scale) ypos int(1485 * asset_scale)
            zoom 0.66
    else:
        add "heart icon empty":
            anchor (0.5, 0.5)
            xpos int(2555 * asset_scale) ypos int(1485 * asset_scale)
            zoom 0.66

    # Ending 0
    if(persistent.ending_0_reached):
        add "umbreon head":
            anchor (0.6, 0.6) xpos 0.96 ypos 0.9 zoom 0.15