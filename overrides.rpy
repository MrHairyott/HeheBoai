## This file is for overriding specific declarations from DDLC
## Use this if you want to change a few variables, but don't want
## to replace entire script files that are otherwise fine.

## Normal overrides
## These overrides happen after any of the normal init blocks in scripts
## Use these to chagne variables on screens, effects, etc
init 10 python:
    pass

## LAte overrides
## These overrides happen aftre prety much everything else in startup.
## Use these to change displayables and other late definitions in renpy.
init 501 python:
    pass

## Early overrides
## These overrides happen befoer the normal init blcosk in scripts
## Use these in the rare event taht you need to overwrite some variable
## before it's called in another init blcok
## You probably wont use this
init -10 python:
    pass

## Super early overrides
## These get called before any of the init blocks are read, before the
## persistent data is read. Basically right after RenPy loads itself but 
## before the game / mod is loaded.
## You almost never will need this
python early:
    pass


label translate_ch1:
    scene bg club_day
    with dissolve_scene_half
    play music t2
    show monika 5a at t11 zorder 2

    m "Unfortunately, [player]!"
    m "Please be careful not to allow us to log in. Yes!"
    mc "At this point it is not fading."
    mc "It's really fun for me, please do not hesitate to contact me."
    show monika at thide zorder 1
    hide monika
    "Yes, he turns to the Nineveh General Assembly."
    "I am ending, so others do not allow me."
    show yuri 1a at t32 zorder 2
    y "Thank you for listening to Sindhu."
    y "I understand that is important to you."
    y 1u "Your list ..."
    show natsuki 4e at t33 zorder 2
    n "Where do we go? How long will it take?"
    n "He told me to attend this meeting."
    n "Last year!"
    n 4c "I do not want to share this message here ..."
    n "But do not despair."
    show monika 2b at l41
    m "I feel very happy to keep your book in your room."
    n 4o "Sorry!"
    show monika at lhide
    hide monika
    "Natsuki agreed that it was \"Monica\" and \"Mango\"."
    show natsuki at h33
    n 1v "A book on the mango!"
    show natsuki at thide zorder 1
    hide natsuki
    "Natsukki lives a long time."
    show yuri at t22 zorder 2
    show sayori 2x at f21 zorder 3
    s "Do not worry, children"
    s "Always happy."
    s "I work for my help."
    s "Please tell me the room."
    show sayori 2a2 at t21 zorder 2
    show yuri at f22 zorder 3
    y 2m "Oommen ..."
    show yuri at t22 zorder 2
    mc "There is a problem in your room here."
    mc "You can see your home in a short time."
    show sayori at s21
    s 5a2 "Well, he ..."
    show yuri at f22 zorder 3
    y 1s "You're a good friend"
    y "I can do many things in my guilt"
    show yuri at t22 zorder 2
    show sayori at f21 zorder 3
    s 1a2 "Good friends when you work!"
    show sayori at t21 zorder 2
    show yuri at f22 zorder 3
    y 4b "One ..."
    show yuri at t22 zorder 2
    mc "even though,"
    show sayori at f21 zorder 3
    s "Okay"
    show sayori at t21 zorder 2
    mc "..."
    "Before that, Saire's marketing bill was about me."
    show sayori at f21 zorder 3
    s 4x "It is best that you are a champion today."
    show sayori at t21 zorder 2
    show yuri at f22 zorder 3
    y 3n "Other languages ​​..."
    show yuri at t22 zorder 2
    mc "Me?"
    show yuri at f22 zorder 3
    y 3o "Ok, nothing ..."
    show yuri at t22 zorder 2
    show sayori at f21 zorder 3
    s 4r "Do not be afraid"
    show sayori at t21 zorder 2
    show yuri at f22 zorder 3
    y "Nothing at all ..."
    show yuri at t22 zorder 2
    mc "What?"
    show yuri at f22 zorder 3
    y 4c "Do not"
    y "It is important that you have important Leo important."
    y "Ok, my job is ..."
    show yuri at t22 zorder 2
    show sayori at f21 zorder 3
    s 1g "Do not allow me to go home, but ..."
    show sayori at thide zorder 1
    hide sayori
    show yuri at t11 zorder 2
    "The project has been focused on saving this theme ..."
    mc "Yes, do not be kind"
    mc "First of all, please consider the old one."
    mc "Well, you're good at it."
    mc "I'm glad you did"
    y 3v "I am ..."
    mc "But you want to do that."
    y "..."
    y 1a "That's it"
    "He wrote and wrote this book."
    y "I do not want to get it."
    y "I wondered what the book was."
    y "There are few things to know about your thoughts."
    y "If we can, then ..."
    show yuri at sink
    y 4b "Report request ..."
    "This one ..."
    "How can it be with me"
    "One book he ever thought was why he was blind"
    mc "Sorry! This prison!"
    "I like books"
    show yuri 2m at t11 zorder 2
    y "Example ..."
    y 2a "Yes, you can say it yourself."
    y "I want to hear my opinion"
    show yuri at thide zorder 1
    hide yuri

    #Exclusive scene starts here

    "At this time, Monica needs several projects at the same time."
    "But it is not."
    "This is good for Monica and Monica's ear."
    "The book is closed in the eyes of Uri."
    "I'm not interested in happy food, but it's time to wait."
    "You're leaving now."
    stop music fadeout 1
    return
