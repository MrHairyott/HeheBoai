# Joy of Painting with Bobyori Ross!

# But first, we need to talk about UNDERTALL BUTTONS!
screen ut():
        
    imagebutton auto "mod_assets/gui/ut/fight_%s.png" action Jump("bobyori_fight") hover_sound "mod_assets/sfx/ut/hover.wav" xalign 0.25 yalign 0.75
    imagebutton auto "mod_assets/gui/ut/act_%s.png" action Jump("bobyori_act") hover_sound "mod_assets/sfx/ut/hover.wav" xalign 0.75 yalign 0.75
    # Act button was later changed into Mercy button. sorry for confusion

########
# DISCLAIMER: THIS MOD IS NOT AFFILIATED WITH TOBY FOX AND TEAM SALVATO.
# THIS SCENE MAY CONTAIN SPOILERS FROM UNDERTALE.
# ALL RIGHTS RESERVED
########

transform sub:
    truecenter
    ycenter 625

image sanseyeb:
    RectCluster(Solid("#85fbff"), 2, 10, 3.5).sm
    size (20, 25)
image sanseyey:
    RectCluster(Solid("#f7ff08"), 2, 10, 3.5).sm
    size (20, 25)

label bobyori:
    $ renpy.sound.set_volume(1)
    $ style.say_dialogue = style.normal
    hide screen ut
    scene black
    hide splash_warning4 onlayer screens
    show black as b1 zorder 99:
        alpha 1
        0.25
        easein 0.75 alpha 0
    show jop:
        zoom 0.7
        truecenter
    show sayori 1a at i44 zorder 2
    show white zorder 1:
        truecenter
        zoom 0.8
        xzoom 0.79 yzoom 1.1
        rotate -0.6
        xcenter 615 ycenter 350
    
    $ pause(0.25)
    play music bobross noloop
    $ pause(0.75)
    show sayori 1a at i44:
        subpixel True
        zoom 1
        xcenter 1081
        ycenter 359
        ease 0.4 rotate -10 xcenter 1020 ycenter 400
        0.2
        ease 0.4 rotate 0 xcenter 1081 ycenter 359
        
    $ pause(1.4)
    play sound squeak
    show sayori 1a ar i44:
        subpixel True
        zoom 0.8
        xcenter 1081 ycenter 359
        parallel:
            ease 0.4 rotate -65 xcenter 775 ycenter 700
        parallel:
            0.4
            "sayori 3a"
            rotate -65
            xcenter 775 ycenter 700
            zoom 0.8
            dizzy(0.5, 0.02)
            time 1
        parallel:
            0.9
            easein_back 0.4 rotate 0 ycenter 359 xcenter 1081
        parallel:
            1.9
            easein 0.1 ycenter 389
            easeout 0.1 ycenter 359
            
    show brush zorder 3:
        subpixel True
        zoom 0.2
        rotate -65
        xcenter 670 ycenter 805
        0.9
        parallel:
            linear 1 xcenter 950 rotate 720
        parallel:
            easein_quad 0.5 ycenter 50
            easeout_quart 0.5 ycenter 360
            easein 0.1 ycenter 390
            easeout 0.1 ycenter 360
    $ pause(1.8)
    play sound fart
    $ pause(0.95)
    show sayori 3a at i11:
        subpixel True
        xcenter 1081 ycenter 359
        zoom 1
        ease 0.5 xcenter 640 ycenter 360
    show brush:
        subpixel True
        zoom 0.2
        xcenter 950 ycenter 360
        ease 0.5 xcenter 509 ycenter 361
    
    $ pause(0.85)
    show sayori 3a:
        subpixel True
        zoom 0.8
        rotate 0
        parallel:
            easeout 2 rotate 3240
            easein 2 rotate 6480
        parallel:
            easeout 1 xoffset -250
            linear 0.75 xoffset 250
            linear 0.75 xoffset -250
            linear 0.75 xoffset 250
            easein 0.75 xoffset 0
    show brush:
        subpixel True
        rotate 0
        parallel:
            easeout 2 rotate 3240
            easein 2 rotate 6480
        parallel:
            easeout 1 xoffset -250
            linear 0.75 xoffset 250
            linear 0.75 xoffset -250
            linear 0.75 xoffset 250
            easein 0.75 xoffset 0
    
    play sound sawblade fadein 2
    $ pause(0.75)
    show white:
        subpixel True
        alpha 1
        linear 2.1 alpha 0
    $ pause(1.15)
    stop sound fadeout 2
    $ pause(2.4)
    hide white
    show sayori 3a at i11:
        subpixel True
        rotate 0
        xcenter 640 ycenter 360
        zoom 1
        ease 0.5 xcenter 1081 ycenter 359
        0.25
        ease 0.4 rotate 10 xcenter 1140 ycenter 375
        0.5
        ease 0.4 rotate 0 xcenter 1081 ycenter 359
    show brush:
        subpixel True
        rotate 0
        zoom 0.2
        xcenter 509 ycenter 361 
        ease 0.5 xcenter 950 ycenter 360
        0.25
        ease 0.4 rotate 12 xcenter 1015 ycenter 346
        0.5
        ease 0.4 rotate 0 xcenter 950 ycenter 360
        
        
    
    $ pause(2.5)
    show jop:
        subpixel True
        zoom 0.7
        truecenter
        ease 1 xoffset -400
    show sayori 3a:
        subpixel True
        zoom 0.8
        ease 1 xoffset -500
    show brush:
        subpixel True
        ease 1 xoffset -500
    show monika 1d at i44:
        subpixel True
        zoom 1
        xoffset 500
        ycenter 360
        ease 1 xoffset 0
    
    $ pause(1.5)
    play sound dafug
    show sayori 3a:
        subpixel True
        zoom 0.8
        xzoom 1
        ease 0.3 xzoom -1
    show brush:
        subpixel True
        xzoom 1
        ease 0.3 xzoom -1 xoffset -230
    $ pause(1)
    show sayori 3a:
        subpixel True
        zoom 0.8
        xzoom -1
        ease 0.4 rotate -30 xoffset -550
        0.4
        easein_elastic 0.5 rotate 20 xoffset -500
        
    show brush:
        subpixel True
        xzoom -1
        xoffset -230
        ease 0.4 rotate -45 xoffset -300 ycenter 300
        0.4
        linear 0.225 rotate 360 xoffset 400
    
    show monika 1d:
        subpixel True
        zoom 0.8
        xoffset 0
        ycenter 360
        0.9
        linear 0.15 xoffset 600 rotate 50
        
    $ pause(0.75)
    show black:
        truecenter
        zoom 3
    play sound whoosh
    $ pause(0.1)
    play audio fistman
    $ pause(0.55)
    play sound glass
    hide monika
    hide brush
    show layer master:
        subpixel True
        truecenter
        xoffset -50 yoffset -50 rotate 10
        parallel:
            easein_elastic 0.75 xoffset 0
        parallel:
            0.1
            easein_elastic 0.75 yoffset 0
        parallel:
            easein_elastic 0.85 rotate 0
    $ pause(0.3)
    
    show sayori 3a:
        subpixel True
        rotate 20
        zoom 0.8
        xzoom -1
        ease 0.4 rotate 0
    
    $ pause(0.85)
    show sayori 3a:
        subpixel True
        zoom 0.8
        xoffset -500 xzoom -1
        easeout 0.2 xzoom 0
        "sayori 1a"
        easein 0.2 xzoom 1
    $ pause(0.8)
    show jop:
        subpixel True
        zoom 0.7
        xoffset -400
        truecenter
        ease 1 xoffset 0
    show sayori 1a:
        subpixel True
        zoom 0.8
        xoffset -500
        ease 1 xoffset 0
    $ pause(1.6)
    play sound gasp
    show sayori 1a:
        subpixel True
        zoom 0.8
        easein 0.1 yoffset -40
        easeout 0.1 yoffset 0
        0.3
        xcenter 1081
        ycenter 359
        ease 0.4 rotate -10 xcenter 1020 ycenter 400
        0.75
        ease 1.5 rotate 10 xcenter 1085 ycenter 359
        0.8
        ease 0.4 rotate 0 xcenter 1081
        0.4
        "sayori 4a"
        easein 0.1 yoffset -20
        easeout 0.1 yoffset 0
    
    $ pause(1.6)
    show splash_warning2 "{color=#000}The{/color}" zorder 5 as sp0:
        subpixel True
        pos (440, 86)
        zoom 1.2
        yoffset 750
        easein_back 1 yoffset 0
    show splash_warning2 "The" zorder 6:
        subpixel True
        pos (438, 84)
        zoom 1.2
        yoffset 750
        easein_back 1 yoffset 0
    show splash_warning4 "{size=75}Joy of\nPainting{/size}" zorder 5:
        subpixel True
        pos (550, 200)
        yoffset 750
        0.4
        easein_back 1 yoffset 0
    show splash_warning2 "{color=#000}with Bobyori Ross{/color}" zorder 5 as sp1:
        subpixel True
        pos (550, 320)
        zoom 1.2
        yoffset 750
        0.8
        easein_back 1 yoffset 0
    show splash_warning2 "with Bobyori Ross" zorder 6 as sp2:
        subpixel True
        pos (548, 318)
        zoom 1.2
        yoffset 750
        0.8
        easein_back 1 yoffset 0
    $ pause(2.95)
    play sound cat
    $ pause(0.9)
    show layer master:
        subpixel True
        truecenter
        xcenter 640 ycenter 360
        easeout 1.5 zoom 1.5 xcenter 300 ycenter 500
    show black as b1 zorder 10:
        alpha 0
        1.5
        linear 1 alpha 1
    show sayori 4a:
        subpixel True
        zoom 0.8 xcenter 1081 ycenter 359
        parallel:
            easeout 1.5 zoom 1 xcenter 1015 ycenter 425
    $ pause(3)
    
