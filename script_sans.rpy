#Sand Undertall in DDLC !!!
screen ch1_choice():
    
    style_prefix "NYEH"
    
    hbox:
        frame:
            textbutton "Yes" action Jump("ch1_s3_yes") at c_trans
        frame:
            textbutton "No" action Jump("ch1_s3_no") at c_trans

style NYEH_frame is empty
style NYEH_hbox is hbox
style NYEH_vbox is vbox:
    xalign 0.5
    yalign 0.75
    yanchor 0.5
    spacing gui.choice_spacing
style NYEH_button is button
style NYEH_button_text is button_text

style NYEH_hbox:
    xalign 0.5
    yalign 0.75
    yanchor 0.5

    spacing gui.choice_spacing
    
style NYEH_button is default:
    properties gui.button_properties("choice_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style NYEH_button_text is default:
    properties gui.button_text_properties("choice_button")
    outlines []
    

label badtime_e:
    $ persistent.ch2_both = None
    hide screen ch1_choice
    stop music fadeout 2.0
    scene black
    with Dissolve(0.5)
label badtime:
    $ quick_menu = True
    hide screen ch1_choice
    if not config.developer:
        $ config.allow_skipping = False
        $ allow_skipping = False
    hide b onlayer screens
    hide s_text onlayer screens
    window hide(None)
    show black as b1 zorder 1:
        alpha 1
        1
        linear 2 alpha 0
    show sans a at TC:
        xcenter 641 ycenter 255
        sans_h_move()
    show sans_t 1 at TC behind sans:
        xcenter 642 ycenter 350
        sans_t_move()
    show sans_l at TC behind sans_t:
        xcenter 647 ycenter 455
    $ pause(3.25)
    show b s at TC onlayer screens:
        xcenter 925 ycenter 300
    if persistent.firstsans:
        jump badtime_e1
    else:
        jump badtime_e2
    return
label badtime_e1:
    show s_text "{bl}{size=25}heya.{/bl}" onlayer screens:
        xcenter 860 ycenter 250
    $ s_say("heya.")
    $ pause()
    $ s_say2("heya.")
    hide black as b1
    show sans b at sans_h_move()
    show sans_t 1 at sans_t_move() behind sans
    show s_text "{bl}{size=25}you've been busy,\nhuh?{/bl}" onlayer screens:
        xcenter 935 ycenter 262
    $ s_say("you've been busy,huh?")
    $ pause()
    $ s_say2("you've been busy, huh?")
    show s_text "{bl}{size=25}...{/bl}" onlayer screens:
        xcenter 852 ycenter 252
    $ s_say("...")
    $ pause()
    $ s_say2("...")
    show sans a at sans_h_move()
    show sans_t 1 at sans_t_move() behind sans
    show s_text "{bl}{size=25}so, i've got a\nquestion for ya.{/bl}" onlayer screens:
        xcenter 932 ycenter 262
    $ s_say("so, i've got aquestion for ya.")
    $ pause()
    $ s_say2("so, i've got a question for ya.")
    show sans e at sans_h_move()
    show sans_t 1 at sans_t_move() behind sans
    show s_text "{bl}{size=25}do you think even\nthe worst person\ncan change...?{/bl}" onlayer screens:
        xcenter 937 ycenter 277
    $ s_say("do you think even the worst personcan change...?")
    $ pause()
    $ s_say2("do you think even the worst person can change...?")
    show s_text "{bl}{size=25}that this mod has\nbig spoilers from\nthe game called\nundertale?{/bl}" onlayer screens:
        xcenter 940 ycenter 290
    $ s_say("that this mod has big spoilers from the game called undertale.?")
    $ pause()
    $ s_say2("that this mod has big spoilers from the game called undertale?")
    hide b onlayer screens
    hide s_text onlayer screens
    scene black
    play sound ut_snap
    $ pause(0.25)
    show sans f at TC:
        xcenter 641 ycenter 255
    show sans_t 1 at TC behind sans:
        xcenter 642 ycenter 350
    show sans_l at TC behind sans_t:
        xcenter 647 ycenter 455
    play sound ut_snap
    $ pause(0.75)
    show b s at TC behind sans_t:
        xcenter 925 ycenter 300
    show s_text "{size=25}{cps=10}so, continue if\nyou dare.":
        xcenter 925 ycenter 265
    $ pause(2.5)
    $ pause()
    $ s_say2("so, continue if you dare.")
    $ persistent.firstsans = False
label badtime_end:
    scene black
    play sound ut_snap
    $ pause(1.5)
    call ch1 from _call_ch1
    return

label badtime_e2:
    show s_text "{size=25}let's just get to\nthe point." onlayer screens:
        xcenter 930 ycenter 260
    $ s_say("let's just get to the point.")
    $ pause()
    $ s_say2("let's just get to the point.")
    hide b onlayer screens
    hide s_text onlayer screens
    jump badtime_end
    return
    
label ch1:
    stop sound
    play music t3 fadein 2
    scene bg club_day:
        SP
        zoom 2 xcenter 100 ycenter 330
        easein 1 ycenter 360
    show black zorder 1:
        alpha 1
        linear 1 alpha 0
    show natsuki 2m at i11:
        SP
        xcenter 850 ycenter 375 zoom 1.3
        easein 1 ycenter 425
    $ pause(0.75)
    n "Uu... I wish I could have a cupcake now!"
    hide black
    n "...but I have to wait until the new member arrives!"
    n 5g "If that would be a boy, I'd be pissed off."
    show yuri 1f at i11 behind natsuki:
        SP
        xcenter 350 ycenter 1200 zoom 1.3
        easein_cubic 1 ycenter 425 
    y "Well, maybe..."
    y "Sayori told me that the new member will look very different from us."
    n 4c "So...?"
    n "Is he really a boy?"
    show yuri 2v at i11:
        SP
        xcenter 350 ycenter 425 zoom 1.3
        easein 0.75 ycenter 440
    y "Umm...I don't know..."
    stop music fadeout 1
    window hide(None)
    window auto
    play sound closet_open
    $ pause(0.5)
    show yuri 2v at i11:
        SP
        xcenter 350 ycenter 440 zoom 1.3 xoffset 0
        easeout_cubic 0.5 xoffset 1250
    show natsuki 4c at i11:
        SP
        xcenter 850 ycenter 425 zoom 1.3 xoffset 0
        easeout_cubic 0.5 xoffset 1250
    show bg club_day:
        SP
        zoom 2 xcenter 100 ycenter 360
        ease_cubic 1 xcenter 1000
    $ pause(1)
    show sayori 4a2 at i11:
        SP
        zoom 1.3 xcenter -300 ycenter 425
        easein_circ 0.6 xcenter 300
    s "Everyone! The new member is here~!"
    window hide(None)
    $ renpy.music.set_volume(0.75)
    play music sans
    show sans_l at TC behind sayori:
        SP
        zoom 2 ycenter 750 xcenter -242
        easein_quint 0.85 xcenter 640
    show sans_t 1 at TC behind sayori:
        SP
        zoom 2 xcenter -250 ycenter 545
        parallel:
            easein_quint 0.85 xcenter 632
        parallel:
            sans_t_move(1.75)
    show sans a at TC behind sayori:
        SP
        zoom 2 xcenter -252 ycenter 355
        parallel:
            easein_quint 0.85 xcenter 630
        parallel:
            sans_h_move(1.75)
    $ pause(0.7)
    show b s at TC:
        zoom 1.5 xcenter 1025 ycenter 400
    show s_text "{size=37}heya.":
        xcenter 930 ycenter 330
    $ s_say("heya.")
    $ pause()
    $ s_say2("heya.")
    scene bg club_day:
        zoom 2 xcenter 100 ycenter 360
    show yuri 2v at i11:
        xcenter 350 ycenter 425 zoom 1.3
    show natsuki 4c at i11:
        xcenter 850 ycenter 425 zoom 1.3
    with Dissolve(0.4)
    $ pause(0.15)
    show yuri 3n at i11:
        SP
        xcenter 350 ycenter 425 zoom 1.3
        easein 0.1 ycenter 410
        easeout 0.1 ycenter 425
    show natsuki 1o at i11:
        SP
        xcenter 850 ycenter 425 zoom 1.3
        easein 0.1 ycenter 410
        easeout 0.1 ycenter 425
    y "E-Eeh!?"
    show natsuki 1p at i11:
        SP
        xcenter 850 ycenter 425 zoom 1.3
        layershake(-10, -10, 0)
    n "Are you kidding me, Sayori?!"
    n "I-It's a talking skeleton!"
    show monika 1k at i11 behind yuri:
        SP
        xcenter 640 ycenter 1150 zoom 1.3
        easein_elastic 0.725 ycenter 425 
    show natsuki 1v at i11:
        SP
        zoom 1.3 xcenter 850 ycenter 425 rotate 0
        easein_cubic 0.35 xcenter 1500 ycenter 950 rotate 110
        block:
            choice:
                layershake2(5, -5)
            choice:
                0.5
            choice:
                1
            choice:
                0.25
            choice:
                layershake2(-5, -5)
            0.1
            repeat
    show yuri 3p at i11:
        SP
        zoom 1.3 xcenter 350 ycenter 425
        easein_cubic 0.35 xcenter -300 ycenter 975 rotate -110
        block:
            choice:
                layershake2(5, -5)
            choice:
                0.5
            choice:
                1
            choice:
                0.25
            choice:
                layershake2(-5, -5)
            0.1
            repeat
    show layer master:
        SP
        TC
        layershake(-50, -50, 3.5)
    show layer screens:
        SP
        TC
        layershake(-10, -10, 1)
    show explode at TC:
        zoom 6
    show explodenew at TC:
        zoom 2.5
    show shockwave at TC:
        shockwave_zoom(0.55)
    show white onlayer front:
        alpha 0.6
        ease 0.25 alpha 0
    $ playexplode()
    m "Ah, what a nice surprise!"
    m "Welcome to the club!"
    hide white onlayer front
    m 1b "My name is Monika. It's so nice to meet you!"
label ch1_s:
    hide screen ch1_choice
    window hide(None)
    scene bg club_day:
        zoom 2.5 xcenter 900 ycenter 300
    show sans_l at TC:
        zoom 2.5 ycenter 775 xcenter 540
    show sans_t 1 at TC:
        zoom 2.5 xcenter 530 ycenter 515
        sans_t_move(2)
    show sans h at TC:
        zoom 2.5 xcenter 527 ycenter 280
        sans_h_move(2)
    with Dissolve(0.65)
    $ pause(0.15)
    show b s at TC:
        zoom 1.5 xcenter 1000
    show s_text "{size=39}yeah,":
        xcenter 905 ycenter 295
    $ s_say("yeah,")
    $ pause(0.4)
    show s_text "{size=39}{space=110}it's real\nnice," as s1:
        xcenter 990 ycenter 315
    $ s_say("it's real nice,")
    $ pause(0.4)
    show s_text "{size=39}isn't it?" as s2:
        xcenter 1035 ycenter 336
    $ s_say("isn't it?")
    $ pause()
    $ s_say2("yeah, its real nice, isn't it?")
    hide s1
    hide s2
    show sans_t 1 at TC:
        zoom 2.5 xcenter 530 ycenter 515
        sans_t_move(2)
    show sans j at TC:
        zoom 2.5 xcenter 527 ycenter 280
        sans_h_move(2)
    show s_text "{size=39}especially\nconsidering i've\nnever met you\nbefore.":
        xcenter 1000 ycenter 353
    $ s_say("especially considering i've never met you before.")
    $ pause()
    $ s_say2("especially considering i've never met you before.")
    show sans_t 1 at TC:
        zoom 2.5 xcenter 530 ycenter 515
        sans_t_move(2)
    show sans h at TC:
        zoom 2.5 xcenter 527 ycenter 280
        sans_h_move(2)
    show s_text "{size=39}the name's sans.":
        xcenter 1010 ycenter 295
    $ s_say("the name's sans.")
    $ pause(0.4)
    show s_text "{size=39}sans the skeleton." as s1:
        xcenter 1028 ycenter 338
    $ s_say("sans the skeleton.")
    $ pause()
    $ s_say2("the name's sans. sans the skeleton.")
    hide s1
    show s_text "{size=39}and,":
        xcenter 895 ycenter 295
    $ s_say("and,")
    $ pause(0.4)
    show s_text "{size=39}uh," as s1:
        xcenter 976 ycenter 295
    $ s_say("uh,")
    $ pause(0.4)
    show s_text "{size=39}same." as s2:
        xcenter 1067 ycenter 295
    $ s_say("same.")
    $ pause()
    $ s_say2("and, uh, same.")
    hide b
    hide s_text
    hide s1
    hide s2
    show sans_t 1 at TC:
        SP
        zoom 2.5 xcenter 530 ycenter 515
        parallel:
            sans_t_move(2)
        parallel:
            easeout 0.375 xcenter -400 ycenter 535
    show sans h at TC:
        SP
        zoom 2.5 xcenter 527 ycenter 280
        parallel:
            sans_h_move(2)
        parallel:
            easeout 0.375 xcenter -403 ycenter 300
    show sans_l at TC:
        SP
        zoom 2.5 ycenter 775 xcenter 540
        easeout 0.375 xcenter -390 ycenter 795
    show bg club_day:
        SP
        zoom 2.5 xcenter 900 ycenter 300
        ease_quad 0.75 xcenter 300 zoom 2 ycenter 360
    $ pause(0.375)
    hide sans
    hide sans_l
    hide sans_t
    show yuri 2o at i11:
        SP
        zoom 1.3 xcenter 500 ycenter 900 rotate -50 xoffset 1000
        parallel:
            easein_cubic 1.5 xcenter 640 ycenter 450 rotate 0
        parallel:
            easein 0.375 xoffset 0
    $ pause(0.35)
    y "Uuu..."
    show yuri 1l at i11:
        SP
        zoom 1.3 xcenter 640 ycenter 450 rotate 0
        easein 0.75 ycenter 470
    y "(Alright, I got this.)"
    show yuri 1l at i11:
        SP
        zoom 1.3 xcenter 640 ycenter 470
        ease 0.25 ycenter 450
    show yuri 1a at i11 as y1:
        SP
        zoom 1.3 xcenter 640 ycenter 470 alpha 0
        ease 0.25 ycenter 450 alpha 1
    y "Welcome to the Literature Club. It's a pleasure meeting you."
    hide y1
    y 1a "Sayori always says nice things abo{nw}"
    $ _history_list[-1].what = "\"Sayori always says nice things abo-\""
    show yuri 3t at i11:
        SP
        zoom 1.3 xcenter 640 ycenter 450
        parallel:
            linear 0.35 zoom 1.05 xcenter 800 ycenter 440
        parallel:
            easein 0.175 yoffset -40
            easeout 0.175 yoffset 0
    show natsuki 4g at i11:
        SP
        zoom 1.3 xcenter 1550 ycenter 435
        easein_back 0.5 xcenter 575 
    show layer master:
        TC
        layershake(-100, -20, 0, 1.5)
    show layer screens:
        TC
        layershake(-50, -10, 0, 1.5)
    play sound whoosh4
    n "Hold up!"
    n 4c "If you are a skeleton, how come you're still alive?"
    window hide(None)
    show yuri 3t at i11:
        SP
        zoom 1.05 xcenter 800 ycenter 440 xoffset 0
        easeout 0.4 xoffset 675
    show natsuki 4c at i11:
        SP
        zoom 1.3 xcenter 575 ycenter 435 xoffset 0
        easeout 0.4 xoffset 975
    show bg club_day:
        SP
        xcenter 300 zoom 2 ycenter 360
        ease_quad 0.8 xcenter 900
    $ pause(1.2)
    hide yuri
    hide natsuki
    n "Eh? Where the hell did he go?"
    show bg club_day:
        SP
        zoom 2 xcenter 900 ycenter 360
        ease_quad 0.8 xcenter 100
    $ pause(0.35)
    show yuri 3v at i11:
        SP
        zoom 1.05 xcenter 600 ycenter 440 xoffset 875
        easein_quad 0.4 xoffset 0
    show natsuki 4g at i11:
        SP
        zoom 1.3 xcenter 375 ycenter 435 xoffset 1175
        easein_quad 0.4 xoffset 0
    show sans_l at TC:
        SP
        zoom 1.75 xcenter 1090 ycenter 725 xoffset 1175
        easein_quad 0.4 xoffset 0
    show sans_t 1 at TC:
        SP
        zoom 1.75 xcenter 1084 ycenter 545 xoffset 1175
        easein_quad 0.4 xoffset 0
        sans_t_move2(1)
    show sans b at TC:
        SP
        zoom 1.75 xcenter 1081 ycenter 382 xoffset 1175
        easein_quad 0.4 xoffset 0
        sans_h_move2(1)
    
    $ pause(0.9)
    show b s at TC:
        zoom 1.2 xzoom -1 xcenter 760 ycenter 425
    show s_text "{size=31}boo.":
        xcenter 632 ycenter 377
    $ s_say("boo.")
    $ pause(0.45)
    $ s_say2("boo.")
    hide b
    hide s_text
    show natsuki 1v at i11:
        SP
        zoom 1.3 xcenter 375 ycenter 435
        layershake(-20,-20, 0)
    show yuri 3e
    n "Eeghk--!"
    show natsuki 1f
    show b s at TC behind sans_t:
        zoom 1.2 xzoom -1 xcenter 760 ycenter 425
    show s_text "{size=31}heheh...":
        xcenter 660 ycenter 375
    $ s_say("heheh...")
    $ pause()
    $ s_say2("heheh...")
    show sans_t 1 at TC:
        zoom 1.75 xcenter 1084 ycenter 545
        sans_t_move(1.5)
    show sans a at TC:
        zoom 1.75 xcenter 1081 ycenter 382
        sans_h_move(1.5)
    show s_text "{size=31}anyways,":
        xcenter 665 ycenter 375
    $ s_say("anyways,")
    $ pause(0.4)
    show s_text "{size=31}{space=137}you don't\nneed to find the\nanswer to that." as s1:
        xcenter 739 ycenter 407
    $ s_say("you don't need to find the answer to that.")
    $ pause()
    $ s_say2("anyways, you don't need to find the answer to that.")
    show sans_t 1 at TC:
        zoom 1.75 xcenter 1084 ycenter 545
        sans_t_move(1.5)
    show sans d at TC:
        zoom 1.75 xcenter 1081 ycenter 382
        sans_h_move(1.5)
    hide s1
    show layer master:
        zoom 1.25 xcenter 300 ycenter 300
    show bg club_day:
        zoom 1.85 xcenter 270 ycenter 390
    show yuri 3e at i11:
        zoom 0.975 xcenter 640 ycenter 450
    show s_text "{size=31}forgeddaboudit.":
        xcenter 715 ycenter 377
    $ s_say("forgeddaboudit.")
    $ pause()
    $ s_say2("forgeddaboudit.")
    show sans_t 2 at TC:
        zoom 1.75 xcenter 1084 ycenter 545
        sans_t_move(1.5)
    show sans d at TC:
        zoom 1.75 xcenter 1081 ycenter 382
        sans_h_move(1.5)
    show s_text "{size=31}you must be\nthinking of hunch.":
        xcenter 740 ycenter 390
    $ s_say("you must be thinking of hunch.")
    $ pause()
    $ s_say2("you must be thinking of hunch.")
    stop music
    scene black
    show splash_warning2 "{size=70}Later..."
    play sound fart
    $ pause(0.3)
label ch1_s2:
    hide screen ch1_choice
    play music t3 fadein 1.5
    scene bg class_day:
        SP
        zoom 4 xcenter 300 ycenter 425 yoffset 50
        easein_back 1.5 yoffset 0
    show layer master:
        TC
        SP
        yoffset -100
        easein_back 1.5 yoffset 0
    show black zorder 1:
        SP
        TC
        zoom 1.5 alpha 1
        easein 1.5 alpha 0
    show sayori 2x at i11:
        zoom 1.25 xcenter 900 ycenter 425
    show sans_l at TC:
        zoom 1.75 xcenter 400 ycenter 725
    show sans_t 1 at TC:
        zoom 1.75 xcenter 392 ycenter 542
        sans_t_move(1.4)
    show sans h at TC:
        zoom 1.75 xcenter 389 ycenter 379
        sans_h_move(1.4)
    $ pause(0.66)
    window auto
    s "Anyway! This is Natsuki, always full of energy."
    s "And this is Yuri, the smartest in the club!"
    s 4a2 "Come sit down, Sans! We made room for you at the table, so you can sit next to me or Monika."
    s 4q "I'll get the cupcakes~"
    window hide(None)
    play sound impact
    $ pause(0.475)
    show rock at TC:
        SP
        zoom 0.75 xcenter -200 ycenter 300 rotate 0
        linear 0.2 xcenter 1500 rotate 540
    $ pause(0.1)
    show smack at TC:
        zoom 2.5 xcenter 890 ycenter 280
    show sayori 4p at i11:
        SP
        zoom 1.25 xcenter 900 ycenter 425 rotate 0
        linear 0.2 xcenter 2250 rotate 405
    show layer master:
        TC2
        layershake(-225, -225, 10)
    show speedline at SL onlayer front:
        alpha 1
        ease 0.75 alpha 0
    play sound2 [ "<silence 0.9>", glass2 ]
    $ pause(1)
    hide sayori
    hide rock
    hide speedline onlayer front
    hide smack
    show layer screens:
        TC
        layershake(-5, -5, 2, 0.75)
    n "Hey! I made them, I'll get them!"
    window hide(None)
    show b m at TC:
        zoom 0.875 xcenter 685 ycenter 375
    show sans_t 1 at TC:
        zoom 1.75 xcenter 392 ycenter 542
        sans_t_move(1.4)
    show sans b at TC:
        zoom 1.75 xcenter 389 ycenter 379
        sans_h_move(1.4)
    show s_text "{size=30}nice throw,":
        xcenter 685 ycenter 295
    $ s_say("nice throw,")
    $ pause(0.4)
    show s_text "{size=30}natsu." as s1:
        xcenter 647 ycenter 327
    $ s_say("natsu.")
    $ pause()
    $ s_say2("nice throw, natsu.")
    hide s_text
    hide s1
    hide b
    n "S-Shut up! Don't call me like that!"
    $ currentpos = get_pos()
    stop music
    window hide(None)
    show vignette onlayer front:
        alpha 0.5
    show dark behind sans_l:
        alpha 0.5
    show layer master:
        zoom 1.25 xcenter 725 ycenter 300
    show bg class_day:
        zoom 3.5 xcenter 300 ycenter 447
    show sans_t 1 at TC:
        zoom 1.75 xcenter 392 ycenter 542
        sans_t_move(1.4)
    show sans e at TC:
        zoom 1.75 xcenter 389 ycenter 379
        sans_h_move(1.4)
    show b m at TC:
        zoom 0.875 xcenter 685 ycenter 375
    show s_text "{size=30}(gee,":
        xcenter 636 ycenter 300
    $ s_say("(gee,")
    $ pause(0.4)
    show s_text "{size=30}lady," as s1:
        xcenter 714 ycenter 300
    $ s_say("lady,")
    $ pause(0.4)
    show s_text "{size=30}{space=152}you\nreally know\nhow to pick\n'em," as s2:
        xcenter 702 ycenter 348
    $ s_say("you really know how to pick 'em,")
    $ pause(0.4)
    show s_text "{size=30}huh...?)" as s3:
        xcenter 728 ycenter 396
    $ s_say("huh...?).")
    $ pause()
    $ s_say2("(gee, lady, you really know how to pick 'em, huh...?)")
    $ audio.t6r = "<from " + str(currentpos) + " loop 4.618>bgm/3.ogg"
    play music t6r fadein 0.5
    show vignette onlayer front:
        alpha 0.5
        ease 0.25 alpha 0
    show dark:
        alpha 0.5
        ease 0.25 alpha 0 
    hide s_text
    hide s1
    hide s2
    hide s3
    hide b
    window auto
    m "Come and sit down, Sans! We got a lot of things to talk!"
    window hide(None)
    hide dark
    hide vignette onlayer front
    show sans_t 1 at TC:
        zoom 1.75 xcenter 392 ycenter 542
        sans_t_move(1.4)
    show sans a at TC:
        zoom 1.75 xcenter 389 ycenter 379
        sans_h_move(1.4)
    show b m at TC:
        zoom 0.875 xcenter 685 ycenter 375
    show s_text "{size=30}wha,":
        xcenter 635 ycenter 300
    $ s_say("wha,")
    $ pause(0.4)
    show s_text "{size=30}nah." as s1:
        xcenter 709 ycenter 300
    $ s_say("nah.")
    $ pause()
    $ s_say2("wha, nah.")
    hide s1
    show s_text "{size=30}i'm going to\ngrillby's.":
        xcenter 690 ycenter 315
    $ s_say("i'm going to grillby's.")
    $ pause(0.4)
    show s_text "{size=30}{space=145}i\nneed to pry\nmyself away\nfrom my\nwork." as s1:
        xcenter 690 ycenter 395
    $ s_say("i need to pry myself away from my work.")
    $ pause()
    $ s_say2("i'm going to grillby's. i need to pry myself away from my work.")
    hide s1
    show s_text "{size=30}wanna come?":
        xcenter 690 ycenter 300
    $ s_say("wanna come?")
    $ pause()
    $ s_say2("wanna come?")
    scene bg club_day:
        zoom 1.5
        TC
    show sayori 1b at i11:
        zoom 1.1 xcenter 250 ycenter 400
    show monika 2g at i11:
        zoom 1.4 ycenter 440 xcenter 640
    show natsuki 5g at i11 behind monika:
        zoom 1.1 xcenter 1050 ycenter 400
    show yuri 1e at i11 behind natsuki:
        zoom 0.8 xcenter 900 ycenter 390
    with Dissolve(0.4)
    $ pause(0.15)
    m "Already...?"
    show monika 2p at i11:
        SP
        zoom 1.4 ycenter 440 xcenter 640
        easein 0.75 yoffset 15
    m "B-But, you just joined a minute ago... Why do you need a break so early...?"
    window hide(None)
    scene bg class_day:
        zoom 3.5 xcenter 300 ycenter 447
    show layer master:
        zoom 1.25 xcenter 725 ycenter 300
    show sans_l at TC:
        zoom 1.75 xcenter 400 ycenter 725
    show sans_t 1 at TC:
        zoom 1.75 xcenter 392 ycenter 542
        sans_t_move(1.4)
    show sans a at TC:
        zoom 1.75 xcenter 389 ycenter 379
        sans_h_move(1.4)
    with Dissolve(0.4)
    $ pause(0.15)
    show b m at TC behind sans_t:
        zoom 0.875 xcenter 685 ycenter 375
    show s_text "{size=30}...":
        xcenter 625 ycenter 300
    $ s_say("....")
    $ pause()
    $ s_say2("...")
    show sans_t 2 at TC:
        zoom 1.75 xcenter 392 ycenter 542
        sans_t_move(1.4)
    show sans d at TC:
        zoom 1.75 xcenter 389 ycenter 379
        sans_h_move(1.4)
    show s_text "{size=30}welp,":
        xcenter 640 ycenter 300
    $ s_say("welp,")
    $ pause(0.4)
    show s_text "{size=30}ok," as s1:
        xcenter 705 ycenter 300
    $ s_say("ok,")
    $ pause(0.4)
    show s_text "{size=30}{space=130}have\nfun." as s2:
        xcenter 696 ycenter 316
    $ s_say("have fun.")
    $ pause()
    $ s_say2("welp, ok, have fun.")
    stop music fadeout 2
    hide b
    hide s_text
    hide s1
    hide s2
    hide sans_l
    hide sans_t
    hide sans
    show sans_w at TC:
        SP
        zoom 2.5 xcenter 375 ycenter 515
        linear 1 xcenter 1200
    play sound run
    $ pause(2)
    scene bg club_day:
        zoom 2 xcenter 1000 ycenter 425
    show sayori 4g at i11:
        zoom 1.35 xcenter 325 ycenter 450
    show monika 1f at i11:
        zoom 1.35 xcenter 900 ycenter 450
    with Dissolve(0.75)
    s "Please..."
    s "I don't wanna--"
    m 1r "It's alright, Sayori. He'll come back soon."
    window hide(None)
    show natsuki 2b at i11:
        xcenter 1460 ycenter 450 zoom 1.35
    show layer master:
        SP
        TC2
        ease_cubic 1 xcenter 100
    show bg club_day:
        SP
        zoom 2 xcenter 1000 ycenter 425
        ease_cubic 1 xcenter 1250
    $ pause(0.5)
    window auto
    n "Anyhow, I'll get the cupcakes. I won't wait for his lazy shenanigans."
    window hide(None)
label ch1_s3:
    window hide(None)
    hide screen ch1_choice
    stop music
    scene black
    show sanes at TC:
        zoom 0.8 xcenter 300 ycenter 525
    show splash_warning2 "{size=70}Later-er..."
    play sound smb3 loop
    
    $ pause(1.2)
    stop sound
    play music t3 fadein 2
    scene bg class_day:
        SP
        zoom 3.75 xcenter 325 ycenter 450
    show layer master:
        TC
        zoom 1.25 ycenter 275
    show black zorder 1:
        alpha 1
        linear 0.75 alpha 0
    $ pause(0.5)
    show sans_l at TC:
        SP
        zoom 1.75 xcenter 1500 ycenter 725
        easein_cubic 0.75 xcenter 640
    show sans_t 1 at TC:
        SP
        zoom 1.75 xcenter 1492 ycenter 542
        parallel:
            easein_cubic 0.75 xcenter 632
        parallel:
            sans_t_move(1.4)
    show sans a at TC:
        SP
        zoom 1.75 xcenter 1489 ycenter 377
        parallel:
            easein_cubic 0.75 xcenter 629
        parallel:
            sans_h_move(1.4)
    $ pause(0.75)
    hide black
    show b m at TC:
        xzoom -1 zoom 0.8 xcenter 350 ycenter 400
    show s_text "{size=30}welp,":
        xcenter 282 ycenter 325
    $ s_say("welp,")
    $ pause(0.4)
    show s_text "{size=30}{space=80}that\nwas a long\nbreak." as s1:
        xcenter 318 ycenter 358
    $ s_say("that was a long break.")
    $ pause()
    $ s_say2("welp, that was a long break.")
    hide s1
    show sans_t 1 at TC:
        zoom 1.75 xcenter 632 ycenter 542
        sans_t_move(1.4)
    show sans b at TC:
        zoom 1.75 xcenter 629 ycenter 377
        sans_h_move(1.4)
    show s_text "{size=30}i can't\nbelieve i let\ny'all pull me\naway from\nwork for\nthat long.":
        xcenter 335 ycenter 405
    $ s_say("i can't believe i let y'all pull me away from work for that long.")
    $ pause()
    $ s_say2("i can't believe i let y'all pull me away from work for that long.")
    show sans_t 1 at TC:
        zoom 1.75 xcenter 632 ycenter 542
        sans_t_move(1.4)
    show sans a at TC:
        zoom 1.75 xcenter 629 ycenter 377
        sans_h_move(1.4)
    show s_text "{size=30}anyways,":
        xcenter 308 ycenter 325
    $ s_say("anyways,")
    $ pause(0.4)
    show s_text "{size=30}what's up?" as s1:
        xcenter 320 ycenter 360
    $ s_say("what's up.?")
    $ pause()
    $ s_say2("anyways, what's up?")
    scene bg club_day:
        zoom 2 xcenter 1000 ycenter 425
    show monika 2j at i11:
        zoom 1.35 xcenter 640 ycenter 450
    with wiperound
    $ pause(0.15)
    window show(None)
    m "Welcome back, Sans!"
    m "I'm very glad to see you again!"
    window hide(None)
    show monika 2j at i11:
        SP
        zoom 1.35 xcenter 640 ycenter 450
        ease_back 1 xcenter 300
    show monika 2a at i11 as m1:
        SP
        zoom 1.35 xcenter 640 ycenter 450 alpha 0
        ease_back 1 xcenter 300 alpha 1
    show bg club_day:
        SP
        zoom 2 xcenter 1000 ycenter 425
        ease_back 1 xcenter 800
    show sayori 2x at i11:
        SP
        zoom 1.35 xcenter 1500 ycenter 450
        ease_back 1 xcenter 900
    $ pause(0.5)
    window auto
    s "Hi Sansy~"
    show monika 2a
    hide m1
    s "We left the last cupcake especially for you." 
    s 2q "And we want to see your nice reactions through it!"
    window hide(None)
    show monika 2a at i11:
        SP
        zoom 1.35 xcenter 300 ycenter 450
        ease_cubic 0.66 xcenter -300
    show bg club_day:
        SP
        zoom 2 xcenter 800 ycenter 425
        ease_cubic 0.66 xcenter 600
    show sayori 2q at i11:
        SP
        zoom 1.35 xcenter 900 ycenter 450
        ease_cubic 0.66 xcenter 300
    show sans_l at TC:
        SP
        zoom 1.75 xcenter 1507 ycenter 725
        ease_cubic 0.66 xcenter 900
    show sans_t 1 at TC:
        SP
        zoom 1.75 xcenter 1500 ycenter 542
        parallel:
            ease_cubic 0.66 xcenter 893
        parallel:
            sans_t_move2(1.25)
    show sans e at TC:
        SP
        zoom 1.75 xcenter 1498 ycenter 379
        parallel:
            ease_cubic 0.66 xcenter 891
        parallel:
            sans_h_move2(1.25)
    $ pause(0.8)
    show b s at TC:
        zoom 1.1 xzoom -1 xcenter 590 ycenter 400
    show s_text "{size=30}nah,":
        xcenter 470 ycenter 355
    $ s_say("nah,")
    $ pause(0.4)
    show s_text "{size=30}{space=70}i don't want\nit." as s1:
        xcenter 565 ycenter 371
    $ s_say("i don't want it.")
    $ pause(0.4)
    show s_text "{size=30}{space=50}you can have\nthe cupcake." as s2:
        xcenter 558 ycenter 402
    $ s_say("you can have the cupcake.")
    $ pause()
    $ s_say2("nah, i don't want it. you can have the cupcake.")
    hide s1
    hide s2
    show sans_t 1 at TC:
        zoom 1.75 xcenter 893 ycenter 542
        sans_t_move2(1.25)
    show sans b at TC:
        zoom 1.75 xcenter 891 ycenter 379
        sans_h_move2(1.25)
    show s_text "{size=30}i'm not hungry\nanyway.":
        xcenter 548 ycenter 371
    $ s_say("i'm not hungry anyway.")
    $ pause()
    $ s_say2("i'm not hungry anyway.")
    hide s_text
    hide b
    show sayori 4h at i11:
        SP
        zoom 1.35 xcenter 300 ycenter 450 yoffset 0
        easein 0.1 yoffset -20
        easeout 0.1 yoffset 0
    window show(None)
    s "Eeh?"
    s 4y "So...that means I have to take it, right?"
    s "Since you're not very hungry, then..."
    show sayori 4r at i11:
        SP
        zoom 1.35 xcenter 300 ycenter 450 yoffset 0
        easein 0.1 yoffset -20
        easeout 0.1 yoffset 0
    s "Yay~! Free cupcake!"
    window hide(None)
    show layer master:
        zoom 1.25 xcenter 300 ycenter 300
    show bg club_day:
        zoom 1.8 xcenter 750 ycenter 437
    show sans_t 1 at TC:
        zoom 1.75 xcenter 893 ycenter 542
        sans_t_move(1.5)
    show sans e at TC:
        zoom 1.75 xcenter 891 ycenter 379
        sans_h_move(1.5)
    show b s at TC zorder 1:
        zoom 1.1 xcenter 1225 ycenter 400
    show s_text "{size=30}hey,"zorder 1:
        xcenter 1150 ycenter 355
    $ s_say("hey,")
    $ pause(0.4)
    show s_text "{size=30}buddy." as s1 zorder 1:
        xcenter 1233 ycenter 355
    $ s_say("buddy.")
    $ pause()
    $ s_say2("hey, buddy.")
    hide s1
    show sans_t 21 at TC:
        zoom 1.75 xcenter 893 ycenter 542
        sans_t_move(1.5)
    show sans d at TC:
        zoom 1.75 xcenter 891 ycenter 379
        sans_h_move(1.5)
    show s_text "{size=30}want some\nketchup?" zorder 1:
        xcenter 1190 ycenter 370
    show ketchup at TC:
        SP
        zoom 3.25 xcenter 675 ycenter 0 yoffset 0
        easein_cubic 1 ycenter 355
        block:
            ease 1 yoffset -10
            ease 1 yoffset 0
            repeat
    show rays at TC behind ketchup:
        SP
        zoom 2.75 xcenter 675 ycenter 0 yoffset 0 alpha 0 additive 0.25
        parallel:
            easein_cubic 1 ycenter 355 alpha 0.5
            block:
                ease 1 yoffset -10
                ease 1 yoffset 0
                repeat
        parallel:
            rotate 0
            linear 6 rotate 360
            repeat
    $ s_say("want some ketchup")
    $ pause()
    $ s_say2("want some ketchup?")
    scene bg club_day:
        zoom 2.5 xcenter 800 ycenter 450
    show sayori 4n at i11:
        zoom 1.75 xcenter 640 ycenter 525
    show sans_t 21 at TC:
        zoom 2 xcenter 1495 ycenter 640
        sans_t_move(1.5)
    show ketchup at TC:
        SP
        zoom 3.5 xcenter 1265 ycenter 440 yoffset 0
        ease 1 yoffset -10
        ease 1 yoffset 0
        repeat
    with wiperound
    $ pause(0.15)
    window show(None)
    s "Eh?"
    s "K-Ketchup...?"
    s 1o "Well..."
    window hide(None)
    play sound whoosh2
    show layer screens:
        TC
        SP
        ycenter 600
        easein_elastic 1 ycenter 360
    call screen ch1_choice()
    return

label ch1_s3_yes: ########## YES ##########
    hide screen ch1_choice
    with None
    scene bg club_day:
        zoom 2 xcenter 600 ycenter 425
    show sayori 1c at i11:
        zoom 1.35 xcenter 300 ycenter 450
    show sans_l at TC:
        zoom 1.75 xcenter 900 ycenter 725
    show sans_t 21 at TC:
        zoom 1.75 xcenter 893 ycenter 542
        sans_t_move(1.5)
    show sans b at TC:
        zoom 1.75 xcenter 891 ycenter 379
        sans_h_move(1.5)
    show ketchup at TC:
        SP
        zoom 3.25 xcenter 675 ycenter 355 yoffset 0
        block:
            ease 1 yoffset -10
            ease 1 yoffset 0
            repeat
    with Dissolve(0.5)
    $ pause(0.05)
    window show(None)
    s "Well...Okay, I want it."
    show ketchup at TC:
        SP
        zoom 3.25 xcenter 675 ycenter 355 rotate 0
        parallel:
            linear 1 xcenter 490 rotate -720
        parallel:
            easein 0.5 yoffset -500
            easeout 0.5 yoffset 0
            easein 0.1 yoffset 20
            easeout 0.1 yoffset 0
    show sans_l at TC:
        SP
        zoom 1.75 xcenter 900 ycenter 725
        easein_quad 0.1 ycenter 685
        ease_quad 0.15 ycenter 725
    show sans_t 1 at TC:
        SP
        zoom 1.75 xcenter 893 ycenter 542
        parallel:
            sans_t_move(1.5)
        parallel:
            easein_quad 0.1 ycenter 502
            ease_quad 0.15 ycenter 542
    show sans b at TC:
        SP
        zoom 1.75 xcenter 891 ycenter 379
        parallel:
            sans_h_move(1.5)
        parallel:
            easein_quad 0.1 ycenter 339
            ease_quad 0.15 ycenter 379
    show sayori 2a2 at i11:
        zoom 1.35 xcenter 300 ycenter 450
        1
        easein 0.1 yoffset 20
        easeout 0.1 yoffset 0
    play sound2 slip2
    play sound [ "<silence 1>", audio.fart ]
    s "Thanks~"
    window hide(None)
    show b m at TC:
        zoom 0.9 xcenter 610 ycenter 390 xzoom -1
    show sans_t 1 at TC:
        zoom 1.75 xcenter 893 ycenter 542
        sans_t_move(1.5)
    show sans d at TC:
        zoom 1.75 xcenter 891 ycenter 379
        sans_h_move(1.5)
    show s_text "{size=32}bone appetit.":
        xcenter 594 ycenter 310
    $ s_say("bone appetit.")
    $ pause()
    $ s_say2("bone appetit.")
    hide s_text
    hide b
    show sans_t 1 at TC:
        zoom 1.75 xcenter 893 ycenter 542
        sans_t_move(1.5)
    show sans b at TC:
        zoom 1.75 xcenter 891 ycenter 379
        sans_h_move(1.5)
    stop sound
    show sayori 2a2 at i11:
        SP
        zoom 1.35 xcenter 300 ycenter 450 xoffset 0 yoffset 0
        easeout_cubic 0.45 xoffset -550
    show ketchup at TC:
        SP
        zoom 3.25 xcenter 490 ycenter 355 rotate 0 yoffset 0 xoffset 0
        easeout_cubic 0.45 xoffset -550
    $ pause(1.5)
    show layer screens:
        TC
        layershake(-5, -5, 2, 0.75)
    hide sayori
    hide ketchup
    s "Ahh!! I accidentally spilled my ketchup all over!"
    show natsuki 1p at i11:
        SP
        zoom 1.35 xcenter 350 ycenter 440 xoffset -550 yoffset 0
        parallel:
            ease_quad 0.35 xoffset 0
        parallel:
            ease_quad 0.175 yoffset -125
            ease_quad 0.175 yoffset 0
    n "EWWEUGH--!! You got ketchup on my clothes, Sayori!"
    show natsuki 1p at i11:
        zoom 1.35 xcenter 350 ycenter 440 xoffset 0 yoffset 0
        layershake(-10, -10, 0)
    n "Are you freaking stupid?"
    window hide(None)
    show b m at TC:
        zoom 0.9 xcenter 610 ycenter 390 xzoom -1
    show s_text "{size=32}uhh,":
        xcenter 525 ycenter 310
    $ s_say("uhh,")
    $ pause(0.4)
    show sans_t 2 at TC zorder 1:
        zoom 1.75 xcenter 893 ycenter 542
        sans_t_move(1.5)
    show sans b at TC zorder 2:
        zoom 1.75 xcenter 891 ycenter 379
        sans_h_move(1.5)
    show s_text "{size=32}whoops." as s1:
        xcenter 622 ycenter 310
    $ s_say("whoops.")
    $ pause()
    $ s_say2("uhh, whoops.")
    $ quick_menu = False
    scene error
    play music onekhz
    show splash_warning "{size=+10}Never give ketchup to Sayori." at TC
    $ pause(0.9)
    $ quick_menu = True
    call ch1_s4(True) from _call_ch1_s4
    return

label ch1_s3_no: ########## NO ##########
    hide screen ch1_choice
    with None
    scene bg club_day:
        zoom 2 xcenter 600 ycenter 425
    show sayori 1d at i11:
        zoom 1.35 xcenter 300 ycenter 450
    show sans_l at TC:
        zoom 1.75 xcenter 900 ycenter 725
    show sans_t 21 at TC:
        zoom 1.75 xcenter 893 ycenter 542
        sans_t_move(1.5)
    show sans b at TC:
        zoom 1.75 xcenter 891 ycenter 379
        sans_h_move(1.5)
    show ketchup at TC:
        SP
        zoom 3.25 xcenter 675 ycenter 355 yoffset 0
        block:
            ease 1 yoffset -10
            ease 1 yoffset 0
            repeat
    with Dissolve(0.5)
    $ pause(0.05)
    window show(None)
    s "No thanks, the cupcake already had it's flavor inside."
    s "It's not necessary either."
    window hide(None)
    show layer master:
        zoom 1.25 xcenter 300 ycenter 300
    show bg club_day:
        zoom 1.8 xcenter 750 ycenter 437
    show sans_t 2 at TC:
        zoom 1.75 xcenter 893 ycenter 542
        sans_t_move(1.5)
    show sans d at TC:
        zoom 1.75 xcenter 891 ycenter 379
        sans_h_move(1.5)
    show b s at TC behind sans_t:
        zoom 1.1 xcenter 1225 ycenter 400
    show s_text "{size=30}well,":
        xcenter 1150 ycenter 355
    $ s_say("well,")
    $ pause(0.4)
    show s_text "{size=30}more for me." as s1:
        xcenter 1285 ycenter 355
    $ s_say("more for me.")
    $ pause()
    $ s_say2("well, more for me.")
    hide s_text
    hide s1
    hide sans
    hide sans_t
    hide sans_l
    hide b
    hide ketchup
    show sans_k at TC:
        zoom 6 xcenter 875 ycenter 515
    play sound ut_drink
    $ pause(0.5)
    play sound ut_drink
    $ pause(0.5)
    play sound ut_drink
    $ pause(0.5)
    play sound ut_drink
    $ pause(1.66)
    scene bg club_day:
        zoom 2.5 xcenter 800 ycenter 450
    show sayori 1b at i11:
        zoom 1.75 xcenter 640 ycenter 525
    hide sans_k
    s "Wait a minute..."
    s 1i "...You drank all the ketchup?"
    show layer master:
        TC2
        SP
        zoom 1
        easein_elastic 1.25 zoom 1.1 ycenter 390
    show bg club_day:
        SP
        zoom 2.5 xcenter 800 ycenter 450
        easein_elastic 1.25 zoom 2.35 xcenter 791 ycenter 430
    show speedline at SL onlayer front:
        alpha 0.5
        easeout 0.75 alpha 0
    s 1j "Well, you {i}are{/i} hungry! Stop lying!"
    window hide(None)
    hide speedline onlayer front
    with None
    scene bg club_day:
        zoom 1.8 xcenter 750 ycenter 437
    show layer master:
        zoom 1.25 xcenter 300 ycenter 300
    show sayori 1j at i11:
        zoom 1.35 xcenter 300 ycenter 450
    show sans_l at TC:
        zoom 1.75 xcenter 900 ycenter 725
    show sans_t 1 at TC:
        zoom 1.75 xcenter 893 ycenter 542
        sans_t_move(1.5)
    show sans e at TC:
        zoom 1.75 xcenter 891 ycenter 379
        sans_h_move(1.5)
    with Dissolve(0.5)
    $ pause(0.05)
    show b s at TC behind sans_t:
        zoom 1.1 xcenter 1225 ycenter 400
    show s_text "{size=30}whoa there,":
        xcenter 1200 ycenter 355
    $ s_say("whoa there,")
    $ pause(0.4)
    show s_text "{size=30}tiger." as s1:
        xcenter 1333 ycenter 355
    $ s_say("tiger.")
    $ pause()
    $ s_say2("whoa there, tiger.")
    show sans_t 2 at TC:
        zoom 1.75 xcenter 893 ycenter 542
        sans_t_move(1.5)
    show sans i at TC:
        zoom 1.75 xcenter 891 ycenter 379
        sans_h_move(1.5)
    hide s1
    show s_text "{size=30}i'm just thirsty,":
        xcenter 1237 ycenter 355
    $ s_say("i'm just thirsty,")
    $ pause(0.4)
    show s_text "{size=30}y'know?" as s1:
        xcenter 1174 ycenter 390
    $ s_say("y'know?")
    $ pause()
    $ s_say2("i'm just thirsty, y'know?")
    hide s1
    show sans_t 1 at TC:
        zoom 1.75 xcenter 893 ycenter 542
        sans_t_move(1.5)
    show sans b at TC:
        zoom 1.75 xcenter 891 ycenter 379
        sans_h_move(1.5)
    show s_text "{size=30}i haven't had\na drink at least\nhalf an hour.":
        xcenter 1229 ycenter 387
    $ s_say("i haven't had a drink at least half an hour.")
    $ pause()
    $ s_say2("i haven't had a drink at least half an hour.")
    call ch1_s4(False) from _call_ch1_s4_1
    return





label ch1_s4(No_trans=False):
    hide b
    hide s_text
    hide s1
    with None
    play music t6 fadeout 1.5
    scene bg closet:
        TC
        zoom 1.25 ycenter 390
    show yuri 1a at i11:
        SP
        zoom 1.25 xcenter 875 ycenter 450 yoffset 0
        block:
            ease_cubic 2.5 yoffset -5
            ease_cubic 2.5 yoffset 0
            repeat
    show sans_l at TC:
        zoom 1.75 xcenter 325 ycenter 700
    show sans_t 1 at TC:
        zoom 1.75 xcenter 318 ycenter 517
        sans_t_move(1.3)
    show sans h at TC:
        zoom 1.75 xcenter 317 ycenter 355
        sans_h_move(1.3)
    if not No_trans:
        play music t6 fadeout 1.5
        with wiperound_scene
        window auto
    else:
        play music t6
    
    y "So, Sans, what kind of things do you like to read?"
    window hide(None)
    show b s at TC behind sans_t:
        zoom 1.15 ycenter 395
    show s_text "{size=32}uh,":
        xcenter 550 ycenter 345
    $ s_say("uh,")
    $ pause(0.4)
    show sans_t 2 at TC:
        zoom 1.75 xcenter 318 ycenter 517
        sans_t_move(1.3)
    show sans h at TC:
        zoom 1.75 xcenter 317 ycenter 355
        sans_h_move(1.3)
    show s_text "{size=32}i dunno." as s1:
        xcenter 650 ycenter 345
    $ s_say("i dunno.")
    $ pause()
    $ s_say2("uh, i dunno.")
    hide s1
    show sans_t 1 at TC:
        zoom 1.75 xcenter 318 ycenter 517
        sans_t_move(1.3)
    show sans h at TC:
        zoom 1.75 xcenter 317 ycenter 355
        sans_h_move(1.3)
    show s_text "{size=32}maybe that joke\nbook tori gave it\nto me.":
        xcenter 655 ycenter 377
    $ s_say("maybe that joke book tori gave it to me.")
    $ pause()
    $ s_say2("maybe that joke book tori gave it to me.")
    show sans_t 1 at TC:
        zoom 1.75 xcenter 318 ycenter 517
        sans_t_move(1.3)
    show sans b at TC:
        zoom 1.75 xcenter 317 ycenter 355
        sans_h_move(1.3)
    show s_text "{size=32}she really likes\nthat alot.":
        xcenter 645 ycenter 362
    $ s_say("she really likes that alot.")
    $ pause()
    $ s_say2("she really likes that alot.")
    hide s_text
    hide b
    y 2e "Eh? T-Tori...?"
    y 2f "Who is Tori?"
    window hide(None)
    show layer master:
        zoom 1.25 xcenter 900 ycenter 300
    show bg closet:
        zoom 1.175 xcenter 550 ycenter 400
    show sans_t 1 at TC:
        zoom 1.75 xcenter 318 ycenter 517
        sans_t_move(1.3)
    show sans h at TC:
        zoom 1.75 xcenter 317 ycenter 355
        sans_h_move(1.3)
    show b s at TC behind sans_t:
        zoom 1.15 ycenter 395
    show s_text "{size=32}a goat.":
        xcenter 585 ycenter 345
    $ s_say("a goat.")
    $ pause()
    $ s_say2("a goat.")
    hide b
    hide s_text
    show layer master:
        zoom 1.25 xcenter 380 ycenter 425
    show bg closet:
        zoom 1.175 xcenter 700 ycenter 390
    show yuri 3n at i11:
        SP
        zoom 1.25 xcenter 875 ycenter 450 yoffset 0
        easein 0.1 yoffset -10
        easeout 0.1 yoffset 0
    y "A g-goat?!"
    y 3o "Um..."
    y "...You're trying to insult her, aren't you?"
    window hide(None)
    show layer master:
        zoom 1.25 xcenter 900 ycenter 300
    show bg closet:
        zoom 1.175 xcenter 550 ycenter 400
    show sans_t 1 at TC:
        zoom 1.75 xcenter 318 ycenter 517
        sans_t_move(1.3)
    show sans j at TC:
        zoom 1.75 xcenter 317 ycenter 355
        sans_h_move(1.3)
    show b s at TC behind sans_t:
        zoom 1.15 ycenter 395
    show s_text "{size=32}no,":
        xcenter 555 ycenter 345
    $ s_say("no,")
    $ pause(0.4)
    show s_text "{size=32}actually," as s1:
        xcenter 657 ycenter 345
    $ s_say("acutally,")
    $ pause(0.4)
    show s_text "{size=32}she's a goat." as s2:
        xcenter 632 ycenter 378
    $ s_say("she's a goat.")
    $ pause()
    $ s_say2("no, actually, she's a goat.")
    hide s1
    hide s2
    show sans_t 1 at TC:
        zoom 1.75 xcenter 318 ycenter 517
        sans_t_move(1.3)
    show sans h at TC:
        zoom 1.75 xcenter 317 ycenter 355
        sans_h_move(1.3)
    show s_text "{size=32}she's used to act\nand behave like\nhumans.":
        xcenter 662 ycenter 378
    $ s_say("she's used to act and behave like humans.")
    $ pause()
    $ s_say2("she's used to act and behave like humans.")
    show sans_t 1 at TC:
        zoom 1.75 xcenter 318 ycenter 517
        sans_t_move(1.3)
    show sans e at TC:
        zoom 1.75 xcenter 317 ycenter 355
        sans_h_move(1.3)
    show s_text "{size=32}...nevermind.":
        xcenter 635 ycenter 345
    $ s_say("...nevermind.")
    $ pause(0.4)
    show s_text "{size=32}you'll probably\nbe confused at\nthis point." as s1:
        xcenter 647 ycenter 411
    $ s_say("you'll probably be confused at this point.")
    $ pause()
    $ s_say2("...nevermind. you'll probably be confused at this point.")
    hide s_text
    hide s1
    hide b
    show layer master:
        zoom 1.25 xcenter 380 ycenter 425
    show bg closet:
        zoom 1.175 xcenter 700 ycenter 390
    y 3u "..."
    show yuri 1m at i11:
        SP
        zoom 1.25 xcenter 875 ycenter 450 yoffset 0
        easein_quad 0.75 yoffset 15
    y "Well, anyways, about mine..."
    show yuri 1m at i11:
        SP
        zoom 1.25 xcenter 875 ycenter 450 yoffset 15
        ease_cubic 0.5 yoffset 0
    show yuri 1a at i11 as y1:
        SP
        zoom 1.25 xcenter 875 ycenter 450 yoffset 15 alpha 0
        ease_cubic 0.5 yoffset 0 alpha 1
    y "My favorites are usually novels that build deep and comple-{nw}"
    $ _history_list[-1].what = "\"My favorites are usually novels that build deep and comple-\""
    hide y1
    show yuri 1a
    show layer master:
        zoom 1.25 xcenter 900 ycenter 300
    show bg closet:
        zoom 1.175 xcenter 550 ycenter 400
    show sans_t 1 at TC:
        zoom 1.75 xcenter 318 ycenter 517
        sans_t_move(1.3)
    show sans b at TC:
        zoom 1.75 xcenter 317 ycenter 355
        sans_h_move(1.3)
    show b s at TC behind sans_t:
        zoom 1.15 ycenter 395
    show s_text "{size=32}blah,":
        xcenter 570 ycenter 345
    $ s_say("blah,")
    $ pause(0.4)
    show s_text "{size=32}whatever," as s1:
        xcenter 692 ycenter 345
    $ s_say("whatever,")
    show yuri 3v at i11:
        SP
        zoom 1.25 xcenter 875 ycenter 450 yoffset 0
        easein 0.1 yoffset -10
        easeout 0.1 yoffset 0
    $ pause(0.4)
    show s_text "{size=32}i'm out." as s2:
        xcenter 596 ycenter 380
    $ s_say("i'm out.")
    $ pause()
    $ s_say2("blah, whatever, i'm out.")
    hide s_text
    hide s1
    hide s2
    hide b
    show sans_l at TC:
        SP
        zoom 1.75 xcenter 325 ycenter 700
        easeout_cubic 0.5 xcenter -293
    show sans_t 1 at TC:
        SP
        zoom 1.75 xcenter 318 ycenter 517
        parallel:
            sans_t_move(1.3)
        parallel:
            easeout_cubic 0.5 xcenter -300
    show sans b at TC:
        SP
        zoom 1.75 xcenter 317 ycenter 355
        parallel:
            sans_h_move(1.3)
        parallel:
            easeout_cubic 0.5 xcenter -301
    stop music fadeout 2
    $ pause(1.5)
label ch1_s5:
    scene bg class_day:
        zoom 4 xcenter 600 ycenter 450
    with wipeleft_scene
    play music t3
    show monika 5a at i11:
        SP
        zoom 1.5 xcenter 1700 ycenter 510 rotate 12
        parallel:
            easein_quint 1 xcenter 725
        parallel:
            easein_circ 1 rotate 0 ycenter 475
    window auto
    m "Okay!"
    m "I have an idea, everyone~"
    show monika 2b at i11:
        zoom 1.5 xcenter 625 ycenter 475 rotate 0
    m "Let's all go home and write a poem of our own!"
    m "Then, next time we meet, we'll all share them with each other."
    show monika 2k at i11:
        SP
        zoom 1.5 xcenter 625 ycenter 475 rotate 0
        easein_circ 0.5 zoom 1.66 ycenter 525
    show bg class_day:
        SP
        zoom 4 xcenter 600 ycenter 450
        easein_circ 0.5 zoom 4.15 ycenter 467
    m "That way, everyone is even!"
    window hide(None)
    scene bg club_day:
        zoom 1.75 xcenter 800 ycenter 400
    show natsuki 2k at i11:
        zoom 1.25 xcenter 375 ycenter 400
    show yuri 3e at i11:
        zoom 1.25 xcenter 875 ycenter 400
    with Dissolve(0.4)
    $ pause(0.1)
    n 5q "U-Um..."
    y 3v "..."
    show natsuki 5r at i11:
        SP
        zoom 1.25 xcenter 375 ycenter 400 yoffset 0
        parallel:
            ease 0.25 zoom 0.9 ycenter 390 xcenter 350
        parallel:
            easein 0.125 yoffset -40
            easeout 0.125 yoffset 0
    show yuri 4b at i11:
        SP
        zoom 1.25 xcenter 875 ycenter 400 yoffset 0
        parallel:
            ease 0.25 zoom 0.9 ycenter 390 xcenter 900
        parallel:
            easein 0.125 yoffset -40
            easeout 0.125 yoffset 0
    show sayori 4r at i11:
        SP
        zoom 1.25 xcenter 640 ycenter 1100
        easein_elastic 0.725 ycenter 400
    show explode at TC:
        zoom 7
    show explodenew at TC:
        zoom 2.5
    show shockwave at TC:
        zoom 0.5
        shockwave_zoom(0.5)
    show layer master:
        SP
        TC
        layershake(-50, -50, 3.5)
    show layer screens:
        SP
        TC
        layershake(-10, -10, 1)
    show white onlayer front:
        alpha 0.6
        ease 0.25 alpha 0
    $ playexplode()
    s "Yeaaah! Let's do it!"
    hide white onlayer front
    $ hide_explosions()
    show sayori 4r at i11:
        SP
        zoom 1.25 xcenter 640 ycenter 400
        ease_cubic 0.66 xcenter 800
    show monika 1a at i11:
        SP
        zoom 1.25 xcenter -350 ycenter 400
        ease_cubic 0.66 xcenter 300
    m "Plus, now that we have a new member, I think it will help us all get a little more comfortable with each other, and strengthen the bond of the club."
    m "Isn't that right, Sans?"
    window show(None)
    $ pause(0.75)
    show layer master:
        SP
        TC2
        ease_cubic 0.75 xcenter 150
    show bg club_day:
        SP
        zoom 1.75 xcenter 800 ycenter 400
        ease_cubic 0.75 xcenter 1075
    show natsuki 5r at i11:
        SP
        zoom 0.9 xcenter 350 ycenter 390 yoffset 0
        ease_cubic 0.75 xcenter 500
    show yuri 4b at i11:
        SP
        zoom 0.9 xcenter 900 ycenter 390 yoffset 0
        ease_cubic 0.75 xcenter 1050
    show sans_l at TC:
        zoom 1.4 xcenter 1550 ycenter 680
    show sans_t 1 at TC:
        zoom 1.4 xcenter 1542 ycenter 532
        sans_t_move2(1.4)
    show sans e at TC:
        zoom 1.4 xcenter 1540 ycenter 402
        sans_h_move2(1.4)
    
    $ pause(0.55)
    show zzz at TC behind sans:
        SP
        zoom 1.5 xcenter 1550 ycenter 400
        parallel:
            block:
                zzz_move(1.5)
                time 2
                xoffset 0 yoffset 0 zoom 1.5
                0.5
            repeat
        parallel:
            easeout_circ 2 ycenter -100
            ycenter 400
            0.5
            repeat
        parallel:
            linear 2 xcenter 1900
            xcenter 1550
            0.5
            repeat
    show zzz at TC as z1 behind sans:
        SP
        zoom 1.5 xcenter 1550 ycenter 400
        0.35
        parallel:
            block:
                zzz_move(1.5)
                time 2
                xoffset 0 yoffset 0 zoom 1.5
                0.5
            repeat
        parallel:
            easeout_circ 2 ycenter -100
            ycenter 400
            0.5
            repeat
        parallel:
            linear 2 xcenter 1900
            xcenter 1550
            0.5
            repeat
    show zzz at TC as z2 behind sans:
        SP
        zoom 1.5 xcenter 1550 ycenter 400
        0.7
        parallel:
            block:
                zzz_move(1.5)
                time 2
                xoffset 0 yoffset 0 zoom 1.5
                0.5
            repeat
        parallel:
            easeout_circ 2 ycenter -100
            ycenter 400
            0.5
            repeat
        parallel:
            linear 2 xcenter 1900
            xcenter 1550
            0.5
            repeat
    $ pause(0.95)
    m "Umm... Sans?"
    show sayori 1j at i11:
        SP
        zoom 1.25 xcenter 800 ycenter 400
        easein 0.1 yoffset -20
        easeout 0.1 yoffset 0
    s "Sans, wake up!"
    s "This isn't the napping club!"
    stop music fadeout 2
    show monika 3m
    $ pause(0.75)
    show layer master:
        SP
        xcenter 150 ycenter 360
        ease_cubic 1 xcenter 640
    show bg club_day:
        SP
        zoom 1.75 xcenter 1075 ycenter 400
        ease_cubic 1 xcenter 800
    show natsuki 5r at i11:
        SP
        zoom 0.9 xcenter 500 ycenter 390 yoffset 0
        ease_cubic 1 xcenter 350
    show yuri 4b at i11:
        SP
        zoom 0.9 xcenter 1050 ycenter 390 yoffset 0
        ease_cubic 1 xcenter 900
    $ pause(0.6)
    hide sans
    hide sans_t
    hide sans_l
    hide zzz
    hide z1
    hide z2
    m "Uhh, let's...forget about this weird situation."
    m "Once he's awake, I'll notify him."
    window hide(None)
    scene black
    $ quick_menu = False
    play sound paulsans1
    show splash_warning2 "After hours of sleeping," at TC:
        ycenter 300
    $ pause(1.6)
    show splash_warning2 "Sans finally woke up," as s1 at TC:
        ycenter 340
    $ pause(1.5)
    show splash_warning2 "and noticed that nobody is here." as s2 at TC:
        ycenter 380
    $ pause(1.9)
    scene black
    with Dissolve(0.5)
    play sound paulsans2
    show splash_warning2 "Also," at TC:
        ycenter 280
    $ pause(0.7)
    show splash_warning2 "he found a mental note from Monika" at TC as s1:
        ycenter 320
    $ pause(1.75)
    show splash_warning2 "about sharing poems," as s2 at TC:
        ycenter 360
    $ pause(1.49)
    show splash_warning2 "and he returned back to his everyday routine." as s3 at TC:
        ycenter 400
    $ pause(2.66)
    return
    