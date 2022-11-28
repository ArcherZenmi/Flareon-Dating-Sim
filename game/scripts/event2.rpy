#
# Filename: event2.rpy
# Author: ArcherZenmi
#
# Description:
#   event2.rpy contains the scripts relating to the second major event,
#       i.e the player raising Flareon's affection meter.
#

label event2_start:
    menu:
        "So, how about that date?":
            pass
    f "After you broke my door?"
    show flareon angry
    f "Well ofcourse n-"
    menu:
        "Don't answer yet, I need to raise your affection meter first.":
            pass
    
    show affection meter:
        anchor (0.5, 0.5) xpos 1620 ypos -100 rotate 0
        easein 0.5 ypos 130
    pause 0.5
    play sound "audio/effects/shiny.wav"
    pause 1.0
    f "If you don’t stop, I’m actually going to call Jolteon ok?"

    menu:
        "Lets get you drunk.":
            jump event2_drunk
        "So what are your hobbies?":
            jump event2_hobbies
        "I have a present for you.":
            jump event2_present


label event2_drunk:
    show flareon neutral
    f "Drunk…? You want to go get a drink or something?"

    menu:
        "We will drink the blood of our enemies.":
            show flareon surprised
            f_silent "..."
            show flareon normal
            f "Ok, yeah! Lets go beat up some bad guys!"
            f "Who are we getting first, lieutenant?"

            menu:
                "The NWI Guild":
                    show flareon scared
                    f "Wait, we can’t attack the guild. Unless..."
                    show flareon happy
                    f "Traitor!"
                    f "Jolteon, this spy is trying to take our intelliegence!"
                    show jolteon tpose with dissolve
                    f "Take him away soldier, MWAHAHAHA!"
                    hide flareon with dissolve
                    j "Hey, uh, thanks for hanging out with Flareon."
                    j "Most guys at the guild don’t like when he does that, so I’m glad he can at least do it here."
                    menu:
                        "No prob bro. Mind if I date your lil bro?":
                            pass
                    j "Haha, no I'm still gonna arrest you for breaking and entering."
                    jump game_over

                "Standard Tech":
                    f "Of course, that company is always trying to steal the guild’s technology!"
                    f "But this time they’ve gone too far. They’re stealing forbidden research on ancient human weapons technology!"
                    f "We must stop them before they take over the whole world!"
                    show flareon happy
                    f "Heehee, maybe tomorrow."
                    jump event3_start

                "Rogue wild Pokemon":
                    f "Yeah, some local wild Pokémon are attacking a nearby town!"
                    f "They’re trying to steal the town’s food, so we need to protect those innocent civilians!"
                    f "Kick out the wild Pokémon so they can… starve in the wild?"
                    show flareon neutral
                    f "I guess the wild Pokémon are just trying to feed themselves and their pack. They don’t know how to grow their own food."
                    f "It’s not like the guild tries to help them. That’s what Glaceon always says."
                    show flareon sad
                    f "...sorry. I get these weird thoughts sometimes."
                    f_silent "..."
                    show flareon normal
                    f "...I'm ok now. Lets do something else!"
                    jump event3_start

        "Let me show you the magical invention of alcohol":
            show jolteon tpose with dissolve
            j "No you won't."
            show flareon normal
            f "Jolteon? What does \"alcohol\" mean?"
            j "Maybe when you're older, kiddo."
            show flareon neutral
            f "What? I'm not a kiddo!!"
            j "Ehh."
            jump game_over

        "Let's go to starbucks":
            f "Eh? Starbucks doesn't even exist in the Pokemon world?"
            show flareon sad
            f "Wait... What's starbucks? What am I eve-"
            # Insert glitchy animation
            scene bg room
            u "Uh oh, you just broke the space-time continuum!{fast}"
            u "To preserve normality, I'm gonna delete you now.{fast}"
            u "Bye bye!{fast}"
            call screen ending(0)


label event2_hobbies:
    show flareon neutral
    f "...I like to watch battle tournaments on my MagnaVision."

    menu:
        "I love those guild hosted tournaments!":
            f "Hmm."
            f "Who’s the current champion of the NWI guild-hosted tournaments?"

            menu:
                "Uhh, Sylveon the Dragon Slayer?":
                    show flareon surprised
                    f "Oh my Arceus, you DO watch them!"
                    show flareon happy
                    f "Sylveon is so cool! He’s not just strong, but his battle style is so stylish. And also he’s shiny!"
                    show flareon surprised
                    f "But he’s so mysterious too! Even though the NWI guild always invites him to join, he always rejects them."
                    show flareon happy
                    f "I really wanna do competitive battles one day, and become a cool hero like him!{nw}"
                    f "I’ve always wanted to meet him, but every time I try to catch him he always disappears for some reason??{nw}"
                    f "I actually have a Sylveon friend too, I wonder if they know each other?{nw}"
                    show flareon surprised
                    f "..."
                    f "Sorry, I get excited over battling. Hehe..."
                    jump event3_start

                "Um... Umbreon the Shadow Cleric?":
                    show flareon angry
                    f "What even is that?"
                    f "You don't even watch the tournaments, do you?"
                    show flareon neutral
                    f "Anyways."
                    show jolteon tpose with dissolve
                    jump game_over

                "Flareon the Fluff Ball?":
                    show flareon neutral
                    f "Did you just say that because I'm a Flareon?"
                    f "Of course not, Flareon’s base stats are way too weak to compete like that!"
                    show flareon sad
                    f "Saying that out loud kinda makes me..."
                    show flareon neutral
                    f "Anyways."
                    show jolteon tpose with dissolve
                    jump game_over

        "Oh... I like to play on my GamePoke instead.":
            f "I..."
            show flareon normal
            f "I love playing with my GamePoke!"
            f "Ever since Standard Tech released it, everyone’s been playing it!"
            show flareon sad
            f "It’s nice, because... It’s like competitive battles, but you don’t need good stats in real life."

            menu:
                "If you have bad stats, you just need to train harder to overcome them.":
                    f "Yeah, that’s what Vaporeon always says."
                    f "I know that hard work beats talent, but that’s only if talent doesn’t work hard too right?"
                    show flareon neutral
                    f "I know plenty of talented people who work hard. If they already have such a head start, can I never catch up?"

                "If only we could live in a world where we’re all given equal opportunity.":
                    f "Yeah, that’s what Glaceon always says."
                    f "It’d be nice if we were all born the same, but I don’t think that’ll ever happen."
                    show flareon neutral
                    f "But all my friends are so unique, and that’s what makes them fun. If they were all just the same, that’s kinda… sad?"

            show flareon surprised
            f "Oh, sorry. I’m always told to not say weird stuff, but I guess it just slipped."
            jump event3_start

        "I’m not interested in tournaments.":
            f "Mm. Why are you here again?"
            show flareon neutral
            f "Sorry, I need to get to my job at the guild. So bye."
            jump game_over


label event2_present:
    show flareon neutral
    f "Present?"
    show flareon normal
    f "!!!"
    f "It’s Vanilluxe brand chocolate! I didn’t know they sold those here!"
    show flareon neutral
    f "But it’s... expired?"
    f_silent "..."
    show flareon angry
    f "Did you just grab whatever you had at home without looking?"

    menu:
        "Yes":
            pass
        "No":
            pass
        "Maybe so":
            pass

    f_silent "..."
    show flareon sad
    f "I guess I’m just stupid for taking you so seriously."
    show jolteon tpose with dissolve
    j "You got a lot of nerve making Flareon cry while I’m around."

    $ presents = 1
    jump game_over