label bobyori2:   # i am fucking tired of yzooms
    hide screen ut
    hide splash_warning4 onlayer screens
    show layer master
    scene black
    with None
    show jop2:
        zoom 0.7
        truecenter
    show sayori 1a at i22:
        xcenter 500
        zoom 1
    with Dissolve(0.5)
    $ pause(0.35)
    play sound2 b_hello
    show sayori 1a:
        subpixel True
        zoom 0.8
        yzoom 1
        0.3
        linear 0.05 yzoom 1.1
        linear 0.05 yzoom 1
        0.01
        linear 0.05 yzoom 1.125
        linear 0.15 yzoom 1
        0.01
        linear 0.03 yzoom 1.05
        linear 0.03 yzoom 1
        0.05
        linear 0.03 yzoom 1.05
        linear 0.03 yzoom 1
        0.05
        linear 0.05 yzoom 1.3
        easein 0.45 yzoom 1
    $ pause(0.3)
    show splash_warning4 "Hello, I'm Bob Ross" at sub onlayer screens
    $ pause(1.25)
    hide splash_warning4 onlayer screens
    play sound2 b_welcome
    show sayori 1a:
        subpixel True
        zoom 0.8
        yzoom 1
        0.032
        linear 0.05 yzoom 1.05
        linear 0.05 yzoom 1
        0.02
        linear 0.05 yzoom 1.05
        linear 0.05 yzoom 1
        0.065
        linear 0.05 yzoom 1.05
        linear 0.05 yzoom 1
        0.065
        linear 0.05 yzoom 1.075
        linear 0.05 yzoom 1
        0.15
        linear 0.025 yzoom 1.075
        linear 0.25 yzoom 1
        linear 0.05 yzoom 1.1
        linear 0.15 yzoom 1
        #0.07
        #linear 0.04 yzoom 1.075
        #linear 0.04 yzoom 1
    $ pause(0.1)
    show splash_warning4 "and I'd like to welcome you to" at sub onlayer screens
    $ pause(1.2)
    show layer master:
        zoom 1.2
        xcenter 740 ycenter 390
    show splash_warning4 "touch" at sub onlayer screens
    $ pause(0.3)
    show layer master:
        zoom 1.4
        xcenter 790 ycenter 450
    show splash_warning4 "my" at sub onlayer screens
    $ pause(0.315)
    show layer master:
        zoom 1.6
        xcenter 840 ycenter 510
    show splash_warning4 "happy" at sub onlayer screens
    $ pause(0.385)
    show layer master:
        zoom 1.9
        xcenter 915 ycenter 600
    show splash_warning4 "parts." at sub onlayer screens
    $ pause(0.6)
    hide splash_warning4 onlayer screens
    play sound2 b_giggle
    show sayori 5a:
        subpixel True
        zoom 0.8
        0.25
        linear 0.07 yzoom 1.1
        easein 0.13 yzoom 1
        linear 0.045 yzoom 1.075
        easein 0.105 yzoom 1
        linear 0.08 yzoom 1.05
        easein 0.22 yzoom 1
        0.05
        linear 0.08 yzoom 1.1
        easein 0.12 yzoom 1
    $ pause(0.25)
    show splash_warning4 "{i}*Giggle*{/i}" at sub onlayer screens
    $ pause(1.5)
    hide splash_warning4 onlayer screens
    play sound2 b_cock
    show layer master:
        zoom 1.6
        xcenter 900 ycenter 510
    show sayori 2a:
        subpixel True
        zoom 0.8
        yzoom 1
        0.1
        linear 0.1 yzoom 1.05
        linear 0.1 yzoom 1
        linear 0.075 yzoom 1.075
        easein 0.125 yzoom 1
        
    hide black
    show black behind jop2:
        truecenter
        zoom 1.1
        
    $ pause(0.1)
    show splash_warning4 "I have a thin 24 inch white cock." at sub onlayer screens
    $ pause(0.25)
    show layer master:
        subpixel True
        zoom 1.6
        xcenter 900 ycenter 510
        ease 0.4 ycenter 125
    show white zorder 2:
        zoom 0.25
        truecenter
        xcenter 350 ycenter 660
        yzoom 0.1
    $ pause(1.13)
    show layer master:
        subpixel True
        zoom 1.6 xcenter 900 ycenter 125
        easein 0.14 zoom 2.5 xcenter 1200 ycenter -225
        easeout 0.14 zoom 1.6 xcenter 900 ycenter 125
        ease 0.5 zoom 1.8 xcenter 900 ycenter 600
        block:
            xzoom -1
            xcenter 400
            0.01
            xzoom 1
            xcenter 900
            0.01
            repeat
            time 0.48
            zoom 1.0
            xzoom 1
            xcenter 640 ycenter 360
    show black zorder 9 as b1:
        alpha 0
        1.26
        alpha 1
    show splash_warning2 "{size=50}{b}CENSORED{/b}" zorder 10:
        truecenter
        alpha 0
        1.26
        alpha 1
    $ pause(0.28)
    hide splash_warning4 onlayer screens
    $ pause(0.32)
    show splash_warning4 "SuuS" at sub onlayer screens
    $ pause(0.28)
    hide splash_warning4 onlayer screens
    $ pause(0.42)
    show splash_warning4 "Stroke the big 24 inch cock," at sub onlayer screens
    $ pause(1.7)
    hide splash_warning4 onlayer screens
    $ pause(0.595)
    show splash_warning4 "and we're still using litte criss cross strokes." at sub onlayer screens
    $ pause(2.025)
    hide splash_warning4 onlayer screens
    $ pause(0.4)
    show splash_warning4 "There..." at sub onlayer screens
    $ pause(0.55)
    hide splash_warning4 onlayer screens
    $ pause(0.28)
    show splash_warning4 "Mmm-!" at sub onlayer screens
    $ pause(0.45)
    show sayori 1a
    hide splash_warning4 onlayer screens
    hide b1
    hide splash_warning2
    show layer master:
        zoom 1.8 xcenter 900 ycenter 600
    $ pause(0.25)
    show splash_warning4 "That's the fun part." at sub onlayer screens
    show sayori 1a:
        subpixel True
        zoom 0.8
        yzoom 1
        linear 0.05 yzoom 1.075
        linear 0.05 yzoom 1
        0.10
        linear 0.03 yzoom 1.05
        linear 0.04 yzoom 1
        0.01
        linear 0.06 yzoom 1.075
        easein 0.12 yzoom 1
        0.02
        linear 0.08 yzoom 1.05
        easein 0.07 yzoom 1
        linear 0.05 yzoom 1.09
        linear 0.05 yzoom 1
    $ pause(1.5)
    hide splash_warning4 onlayer screens
    hide white
    show layer master
    window show(None)
    window auto
    show black:
        zoom 2
    m "Hey, Sayori..."
    window hide(None)
    window auto
    show sayori 5c
    play audio ball
    play audio ugh 
    $ pause(0.75)
    show sayori 5c:
        subpixel True
        zoom 0.8
        xzoom 1
        ease 0.2 xzoom -1
    $ pause(0.05)
    play sound whoosh
    $ pause(0.7)
    play sound fart2
    show layer master:
        subpixel True
        truecenter
        xcenter 640
        ease 0.5 xcenter 250
    show monika 1d at i11:
        zoom 1
        xcenter 1500
    $ pause(0.65)
    play sound chicken
    show monika 1g at i11:
        subpixel True
        zoom 1
        xcenter 1500
        yoffset 0
        easein 0.125 yoffset -20
        easeout 0.125 yoffset 0
    window show(None)
    window auto
    m "Ah... I didn't mean to distract you or anything!"
    show layer master:
        truecenter
        zoom 1.5
        xcenter -350 ycenter 500
    m 1i "Hold on a second..."
    m "You're not Sayori, are you?"
    window hide(None)
    window auto
    show layer master:
        subpixel True
        xcenter -350 ycenter 500
        zoom 1.5
        ease 0.55 xcenter 500
    $ pause(0.9)
    play sound shake
    show sayori 5c:
        subpixel True
        zoom 0.8
        ycenter 359
        ease 0.125 rotate 10
        ease 0.125 rotate 0
        ease 0.125 rotate 10
        ease 0.125 rotate 0
        ease 0.125 rotate 10
        ease 0.125 rotate 0
    $ pause(1.2)
    show layer master:
        subpixel True
        xcenter 500 ycenter 500
        zoom 1.5
        ease 0.55 xcenter -350
    $ pause(1.35)
    show monika 1q:
        subpixel True
        zoom 0.8
        xcenter 1500 ycenter 360 rotate 0
        easein 0.5 rotate -10 xcenter 1480 ycenter 380
    window show(None)
    window auto
    m "{i}*Sigh*{/i}"
    m "..."
    show monika 1q zorder 2 as m1:
        subpixel True
        alpha 1
        zoom 0.8
        xcenter 1480 ycenter 380 rotate -10
        ease 0.25 rotate 0 xcenter 1500 ycenter 360 alpha 0
    show monika 1h:
        subpixel True
        zoom 0.8
        xcenter 1480 ycenter 380 rotate -10
        ease 0.25 rotate 0 xcenter 1500 ycenter 360
    m "..."
    hide m1
    m "Well, then..."
    m 2h "Listen, whoever you are."
    show layer master:
        zoom 1.75 xcenter -600 ycenter 550
    m 2d "What is up with this show?"
    m "Are you trying to paint?"
    m "I didn't see any reason why you started a show like this."
    m 2c "Look..."
    m "You're now just rubbing your...whatever that is called."
    m 2h "It's not a part of the show. The part is that you need to start your job in the first place."
    m "...And you haven't done it."
    m 4d "So why?"
    m "Why did you start this show when you do things that you shouldn't? To be ignorant? To distract the audiences?"
    m 2q "Well, I don't like to say this, but..."
    m "I guess there are plenty of artists in the world who are more kind, and they made some beautiful art."
    m 2h "More beautiful than your {i}crappy{/i} art." #Roasted.
    window hide(None)
    window auto
    show layer master:
        subpixel True
        zoom 1.75 xcenter -600 ycenter 550
        ease 0.25 xcenter 500 
    $ pause(0.25)
    play audio alert
    show splash_warning4 "{size=+60}!{/size}" as sp0:
        xcenter 700 ycenter -200
        easein_elastic 0.75 ycenter 200
    show splash_warning4 "{size=200}!{/size}" as sp1 behind sp0:
        alpha 0
        0.05
        alpha 0.15
        xcenter 699 ycenter -200
        easein_elastic 0.75 ycenter 200
    show sayori 5c:
        subpixel True
        zoom 0.8
        ycenter 360
        linear 0.05 yzoom 1.4
        easein_elastic 0.75 yzoom 1
    $ pause(0.85)
    hide sp0
    hide sp1
    play audio fatality
    show speedline at SL onlayer front zorder 1:
        alpha 0
        SP
        linear 0.25 alpha 1
    show layer master:
        subpixel True
        zoom 1.75 xcenter 500 ycenter 550
        easein_back 0.4 zoom 3.5 xcenter 750 ycenter 800
        linear 3.5 xcenter 1090
    show black onlayer front as bdown:
        subpixel True
        alpha 1
        ycenter 1080
        easein_back 0.4 ycenter 800
    show black onlayer front as bup:
        subpixel True
        alpha 1
        ycenter -400
        easein_back 0.4 ycenter -100
    show vignette onlayer front as vig:
        alpha 0
        0.4
        linear 1.8 alpha 0.6
        
    $ pause(2.3)
    hide bup onlayer front
    hide bdown onlayer front
    hide vig onlayer front
    hide speedline onlayer front
    show layer master:
        zoom 1.75 xcenter -600 ycenter 550
    window show(None)
    window auto
    m 3d "And one more thing..."
    m 3g "Is that Natsuki with the disturbing black eyes behind you?"
    window hide(None)
    window auto
    show layer master:
        subpixel True
        zoom 1.75 xcenter -600 ycenter 550
        ease 0.5 zoom 1 xcenter 300 ycenter 360
    $ pause(0.75)
    show sayori 5c:
        subpixel True
        zoom 0.8
        xzoom -1
        ease 0.2 xzoom 1
    $ pause(0.05)
    play sound whoosh
    $ pause(0.6)
    show layer master:
        subpixel True
        zoom 1 xcenter 300 ycenter 360
        ease 1 xcenter 750
    show natsuki ghost2 at i11 zorder 2:
        zoom 1
        xcenter 100 
        dizzy(1, 0.01)
    show n_rects zorder 4 as rectr:
        xcenter 108 ycenter 250
        dizzy(1, 0.01)
    show n_rects zorder 4 as rectl:
        xcenter 40 ycenter 257
        dizzy(1, 0.01)
    $ pause(1.5)
    show sayori 5c:
        subpixel True
        zoom 0.8
        rotate 0
        xcenter 500
        ease 0.25 rotate -20 xcenter 250
    $ pause(0.25)
    show sayori 5c:
        subpixel True
        zoom 0.8 rotate -20
        xcenter 250
        ease_expo 0.5 rotate 0 xcenter 500
    show natsuki ghost2:
        subpixel True
        zoom 0.81 xcenter 100
        rotate 0
        ycenter 360
        parallel:
            dizzy(1, 0.01)
        parallel:
            ease_expo 0.5 rotate 60 xcenter 450 ycenter 400
    show n_rects zorder 4 as rectr:
        subpixel True
        xcenter 108 ycenter 250
        parallel:
            dizzy(1, 0.01)
        parallel:
            ease_expo 0.5 rotate 60 xcenter 550 ycenter 357
    show n_rects zorder 4 as rectl:
        subpixel True
        xcenter 40 ycenter 257
        parallel:
            dizzy(1, 0.01)
        parallel:
            ease_expo 0.5 rotate 60 xcenter 507 ycenter 300
    $ pause(0.8)
    play sound2 subaluwa_f
    show sayori 5c:
        subpixel True
        xcenter 500
        zoom 0.8
        rotate 0
        ycenter 360
        parallel:
            dizzy(1.5, 0.02)
            time 1.5
            xoffset 0 yoffset 0
        parallel:
            1.35
            ease 0.1 rotate -15 xcenter 495
            easein 0.35 rotate 380 xcenter 515
    show natsuki ghost2:
        subpixel True
        zoom 0.81
        rotate 60
        ycenter 400
        parallel:
            dizzy(1, 0.01)
        parallel:
            1.35
            ease 0.1 ycenter 410
            easein 0.35 ycenter 300
    show n_rects zorder 4 as rectr:
        subpixel True
        ycenter 357
        rotate 60
        parallel:
            dizzy(1, 0.01)
        parallel:
            1.35
            ease 0.1 ycenter 367
            easein 0.35 ycenter 257
    show n_rects zorder 4 as rectl:
        subpixel True
        ycenter 300
        rotate 60
        parallel:
            dizzy(1, 0.01)
        parallel:
            1.35
            ease 0.1 ycenter 310    
            easein 0.35 ycenter 200
    $ pause(1.75)
    
    show sayori 5c:
        subpixel True
        xcenter 515
        zoom 0.8
        rotate 20
        ycenter 360
        easeout_quint 0.2 rotate -10 xcenter 495
    show natsuki ghost2:
        subpixel True
        zoom 0.81
        rotate 60
        ycenter 300
        parallel:
            dizzy(1, 0.01)
        parallel:
            easeout_quint 0.2 ycenter 410
    show n_rects zorder 4 as rectr:
        subpixel True
        ycenter 257
        rotate 60
        parallel:
            dizzy(1, 0.01)
        parallel:
            easeout_quint 0.2 ycenter 367
    show n_rects zorder 4 as rectl:
        subpixel True
        ycenter 200
        rotate 60
        parallel:
            dizzy(1, 0.01)
        parallel:
            easeout_quint 0.2 ycenter 310
    $ pause(0.15)
    play sound neck
    show natsuki ghost3:
        subpixel True
        zoom 0.81 rotate 60 ycenter 410
        parallel:
            dizzy(1, 0.01)
        parallel:
            xoffset 10 yoffset -40
            easein_elastic 0.75 xoffset 0 yoffset 0
    show n_rects zorder 4 as rectr:
        subpixel True
        ycenter 503 rotate 150 xcenter 485
        parallel:
            dizzy(1, 0.01)
        parallel:
            xoffset 10 yoffset -40
            easein_elastic 0.75 xoffset 0 yoffset 0
    show n_rects zorder 4 as rectl:
        subpixel True
        xcenter 550 ycenter 468 rotate 150
        parallel:
            dizzy(1, 0.01)
        parallel:
            xoffset 10 yoffset -40
            easein_elastic 0.75 xoffset 0 yoffset 0
    $ pause(1.05)
    
    show layer master:
        zoom 1.75 xcenter -600 ycenter 550
    show monika 1i at i11:
        subpixel True
        zoom 1
        xcenter 1500
        yoffset 0
        ycenter 360
        linear 0.085 yoffset -20
        linear 0.085 yoffset 0
    play sound quack
    $ pause(0.9)
    
    show layer master:
        subpixel True
        zoom 1.75 xcenter -600 ycenter 550
        ease 0.75 zoom 1 xcenter 750 ycenter 360
    $ pause(1.4)
    show natsuki ghost3:
        subpixel True
        zoom 0.81 rotate 60 ycenter 410
        parallel:
            dizzy(1, 0.01)
        parallel:
            easeout 0.6 ycenter 1410
    show n_rects zorder 4 as rectr:
        subpixel True
        ycenter 503 rotate 150 xcenter 485
        parallel:
            dizzy(1, 0.01)
        parallel:
            easeout 0.6 ycenter 1485
    show n_rects zorder 4 as rectl:
        subpixel True
        xcenter 550 ycenter 468 rotate 150
        parallel:
            dizzy(1, 0.01)
        parallel:
            easeout 0.6 ycenter 1468
    show sayori 5c:
        subpixel True
        xcenter 495
        zoom 0.8
        rotate -10
        ycenter 360
        ease 0.4 rotate 0 xcenter 515
    $ pause(0.4)
    play sound fall2
    $ pause(0.9)
    show monika 1h
    hide natsuki
    hide rectr
    hide rectl
    show layer master:
        subpixel True
        zoom 1 xcenter 750 ycenter 360
        ease 1 xcenter 300
    show sayori 5c:
        subpixel True
        zoom 0.8
        xzoom 1
        ease 0.2 xzoom -1
    $ pause(0.05)
    play sound whoosh
    $ pause(1.6)
    m "..."
    show layer master:
        zoom 1.75 xcenter -600 ycenter 550
    hide sayori
    m 2h "Well, you just broke Natsuki's neck."
    m "But still, you should've learned to hustle up instead of going insane." #nobody cares about your pathetic show."
    show layer master:
        subpixel True
        zoom 1.75 xcenter -600 ycenter 550
        easein_circ 0.75 zoom 2 xcenter -850 ycenter 600
    show vignette onlayer front:
        alpha 0
        easein_circ 0.75 alpha 0.25
    m 2c "In fact, I have a {i}good{/i} chance to delete you, but I'd also end up deleting Sayori inside you."
    window hide(None)
    show sayori 5c at i22:
        zoom 1
        xcenter 515 ycenter 360
        xzoom -1
    show layer master:
        subpixel True
        zoom 2 xcenter -850 ycenter 600
        ease 0.25 zoom 1.75 xcenter 750 ycenter 550
    show vignette onlayer front:
        alpha 0.25
        ease 0.25 alpha 0
    $ pause(0.35)
    hide vignette onlayer front
    show monika 2h
    play sound2 b_fuck
    show sayori 5c at i22:
        subpixel True
        zoom 1
        xcenter 515
        ycenter 360
        xzoom -1
        linear 0.1 yzoom 1.15
        linear 0.1 yzoom 1
        linear 0.1 yzoom 1.2
        easein 0.2 yzoom 1
    $ pause(0.01)
    show layer screens
    show splash_warning4 "Fuck you." at sub onlayer screens
    $ pause(0.85)
    hide splash_warning4 onlayer screens
    show layer screens:
        SP
        TC
        zoom 1.5 yoffset 200 nearest True
        easein_elastic 1 yoffset 0
