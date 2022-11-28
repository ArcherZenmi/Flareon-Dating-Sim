#
# Filename: event3.rpy
# Author: ArcherZenmi
#
# Description:
#   event3.rpy contains the scripts relating to the third major event,
#       i.e Flareon quizzing the player.
#

label event3_start:
    scene bg
    # Animate raising affection meter (and maybe change music)
    show flareon flustered
    f_silent "..."
    f "You know, I'm starting to feel..."

    play sound "audio/effects/break.wav"
    show affection meter:
        anchor (0.5, 0.5) xpos 1620 ypos 130 rotate 0
        parallel:
            linear 0.5 xpos 1820 rotate 45
        parallel:
            easein_quad 0.1 ypos 80
            easeout_quad 0.4 ypos 1600
    show flareon neutral with vpunch

    f "Still unsatisfied?"
    play music "sound/music/dating-tense"
    f "I mean, do you really know anything about me? We just barely met."
    show flareon angry
    f "If you really want to date... How about we do a quiz about me?"

    menu:
        "Bring it on!":
            jump event3_quiz

        "I'd rather just hang out and play GamePoke.":
            jump hangout


label hangout:
    # Music stop
    show flareon neutral
    f_silent "..."
    # Music normal
    show flareon normal
    f "You know what? Sure!"
    f "You're a bit weird, but I don't think you're a bad person."
    f "I’m really good at GamePoke battles though, so I won’t go easy!"
    show flareon happy
    f "Let's play!"
    call screen ending(2)


label quiz_wrong:
    show jolteon tpose with dissolve
    f "Nope."
    jump game_over


label quiz_wrong2:
    show flareon sad with None
    show jolteon tpose with dissolve
    f "oh... nope."
    jump game_over


label event3_quiz:
    f "Ok, what's my job?"
    menu:
        f_silent "Ok, what's my job?{fast}"

        "Medical Officer":
            f "Hm."
        "Gardener":
            jump quiz_wrong
        "Rescuer":
            jump quiz_wrong

    f "Then where do I work?"
    menu:
        f_silent "Then where do I work?{fast}"

        "Standard Tech":
            jump quiz_wrong
        "You have a Pokemon trainer":
            jump quiz_wrong
        "NWI Guild":
            show flareon neutral
            f "Eh?"

    show flareon normal
    f "Then... What's always been my dream?"
    menu:
        f "Then... What's always been my dream?{fast}"

        "Become a researcher!":
            jump quiz_wrong2

        "Become a hero!":
            jump finale

        "Become a guild battler!":
            jump quiz_wrong2
