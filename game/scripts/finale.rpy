#
# Filename: finale.rpy
# Author: ArcherZenmi
#
# Description:
#   finale.rpy contains the scripts relating to the final ending of the game,
#       I.e right after the player passes Flareon's quiz.
#

label finale:
    stop music fadeout 1.0
    show flareon surprised
    f "Oh my Arceus! Could it be?"
    f "Are you... the one for me?"

    play music "audio/music/oh-one-true-love.mp3"
    show flareon happy
    f "Hello?"
    menu:
        "Is it me you're looking for?":
            pass
    f "I can see it in your floof, I can see it in your smile."
    menu:
        "You're all I've ever wanted and my paws are open wide.":
            pass
    f "'Cause you know just what to say, and you know just what to do."
    menu:
        "And I want to tell you so much...":
            pass
    show flareon flustered
    f "I WUV YOU!!"

    stop music fadeout 1.0
    f "Hehe... well, I did promise we could date if you passed."
    f "But since you’ve gotten to learn so much of me already..."
    play music "audio/music/dating-start.mp3"
    show flareon happy
    f "In a way, this was almost like a date wasn't it?"
    show flareon neutral
    f "Even though we only met... once? Or was it [persistent.game_counter] times?"
    show flareon normal
    f "Anyways, lets get go-"
    menu:
        "One more thing. Once we're back...":
            pass
    f "Huh? What is it?"
    menu:
        "I'll fix that door for you.":
            show flareon flustered
            f "Oh, thanks! That'd help me a lot!"

        "Nothin'.":
            show flareon neutral
            f "...ok?"

    show jolteon tpose with dissolve
    j "Hold up. You’re not seriously going out alone with a complete stranger?"
    show flareon neutral
    f "...I guess you're right, it's a bit too dangerous."
    show flareon normal
    f "Well, you can come with us Jolteon!"
    j "What."
    menu:
        "What.":
            pass
    j "Oi! Don't copy me!"
    f "Come on, Jolteon! It’ll be more fun together, and you can make sure I’m safe too."
    j "Yeah... I'll be keeping a real close eye on {i}you{/i}."
    show flareon happy
    f "Well let's go then. Now!"

    $ persistent.ending_3_reached = True
    call screen ending(3)
