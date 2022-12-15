#
# Filename: game_over tracker.rpy
# Author: ArcherZenmi
#
# Description:
#   game_over tracker.rpy gives an API to keep track of which game overs have been achieved,
#   for each individual events.
#

init:
    default persistent.event1_game_overs = [False] * 7
    default persistent.event2_game_overs = [False] * 6
    default persistent.event3_game_overs = [False] * 2

init python:
    def event1_fail_count():
        count: int = 0

        for b in persistent.event1_game_overs:
            if(b):
                count += 1

        return count

    def event2_fail_count():
        count: int = 0

        for b in persistent.event2_game_overs:
            if(b):
                count += 1

        return count

    def event3_fail_count():
        count: int = 0

        for b in persistent.event3_game_overs:
            if(b):
                count += 1

        return count