###### Trying to change the cursor to heart, but
###### it resets back to normal everytime -_-
#    $ config.mouse = {"default": [
#                                ("mod_assets/gui/ut/heart.png", 25, 25),
#                                ("mod_assets/gui/ut/heart.png", 25, 25),
#                                ("mod_assets/gui/ut/heart.png", 25, 25),
#                                ("mod_assets/gui/ut/heart.png", 25, 25),
#                                ("mod_assets/gui/ut/heart.png", 25, 25),
#                                ("mod_assets/gui/ut/heart.png", 25, 25),
#                                ("mod_assets/gui/ut/heart.png", 25, 25),
#                                ("mod_assets/gui/ut/heart.png", 25, 25),
#                                ("mod_assets/gui/ut/heart.png", 25, 25),
#                                ("mod_assets/gui/ut/heart.png", 25, 25),
#                                ("mod_assets/gui/ut/heart.png", 25, 25),
#                                ("mod_assets/gui/ut/heart.png", 25, 25),
#                                ("mod_assets/gui/ut/heart.png", 25, 25),
#                                ("mod_assets/gui/ut/heart.png", 25, 25),
#                                ("mod_assets/gui/ut/heart.png", 25, 25),
#                                ]}
    play sound whoosh2
    call screen ut()
    return
