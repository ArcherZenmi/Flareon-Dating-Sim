#
# Filename: event1.rpy
# Author: ArcherZenmi
#
# Description:
#   event1.rpy contains the scripts relating to the first major event,
#       i.e the player breaking into Flareon's house.
#

label event1_start:
    $ persistent.event1_reached = True

    f "W-who are you??"

    menu:
        "Oh, sorry... Hope I didn't disturb you...":
            jump event1_sorry

        "My name’s *insert name*, and I want to date you!":
            jump event1_date

        "LET’S HAVE BABIES RIGHT NOW!!":
            jump event1_babies

        "I have another present for you." if persistent.presents == 1:
            jump presents1

        "I have even more presents." if persistent.presents == 2:
            jump presents2

        "I have nothing to give but my love." if persistent.presents == 3:
            jump presents3


label event1_restart:
    $ persistent.game_counter += 1

    scene bg
    show flareon surprised

    play music "audio/music/dating-start.mp3"

    jump event1_start


label event1_sorry:
    show flareon sad
    f "T-that's ok... {size=20}Even though you broke down my door.{/size}"
    show flareon neutral
    f "So, what are you doing here?"

    menu:
        "I was wondering if we could... date?":
            show flareon surprised
            f "D-date??"
            f "I mean, we just barely met! I feel like I hardly know you yet, this relationship is going so fast and..."
            show flareon angry
            f "...wait, you just broke down my door!"

            menu:
                "Yes I did.":
                    f "Criminal!"
                    show jolteon tpose with dissolve
                    j "Criminal?"
                    menu:
                        "No criminal.":
                            pass
                    
                    $ persistent.event1_game_overs[0] = True
                    jump game_over

                "No I didn't.":
                    f "I-"
                    show flareon surprised
                    f_silent "(Oh no. They’ve completely countered my argument!)"
                    jump event2_start

        "I'm the milkman.":
            show flareon normal
            f "Oh! You're on delivery?"
            f "Jolteon!!"
            show jolteon tpose with dissolve
            j "Eh, Is it the milkman?"
            f "Yup! Did we order any milk?"
            j "Nope."
            menu:
                "Well darn.":
                    pass

            $ persistent.event1_game_overs[1] = True
            jump game_over
            

label event1_date:
    show flareon neutral
    f_silent "..."
    f "Are you ok?"

    menu:
        "Yes.":
            f "So you're serious..."
            show flareon sad
            f_silent "(Should I really be talking to this crazy person?)"
            show flareon neutral
            f "Um... You're not a crazy person, are you?"

            menu:
                "Nope! I'm just a normal human being.":
                    show flareon surprised
                    f "You're a HUMAN??"
                    show flareon scared
                    f "B-but I thought humans went extinct, right? You can't really..."
                    f_silent "..."
                    f "Jolteon help! There's a human!!"
                    show jolteon tpose with dissolve
                    j "Human huh? Yeah right. Wrong season for trick or treating bud."
                    
                    $ persistent.event1_game_overs[2] = True
                    jump game_over

                "Would a crazy person break down your door?":
                    show flareon normal
                    f "...I guess not?"
                    f "People around here are pretty eccentric, so things break all the time."
                    show flareon happy
                    f "I sometimes wonder if we're living in a cartoon? hehe."
                    jump event2_start

                "HAHAHAHAHA":
                    show flareon normal
                    f "HAHAHAHAHAHAHAHAHAHA"
                    menu:
                        "HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA":
                            pass
                    show flareon happy
                    f "HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA"
                    show flareon scared
                    f "...Jolteon pls help."
                    show jolteon tpose with dissolve

                    $ persistent.event1_game_overs[3] = True
                    jump game_over

        "No.":
            show flareon sad
            f "Oh, you must have had an episode and ran into the nearest house. Poor thing."
            show flareon normal
            f "Don’t worry, I’m a medical officer so I can help you!"
            f "But I’m not certified for mental stuff yet, so I’ll send you to the nearest hospital."

            menu:
                "Yes please.":
                    pass

                "I'd rather be treated by you.":
                    show flareon happy
                    f "Nope! Breaking down people's doors means you're clearly a public menace. (and dangerous!)"
            
            show flareon normal
            f "Jolteon!!"
            show jolteon tpose with dissolve
            f "Can you send them to the psychic hospital?"
            j "Again? You’re too nice, just kick ‘em out next time."

            $ persistent.event1_game_overs[4] = True
            jump game_over



label event1_babies:
    show flareon scared
    f "...what?"

    menu:
        "I wanna put my AVOCADO in your {i}tuna{/i}.":
            f "Jolteon!! There's some weird person in our house!"
            show jolteon tpose with dissolve
            j "The hell?"
            j "Get out you crazy hobo!"

            $ persistent.event1_game_overs[5] = True
            jump game_over

        "Sorry. You’re just very pretty, and I really want to date you!":
            show flareon neutral
            f "...ok?"
            show flareon normal
            f "So, how are you gonna rob my house with that avocado and tuna in your hands?"

            menu:
                "I'm not robbing your house!":
                    f "Ha! That's just what a robber would say!"
                    show flareon happy
                    f "Worry not, because hero Flareon's gonna stop this bad guy!"
                    f_silent "..."
                    show flareon scared
                    f "JOLTEON!!"
                    show jolteon tpose with dissolve
                    j "Dude… weren’t you gonna fight robbers on your own?"
                    f "B-but..."
                    j "If being a hero really is your dream, you gotta fight for yourself. <-(Jolteon big brother mode)"
                    f "O-ok..."
                    show flareon scared as f_temp behind jolteon
                    hide flareon
                    show flareon scared with dissolve
                    hide f_temp
                    f_silent "..."
                    show flareon angry
                    f "HIYA!!!"

                    scene black
                    stop music
                    play sound "audio/effects/punch.wav"
                    pause(1.0)

                    j "Huh... nice shot!"

                    $ persistent.event1_game_overs[6] = True
                    call game_over(False) from _call_game_over

                "I'm making a salad for our date.":
                    show flareon surprised
                    f "Wait..."
                    f "Wait...\n{fast}You're gonna rob AND date me??"
                    show flareon scared
                    f "You need better hobbies."
                    jump event2_start