#
# Filename: presents.rpy
# Author: ArcherZenmi
#
# Description:
#   presents.rpy contains any miscellaneous scripts associated with the presents ending.
#   Note: A large part of presents begins at event1_start.
#

label presents1:
    show flareon normal
    f "\"Another?\" I think you have the wrong person..."
    show flareon happy
    f_silent "!!"
    f "You brought me a Flareon plushie!?"
    f "I..."
    show flareon flustered
    f "I... {fast}wanted a Jolteon plushie."
    show jolteon tpose with dissolve
    j "Oi! Stop awakening Flareon without my permission!"

    $ persistent.presents = 2
    jump game_over


label presents2:
    show flareon normal
    f "Ooo! A flower bouquet!"
    f_silent "..."
    show flareon scared
    f "ACHOOOO!!!"
    show flareon normal
    f "Sorry, I’m just allergic to pollen."
    show jolteon tpose with dissolve
    show flareon surprised
    f "Wait, I didn't even call you yet??"

    $ persistent.presents = 3
    jump game_over


label presents3:
    show flareon normal
    f_silent "!!!"
    f "Oh, uhh... hehe. Thanks."
    f_silent "..."
    f "Uh, did we meet somewhere before?"
    show flareon happy
    f "I kinda feel like I already know you."
    menu:
        "Wil you go on a date with me?":
            pass
    show flareon surprised
    f_silent "..."
    show flareon happy
    f "...You know what, sure!"
    show flareon normal
    f "But you'll be paying."

    menu:
        "Whaat":
            pass
        "Uuhhhhh":
            pass
        "Why can't I say no?":
            pass

    f "Well, you seem like the kind of person that showers their date with gifts."
    f "If you’re gonna break into my house and kidnap me on a date, you can at least buy me dinner right?"
    show flareon happy
    f "C'mon, lets go right now! I want ramen!"

    $ persistent.ending_1_reached = True
    call screen ending(1)
    