############# We don't need this right now....##################

#    show act at truecenter as ac:
#        subpixel True
#        zoom 1.5 xcenter 720 ycenter 390
#        yoffset 150
#        parallel:
#            easein_elastic 1 yoffset 0
#        parallel:
#            0.65
#            "act_h"
#            0.95
#            "act"
#            0.95
#            "act_h"
#            1.45
#            "act"
#    show fight at truecenter as fi:
#        subpixel True
#        zoom 1.5 xcenter 400 ycenter 390
#        yoffset 150
#        0.5
#        parallel:
#            easein_elastic 1 yoffset 0
#        parallel:
#            1.1
#            "fight_h"
#            0.95
#            "fight"
#            1.45
#            "fight_h"
#    show sayori 5c at i22:
#        subpixel True
#        zoom 1
#        xcenter 515 ycenter 360
#        xzoom -1 rotate 0
#        0.4
#        ease 0.25 rotate 15 xcenter 540
#        0.75
#        ease 0.2 xzoom 1 rotate -15 xcenter 560
#        0.75
#        ease 0.2 xzoom -1 rotate 15 xcenter 540
#        1.25
#        ease 0.2 xzoom 1 rotate -15 xcenter 560
        
#    $ pause(0.05)
#    play audio whoosh2
#    $ pause(0.45)
#    play audio whoosh2
#    $ pause(0.1)
#    play audio ut_hover
#    $ pause(0.7)
#    play audio whoosh
#    $ pause(0.15)
#    play audio ut_hover
#    $ pause(0.65)
#    play audio whoosh
#    $ pause(0.11)
#    play audio ut_hover
#    $ pause(1.25)
#    play audio whoosh
#    $ pause(0.16)
#    play audio ut_hover
#    $ pause(0.5)
label bobyori_fight:
    hide screen ut
    show layer screens
    play audio ut_select
    show layer master:
        subpixel True
        zoom 1.75 xcenter -600 ycenter 550
    $ pause(0.4)
    show monika 1d at i11:
        subpixel True
        zoom 1
        xcenter 1500
        yoffset 0
        ycenter 360
        easein 0.1 yoffset -20
        easeout 0.1 yoffset 0
    $ pause(0.5)
    play sound ut_swing # MONIKA = SANS CONFIRMED?
    
    show monika 1d at i11:
        subpixel True
        zoom 1
        xcenter 1500 ycenter 360
        easein_quint 0.5 zoom 0.85 xcenter 1465 alpha 0.5
        0.65
        ease_quint 0.75 zoom 1 xcenter 1500 alpha 1
    show brush zorder 2:
        subpixel True
        zoom 0.15
        xcenter 900 ycenter 290
        rotate 0
        linear 0.5 xcenter 1750 rotate 720
    $ pause(0.95)
    
    if config.developer or renpy.random.randint(0, 3) == 0:
        play sound [ "<silence 1.25>", ut_ding ]
        show sanseyeb at truecenter:
            xcenter 1532 ycenter 200
            alpha 0
            1.25
            block:
                0.01
                alpha 1
                0.01
                alpha 0
                repeat
        show sanseyey at truecenter:
            xcenter 1532 ycenter 200
            alpha 0
            1.25
            alpha 1
            block:
                0.01
                alpha 0
                0.01
                alpha 1
                repeat
                
    play sound2 bum
    show splash_warning4 "{size=+60}{k=10}MISS{/k}{/size}" onlayer screens:
        truecenter
        subpixel True
        zoom 1
        xcenter 900 ycenter 90
        easein 0.1 yoffset -50
        easein_elastic 1.25 yoffset 0
        easeout 0.25 alpha 0
    $ pause(0.4)
    m "Okay! Okay!"
    hide sanseyeb
    hide sanseyey
    stop sound
    m 1c "Jesus Christ, I didn't mean that."
    m 1f "Can you get started already?"
    hide splash_warning4 onlayer screens
    window hide(None)
    show sayori 5c at i22:
        zoom 1
        xcenter 515 ycenter 360
        xzoom -1
        rotate 0
    show layer master:
        subpixel True
        zoom 1.75 xcenter -600 ycenter 550
        ease 0.25 xcenter 750
    $ pause(0.75)
label bobyori_end:
    show sayori 5c at i22:
        subpixel True
        zoom 1
        xcenter 515 ycenter 360
        xzoom -1
        rotate 0
        ease 0.25 rotate 30 xcenter 550 ycenter 475
        0.25
        ease 0.25 rotate 0 xcenter 515 ycenter 360
    show brush zorder 1:
        subpixel True
        zoom 0.15
        alpha 0
        truecenter
        ycenter 515 xcenter 640
        rotate 60
        0.5
        parallel:
            ease 0.25 xcenter 610 rotate 30 ycenter 350
        parallel:
            easein 0.05 alpha 1
    $ pause(1.25)
    play sound scored
    show sayori 2a at i11:
        subpixel True
        zoom 1 xzoom 1
        xcenter 515 ycenter 360
        easein 0.1 yoffset -15
        easeout 0.1 yoffset 0
    show brush:
        subpixel True
        zoom 0.15
        xcenter 670 ycenter 330
        rotate 30
        easein 0.1 yoffset -15
        easeout 0.1 yoffset 0
    $ pause(1.25)
    show layer master:
        subpixel True
        zoom 1.75 xcenter 750 ycenter 550
        ease 0.5 xcenter 100
    $ pause(0.85)
    play sound sawblade fadein 1
    show brush zorder 1:
        zoom 0.15
        xcenter 670 ycenter 330
        rotate 30
        easeout 0.5 rotate 390 xcenter 940 ycenter 250
        parallel:
            dizzy(7, 0.05)
            time 1.5
        parallel:
            rotate 30
            linear 1.5 rotate 1830
            repeat
            time 1.5
        parallel:
            1.5
            rotate -330
            easein 0.5 rotate 30 xcenter 670 ycenter 330 xoffset 0 yoffset 0
    show image "mod_assets/spysuki/2bt.png" as spy:
        zoom 0.8
        xcenter 950 ycenter 360
        xzoom 0.8
        rotate -0.5
        alpha 0
        0.75
        linear 1.5 alpha 1
    $ pause(1.75)
    stop sound fadeout 1
    $ pause(1.5)
    show layer master:
        subpixel True
        zoom 1.75 xcenter -600 ycenter 550
    show monika 1d
    m "Oh..."
    show layer master:
        subpixel True
        zoom 1.75 xcenter -600 ycenter 550
        easein_elastic 1 zoom 2 xcenter -850 ycenter 600
    m "My..."
    show layer master:
        subpixel True
        zoom 2 xcenter -850 ycenter 600
        easein_elastic 1 zoom 2.25 xcenter -1100 ycenter 650
    m "God..."
    show layer master:
        zoom 2.25 xcenter 0 ycenter 600
    show monika 1i
    play sound cow
    $ pause(2.25)
    show layer master:
        subpixel True
        zoom 2.25 xcenter 0 ycenter 600
        ease 1.5 zoom 1.3 xcenter 100 ycenter 450
    show monika 1i at i11 zorder 1:
        subpixel True
        zoom 1 xcenter 1500 ycenter 360
        parallel:
            ease 2 xcenter 1250
        parallel:
            ease 1 yoffset -20
            ease 1 yoffset 0
    $ pause(0.8)
    m "Is that Natsuki..."
    m "with a..."
    show monika 3d
    m "...masked face?"
    $ cocaine_level = 25
    play sound spy
    window hide(None)
    show layer master:
        subpixel True
        zoom 1.3 xcenter 100 ycenter 450
        parallel:
            1
            easeout_expo 1 zoom 6 xcenter -1000 ycenter 690
        parallel:
            0.7
            function lineardizzy
    $ pause(2)
    $ cocaine_level = 1
    scene black
    stop sound
    show jop:
        zoom 1.2 xcenter 650 ycenter 360
    show vignette:
        alpha 1
        block:
            ease 1 alpha 0.5
            ease 1 alpha 1
            repeat
    play music bobross2 noloop
    show splash_warning2 "Director:\nBobyori Ross\n\n\nProducer:\nBobyori Ross\n\n\nCamera:\nMy papa UwU\n\n\nSpecial thanks:\nMonika\n(For interrupting my show)\n\n\nCopyright 2069\nBobyori Ross, Inc.\nWanna sprite cranberry?\n\n{size=25}Wait, the meme is dead?\nsorry.{/size}" as sp1 zorder 1:
        subpixel True
        ycenter 1100
        linear 5 ycenter -500
    show splash_warning2 "{color=#000}Director:\nBobyori Ross\n\n\nProducer:\nBobyori Ross\n\n\nCamera:\nMy papa UwU\n\n\nSpecial thanks:\nMonika\n(For interrupting my show)\n\n\nCopyright 2069\nBobyori Ross, Inc.\nWanna sprite cranberry?\n\n{size=25}Wait, the meme is dead?\nsorry.{/size}{/color}" as sp2:
        subpixel True
        xoffset 2 yoffset 2
        ycenter 1100
        linear 5 ycenter -500
    show wannasprite:
        subpixel True
        zoom 0.25
        xcenter 860 ycenter 1100 yoffset 325 rotate 10
        linear 5 ycenter -500
    $ pause(5)
    hide sp1
    hide sp2
    hide wannasprite
    show splash_warning2 "R.I.P Bob Ross\nThe First ASMR Painter." as sp1 zorder 1:
        subpixel True
        truecenter
        linear 5 zoom 1.2
    show splash_warning2 "{color=#000}R.I.P Bob Ross\nThe First ASMR Painter.{/color}" as sp2:
        truecenter
        xoffset 2 yoffset 2
        subpixel True
        linear 5 zoom 1.2
    with Dissolve(1)
    $ pause(3)
    scene black
    with Dissolve(1)
    $ pause(0.75)
    stop music fadeout 2
    $ pause(2)
    return

image monikas_big_tight_smooth_and_juicy_ass_remastered:
    "monika/3a.png"
    crop (330, 590, 409, 345)

label bobyori_act:
    hide screen ut
    play audio ut_select
    show layer screens
    $ config.mouse = None
    $ pause(0.4)
    hide sayori
    play sound b_extend
    show sayori 5c at i11:
        center
        subpixel True
        zoom 1 xcenter 515 ycenter 360 xzoom -1
        linear 0.05 yzoom 1.1
        linear 0.15 yzoom 1
        0.05
        linear 0.05 yzoom 1.05
        linear 0.05 yzoom 1
        linear 0.05 yzoom 1.05
        linear 0.15 yzoom 1
        0.1
        linear 0.1 yzoom 1.1
        linear 0.1 yzoom 1
        linear 0.1 yzoom 1.1
        linear 0.1 yzoom 1
        0.125
        linear 0.05 yzoom 1.2
        easein 0.35 yzoom 1
        0.025
        linear 0.05 yzoom 1.05
        linear 0.05 yzoom 1
        0.1
        linear 0.05 yzoom 1.1
        linear 0.05 yzoom 1
        linear 0.05 yzoom 1.1
        linear 0.05 yzoom 1
        linear 0.05 yzoom 1.05
        linear 0.1 yzoom 1
        0.05
        linear 0.05 yzoom 1.25
        linear 0.1 yzoom 1
        0.15
        linear 0.1 yzoom 1.025
        linear 0.1 yzoom 1
        linear 0.05 yzoom 1.05
        linear 0.1 yzoom 1
        linear 0.1 yzoom 1.025
        linear 0.1 yzoom 1
        0.05
        linear 0.05 yzoom 1.05
        linear 0.05 yzoom 1
        linear 0.05 yzoom 1.15
        easein 0.15 yzoom 1
        
    show splash_warning4 "Let me extend your personal invitation for you to drag out your" at sub onlayer screens
    $ pause(2.23)
    hide splash_warning4 onlayer screens
    show monikas_big_tight_smooth_and_juicy_ass_remastered onlayer screens:
        TC
        zoom 0.5 ycenter 640
        dizzy(2, 0.01)
    $ pause(0.23)
    hide monikas_big_tight_smooth_and_juicy_ass_remastered onlayer screens
    $ pause(0.1) 
    show splash_warning4 "and paint along with us." at sub onlayer screens
    $ pause(1.25)
    hide splash_warning4 onlayer screens
    show layer master:
        zoom 1.75 xcenter -600 ycenter 550
    show monika 1d at i11:
        subpixel True
        zoom 1
        xcenter 1500
        yoffset 0
        ycenter 360
        easein 0.1 yoffset -15
        easeout 0.1 yoffset 0
    m "Huh? Me...?" 
    m 1e "Sorry, but I don't know how to paint..."
    m "I read poetry more often than creating art."
    m "I'm pretty glad if you invite Yuri to paint along with you."
    m 1f "I'm not used to be a professional painter, so... yeah."
    window hide(None)
    show sayori 5c at i22:
        zoom 1
        xcenter 515 ycenter 360
        xzoom -1
        rotate 0
    show layer master:
        subpixel True
        zoom 1.75 xcenter -600 ycenter 550
        ease 0.25 xcenter 750
    $ pause(0.75)
    jump bobyori_end
