
screen ch2_choice():
    
    style_prefix "NYEH"
    
    hbox:
        frame:
            textbutton "Yes" action Jump("ch2_yes") at c_trans
        frame:
            textbutton "No" action Jump("ch2_no") at c_trans
    
    timer 0.75 action Jump("ch2_timesup")
            
label ch2:
    stop music
    window hide(None)
    scene black
    with Dissolve(0.5)
    play sound paulsans3
    show splash_warning3 "The next day..."
    $ pause(1)
    scene black
    with Dissolve(0.5)
    $ quick_menu = True
    play music t2 fadein 2
    scene bg club_day:
        zoom 1.75 xcenter 800 ycenter 400
    show sayori 1a2 at i11:
        SP
        zoom 1.35 xcenter -300 ycenter 425
        0.66
        easein_quint 0.85 xcenter 400
    with Dissolve(1)
    window auto
    s "Hi everyone~!"
    s 1d "Sorry, I'm pretty late... Don't expect me being lazy!"
    show natsuki 2k at i11:
        SP
        zoom 1.35 xcenter 1500 ycenter 425
        easein_quint 0.85 xcenter 900
    n "Hrm... You didn't bring that skeleton with you."
    n "And, I'm not expecting his motivations getting even lazier."
    n 2c "It's more than that."
    show layer master:
        SP
        TC2
        zoom 1
        easein_elastic 1 zoom 1.15 xcenter 500
    show bg club_day:
        SP
        zoom 1.75 xcenter 800 ycenter 400
        easein_elastic 1 zoom 1.65 xcenter 850
    show speedline onlayer front at SL:
        alpha 1
        easeout 0.75 alpha 0
    n 1b "Where the {i}hell{/i} is he, anyway?"
    hide speedline onlayer front
    show layer master:
        zoom 1.15 xcenter 900 ycenter 400
    show bg club_day:
        zoom 1.75 xcenter 775 ycenter 380
    show sayori 4l at i11:
        SP
        zoom 1.35 xcenter 400 ycenter 425 yoffset 0
        easein 0.1 yoffset -20
        easeout 0.1 yoffset 0
    s "Ah..."
    s "Well, I think he's coming right now."
    s 1d "You can just stay here and wait."
    show sayori 4q at i11:
        SP
        zoom 1.35 xcenter 400 ycenter 425 yoffset 0
        parallel:
            ease 0.75 zoom 1 ycenter 385
        parallel:
            ease 0.375 yoffset -20
            ease 0.375 yoffset 0
    s "Ehehe..."
    stop music fadeout 3
    show sayori 4q at i11:
        zoom 1 xcenter 475 ycenter 385 yoffset 0
    show layer master:
        zoom 1 xcenter 500 ycenter 360
    show bg club_day:
        zoom 1.75 xcenter 870 ycenter 410
    n 4f "What are you giggling about?"
    $ quick_menu = True
    n "And why are you stepping further away?"
    window hide(None)
    $ quick_menu = False
    play sound horn2
    $ pause(2.1)
    play sound2 impact
    $ pause(0.48)
    show sans_b at TC:
        SP
        nearest True
        zoom 2 xcenter -50 ycenter 505
        linear 0.09 xcenter 900
    $ pause(0.08)
    play audio explode
    show explode at TC:
        zoom 8.75 xcenter 925 ycenter 360
    show explodenew at TC:
        zoom 3.125 xcenter 925 ycenter 360
    show shockwave at TC:
        zoom 0.5 xcenter 925 ycenter 360
        shockwave_zoom(0.5)
    show layer master:
        TC2
        zoom 1 xcenter 500
        layershake(-150, -200, 15)
    show natsuki 1v at i11:
        SP
        zoom 1.35 xcenter 900 ycenter 425
        linear 0.25 xcenter 1650 rotate 360
    show speedline at SL onlayer front:
        alpha 1
        ease 1 alpha 0
    show white onlayer front:
        alpha 0.7
        easeout 0.35 alpha 0
    $ pause(2)
    $ hide_explosions()
    $ quick_menu = True
    hide white onlayer front
    hide speedline onlayer front
    hide natsuki
    play music sans
    show b s at TC:
        zoom 1.05 xzoom -1 xcenter 585 ycenter 400
    show s_text "{size=30}strrriike!!":
        xcenter 518 ycenter 355
    $ s_say("strrriike!!")
    $ pause()
    $ s_say2("strrriike!!")
    hide b
    hide s_text
    show sayori 4r at i11:
        SP
        zoom 1 xcenter 475 ycenter 385 yoffset 0
        easein 0.1 yoffset -20
        easeout 0.1 yoffset 0
    s "Ahaha! We got Natsuki, Sans!"
    show monika 1e at i11 behind sans_b:
        SP
        zoom 1 xcenter 1610 ycenter 385
        easein_quint 0.85 xcenter 1175
    m "Hey, Sans..."
    m "There's a question I need to say."
    m "I saw you hurting our club members."
    m "Could you please make a promise not to do that again?"
    window hide(None)
    play audio ut_ding
    hide sans_b
    show sans_shockwave zorder 1:
        zoom 0.45 xcenter 860 ycenter 450
        easein 0.75 zoom 2.5 alpha 0
    show sans_shockwave zorder 1 as ss1:
        zoom 0.45 xcenter 860 ycenter 450 alpha 0.25
        easein 0.75 zoom 1 alpha 0
    show sans_l at TC:
        zoom 1.5 xcenter 875 ycenter 670
    show sans_t 1 at TC:
        zoom 1.5 xcenter 868 ycenter 515
        sans_t_move(1.15)
    show sans e at TC:
        zoom 1.5 xcenter 865 ycenter 375
        sans_h_move(1.15)
    $ pause(0.75)
    hide sans_shockwave
    hide ss1
    show b s at TC:
        zoom 1.05 xzoom -1 xcenter 585 ycenter 400
    show s_text "{size=30}probably not.":
        xcenter 545 ycenter 350
    $ s_say("probably not.")
    $ pause()
    $ s_say2("probably not.")
    show sans_t 1 at TC:
        zoom 1.5 xcenter 868 ycenter 515
        sans_t_move(1.15)
    show sans h at TC:
        zoom 1.5 xcenter 865 ycenter 375
        sans_h_move(1.15)
    show s_text "{size=30}b'cause you\nalready hurt\nthem from the\nday i came in.":
        xcenter 552 ycenter 399
    $ s_say("b'cause you already hurt them from the day i came in.")
    $ pause()
    $ s_say2("b'cause you already hurt them from the day i came in.")
label ch2_s:
    play sound alert2
    scene bg club_day:
        zoom 1.6 xcenter 935 ycenter 380
    show layer master:
        zoom 1.5 xcenter 0 ycenter 450
    show monika 1d at i11:
        SP
        zoom 1 xcenter 1175 ycenter 385
        easein 0.1 yoffset -12.5
        easeout 0.1 yoffset 0
    show sans_l at TC:
        zoom 1.5 xcenter 875 ycenter 670
    show sans_t 1 at TC:
        zoom 1.5 xcenter 868 ycenter 515
        sans_t_move(1.15)
    show sans h at TC:
        zoom 1.5 xcenter 865 ycenter 375
        sans_h_move(1.15)
    show splash_warning4_5 "{size=100}!" as sp:
        SP
        xcenter 1350 ycenter 225 alpha 1
        parallel:
            easein 0.1 yoffset -30
            easein_elastic 1 yoffset 0
        parallel:
            0.5
            easeout 0.5 alpha 0
    $ pause(1.5)
    window auto
    hide sp
    show monika 1n at i11:
        SP
        zoom 1 xcenter 1175 ycenter 385
        easein_quad 0.75 yoffset 15
    m "Ah..ahaha..."
    show monika 1n at i11:
        SP
        zoom 1 xcenter 1175 ycenter 385 yoffset 15
        ease_cubic 0.25 yoffset 0
    m 3l "Well, I...shouldn't have done that. Apologies!"
    m "We'll both stop hurting each other, okay?"
    window hide(None)
    $ currentpos = get_pos() + 6
    $ audio.t2g3 = "<from " + str(currentpos) + " loop 0>mod_assets/caudio/sans.ogg"
    stop music fadeout 6
    show black at TC behind monika:
        zoom 2.5
        alpha 0
        ease 5 alpha 0.66
    show vignette onlayer front:
        alpha 0
        ease 5 alpha 0.5
    show layer master:
        zoom 1.5 xcenter 350 ycenter 275
    show bg club_day:
        zoom 1.6 xcenter 880 ycenter 400
    show bg club_day_blur as bg1 behind black:
        zoom 1.6 xcenter 880 ycenter 400 alpha 0
        ease 5 alpha 1
        dizzy(0.75, 1.5)
    show sans_t 1 at TC:
        zoom 1.5 xcenter 868 ycenter 515
        sans_t_move(1.15)
    show sans e at TC:
        zoom 1.5 xcenter 865 ycenter 375
        sans_h_move(1.15)
    # let's add that little madlad as a secret, hehe boai!
    show ainsley behind monika:
        zoom 0.1 xcenter 1255 ycenter 530 alpha 0
        2
        alpha 1
        0.05
        alpha 0
    show b s at TC:
        zoom 1.05 xzoom -1 xcenter 595 ycenter 400
    show s_text "{size=30}hmph...":
        xcenter 510 ycenter 350
    $ s_say("hmph...")
    $ pause(0.4)
    show s_text "{size=30}{space=120}good\ngrief." as s1:
        xcenter 547 ycenter 366
    $ s_say("Yare yare..")# daze...
    $ pause()
    $ s_say2("hmph... good grief.")
    hide s1
    show s_text "{size=30}'cause if you\ndon't,":
        xcenter 550 ycenter 368
    $ s_say("'cause if you don't,")
    $ pause(0.4)
    show s_text "{size=30}then..." as s1:
        xcenter 605 ycenter 384
    $ s_say("then...")
    $ pause()
    $ s_say2("'cause if you don't, then...")
    hide b
    hide s_text
    hide s1
    $ pause(0.75)
    hide ainsley
    show black onlayer front
    play sound ut_snap
    $ pause(0.25)
    hide black onlayer front
    play sound ut_snap
    show sans_t 1 at TC:
        zoom 1.5 xcenter 868 ycenter 515 xoffset 0 yoffset 0
    show sans f at TC:
        zoom 1.5 xcenter 865 ycenter 375 xoffset 0 yoffset 0
    $ pause(0.75)
    show b s at TC:
        zoom 1.05 xzoom -1 xcenter 595 ycenter 400
    show s_text "{size=30}{cps=10}i'll keep hurting\nyou 'til you're\ndead.":
        xcenter 575 ycenter 380
    $ pause(3.9)
    $ pause()
    $ s_say2("i'll keep hurting you 'til you're dead.")
    play audio eye
    show layer master:
        SP
        zoom 1.5 xcenter 350 ycenter 275
        easein_circ 0.85 zoom 1.75 xcenter 290 ycenter 250
    with None
    hide b
    hide s_text
    show layer master:
        zoom 1.5 xcenter 0 ycenter 450
    show bg club_day_blur as bg1:
        zoom 1.6 xcenter 935 ycenter 380 alpha 1
        dizzy(0.75, 1.5)
    show monika 1g
    with Dissolve(0.75)
    $ pause(0.5)
    play sound bonk2
    show monika 1r at i11:
        zoom 1 xcenter 1175 ycenter 385
        0.1
        "monika 1g"
        zoom 0.8
    $ pause(0.4)
    play sound bonk3
    show monika 1r at i11:
        zoom 1 xcenter 1175 ycenter 385
        0.1
        "monika 1g"
        zoom 0.8
    $ pause(0.75)
    show layer master:
        zoom 1.5 xcenter 350 ycenter 275
    $ pause(0.5)
    play music t2g3 fadein 0.5
    hide black
    hide vignette onlayer front
    hide bg1
    with Dissolve(0.4)
    $ pause(0.6)
    show sans_t 1 at TC:
        zoom 1.5 xcenter 868 ycenter 515
        sans_t_move(1.15)
    show sans e at TC:
        zoom 1.5 xcenter 865 ycenter 375
        sans_h_move(1.15)
    show b s at TC:
        zoom 1.05 xzoom -1 xcenter 595 ycenter 400
    show s_text "{size=30}...":
        xcenter 480 ycenter 350
    $ s_say("...")
    $ pause()
    $ s_say2("...")
    show sans_t 1 at TC:
        zoom 1.5 xcenter 868 ycenter 515
        sans_t_move(1.15)
    show sans h at TC:
        zoom 1.5 xcenter 865 ycenter 375
        sans_h_move(1.15)
    show s_text "{size=30}hey,":
        xcenter 488 ycenter 350
    $ s_say("hey,")
    $ pause(0.4)
    show s_text "{size=30}lighten up," as s1:
        xcenter 605 ycenter 350
    $ s_say("lighten up,")
    $ pause(0.4)
    show s_text "{size=30}bucko!" as s2:
        xcenter 499 ycenter 385
    $ s_say("bucko!")
    $ pause()
    $ s_say2("hey, lighten up, bucko!")
    show sans_t 1 at TC:
        zoom 1.5 xcenter 868 ycenter 515
        sans_t_move(1.15)
    show sans j at TC:
        zoom 1.5 xcenter 865 ycenter 375
        sans_h_move(1.15)
    hide s1
    hide s2
    show s_text "{size=30}i'm just joking\nwith you.":
        xcenter 562 ycenter 367
    $ s_say("i'm just joking with you.")
    $ pause()
    $ s_say2("i'm just joking with you.")
    show sans_t 1 at TC:
        zoom 1.5 xcenter 868 ycenter 515
        sans_t_move(1.15)
    show sans h at TC:
        zoom 1.5 xcenter 865 ycenter 375
        sans_h_move(1.15)
    show s_text "{size=30}besides...":
        xcenter 527 ycenter 351
    $ s_say("besides...")
    $ pause()
    $ s_say2("besides...")
    show s_text "{size=30}there's no such\nreason to hurt\nanyone like you.":
        xcenter 577 ycenter 383
    $ s_say("there's no such reason to hurt anyone like you.")
    $ pause()
    $ s_say2("there's no such reason to hurt anyone like you.")
    hide b
    hide s_text
    show layer master:
        zoom 1.5 xcenter 0 ycenter 450
    show bg club_day:
        zoom 1.6 xcenter 935 ycenter 380
    show monika 2n at i11:
        SP
        zoom 1 xcenter 1175 ycenter 385
        easein 0.1 yoffset -12.5
        easeout 0.1 yoffset 0
    m "Ah.. yeah...!"
    m 4l "Y-You're right! We won't make any big violence."
    m 2m "Anyways, did you remember to write a poem last night?"
    window hide(None)
    show layer master:
        zoom 1.5 xcenter 350 ycenter 275
    show bg club_day:
        zoom 1.6 xcenter 880 ycenter 400
    with Dissolve(0.5)
    $ pause(0.2)
    show sans_t 1 at TC:
        zoom 1.5 xcenter 868 ycenter 515
        sans_t_move(1.15)
    show sans b at TC:
        zoom 1.5 xcenter 865 ycenter 375
        sans_h_move(1.15)
    show b s at TC behind sans_t:
        zoom 1.05 xzoom -1 xcenter 595 ycenter 400
    show s_text "{size=30}yeah,":
        xcenter 498 ycenter 351
    $ s_say("yeah,")
    $ pause(0.4)
    show s_text "{size=30}but..." as s1:
        xcenter 591 ycenter 351
    $ s_say("but...")
    $ pause()
    $ s_say2("yeah, but...")
    hide s1
    show sans_t 2 at TC:
        zoom 1.5 xcenter 868 ycenter 515
        sans_t_move(1.15)
    show sans c at TC:
        zoom 1.5 xcenter 865 ycenter 375
        sans_h_move(1.15)
    show s_text "{size=30}i'm pretty tired\nto make one.":
        xcenter 576 ycenter 368
    $ s_say("i'm pretty tired to make one.")
    $ pause()
    $ s_say2("i'm pretty tired to make one.")
    show sans_t 1 at TC:
        zoom 1.5 xcenter 868 ycenter 515
        sans_t_move(1.15)
    show sans i at TC:
        zoom 1.5 xcenter 865 ycenter 375
        sans_h_move(1.15)
    show s_text "{size=30}so i let my\nbrother do the\nwork.":
        xcenter 562 ycenter 383
    $ s_say("so i let my brother do the work.")
    $ pause()
    $ s_say2("so i let my brother do the work.")
    show sans_t 1 at TC:
        zoom 1.5 xcenter 868 ycenter 515
        sans_t_move(1.15)
    show sans h at TC:
        zoom 1.5 xcenter 865 ycenter 375
        sans_h_move(1.15)
    show s_text "{size=30}pretty cool,":
        xcenter 547 ycenter 351
    $ s_say("pretty cool,")
    $ pause(0.4)
    show s_text "{size=30}huh?" as s1:
        xcenter 487 ycenter 385
    $ s_say("huh?")
    $ pause()
    $ s_say2("pretty cool, huh?")
    hide s_text
    hide s1
    hide b
    show layer master:
        zoom 1.5 xcenter 350 ycenter 275
        layershake(-50, -50, 5, 0.75)
    show speedline onlayer front at SL:
        alpha 1
        easeout 0.75 alpha 0
    show layer screens:
        TC
        layershake(-10, -10, 2, 0.75)
    s "W-WHAT?!"
    window hide(None)
    play sound whoosh3
    show layer master:
        SP
        zoom 1.5 xcenter 350 ycenter 275
        ease_circ 0.35 xcenter 1500 ycenter 400
    show bg club_day:
        SP
        zoom 1.6 xcenter 880 ycenter 400
        ease_circ 0.35 xcenter 400 ycenter 375
    show sayori 1j at i11:
        zoom 1 xcenter 65 ycenter 385
    $ pause(0.75)
    hide speedline onlayer front
    s "Not cool!"
    s "You gave your brother your work?"
    show sans_t 1 at TC:
        zoom 1.5 xcenter 868 ycenter 515
        sans_t_move(1.15)
    show sans b at TC:
        zoom 1.5 xcenter 865 ycenter 375
        sans_h_move(1.15)
    show bg club_day:
        SP
        zoom 1.6 xcenter 400 ycenter 375
        layershake2(5, 5, 0.75)
    show layer master:
        SP
        zoom 1.5 xcenter 1500 ycenter 400
        layershake2(-15, -15, 0.75)
    show layer screens:
        TC
        SP
        layershake2(-5, -5, 0.75)
    s "What a shameful thing to do!"
    s "I thought you made it!"
    show layer master:
        zoom 1.5 xcenter 0 ycenter 450
    show bg club_day:
        zoom 1.6 xcenter 935 ycenter 380
    show monika 4b
    m "That's okay, Sayori."
    m "Give him a chance; He was very exhausted to write a poem."
    m "And since this is the first time sharing, he'll come up with a masterpiece in the next day!"
    m 4k "Alright! Let's get started, shall we?"
    window hide(None)
    show layer master:
        zoom 1.5 xcenter 350 ycenter 275
    show bg club_day:
        zoom 1.6 xcenter 880 ycenter 400
    show b s at TC behind sans_t:
        zoom 1.05 xzoom -1 xcenter 595 ycenter 400
    show s_text "{size=30}...":
        xcenter 480 ycenter 351
    $ s_say("...")
    $ pause()
    $ s_say2("...")
    show sans_t 1 at TC:
        zoom 1.5 xcenter 868 ycenter 515
        sans_t_move(1.15)
    show sans h at TC:
        zoom 1.5 xcenter 865 ycenter 375
        sans_h_move(1.15)
    show s_text "{size=30}nope.":
        xcenter 496 ycenter 351
    $ s_say("nope.")
    $ pause()
    $ s_say2("nope.")
    show sans_t 1 at TC:
        zoom 1.5 xcenter 868 ycenter 515
        sans_t_move(1.15)
    show sans j at TC:
        zoom 1.5 xcenter 865 ycenter 375
        sans_h_move(1.15)
    show s_text "{size=30}i'm going to\ngrillby's.":
        xcenter 544 ycenter 369
    $ s_say("i'm going to grillby's.")
    $ pause()
    $ s_say2("i'm going to grillby's.")
    hide b
    hide s_text
    show layer master:
        zoom 1.5 xcenter 0 ycenter 450
    show bg club_day:
        zoom 1.6 xcenter 935 ycenter 380
    show monika 1g at i11:
        SP
        zoom 1 xcenter 1175 ycenter 385
        easein 0.1 yoffset -12.5
        easeout 0.1 yoffset 0
    m "Again?!"
    show layer master:
        zoom 1.5 xcenter 350 ycenter 275
    show bg club_day:
        zoom 1.6 xcenter 880 ycenter 400
    show sans_t 1 at TC:
        zoom 1.5 xcenter 868 ycenter 515
        sans_t_move(1.15)
    show sans e at TC:
        zoom 1.5 xcenter 865 ycenter 375
        sans_h_move(1.15)
    show b s at TC behind sans_t:
        zoom 1.05 xzoom -1 xcenter 595 ycenter 400
    show s_text "{size=30}sorry,":
        xcenter 505 ycenter 351
    $ s_say("sorry,")
    $ pause(0.4)
    show s_text "{size=30}pal." as s1:
        xcenter 590 ycenter 351
    $ s_say("pal.")
    $ pause()
    $ s_say2("sorry, pal.")
    hide s1
    show sans_t 1 at TC:
        zoom 1.5 xcenter 868 ycenter 515
        sans_t_move(1.15)
    show sans b at TC:
        zoom 1.5 xcenter 865 ycenter 375
        sans_h_move(1.15)
    show s_text "{size=30}i must have a\nbrunch.":
        xcenter 553 ycenter 367
    $ s_say("i must have a brunch.")
    $ pause()
    $ s_say2("i must have a brunch.")
    show sans_t 1 at TC:
        zoom 1.5 xcenter 868 ycenter 515
        sans_t_move(1.15)
    show sans d at TC:
        zoom 1.5 xcenter 865 ycenter 375
        sans_h_move(1.15)
    show s_text "{size=30}cya.":
        xcenter 490 ycenter 351
    $ s_say("cya.")
    $ pause()
    $ s_say2("cya.")
    stop music fadeout 2
    play sound run2
    hide b
    hide s_text
    hide sans
    hide sans_t
    hide sans_l
    show sans_w2 at TC:
        SP
        nearest True
        zoom 2.5 xcenter 870 ycenter 480 xzoom -1
        linear 1 xcenter 900
        linear 0.25 xcenter 300
    $ pause(1)
    play sound run3
    $ pause(1.33)
label ch2_s2:
    if not persistent.ch2_both:
        $ persistent.ch2_both = None
    else:
        pass
    stop music
    scene black ######### <(0_0<) <(0_0)> (>0_0)>  .+* KIRBY DANCE! *+.
    play audio hihats 
    show splash_warning2 "{size=70} (._.  \")":
        ycenter 440 xcenter 655
    show splash_warning2 "{size=70}\      \ " as s1:
        SP
        ycenter 440 xcenter 623
        ease_back 0.5 ycenter 410
        0.25
        ease_cubic 0.5 ycenter 440
    show splash_warning2 "{size=80}1 hour later..." as s2:
        SP
        xcenter 625 ycenter 370
        ease_back 0.5 ycenter 340
    $ pause(1.25)
    scene black
    with Dissolve(0.5)
    ################################# This will create a little bites-of-lag.
    ####### REN'PY QUEEN. DAISEN NO BAKOUDAN. BITES ZA LAG'O!
    play music corridors fadein 4
    scene bg corridor:
        TC
        zoom 1.75 ycenter 325
        easein_back 2 ycenter 300
    show vignette zorder 3:
        alpha 0.6 additive -0.25
    show dark zorder 2:
        alpha 0.75
        block:
            6
            ease_cubic 3 alpha 0.65
            ease_cubic 3 alpha 0.75
            repeat
    show mask zorder 1 at TC as m1:
        SP
        zoom 1 ycenter 410 xtile 3 additive 0.25 alpha 0.65 xzoom -1
        parallel:
            xcenter 640
            linear 120 xcenter -640
            repeat
        parallel:
            easein_back 2 ycenter 360
    show mask zorder 1 at TC as m2:
        SP
        zoom 1.5 ycenter 410 xtile 3 additive 0.25 alpha 0.65
        parallel:
            xcenter 640
            linear 60 xcenter -1280
            repeat
        parallel:
            easein_back 2 ycenter 360
    show sans_l at TC:
        SP
        zoom 1.75 xcenter 1509 ycenter 670
        1
        easein_cubic 1 xcenter 670
    show sans_t 1 at TC:
        SP
        zoom 1.75 xcenter 1500 ycenter 485
        parallel:
            sans_t_move(1.25)
        parallel:
            1
            easein_cubic 1 xcenter 661
    show sans a at TC:
        SP
        zoom 1.75 xcenter 1497 ycenter 322
        parallel:
            sans_h_move(1.25)
        parallel:
            1
            easein_cubic 1 xcenter 658
    with Dissolve(2)
    $ pause(0.25)
    show b m at TC behind sans_t:
        xzoom -1 xcenter 350
    show s_text "{size=38}huh,":
        xcenter 260 ycenter 270
    $ s_say("huh,")
    $ pause(0.4)
    show s_text "{size=38}{space=80}it's\npretty dark\nin here." as s1:
        xcenter 335 ycenter 310
    $ s_say("it's pretty dark in here.")
    $ pause()
    $ s_say2("huh, it's pretty dark in here.")
    hide s1
    show sans_t 1 at TC:
        zoom 1.75 xcenter 661 ycenter 485
        sans_t_move(1.25)
    show sans b at TC:
        zoom 1.75 xcenter 658 ycenter 322
        sans_h_move(1.25)
    show s_text "{size=38}there's a\nlight switch\nnearby.":
        xcenter 332 ycenter 310
    $ s_say("there's a light switch nearby.")
    $ pause()
    $ s_say2("there's a light switch nearby.")
    show sans_t 2 at TC:
        zoom 1.75 xcenter 661 ycenter 485
        sans_t_move(1.25)
    show sans b at TC:
        zoom 1.75 xcenter 658 ycenter 322
        sans_h_move(1.25)
    show s_text "{size=38}i dunno why\npeople left\nthis place\ngloomy.":
        xcenter 331 ycenter 329
    $ s_say("i dunno why people left this place gloomy.")
    $ pause()
    $ s_say2("i dunno why people left this place gloomy.")
    show sans_t 1 at TC:
        zoom 1.75 xcenter 661 ycenter 485
        sans_t_move(1.25)
    show sans e at TC:
        zoom 1.75 xcenter 658 ycenter 322
        sans_h_move(1.25)
    show s_text "{size=38}tell ya\nwhat?":
        xcenter 290 ycenter 289
    $ s_say("tell ya what?")
    $ pause()
    $ s_say2("tell ya what?")
    show sans_t 1 at TC:
        zoom 1.75 xcenter 661 ycenter 485
        sans_t_move(1.25)
    show sans a at TC:
        zoom 1.75 xcenter 658 ycenter 322
        sans_h_move(1.25)
    show s_text "{size=38}has the\nschool\nbothered us\nto switch on\nthe lights?":
        xcenter 336 ycenter 349
    $ s_say("has the school bothered us to switch on the lights?")
    $ pause()
    $ s_say2("has the school bothered us to switch on the lights?")
    hide s_text
    hide b
    call screen ch2_choice()
    return

label ch2_yes:                   ####### YES #######
    hide screen ch2_choice
    show b m at TC behind sans_t:
        xzoom -1 xcenter 350
    show s_text "{size=38}wow,":
        xcenter 270 ycenter 270
    $ s_say("wow,")
    $ pause(0.4)
    show s_text "{size=38}{space=100}you\nanswered\nfast," as s1:
        xcenter 304 ycenter 310
    $ s_say("you answered fast,")
    $ pause(0.4)
    show s_text "{size=38}huh?" as s2:
        xcenter 368 ycenter 350
    $ s_say("huh?")
    $ pause()
    $ s_say2("wow, you answered fast, huh?")
    hide s1
    hide s2
    show sans_t 1 at TC:
        zoom 1.75 xcenter 661 ycenter 485
        sans_t_move(1.25)
    show sans b at TC:
        zoom 1.75 xcenter 658 ycenter 322
        sans_h_move(1.25)
    show s_text "{size=38}you should\nprobably\nhesitate\nmore.":
        xcenter 319 ycenter 329
    $ s_say("you should probably hesitate more.")
    $ pause()
    $ s_say2("you should probably hesitate more.")
    show s_text "{size=38}i guess the\nlights ain't\nnecessary\nanymore.":
        xcenter 327 ycenter 329
    $ s_say("i guess the lights ain't necessary anymore.")
    $ pause()
    $ s_say2("i guess the lights ain't necessary anymore.")
    show sans_t 2 at TC:
        zoom 1.75 xcenter 661 ycenter 485
        sans_t_move(1.25)
    show sans b at TC:
        zoom 1.75 xcenter 658 ycenter 322
        sans_h_move(1.25)
    show s_text "{size=38}'cause we\ngot sunlight\ncomin'.":
        xcenter 333 ycenter 310
    $ s_say("'cause we got sunlight comin'.")
    $ pause()
    $ s_say2("'cause we got sunlight comin'.")
    if persistent.ch2_both:
        jump ch2_both
    elif persistent.ch2_both == None:
        $ persistent.ch2_both = True
    else:
        pass
label ch2_sunday:
    hide s_text
    hide s1
    hide b
    $ pause(1.5)
    show b m at TC behind sans_t:
        xzoom -1 xcenter 350
    show sans_t 1 at TC:
        zoom 1.75 xcenter 661 ycenter 485
        sans_t_move(1.25)
    show sans e at TC:
        zoom 1.75 xcenter 658 ycenter 322
        sans_h_move(1.25)
    show s_text "{size=38}hmm...":
        xcenter 285 ycenter 270
    $ s_say("hmm...")
    $ pause()
    $ s_say2("hmm...")
    show s_text "{size=38}i see that\nthe sun is\nvery far\naway.":
        xcenter 314 ycenter 329
    $ s_say("i see that the sun is very far away.")
    $ pause()
    $ s_say2("i see that the sun is very far away.")
    show sans_t 1 at TC:
        zoom 1.75 xcenter 661 ycenter 485
        sans_t_move(1.25)
    show sans d at TC:
        zoom 1.75 xcenter 658 ycenter 322
        sans_h_move(1.25)
    show s_text "{size=38}probably\nit'll come\nback when it\nis {color=#d7df88}sun{/color}-day.":
        xcenter 337 ycenter 329
    $ s_say("probably it'll come back when it is sun-day.")
    $ pause()
    $ s_say2("probably it'll come back when it is sun-day.")
    jump ch2_end

label ch2_no:                   ####### NO #######
    hide screen ch2_choice
    show b m at TC behind sans_t:
        xzoom -1 xcenter 350
    show s_text "{size=38}wow,":
        xcenter 270 ycenter 270
    $ s_say("wow,")
    $ pause(0.4)
    show s_text "{size=38}{space=100}you\nanswered\nfast," as s1:
        xcenter 304 ycenter 310
    $ s_say("you answered fast,")
    $ pause(0.4)
    show s_text "{size=38}huh?" as s2:
        xcenter 368 ycenter 350
    $ s_say("huh?")
    $ pause()
    $ s_say2("wow, you answered fast, huh?")
    hide s1
    hide s2
    show sans_t 1 at TC:
        zoom 1.75 xcenter 661 ycenter 485
        sans_t_move(1.25)
    show sans b at TC:
        zoom 1.75 xcenter 658 ycenter 322
        sans_h_move(1.25)
    show s_text "{size=38}you should\nprobably\nhesitate\nmore.":
        xcenter 319 ycenter 329
    $ s_say("you should probably hesitate more.")
    $ pause()
    $ s_say2("you should probably hesitate more.")
    show s_text "{size=38}hmm,":
        xcenter 266 ycenter 270
    $ s_say("hmm,")
    $ pause(0.4)
    show s_text "{size=38}{space=90}that's\na great\nanswer." as s1:
        xcenter 327 ycenter 310
    $ s_say("that's a great answer.")
    $ pause()
    $ s_say2("hmm, that's a great answer.")
    hide s1
    show s_text "{size=38}we'll just\nleave it,":
        xcenter 317 ycenter 289
    $ s_say("we'll just leave it,")
    $ pause(0.4)
    show s_text "{size=38}the sunlight\nwill lit up\nthis place." as s1:
        xcenter 333 ycenter 390
    $ s_say("the sunlight will lit up this place.")
    $ pause()
    $ s_say2("we'll just leave it, the sunlight will lit up this place.")
    if persistent.ch2_both:
        jump ch2_both
    elif persistent.ch2_both == None:
        $ persistent.ch2_both = True
    else:
        pass
    jump ch2_sunday

label ch2_both:                  ####### BOTH #######
    hide s1
    show sans_t 1 at TC:
        zoom 1.75 xcenter 661 ycenter 485
        sans_t_move(1.25)
    show sans a at TC:
        zoom 1.75 xcenter 658 ycenter 322
        sans_h_move(1.25)
    show s_text "{size=38}wait,":
        xcenter 273 ycenter 270
    $ s_say("wait,")
    $ pause(0.4)
    show s_text "{size=38}{space=105}am i\nasking this\ntwice?" as s1:
        xcenter 322 ycenter 310
    $ s_say("am i asking this twice?")
    $ pause()
    $ s_say2("wait, am i asking this twice?")
    hide s1
    show sans_t 1 at TC:
        zoom 1.75 xcenter 661 ycenter 485
        sans_t_move(1.25)
    show sans k at TC:
        zoom 1.75 xcenter 658 ycenter 322
        sans_h_move(1.25)
    show s_text "{size=38}i mean...":
        xcenter 309 ycenter 270
    $ s_say("i mean...")
    $ pause()
    $ s_say2("i mean...")
    show s_text "{size=38}you chose\nboth,":
        xcenter 314 ycenter 289
    $ s_say("you chose both,")
    $ pause(0.4)
    show s_text "{size=38}{space=105}and i\nend up with\nsunlights." as s1:
        xcenter 330 ycenter 349
    $ s_say("and i end up with sunlights.")
    $ pause()
    $ s_say2("you chose both, and i end up with sunlights.")
    hide s1
    show sans_t 2 at TC:
        zoom 1.75 xcenter 661 ycenter 485
        sans_t_move(1.25)
    show sans e at TC:
        zoom 1.75 xcenter 658 ycenter 322
        sans_h_move(1.25)
    show s_text "{size=38}eh,":
        xcenter 253 ycenter 270
    $ s_say("eh,")
    $ pause(0.4)
    show s_text "{size=38}{space=70}choices\nno matter." as s1:
        xcenter 324 ycenter 290
    $ s_say("choices no matter.")
    $ pause()
    $ s_say2("eh, choices no matter.")

    hide s1
    show sans_t 1 at TC:
        zoom 1.75 xcenter 661 ycenter 485
        sans_t_move(1.25)
    show sans i at TC:
        zoom 1.75 xcenter 658 ycenter 322
        sans_h_move(1.25)
    show s_text "{size=38}anyhooow...":
        xcenter 335 ycenter 270
    $ s_say("anyhooow...")
    $ pause()
    $ s_say2("anyhooow...")
    $ persistent.ch2_both = False
    jump ch2_sunday

label ch2_timesup:               ####### TIMES UP #######
    hide screen ch2_choice
    show b m at TC behind sans_t:
        xzoom -1 xcenter 350
    show s_text "{size=38}eh,":
        xcenter 255 ycenter 270
    $ s_say("eh,")
    $ pause(0.4)
    show s_text "{size=38}{space=75}don't\nbother\nanswering\nthat." as s1:
        xcenter 311 ycenter 330
    $ s_say("don't bother answering that.")
    $ pause()
    $ s_say2("eh, don't bother answering that.")
    hide s1
    show sans_t 1 at TC:
        zoom 1.75 xcenter 661 ycenter 485
        sans_t_move(1.25)
    show sans b at TC:
        zoom 1.75 xcenter 658 ycenter 322
        sans_h_move(1.25)
    show s_text "{size=38}this is kinda\npower-saving,":
        xcenter 347 ycenter 289
    $ s_say("this is kinda power-saving,")
    $ pause(0.4)
    show s_text "{size=38}i think." as s1:
        xcenter 295 ycenter 355
    $ s_say("i think.")
    $ pause()
    $ s_say2("this is kinda power-saving, i think.")
    
label ch2_end:
    hide s1
    show sans_t 1 at TC:
        zoom 1.75 xcenter 661 ycenter 485
        sans_t_move(1.25)
    show sans a at TC:
        zoom 1.75 xcenter 658 ycenter 322
        sans_h_move(1.25)
    show s_text "{size=38}anyways,":
        xcenter 309 ycenter 270
    $ s_say("anyways,")
    $ pause(0.4)
    show s_text "{size=38}forget about\nthe lights," as s1:
        xcenter 340 ycenter 330
    $ s_say("forget about the lights,")
    $ pause(0.4)
    show s_text "{size=38}let's\ncontinue." as s2:
        xcenter 310 ycenter 412
    $ s_say("let's continue.")
    $ pause()
    $ s_say2("anyways, forget about the lights, let's continue.")
label ch2_s3:
    stop music
    scene black
    play sound closet_close
    $ pause(1.5)
    play music sotl fadein 2
    scene bg club_day at TC:
        zoom 1.75 xcenter 800
    # Another little madlade that lives on the corner! HELLYEEA
    show ainsley at TC:
        zoom 0.2 xcenter 25 ycenter 20 xzoom -1 alpha 0
        1
        alpha 1
        0.05
        alpha 0
    show sans_l at TC:
        SP
        zoom 1.5 xcenter -193 ycenter 670
        0.25
        easein_cubic 1 xcenter 300
    show sans_t 1 at TC:
        SP
        zoom 1.5 xcenter -200 ycenter 512
        parallel:
            sans_t_move(1.25)
        parallel:
            0.25
            easein_cubic 1 xcenter 293
    show sans a at TC:
        SP
        zoom 1.5 xcenter -202 ycenter 372
        parallel:
            sans_h_move(1.25)
        parallel:
            0.25
            easein_cubic 1 xcenter 291
    with wipeleft
    $ pause(0.5)
    show b s at TC:
        zoom 1.1 xcenter 600 ycenter 390
    show s_text "{size=32}hey,":
        xcenter 535 ycenter 335
    $ s_say("hey,")
    $ pause(0.4)
    show s_text "{size=32}everyone." as s1:
        xcenter 650 ycenter 335
    $ s_say("everyone.")
    $ pause()
    $ s_say2("hey, everyone.")
    hide ainsley
    hide b
    hide s_text
    hide s1
    show monika 1b at i11 zorder 9:
        SP
        xcenter 1500
        easein_back 0.75 xcenter 875
    show monika 1b at i11 as m1 zorder 8:
        SP
        xcenter 1500 alpha 0.4
        0.075
        easein_back 0.75 xcenter 875
    show monika 1b at i11 as m2 zorder 7:
        SP
        xcenter 1500 alpha 0.25
        0.15
        easein_back 0.75 xcenter 875
    show monika 1b at i11 as m3 zorder 6:
        SP
        xcenter 1500 alpha 0.1
        0.225
        easein_back 0.75 xcenter 875
    play sound [ "<silence 0.05>", audio.whoosh4 ]
    m "Oh, thank goodness. Your back!"
    m "The time for sharing poems has already been started, so I kept worrying about you..."
    hide m1
    hide m2
    hide m3
    m "...and you're back on a habit!"
    show monika 5a zorder 0
    m "I highly recommend that you'd show your poem to me first, if you insist~"
    window hide(None)
    show b s at TC zorder 1:
        zoom 1.1 xcenter 600 ycenter 390
    show sans_t 1 at TC:
        zoom 1.5 xcenter 293 ycenter 512
        sans_t_move(1.25)
    show sans h at TC:
        zoom 1.5 xcenter 291 ycenter 372
        sans_h_move(1.25)
    show s_text "{size=32}'aight," zorder 2:
        xcenter 552 ycenter 335
    $ s_say("'aight,")
    $ pause(0.4)
    show s_text "{size=32}{space=112}let's do\nit then." as s1 zorder 2:
        xcenter 618 ycenter 351
    $ s_say("let's do it then.")
    $ pause()
    $ s_say2("'aight, let's do it then.")
    hide s_text
    hide s1
    hide b
    show black at TC zorder 99
    show splash_warning2 "{size=100}5 seconds later..." at TC zorder 100
    $ pause(1)
    hide black
    hide splash_warning2
    show layer master:
        zoom 1.5 xcenter 450 ycenter 475
    show bg club_day:
        zoom 1.6 xcenter 825 ycenter 340
    show monika 3a zorder 0
    show papyrus at TC zorder 2:
        zoom 0.2 xcenter 670 ycenter 260 rotate -7.5
    show splash_warning4_5 "{size=40}-{space=0}->" as sp1:
        xcenter 625 ycenter 140 rotate 70 alpha 1
        parallel:
            dizzy(0.5, 0.01)
        parallel:
            1.5
            ease 0.5 alpha 0
    show splash_warning4_5 "{size=25}(Papyrus's poem made\nout of papyrus)" as sp2:
        xcenter 500 ycenter 100 alpha 1
        1.5
        ease 0.5 alpha 0
    $ pause(2.25)
    hide sp1
    hide sp2
    m 3b "I kinda like this one!"
    m "It looks very unique, by the way. This poem uses papyrus for the first time."
    window hide(None)
    play sound machine
    show layer master:
        SP
        zoom 1.5 xcenter 450 ycenter 475
        linear 0.25 xcenter 900 ycenter 310
    show bg club_day:
        SP
        zoom 1.6 xcenter 825 ycenter 340
        linear 0.25 xcenter 750 ycenter 380
    $ pause(0.25)
    stop sound
    $ pause(0.25)
    show b s at TC zorder 2:
        zoom 1.1 xcenter 600 ycenter 390
    show s_text "{size=32}huh?" zorder 2:
        xcenter 535 ycenter 335
    $ s_say("huh?")
    $ pause(0.4)
    show s_text "{size=32}{space=80}did you\nmention my\nbrother's name?" as s1 zorder 2:
        xcenter 621 ycenter 367
    $ s_say("did you mention my brother's name?")
    $ pause()
    $ s_say2("huh? did you mention my brother's name?")
    hide b
    hide s_text
    hide s1
    play sound "<from 0.679>mod_assets/sfx/machine2.ogg"
    show layer master:
        SP
        zoom 1.5 xcenter 900 ycenter 310
        linear 0.25 xcenter 450 ycenter 475
    show bg club_day:
        SP
        zoom 1.6 xcenter 750 ycenter 380
        linear 0.25 xcenter 825 ycenter 340
    show monika 3d at i11 as m1 zorder 1:
        xcenter 875 alpha 0
        linear 0.25 alpha 1
    $ pause(0.25)
    stop sound
    $ pause(0.125)
    m 3d "No, I mean... the paper itself!"
    hide m1
    m "I never saw a poem written on a piece of paper like this!"
    m "Wait, your brother's name is Papyrus?"
    m 4b "Well, I guess you two must be the best {i}font{/i} brothers! Ahaha!"
    window hide
    play sound machine
    show layer master:
        SP
        zoom 1.5 xcenter 450 ycenter 475
        linear 0.25 xcenter 900 ycenter 310
    show bg club_day:
        SP
        zoom 1.6 xcenter 825 ycenter 340
        linear 0.25 xcenter 750 ycenter 380
    $ pause(0.25)
    stop sound
    $ pause(0.25)
    show sans_t 1 at TC:
        zoom 1.5 xcenter 293 ycenter 512
        sans_t_move(1.25)
    show sans e at TC:
        zoom 1.5 xcenter 291 ycenter 372
        sans_h_move(1.25)
    show b s at TC zorder 2:
        zoom 1.1 xcenter 600 ycenter 390
    show s_text "{size=32}..." zorder 2:
        xcenter 525 ycenter 335
    $ s_say("...")
    $ pause()
    $ s_say2("...")
    show s_text "{size=32}whatever you\nsay," zorder 2:
        xcenter 602 ycenter 351
    $ s_say("whatever you say,")
    $ pause(0.4)
    show s_text "{size=32}pal..." as s1 zorder 2:
        xcenter 625 ycenter 368
    $ s_say("pal...")
    $ pause()
    $ s_say2("whatever you say, pal...")
    hide s1
    show sans_t 1 at TC:
        zoom 1.5 xcenter 293 ycenter 512
        sans_t_move(1.25)
    show sans h at TC:
        zoom 1.5 xcenter 291 ycenter 372
        sans_h_move(1.25)
    show s_text "{size=32}my brother did\na great job\nputting effort\ninto it." zorder 2:
        xcenter 614 ycenter 384
    $ s_say("my brother did a great job putting effort into it.")
    $ pause()
    $ s_say2("my brother did a great job putting effort into it.")
    show s_text "{size=32}so maybe the\npoem will\nimpress you." zorder 2:
        xcenter 600 ycenter 368
    $ s_say("so maybe the poem will impress you.")
    $ pause()
    $ s_say2("so maybe the poem will impress you.")
    show sans_t 1 at TC:
        zoom 1.5 xcenter 293 ycenter 512
        sans_t_move(1.25)
    show sans b at TC:
        zoom 1.5 xcenter 291 ycenter 372
        sans_h_move(1.25)
    show s_text "{size=32}...or the other\nfellas around." zorder 2:
        xcenter 621 ycenter 352
    $ s_say("...or the other fellas around.")
    $ pause()
    $ s_say2("...or the other fellas around.")
    hide b
    hide s_text
    show layer master:
        zoom 1.75 xcenter 400 ycenter 525
    show bg club_day:
        zoom 1.5 xcenter 840 ycenter 330
    m 3p "Hey, this poem is all about spaghetti and stuff."
    m "Why does he love spaghetti and write it in this way?"
    play sound2 fart4
    show layer master:
        zoom 1.5 xcenter 900 ycenter 310
    show bg club_day:
        zoom 1.6 xcenter 750 ycenter 380
    show sans_t 1 at TC zorder 3:
        zoom 1.5 xcenter 293 ycenter 512 xoffset 0 yoffset 0
    show sans i at TC zorder 4:
        zoom 1.5 xcenter 291 ycenter 372 xoffset 0 yoffset 0
    $ pause(0.66)
    show b s at TC zorder 2:
        zoom 1.1 xcenter 600 ycenter 390
    show s_text "{size=32}cool or not," zorder 2:
        xcenter 596 ycenter 335
    $ s_say("cool or not,")
    $ pause(0.4)
    show s_text "{size=32}he's the best\nat cooking\nspaghetti." as s1 zorder 2:
        xcenter 600 ycenter 402
    $ s_say("he's the best at cooking spaghetti.")
    $ pause()
    $ s_say2("cool or not, he's the best at cooking spaghetti.")
    hide s1
    show s_text "{size=32}it's his\nfavorite hobby." zorder 2:
        xcenter 620 ycenter 351
    $ s_say("it's his favorite hobby.")
    $ pause()
    $ s_say2("it's his favorite hobby.")
    show sans_t 2 zorder 3
    show s_text "{size=32}so why are you\ntryin' to judge?" zorder 2:
        xcenter 630 ycenter 351
    $ s_say("so why are you tryin' to judge?")
    $ pause()
    $ s_say2("so why are you tryin' to judge?")
label ch2_poemstart:
    $ n_readpoem = False
    $ y_readpoem = False
    $ s_readpoem = False
    $ poemsread = 0
    
label ch2_poemloop:
    scene black:
        TC
        zoom 2
    with wiperound
    show layer master at topleft:
        zoom 0.8 ycenter 250
    show layer screens at TC:
        SP
        xcenter -640
        easein_back 1 xcenter 640
    
    show sans_l at TC:
        SP
        zoom 1.5 xcenter -193 ycenter 670
        easein_back 1 xcenter 300
    show sans_t 1 at TC:
        SP
        zoom 1.5 xcenter -200 ycenter 514
        parallel:
            sans_t_move(1.25)
        parallel:
            easein_back 1 xcenter 293
    show sans a at TC:
        SP
        zoom 1.5 xcenter -202 ycenter 374
        parallel:
            sans_h_move(1.25)
        parallel:
            easein_back 1 xcenter 291
    show splash_warning2 "(I'm too lazy to make sans's reaction to their poems, sorry.)":
        xcenter 800 ycenter 100 alpha 0
        ease 0.5 alpha 0.33 
    window hide(None)
    menu:
        "Who should Sans show his brother's poem to next?"
        
        "Sayori" if not s_readpoem:
            $ s_readpoem = True
            call ch2_sayori from _call_ch2_sayori
        "Natsuki" if not n_readpoem:
            $ n_readpoem = True
            call ch2_natsuki from _call_ch2_natsuki
        "Yuri" if not y_readpoem:
            $ y_readpoem = True
            call ch2_yuri from _call_ch2_yuri
    
    $ poemsread += 1
    if poemsread < 3:
        jump ch2_poemloop
    
    $ n_readpoem = False
    $ y_readpoem = False
    $ s_readpoem = False
    $ poemsread = 0
    
    call ch2_poemend from _call_ch2_poemend
    return


label ch2_natsuki:
    scene bg class_day:
        TC2
        zoom 2.25 xcenter 250
    show natsuki 1c at i11:
        zoom 1.125 xcenter 900 ycenter 365
    show sans_l at TC:
        zoom 1.5 xcenter 325 ycenter 690
    show sans_t 1 at TC:
        zoom 1.5 xcenter 317 ycenter 536
        sans_t_move(1.25)
    show sans h at TC:
        zoom 1.5 xcenter 315 ycenter 395
        sans_h_move(1.25)
    show papyrus at TC:
        zoom 0.25 xcenter 700 ycenter 350 rotate -7.5
    with wiperound_scene
    window auto
    n "..."
    n 2b "Sans, you expect me to believe that you actually put effort into this?"
    n "Thanks, but it really didn't come out nice at all!"
    window hide(None)
    show b m at TC:
        zoom 0.9 xcenter 610 ycenter 420
    show s_text "{size=32}hey,":
        xcenter 565 ycenter 330
    $ s_say("hey,")
    $ pause(0.4)
    show s_text "{size=32}pal." as s1:
        xcenter 637 ycenter 330
    $ s_say("pal.")
    $ pause()
    $ s_say2("hey, pal.")
    hide s1
    show s_text "{size=32}i have two\npurposes.":
        xcenter 611 ycenter 346
    $ s_say("i have two purposes.")
    $ pause()
    $ s_say2("i have two purposes.")
    show sans_t 1 at TC:
        zoom 1.5 xcenter 317 ycenter 536
        sans_t_move(1.25)
    show sans b at TC:
        zoom 1.5 xcenter 315 ycenter 395
        sans_h_move(1.25)
    show s_text "{size=32}first,":
        xcenter 577 ycenter 330
    $ s_say("first,")
    $ pause(0.4)
    show s_text "{size=32}sarcasm isn't\nfunny." as s1:
        xcenter 632 ycenter 379
    $ s_say("sarcasm isn't funny.")
    $ pause()
    $ s_say2("first, sarcasm isn't funny.")
    hide s1
    show sans_t 1 at TC:
        zoom 1.5 xcenter 317 ycenter 536
        sans_t_move(1.25)
    show sans h at TC:
        zoom 1.5 xcenter 315 ycenter 395
        sans_h_move(1.25)
    show s_text "{size=32}second,":
        xcenter 588 ycenter 330
    $ s_say("second,")
    $ pause(0.4)
    show s_text "{size=32}my brother\nmade this\npoem," as s1:
        xcenter 614 ycenter 397
    $ s_say("my brother made this poem,")
    $ pause(0.4)
    show s_text "{size=32}not me." as s2:
        xcenter 679 ycenter 430
    $ s_say("not me.")
    $ pause()
    $ s_say2("second, my brother made this poem, not me.")
    hide s_text
    hide s1
    hide s2
    hide b
    show layer master at TC:
        TC2
        SP
        zoom 1
        easein_elastic 1 zoom 1.35 xcenter 425 ycenter 390
    show bg class_day at TC2:
        SP
        zoom 2.25 xcenter 250
        easein_elastic 1 zoom 1.95 xcenter 355 ycenter 355
    n 1f "Your brother made this?"
    n "Why aren't you--"
    n 1r "Uuu...!"
    n "Well, you know what?"
    n 5g "You'll get better next time."
    n "I would have cared if you actually made it in the first place."
    play sound fart2
    show layer master at TC:
        SP
        zoom 1.35 xcenter 425 ycenter 390
        ease 0.4 xcenter 825 ycenter 300
    show bg class_day:
        SP
        zoom 1.95 xcenter 355 ycenter 355
        ease 0.4 xcenter 275 ycenter 375
    $ pause(0.65)
    show b m at TC:
        zoom 0.9 xcenter 610 ycenter 420
    show s_text "{size=32}so,":
        xcenter 555 ycenter 330
    $ s_say("so,")
    $ pause(0.4)
    show s_text "{size=32}{space=55}that\nmeans my\nbrother's\npoem is\ngreat," as s1:
        xcenter 599 ycenter 395
    $ s_say("that means my brother's poem is great,")
    $ pause(0.4)
    show s_text "{size=32}right?" as s2:
        xcenter 682 ycenter 463
    $ s_say("right?")
    $ pause()
    $ s_say2("so, that means my brother's poem is great, right?")
    hide s1
    hide s2
    show sans_t 1 at TC:
        zoom 1.5 xcenter 317 ycenter 536
        sans_t_move(1.25)
    show sans j at TC:
        zoom 1.5 xcenter 315 ycenter 395
        sans_h_move(1.25)
    show s_text "{size=32}thanks for\nthe\nappreciation.":
        xcenter 632 ycenter 363
    $ s_say("thanks for the appreciation.")
    $ pause()
    $ s_say2("thanks for the appreciation.")
    show s_text "{size=32}anyways,":
        xcenter 601 ycenter 330
    $ s_say("anyways,")
    $ pause(0.4)
    show s_text "{size=32}{space=140}i'll\nbe standing\nhere doing\nnothing." as s1:
        xcenter 627 ycenter 380
    $ s_say("i'll be standing here doing nothing.")
    $ pause()
    $ s_say2("anyways, i'll be standing here doing nothing.")
    hide s1
    hide s_text
    hide b
    play sound2 dog
    show sans_t 1 at TC:
        zoom 1.5 xcenter 317 ycenter 536
        sans_t_move(1.25)
    show sans a at TC:
        zoom 1.5 xcenter 315 ycenter 395
        sans_h_move(1.25)
    show layer master at TC:
        zoom 1.35 xcenter 425 ycenter 390
    show bg class_day:
        zoom 1.95 xcenter 355 ycenter 355
    $ pause(1.5)
    show natsuki 1f at i11:
        SP
        zoom 1.125 xcenter 900 ycenter 365 yoffset 0
        easein 0.1 yoffset -20
        easeout 0.1 yoffset 0
    n "Wait, what the heck?"
    n "I didn't even say that!"
    show bone at TC behind natsuki:
        SP
        zoom 4 xcenter 1500 ycenter 300 rotate 90
        nearest True
        easein_elastic 0.75 xcenter 1100
    $ pause(0.04)
    play sound punch
    show natsuki 1v at i11:
        SP
        zoom 1.125 xcenter 900 ycenter 365 yoffset 0 rotate 0
        linear 0.2 xcenter 300 ycenter 1100 rotate -120
    show papyrus at TC:
        SP
        zoom 0.25 xcenter 700 ycenter 350 rotate -7.5
        parallel:
            linear 0.75 xcenter 300 rotate -720
        parallel:
            easein_cubic 0.175 ycenter 150
            easeout_cubic 0.525 ycenter 800 
    $ pause(0.35)
    hide natsuki
    show layer master at TC:
        zoom 1.35 xcenter 425 ycenter 390
        layershake(-100, -100, 7.5)
    show bg class_day:
        zoom 1.95 xcenter 355 ycenter 355
        layershake(50, 50, -2.5)
    play sound2 fart5
    $ pause(0.75)
    hide papyrus
    play sound [ "<silence 0.05>" , whoosh3 ]
    show layer master at TC:
        SP
        zoom 1.35 xcenter 425 ycenter 390
        ease_circ 0.35 xcenter 825 ycenter 300
    show bg class_day:
        SP
        zoom 1.95 xcenter 355 ycenter 355
        ease_circ 0.35 xcenter 275 ycenter 375
    $ pause(0.6)
    show b m at TC:
        zoom 0.9 xcenter 610 ycenter 420
    show sans_t 1 at TC:
        zoom 1.5 xcenter 317 ycenter 536
        sans_t_move(1.25)
    show sans b at TC:
        zoom 1.5 xcenter 315 ycenter 395
        sans_h_move(1.25)
    show s_text "{size=32}oh?":
        xcenter 557 ycenter 330
    $ s_say("oh?")
    $ pause(0.4)
    show s_text "{size=32}{space=60}didja say\nsomething?" as s1:
        xcenter 630 ycenter 346
    $ s_say("didja say something?")
    $ pause()
    $ s_say2("oh? didja say something?")
    hide s1
    show s_text "{size=32}gee,":
        xcenter 563 ycenter 330
    $ s_say("gee,")
    $ pause(0.4)
    show s_text "{size=32}{space=75}you\nreally like\nto stick a\nsock on 'em," as s1:
        xcenter 627 ycenter 379
    $ s_say("you really like to stick a sock on 'em,")
    $ pause(0.4)
    show s_text "{size=32}huh?" as s2:
        xcenter 564 ycenter 464
    $ s_say("huh?")
    $ pause()
    $ s_say2("gee, you really like to stick a sock on 'em, huh?")
    hide s1
    hide s2
    show sans_t 1 at TC:
        zoom 1.5 xcenter 317 ycenter 536
        sans_t_move(1.25)
    show sans e at TC:
        zoom 1.5 xcenter 315 ycenter 395
        sans_h_move(1.25)
    show s_text "{size=32}harsh,":
        xcenter 577 ycenter 330
    $ s_say("harsh,")
    $ pause(0.4)
    show s_text "{size=32}{space=105}but\nfair." as s1:
        xcenter 607 ycenter 346
    $ s_say("but fair.")
    $ pause()
    $ s_say2("harsh, but fair.")
    return
    
label ch2_yuri:
    play music pizzicato fadeout 2
    scene bg closet at TC:
        zoom 1.25
    show yuri 1g at i11:
        SP
        zoom 1.125 xcenter 900 ycenter 385 yoffset 0
        block:
            ease_cubic 2.5 yoffset -5
            ease_cubic 2.5 yoffset 0
            repeat
    show sans_l at TC:
        zoom 1.5 xcenter 325 ycenter 690
    show sans_t 1 at TC:
        zoom 1.5 xcenter 317 ycenter 534
        sans_t_move(1.25)
    show sans h at TC:
        zoom 1.5 xcenter 315 ycenter 393
        sans_h_move(1.25)
    show papyrus at TC:
        zoom 0.25 xcenter 700 ycenter 300 rotate -10
    with wiperound_scene
    window auto
    y "..."
    y "......"
    window hide(None)
    show b m at TC:
        zoom 0.9 xcenter 610 ycenter 420
    show s_text "{size=32}so,":
        xcenter 555 ycenter 330
    $ s_say("so,")
    $ pause(0.4)
    show s_text "{size=32}{space=55}whaddya\nthink?" as s1:
        xcenter 620 ycenter 346
    $ s_say("whaddya think?")
    $ pause()
    $ s_say2("so, whaddya think?")
    hide s1
    show s_text "{size=32}is it great\nor not?":
        xcenter 614 ycenter 346
    $ s_say("is it great or not?")
    $ pause()
    $ s_say2("is it great or not?")
    hide b
    hide s_text
    show yuri 3n at i11:
        SP
        zoom 1.125 xcenter 900 ycenter 385
        easein 0.1 yoffset -10
        easeout 0.1 yoffset 0
    y "Oh!"
    y "S-Sorry...!"
    y 3o "I forgot to start speaking..."
    y "U-Um!"
    y 1v "Hold on..."
    y "...Okay."
    y 1e "This is your first time writing a poem, right?"
    show sans_t 1 at TC:
        zoom 1.5 xcenter 317 ycenter 534
        sans_t_move(1.25)
    show sans b at TC:
        zoom 1.5 xcenter 315 ycenter 393
        sans_h_move(1.25)
    show b m at TC:
        zoom 0.9 xcenter 610 ycenter 420
    show s_text "{size=32}nope,":
        xcenter 572 ycenter 330
    $ s_say("nope,")
    $ pause(0.4)
    show s_text "{size=32}{space=86}not\nyet." as s1:
        xcenter 600 ycenter 346
    $ s_say("not yet.")
    $ pause()
    $ s_say2("nope, not yet.")
    show sans_t 1 at TC:
        zoom 1.5 xcenter 317 ycenter 534
        sans_t_move(1.25)
    show sans i at TC:
        zoom 1.5 xcenter 315 ycenter 393
        sans_h_move(1.25)
    hide s1
    show s_text "{size=32}in fact,":
        xcenter 594 ycenter 330
    $ s_say("in fact,")
    $ pause(0.4)
    show s_text "{size=32}{space=130}this\nis my\nbrother's\npoem." as s1:
        xcenter 625 ycenter 379
    $ s_say("this is my brother's poem.")
    $ pause()
    $ s_say2("in fact, this is my brother's poem.")
    hide b
    hide s_text
    hide s1
    show layer master at TC:
        SP
        TC2
        zoom 1
        easein_circ 2 zoom 1.5 xcenter 300 ycenter 500
    show bg closet at TC:
        SP
        TC2
        zoom 1.25
        easein_circ 2 zoom 1.05 xcenter 750 ycenter 330
    y 2f "R-Really?"
    y 2h "Well...umm.."
    y "I'm just making sure..."
    y "...that this one looks quite different."
    y "Your brother's poem actually uses a thin silk of paper."
    y 2i "I can feel the smooth cloth of this, like I was living in Egypt or something."
    show sans_t 1 at TC:
        zoom 1.5 xcenter 317 ycenter 534
        sans_t_move(1.25)
    show sans h at TC:
        zoom 1.5 xcenter 315 ycenter 393
        sans_h_move(1.25)
    show layer master:
        SP
        zoom 1.5 xcenter 300 ycenter 500
        easein_circ 0.5 xcenter 875 ycenter 275
    show bg closet at TC:
        SP
        zoom 1.05 xcenter 750 ycenter 330
        easein_circ 0.5 xcenter 550 ycenter 390
    $ pause(0.75)
    show b m at TC:
        zoom 0.9 xcenter 610 ycenter 420
    show s_text "{size=32}yeah yeah,":
        xcenter 615 ycenter 330
    $ s_say("yeah yeah,")
    $ pause(0.4)
    show s_text "{size=32}pharaohs n'\nstuff..." as s1:
        xcenter 617 ycenter 381
    $ s_say("pharaohs n' stuff...")
    $ pause()
    $ s_say2("yeah yeah, pharaohs n' stuff...")
    hide s1
    show s_text "{size=32}it's perfect,":
        xcenter 631 ycenter 330
    $ s_say("it's perfect,")
    $ pause(0.4)
    show s_text "{size=32}isn't it?" as s1:
        xcenter 599 ycenter 365
    $ s_say("isn't it?")
    $ pause()
    $ s_say2("it's perfect, isn't it?")
    hide s1
    hide s_text
    hide b
    show layer master at TC:
        zoom 1.5 xcenter 300 ycenter 500
    show bg closet at TC:
        zoom 1.05 xcenter 750 ycenter 330
    show sans_t 1 at TC:
        zoom 1.5 xcenter 317 ycenter 534
        sans_t_move2(1.05)
    show sans e at TC:
        zoom 1.5 xcenter 315 ycenter 393
        sans_h_move2(1.05)
    y 1a "Of course, really."
    y 3v "N-Not the poem...! The paper itself!"
    $ currentpos = get_pos() + 2
    $ audio.t6r = "<from " + str(currentpos) + " loop 0.0>mod_assets/caudio/pizzicato.ogg"
    stop music fadeout 2
    $ pause(1.5)
    show vignette onlayer front:
        alpha 0
        easein 4 alpha 0.5
    show layer master:
        SP
        zoom 1.25 xcenter 1050 ycenter 275
        easein 4 zoom 1.4 xcenter 1100
    show bg closet:
        SP
        zoom 1.1 xcenter 450 ycenter 390
        easein 4 zoom 0.9 xcenter 422 ycenter 385
    show dark behind yuri at TC:
        alpha 0 zoom 1.5
        easein 4 alpha 0.66
    $ pause(0.5)
    $ renpy.music.set_volume(0.5)
    play music eq fadein 4
    $ pause(3.75)
    show b m at TC:
        zoom 0.9 xcenter 610 ycenter 420
    show s_text "{size=32}so the poem's\nthat bad,":
        xcenter 634 ycenter 346
    $ s_say("so the poem's that bad,")
    $ pause(0.4)
    show s_text "{size=32}huh?" as s1:
        xcenter 565 ycenter 397
    $ s_say("huh?")
    $ pause()
    $ s_say2("so the poem's that bad, huh?")
    show layer master at TC:
        zoom 1.5 xcenter 300 ycenter 500
    show bg closet at TC:
        zoom 1.05 xcenter 750 ycenter 330
    hide b
    hide s_text
    hide s1
    show yuri 3p at i11:
        SP
        zoom 1.125 xcenter 900 ycenter 385
        easein 0.1 yoffset -10
        easeout 0.1 yoffset 0
    y "No!!"
    y 3o "...Did I just raise my voice...?"
    y 4c "Uu, I'm so sorry..."
    show vignette onlayer front:
        alpha 0.5
        ease_cubic 0.5 alpha 0
    show dark:
        alpha 0.66
        ease_cubic 0.5 alpha 0
    show sans_t 1 at TC:
        zoom 1.5 xcenter 317 ycenter 534
        sans_t_move(1.25)
    show sans h at TC:
        zoom 1.5 xcenter 315 ycenter 393
        sans_h_move(1.25)
    show layer master:
        SP
        zoom 1.5 xcenter 300 ycenter 500
        easein_circ 0.5 xcenter 875 ycenter 275
    show bg closet at TC:
        SP
        zoom 1.05 xcenter 750 ycenter 330
        easein_circ 0.5 xcenter 550 ycenter 390
    stop music fadeout 0.75
    $ pause(0.75)
    $ renpy.music.set_volume(1)
    play music t6r fadein 2
    hide dark
    hide vignette onlayer front
    show b m at TC:
        zoom 0.9 xcenter 610 ycenter 420
    show s_text "{size=32}it's fine,":
        xcenter 605 ycenter 330
    $ s_say("it's fine,")
    $ pause(0.4)
    show s_text "{size=32}buddy." as s1:
        xcenter 580 ycenter 365
    $ s_say("buddy.")
    $ pause()
    $ s_say2("it's fine, buddy.")
    hide s1
    show s_text "{size=32}i don't\nactually care\nabout poetry.":
        xcenter 635 ycenter 363
    $ s_say("i don't actually care about poetry.")
    $ pause()
    $ s_say2("i don't actually care about poetry.")
    show sans_t 1 at TC:
        zoom 1.5 xcenter 317 ycenter 534
        sans_t_move(1.25)
    show sans b at TC:
        zoom 1.5 xcenter 315 ycenter 393
        sans_h_move(1.25)
    show s_text "{size=32}it's just\nwasting my\nlifetime.":
        xcenter 613 ycenter 363
    $ s_say("it's just wasting my lifetime.")
    $ pause()
    $ s_say2("it's just wasting my lifetime.")
    show sans_t 1 at TC:
        zoom 1.5 xcenter 317 ycenter 534
        sans_t_move(1.25)
    show sans h at TC:
        zoom 1.5 xcenter 315 ycenter 393
        sans_h_move(1.25)
    show s_text "{size=32}so,":
        xcenter 554 ycenter 330
    $ s_say("so,")
    $ pause(0.4)
    show s_text "{size=32}{space=50}what were\nyou saying?" as s1:
        xcenter 632 ycenter 346
    $ s_say("what were you saying?")
    $ pause()
    $ s_say2("so, what were you saying?")
    hide s1
    hide s_text
    hide b
    show layer master at TC:
        zoom 1.5 xcenter 300 ycenter 500
    show bg closet at TC:
        zoom 1.05 xcenter 750 ycenter 330
    show sans_t 1 at TC:
        zoom 1.5 xcenter 317 ycenter 534
        sans_t_move2(1.05)
    show sans e at TC:
        zoom 1.5 xcenter 315 ycenter 393
        sans_h_move2(1.05)
    y 2q "Right...um..."
    y 1a "It's just that there are specific writing habits that are usually typical of new writers."
    y "And having been through that myself, I kind of learned to pick up on them."
    y 1i "I think the most noticeable thing I recognize in new writers is that they try to make their style very deliberate."
    y "In this case, perhaps the subject of your brother's poem is somehow being symbolically compared to a..."
    y 2v "...A person who enjoys cooking his beloved pasta...?"
    y 1a "But next time, you still have the power to express the way it feels for you to indulge in your hobbies..."
    y "Try to use imagery or metaphors that indicates you've written a lot of poetry before."
    y "I'm looking foward to your future careers."
    play sound ding
    show layer master:
        zoom 1.5 xcenter 875 ycenter 275
    show bg closet at TC:
        zoom 1.05 xcenter 550 ycenter 390
    show zzz at TC behind yuri:
        SP
        zoom 1.75 xcenter 335 ycenter 400
        0.7
        parallel:
            block:
                zzz_move(1.75)
                time 2
                xoffset 0 yoffset 0 zoom 1.75
                0.66
            repeat
        parallel:
            easeout_circ 2 ycenter 100 alpha 0
            ycenter 400
            0.66
            alpha 1
            repeat
        parallel:
            linear 2 xcenter 750
            xcenter 335
            0.66
            repeat
    show zzz at TC behind yuri as z1:
        SP
        zoom 1.75 xcenter 335 ycenter 400
        0.35
        parallel:
            block:
                zzz_move(1.75)
                time 2
                xoffset 0 yoffset 0 zoom 1.75
                0.66
            repeat
        parallel:
            easeout_circ 2 ycenter 100 alpha 0
            ycenter 400
            0.66
            alpha 1
            repeat
        parallel:
            linear 2 xcenter 750
            xcenter 335
            0.66
            repeat
    show zzz at TC behind yuri as z2:
        SP
        zoom 1.75 xcenter 335 ycenter 400
        parallel:
            block:
                zzz_move(1.75)
                time 2
                xoffset 0 yoffset 0 zoom 1.75
                0.66
            repeat
        parallel:
            easeout_circ 2 ycenter 100 alpha 0
            ycenter 400
            0.66
            alpha 1
            repeat
        parallel:
            linear 2 xcenter 750
            xcenter 335
            0.66
            repeat
    $ pause(1.75)
    show yuri 3o at i11:
        SP
        zoom 1.125 xcenter 900 ycenter 385
        easein 0.1 yoffset -15
        easeout 0.1 yoffset 0
    y "Ah--"
    y "S-Sans...?"
    y "A-Are you--"
    stop music fadeout 2
    show layer master:
        SP
        zoom 1.5 xcenter 875 ycenter 275
        ease_cubic 1.5 xcenter 300 ycenter 500
    show bg closet at TC:
        SP
        zoom 1.05 xcenter 550 ycenter 390
        ease_cubic 1.5 xcenter 750 ycenter 330
    y "..."
    y "(He said that he doesn't care about poetry...)"
    y 4c "(Then why am I saying all of this when he ignores me...?)"
    if not (n_readpoem and s_readpoem):
        play music sotl fadein 2
    return

label ch2_sayori:
    scene bg club_day at TC:
        zoom 1.5 ycenter 390
    show sayori 3b at i11:
        zoom 1.1 xcenter 855 ycenter 395
    show papyrus at TC:
        zoom 0.25 xcenter 665 ycenter 375 rotate -12
    show sans_l at TC:
        zoom 1.4 xcenter 350 ycenter 690
    show sans_t 1 at TC:
        zoom 1.4 xcenter 344 ycenter 545
        sans_t_move(1.2)
    show sans h at TC:
        zoom 1.4 xcenter 343 ycenter 415
        sans_h_move(1.2)
    with wiperound_scene
    window auto 
    s "..."
    s "...Wow!"
    s "Sans..."
    s 4r "Your poem-- I mean, your brother's poem is really bad!"
    s "Ahahaha!"
    window hide(None)
    show b l at TC:
        zoom 0.45 xcenter 625 ycenter 420
    show s_text "{size=32}what.":
        xcenter 580 ycenter 330
    $ s_say("what.")
    $ pause()
    $ s_say2("what.")
    hide b
    hide s_text
    s 3x "It's fine, it's fine~"
    s "It's his first time."
    s "Besides..."
    s 3q "I'm obliged just that he wrote one."
    s "It just reminds me of how you're really a part of the club now~"
    show layer master:
        zoom 1.5 xcenter 900 ycenter 250
    show bg club_day at TC:
        zoom 1.25 xcenter 525 ycenter 410
    show b l at TC:
        zoom 0.45 xcenter 625 ycenter 420
    show sans_t 1 at TC:
        zoom 1.4 xcenter 344 ycenter 545
        sans_t_move(1.2)
    show sans i at TC:
        zoom 1.4 xcenter 343 ycenter 415
        sans_h_move(1.2)
    show s_text "{size=32}not to\nmention the\nfact that...":
        xcenter 635 ycenter 363
    $ s_say("not to mention the fact that...")
    $ pause()
    $ s_say2("not to mention the fact that...")
    show s_text "{size=32}i was\nsleeping in\nthe middle of\nthe club...?":
        xcenter 640 ycenter 379
    $ s_say("i was sleeping in the middle of the club...?")
    $ pause()
    $ s_say2("i was sleeping in the middle of the club...?")
    hide b
    hide s_text
    show layer master:
        zoom 1.5 xcenter 400 ycenter 450
    show bg club_day at TC:
        zoom 1.25 xcenter 700 ycenter 370
    s 3a2 "Yep~"
    show sayori 3n at i11:
        SP
        zoom 1.1 xcenter 855 ycenter 395 yoffset 0
        easein 0.1 yoffset -15
        easeout 0.1 yoffset 0
    show papyrus at TC:
        SP
        zoom 0.25 xcenter 665 ycenter 375 rotate -12 yoffset 0
        easein 0.1 yoffset -15
        easeout 0.1 yoffset 0
    s "N-No!"
    s 3o "Umm... maybe..."
    show layer master:
        zoom 1.5 xcenter 900 ycenter 250
    show bg club_day at TC:
        zoom 1.25 xcenter 525 ycenter 410
    show b l at TC:
        zoom 0.45 xcenter 625 ycenter 420
    show sans_t 1 at TC:
        zoom 1.4 xcenter 344 ycenter 545
        sans_t_move(1.2)
    show sans b at TC:
        zoom 1.4 xcenter 343 ycenter 415
        sans_h_move(1.2)
    show s_text "{size=32}that's weird.":
        xcenter 640 ycenter 330
    $ s_say("that's weird.")
    $ pause()
    $ s_say2("that's weird.")
    show s_text "{size=32}a poem of\nspaghetti\nreminds you\nof my motives.":
        xcenter 653 ycenter 378
    $ s_say("a poem of spaghetti reminds you of my motives")
    $ pause()
    $ s_say2("a poem of spaghetti reminds you of my motives.")
    show sans_t 1 at TC:
        zoom 1.4 xcenter 344 ycenter 545
        sans_t_move(1.2)
    show sans i at TC:
        zoom 1.4 xcenter 343 ycenter 415
        sans_h_move(1.2)
    show s_text "{size=32}what kind of\nperson are\nyou?":
        xcenter 635 ycenter 363
    $ s_say("what kind of person are you?")
    $ pause()
    $ s_say2("what kind of person are you?")
    hide b
    hide s_text
    show layer master:
        zoom 1.5 xcenter 400 ycenter 450
    show bg club_day at TC:
        zoom 1.25 xcenter 700 ycenter 370
    show sayori 5a2 at i11:
        SP
        zoom 1.1 xcenter 855 ycenter 395 yoffset 0
        easein 0.75 yoffset 10
    show papyrus at TC:
        SP
        zoom 0.25 xcenter 665 ycenter 375 rotate -12 yoffset 0
        easein 0.75 yoffset 10
    s "Ehehe... don't make me feel embarrassed."
    s "Sometimes, my mind becomes nothing but an empty space, you know?"
    show sayori 3d at i11:
        SP
        zoom 1.1 xcenter 855 ycenter 395 yoffset 10
        ease 0.25 yoffset 0
    show papyrus at TC:
        SP
        zoom 0.25 xcenter 665 ycenter 375 rotate -12 yoffset 10
        ease 0.25 yoffset 0
    s "After all, you're not selfish at everything, are you?"
    s "As much as you learn new things like this, you'll soon be better than your brother!"
    show layer master:
        zoom 1.5 xcenter 900 ycenter 250
    show bg club_day at TC:
        zoom 1.25 xcenter 525 ycenter 410
    show b l at TC:
        zoom 0.45 xcenter 625 ycenter 420
    show sans_t 1 at TC:
        zoom 1.4 xcenter 344 ycenter 545
        sans_t_move(1.2)
    show sans h at TC:
        zoom 1.4 xcenter 343 ycenter 415
        sans_h_move(1.2)
    show s_text "{size=32}okay okay,":
        xcenter 622 ycenter 330
    $ s_say("okay okay,")
    $ pause(0.4)
    show s_text "{size=32}i trusted\nyour opinion." as s1:
        xcenter 640 ycenter 380
    $ s_say("i trusted your opinion.")
    $ pause()
    $ s_say2("okay okay, i trusted your opinion.")
    hide s1
    show s_text "{size=32}i will just\nwrite one\nduring the\nclub.":
        xcenter 617 ycenter 379
    $ s_say("i will just write one during the club.")
    $ pause()
    $ s_say2("i will just write one during the club.")
    show sans_t 1 at TC:
        zoom 1.4 xcenter 344 ycenter 545
        sans_t_move(1.2)
    show sans i at TC:
        zoom 1.4 xcenter 343 ycenter 415
        sans_h_move(1.2)
    show s_text "{size=32}then,":
        xcenter 578 ycenter 330
    $ s_say("then,")
    $ pause(0.4)
    show s_text "{size=32}{space=90}i can\nspend my\nwhole day in\ngrillby's." as s1:
        xcenter 635 ycenter 379
    $ s_say("i can spend my whole day in grillby's.")
    $ pause()
    $ s_say2("then, i can spend my whole day in grillby's.")
    hide b
    hide s_text
    hide s1
    show layer master:
        zoom 1.5 xcenter 400 ycenter 450
    show bg club_day at TC:
        zoom 1.25 xcenter 700 ycenter 370
    show sayori 4h at i11:
        SP
        zoom 1.1 xcenter 855 ycenter 395 yoffset 0
        easein 0.1 yoffset -15
        easeout 0.1 yoffset 0
    show papyrus at TC:
        SP
        zoom 0.25 xcenter 665 ycenter 375 rotate -12 yoffset 0
        easein 0.1 yoffset -15
        easeout 0.1 yoffset 0
    s "Aww, c'monnn...!"
    show layer master:
        zoom 1.5 xcenter 900 ycenter 250
    show bg club_day at TC:
        zoom 1.25 xcenter 525 ycenter 410
    show b l at TC:
        zoom 0.45 xcenter 625 ycenter 420
    show sans_t 1 at TC:
        zoom 1.4 xcenter 344 ycenter 545
        sans_t_move(1.2)
    show sans h at TC:
        zoom 1.4 xcenter 343 ycenter 415
        sans_h_move(1.2)
    show s_text "{size=32}just kidding.":
        xcenter 638 ycenter 330
    $ s_say("just kidding.")
    $ pause(0.4)
    show s_text "{size=32}i'm rootin\nfor ya," as s1:
        xcenter 615 ycenter 382
    $ s_say("i'm rootin for ya,")
    $ pause(0.4)
    show s_text "{size=32}kid." as s2:
        xcenter 695 ycenter 399
    $ s_say("kid.")
    $ pause()
    $ s_say2("just kidding. i'm rootin for ya, kid.")
    hide b
    hide s_text
    hide s1
    hide s2
    show layer master:
        zoom 1.5 xcenter 400 ycenter 450
    show bg club_day at TC:
        zoom 1.25 xcenter 700 ycenter 370
    s 4y "Meanie..."
    s 4k "But Sans, everything you do isn't the same as you always have been."
    show layer master:
        zoom 1.5 xcenter 400 ycenter 450
        layershake2(20, -40, 1)
    show bg club_day at TC:
        zoom 1.25 xcenter 700 ycenter 370
        layershake2(-10, 20, 1)
    show speedline at SL onlayer front:
        alpha 1
        linear 0.75 alpha 0
    s 3h "It doesn't have to be that way!"
    hide speedline onlayer front
    s "It's like you're not putting any heart into this at all!"
    show layer master:
        zoom 1.5 xcenter 900 ycenter 250
    show bg club_day at TC:
        zoom 1.25 xcenter 525 ycenter 410
    show b l at TC:
        zoom 0.45 xcenter 625 ycenter 420
    show sans_t 1 at TC:
        zoom 1.4 xcenter 344 ycenter 545
        sans_t_move(1.2)
    show sans j at TC:
        zoom 1.4 xcenter 343 ycenter 415
        sans_h_move(1.2)
    show s_text "{size=32}i know,":
        xcenter 593 ycenter 330
    $ s_say("i know,")
    $ pause(0.4)
    show s_text "{size=32}because my\nheart doesn't\nexist." as s1:
        xcenter 640 ycenter 395
    $ s_say("because my heart doesn't exist.")
    $ pause()
    $ s_say2("i know, because my heart doesn't exist.")
    hide b
    hide s_text
    hide s1
    show sayori 3b
    show bg club_day at TC:
        zoom 1.5 ycenter 390
    show layer master
    play audio ut_rimshot
    $ pause(2)
    $ currentpos = get_pos() + 2
    $ audio.t6r = "<from " + str(currentpos) + " loop 0.0>mod_assets/caudio/sotl.ogg"
    stop music fadeout 2
    window auto
    s 3c "What?"
    s "I don't understand..."
    window hide(None)
    show sans_t 1 at TC:
        zoom 1.4 xcenter 344 ycenter 545
        sans_t_move(1.2)
    show sans i at TC:
        zoom 1.4 xcenter 343 ycenter 415
        sans_h_move(1.2)
    show layer master:
        zoom 1.5 xcenter 900 ycenter 250
    show bg club_day at TC:
        zoom 1.25 xcenter 525 ycenter 410
    show b l at TC:
        zoom 0.45 xcenter 625 ycenter 420
    show s_text "{size=32}think twice,":
        xcenter 632 ycenter 330
    $ s_say("think twice,")
    $ pause(0.4)
    show s_text "{size=32}and you'll\nget it." as s1:
        xcenter 615 ycenter 380
    $ s_say("and you'll get it.")
    $ pause()
    $ s_say2("think twice, and you'll get it.")
    $ quick_menu = False
    hide b
    hide s_text
    hide s1
    show sayori 4o
    show sans_t 1 at TC:
        zoom 1.4 xcenter 344 ycenter 545
        sans_t_move2()
    show sans h at TC:
        zoom 1.4 xcenter 343 ycenter 415
        sans_h_move2()
    show layer master:
        zoom 1.5 xcenter 400 ycenter 450
    show bg club_day at TC:
        zoom 1.25 xcenter 700 ycenter 370
    show splash_warning4_5 "{size=40}SAYORI PROCESSING MODE" onlayer front at sub:
        block:
            alpha 0
            0.5
            alpha 1
            0.5
            repeat
    play sound dialup
    $ pause(4)
    show layer master:
        zoom 1.5 xcenter 900 ycenter 250
    show bg club_day at TC:
        zoom 1.25 xcenter 525 ycenter 410
    $ pause(6)
    show layer master:
        zoom 1.5 xcenter 400 ycenter 450
    show bg club_day at TC:
        zoom 1.25 xcenter 700 ycenter 370
    $ pause(2)
    stop sound
    hide splash_warning4_5 onlayer front
    show sayori 4x at i11:
        SP
        zoom 1.1 xcenter 855 ycenter 395 yoffset 0
        easein 0.1 yoffset -15
        easeout 0.1 yoffset 0
    show papyrus at TC:
        SP
        zoom 0.25 xcenter 665 ycenter 375 rotate -12 yoffset 0
        easein 0.1 yoffset -15
        easeout 0.1 yoffset 0
    $ quick_menu = True
    s "Oh! Oh! I get it~!"
    s "Your heart lives right inside your head!"
    show layer master:
        zoom 1.5 xcenter 900 ycenter 250
    show bg club_day at TC:
        zoom 1.25 xcenter 525 ycenter 410
    show b l at TC:
        zoom 0.45 xcenter 625 ycenter 420
    show s_text "{size=32}...":
        xcenter 561 ycenter 330
    $ s_say("...")
    $ pause()
    $ s_say2("...")
    show sans_t 1 at TC:
        zoom 1.4 xcenter 344 ycenter 545
        sans_t_move2()
    show sans b at TC:
        zoom 1.4 xcenter 343 ycenter 415
        sans_h_move2()
    show s_text "{size=32}(dumber than\ndirt,":
        xcenter 633 ycenter 346
    $ s_say("(dumber than dirt,")
    $ pause(0.4)
    show s_text "{size=32}ain'tcha?)" as s1:
        xcenter 615 ycenter 398
    $ s_say("ain'tcha?)")
    $ pause()
    $ s_say2("(dumber than dirt, ain'tcha?)")
    hide s1
    show sans_t 1 at TC:
        zoom 1.4 xcenter 344 ycenter 545
        sans_t_move2()
    show sans h at TC:
        zoom 1.4 xcenter 343 ycenter 415
        sans_h_move2()
    show s_text "{size=32}hey,":
        xcenter 571 ycenter 330
    $ s_say("hey,")
    $ pause(0.4)
    show s_text "{size=32}buddy." as s1:
        xcenter 662 ycenter 330
    $ s_say("buddy.")
    $ pause()
    $ s_say2("hey, buddy.")
    hide s1
    show s_text "{size=32}pick any\nnumber\nbetween 1 to\n10.":
        xcenter 636 ycenter 379
    $ s_say("pick any number between 1 to 10.")
    $ pause()
    $ s_say2("pick any number between 1 to 10.")
    show layer master:
        zoom 1.5 xcenter 400 ycenter 450
    show bg club_day at TC:
        zoom 1.25 xcenter 700 ycenter 370
    hide b
    hide s_text
    $ S_RNG = renpy.random.randint(1, 10)
    s 3a2 "Oh, okay."
    s "[S_RNG]"
    show layer master:
        zoom 1.5 xcenter 900 ycenter 250
    show bg club_day at TC:
        zoom 1.25 xcenter 525 ycenter 410
    show sans_t 2 at TC:
        zoom 1.4 xcenter 344 ycenter 545
        sans_t_move(1.2)
    show sans j at TC:
        zoom 1.4 xcenter 343 ycenter 415
        sans_h_move(1.2)
    show b l at TC behind sans_t:
        zoom 0.45 xcenter 625 ycenter 420
    show s_text "{size=32}that is your\niq.":
        xcenter 633 ycenter 346
    show sans_shockwave at TC behind sans_l:
        SP
        zoom 0.15 xcenter 345 ycenter 500
        easein 0.75 zoom 2 alpha 0 
    show sans_shockwave at TC behind sans_l as ss1:
        SP
        zoom 0.15 xcenter 345 ycenter 500 alpha 0.25
        easein 0.75 zoom 1 alpha 0 
    play audio ut_ding
    $ s_say("that is your iq.")
    $ pause()
    $ s_say2("that is your iq.")
    hide b
    hide s_text
    hide sans_shockwave
    hide ss1
    play sound crit
    show layer master:
        zoom 1.5 xcenter 400 ycenter 450
    show bg club_day at TC:
        zoom 1.25 xcenter 700 ycenter 370
    show sayori 4n at i11:
        SP
        zoom 1.1 xcenter 855 ycenter 395 yoffset 0
        easein 0.1 yoffset -15
        easeout 0.1 yoffset 0
    show papyrus at TC:
        SP
        zoom 0.25 xcenter 665 ycenter 375 rotate -12 yoffset 0
        easein 0.1 yoffset -15
        easeout 0.1 yoffset 0
    show smack at TC:
        zoom 0.75 xcenter 725 ycenter 150
    $ pause(1.5)
    hide smack
    show layer master:
        zoom 1.5 xcenter 900 ycenter 250
    show bg club_day at TC:
        zoom 1.25 xcenter 525 ycenter 410
    show sans_t 1 at TC:
        zoom 1.4 xcenter 344 ycenter 545
        sans_t_move(1.2)
    show sans b at TC:
        zoom 1.4 xcenter 343 ycenter 415
        sans_h_move(1.2)
    show b l at TC behind sans_t:
        zoom 0.45 xcenter 625 ycenter 420
    show s_text "{size=32}guess i'll be\noff,":
        xcenter 632 ycenter 346
    $ s_say("guess i'll be off,")
    $ pause(0.4)
    show s_text "{size=32}then." as s1:
        xcenter 655 ycenter 363
    $ s_say("then.")
    $ pause()
    $ s_say2("guess i'll be off, then.")
    hide s1
    show sans_t 1 at TC:
        zoom 1.4 xcenter 344 ycenter 545
        sans_t_move(1.2)
    show sans d at TC:
        zoom 1.4 xcenter 343 ycenter 415
        sans_h_move(1.2)
    show s_text "{size=32}thanks for\nsharing.":
        xcenter 619 ycenter 346
    $ s_say("thanks for sharing.")
    $ pause()
    $ s_say2("thanks for sharing.")
    show black onlayer front
    hide papyrus
    hide sans
    hide sans_t
    hide sans_l
    hide b
    hide s_text
    play sound ut_snap
    $ pause(0.25)
    hide black onlayer front
    play sound ut_snap
    $ pause(1.5)
    if not (n_readpoem and y_readpoem):
        play music t6r fadein 2
    return

label ch2_poemend:
    if not renpy.music.get_playing(channel='music') == None:
        play music workaday fadeout 2
    scene bg club_day:
        zoom 1.75 xcenter 1000 ycenter 400
    show sans_l at TC:
        zoom 1.5 xcenter 640 ycenter 690
    show sans_t 1 at TC:
        zoom 1.5 xcenter 633 ycenter 532
        sans_t_move2()
    show sans e at TC:
        zoom 1.5 xcenter 630 ycenter 392
        sans_h_move2()
    with wiperound_scene
    if renpy.music.get_playing(channel='music') == None:
        play music workaday fadein 2
    $ pause(0.25)
    show b l at TC behind sans_t:
        zoom 0.5 xzoom -1 xcenter 325 ycenter 400
    show s_text "{size=32}done and done.":
        xcenter 300 ycenter 300
    $ s_say("done and done.")
    $ pause()
    $ s_say2("done and done.")
    show sans_t 1 at TC:
        zoom 1.5 xcenter 633 ycenter 532
        sans_t_move2()
    show sans b at TC:
        zoom 1.5 xcenter 630 ycenter 392
        sans_h_move2()
    show s_text "{size=32}hell,":
        xcenter 222 ycenter 300
    $ s_say("hell,")
    $ pause(0.4)
    show s_text "{size=32}{space=80}that was\neasy." as s1:
        xcenter 293 ycenter 315
    $ s_say("that was easy.")
    $ pause()
    $ s_say2("hell, that was easy.")
    hide s1
    show s_text "{size=32}i should've\nought to give\n'em a great\nfeedback.":
        xcenter 289 ycenter 349
    $ s_say("i should've ought to give 'em a great feedback.")
    $ pause()
    $ s_say2("i should've ought to give 'em a great feedback.")
    show s_text "{size=32}and...":
        xcenter 235 ycenter 300
    $ s_say("and...")
    $ pause()
    $ s_say2("and...")
    show sans_t 1 at TC:
        zoom 1.5 xcenter 633 ycenter 532
        sans_t_move2()
    show sans e at TC:
        zoom 1.5 xcenter 630 ycenter 392
        sans_h_move2()
    show s_text "{size=32}i knew it;":
        xcenter 263 ycenter 300
    $ s_say("i knew it;")
    $ pause(0.4)
    show s_text "{size=32}despite that\nthey're acting\nnice..." as s1:
        xcenter 299 ycenter 367
    $ s_say("despite that\nthey're acting\nnice...")
    $ pause()
    $ s_say2("i knew it; despite that they're acting nice...")
    hide s1
    show s_text "{size=32}my brother's\npoem can't\nstand up to\ntheirs.":
        xcenter 284 ycenter 349
    $ s_say("my brother's poem can't stand up to theirs.")
    $ pause()
    $ s_say2("my brother's poem can't stand up to theirs.")
    show sans_t 1 at TC:
        zoom 1.5 xcenter 633 ycenter 532
        sans_t_move2()
    show sans a at TC:
        zoom 1.5 xcenter 630 ycenter 392
        sans_h_move2()
    show s_text "{size=32}eh,":
        xcenter 211 ycenter 300
    $ s_say("eh,")
    $ pause(0.4)
    show s_text "{size=32}{space=60}i don't\ncare." as s1:
        xcenter 270 ycenter 316
    $ s_say("i don't care.")
    $ pause()
    $ s_say2("eh, i don't care.")
    hide s1
    show s_text "{size=32}...?":
        xcenter 220 ycenter 300
    $ s_say("...?")
    $ pause()
    $ s_say2("...?")
    hide b
    hide s_text
    show layer master at TC2:
        SP
        ease_cubic 1 xcenter -600
    show bg club_day:
        SP
        zoom 1.75 xcenter 1000 ycenter 400
        ease_cubic 1 xcenter 1550
    show yuri 2i at i11:
        zoom 1.15 xcenter 1625 ycenter 400
    show natsuki 1q at i11:
        zoom 1.15 xcenter 2150 ycenter 400
    show splash_warning4_5 "*Sharing poems*" at SP:
        xcenter 1900 ycenter 50 rotate 2.5
        block:
            ease 1 rotate -2.5
            ease 1 rotate 2.5
            repeat
    $ pause(1)
    window auto
    n "{i}(What's with this language...?){/i}"
    window hide(None)
    scene bg club_day:
        zoom 1.75 xcenter 310 ycenter 400
    show yuri 2f at i11:
        zoom 1.15 xcenter 384 ycenter 400
    show natsuki 1q at i11:
        zoom 1.15 xcenter 910 ycenter 400
    y "Eh?"
    y "Um...did you say something?"
    n 2c "Oh, it's nothing."
    n "I guess you could say it's fancy."
    y 2i "Ah-- Thanks..."
    y "Yours is...cute..."
    show layer master at TC:
        SP
        zoom 1 xcenter 640 ycenter 360
        easein_elastic 1.25 zoom 1.5 xcenter 300 ycenter 380
    show bg club_day:
        SP
        zoom 1.75 xcenter 310 ycenter 400
        easein_elastic 1.25 zoom 1.5 xcenter 430 ycenter 380
    n 2h "Cute?"
    n 1h "Did you completely miss the symbolism or something?"
    n "It's clearly about the feeling of giving up."
    n "How can that be cute?"
    show yuri 3f
    show layer master:
        SP
        zoom 1.5 xcenter 300 ycenter 380
        ease_cubic 0.5 xcenter 1050 ycenter 500
    show bg club_day:
        SP
        zoom 1.5 xcenter 430 ycenter 380
        ease_cubic 0.5 xcenter 310 ycenter 350
    $ pause(0.6)
    y "I-I know that!"
    y "I just meant..."
    y 3h "The language, I guess..."
    y "I was trying to say something nice..."
    show layer master:
        SP
        zoom 1.5 xcenter 1050 ycenter 500
        ease_cubic 0.5 xcenter 300 ycenter 380
    show bg club_day:
        SP
        zoom 1.5 xcenter 310 ycenter 350
        ease_cubic 0.5 xcenter 430 ycenter 380
    $ pause(0.6)
    n "Eh?"
    n 4w "You mean you have to try that hard to come up with something nice to say?"
    n "Thanks, but it really didn't come out nice at all!"
    show layer master:
        zoom 1.5 xcenter 1400 ycenter 340
    show bg club_day:
        zoom 1.5 xcenter 200 ycenter 390
    $ pause(0.1)
#    show sans_l at TC:
#        zoom 1.5 xcenter 0 ycenter 690
    show sans_t 1 at TC:
        SP
        zoom 1.5 xcenter -500 ycenter 532
        parallel:
            sans_t_move(1.2)
        parallel:
            easein_cubic 0.75 xcenter -7
    show sans a at TC:
        SP
        zoom 1.5 xcenter -503 ycenter 392
        parallel:
            sans_h_move(1.2)
        parallel:
            easein_cubic 0.75 xcenter -10
    $ pause(0.8)
    show b l at TC:
        zoom 0.5 xcenter 300 ycenter 400
    show s_text "{size=32}hey,":
        xcenter 235 ycenter 300
    $ s_say("hey,")
    $ pause(0.4)
    show s_text "{size=32}{space=77}what's\ngoing on here?" as s1:
        xcenter 315 ycenter 316
    $ s_say("what's going on here?")
    $ pause()
    $ s_say2("hey, what's going on here?")
    hide b
    hide s_text
    hide s1
    show sans_t 1 at TC:
        zoom 1.5 xcenter -7 ycenter 532
        sans_t_move(1.2)
    show sans h at TC:
        zoom 1.5 xcenter -10 ycenter 392
        sans_h_move(1.2)
    show layer master:
        zoom 1.5 xcenter 300 ycenter 380
        layershake(-20, -20, 2.5)
    show bg club_day:
        zoom 1.5 xcenter 430 ycenter 380
        layershake(5, 5, -1.25)
    n 4e "Sans!"
    n "Yuri is giving me a really disgraceful feedback."
    show yuri 3n
    show layer master:
        SP
        zoom 1.5 xcenter 300 ycenter 380
        ease_cubic 0.5 xcenter 1050 ycenter 500
    show bg club_day:
        SP
        zoom 1.5 xcenter 430 ycenter 380
        ease_cubic 0.5 xcenter 310 ycenter 350
    $ pause(0.5)
    y 3n "No, I didn't!"
    y "I was just--!"
    show natsuki 4h
    show layer master:
        SP
        zoom 1.5 xcenter 1050 ycenter 500
        ease_cubic 0.5 xcenter 300 ycenter 380
    show bg club_day:
        SP
        zoom 1.5 xcenter 310 ycenter 350
        ease_cubic 0.5 xcenter 430 ycenter 380
    $ pause(0.6)
    n "She misunderstands that my poem is cute like it's not a part of its language!"
    n 4w "This makes my poem utterly convoluted for no reason!"
    show yuri 1o
    show layer master:
        zoom 1.5 xcenter 1400 ycenter 340
    show bg club_day:
        zoom 1.5 xcenter 200 ycenter 390
    show sans_t 1 at TC:
        zoom 1.5 xcenter -7 ycenter 532
        sans_t_move(1.2)
    show sans a at TC:
        zoom 1.5 xcenter -10 ycenter 392
        sans_h_move(1.2)
    show b l at TC:
        zoom 0.5 xcenter 300 ycenter 400
    show s_text "{size=32}...":
        xcenter 225 ycenter 300
    $ s_say("...")
    $ pause()
    $ s_say2("...")
    show sans_t 1 at TC:
        zoom 1.5 xcenter -7 ycenter 532
        sans_t_move(1.2)
    show sans k at TC:
        zoom 1.5 xcenter -10 ycenter 392
        sans_h_move(1.2)
    show s_text "{size=32}cool.":
        xcenter 241 ycenter 300
    $ s_say("cool.")
    $ pause()
    $ s_say2("cool.")
    hide b
    hide s_text
    show layer master:
        zoom 1.5 xcenter 300 ycenter 380
        layershake2(30, -30)
    show bg club_day:
        zoom 1.5 xcenter 430 ycenter 380
        layershake2(-10, 10)
    show sans_t 1 at TC:
        zoom 1.5 xcenter -7 ycenter 532
        sans_t_move(1.2)
    show sans h at TC:
        zoom 1.5 xcenter -10 ycenter 392
        sans_h_move(1.2)
    show yuri 1t
    n 1o "Hey--!"
    n "It's not cool!"
    n "It's really a--"
    show layer master:
        SP
        zoom 1.5 xcenter 300 ycenter 380
        ease_cubic 0.5 xcenter 1050 ycenter 500
    show bg club_day:
        SP
        zoom 1.5 xcenter 430 ycenter 380
        ease_cubic 0.5 xcenter 310 ycenter 350
    $ pause(0.6)
    y "W-Wait!"
    y "I do have a couple sugesstions..."
    show layer master:
        SP
        zoom 1.5 xcenter 1050 ycenter 500
        ease_cubic 0.5 xcenter 300 ycenter 380
    show bg club_day:
        SP
        zoom 1.5 xcenter 310 ycenter 350
        ease_cubic 0.5 xcenter 430 ycenter 380
    $ pause(0.5)
    n 5x "Oh really? You do have suggesstions?"
    n "If I was looking for suggestions, I would have asked someone who actually liked it."
    n "Which people {i}did{/i}, by the way."
    n 5e "Sayori liked it."
    n "And Sans did, too!"
    n "So based on that, I'll gladly give you some suggestions of my own."
    n "First of all--"
    show layer master:
        zoom 1.5 xcenter 1050 ycenter 500
    show bg club_day:
        zoom 1.5 xcenter 310 ycenter 350

    y 2l "Excuse me..."
    y "I appreciate the offer, but I've spent a long time establishing my writing style."
    y 2f "I don't expect it to change anytime soon, unless of course I come across something particularly inspiring."
    y "Which I haven't yet."
    show layer master:
        SP
        zoom 1.5 xcenter 300 ycenter 380
        ease 2 zoom 1.75 xcenter 200 ycenter 420
    show bg club_day:
        SP
        zoom 1.5 xcenter 430 ycenter 380
        ease 2 zoom 1.375 xcenter 475 ycenter 365
    show sans_t 1 at TC:
        zoom 1.5 xcenter -7 ycenter 532
        sans_t_move(1.2)
    show sans i at TC:
        zoom 1.5 xcenter -10 ycenter 392
        sans_h_move(1.2)

    n 1o "Nn...!"
    show layer master:
        zoom 1.5 xcenter 1050 ycenter 500
    show bg club_day:
        zoom 1.5 xcenter 310 ycenter 350
    y 1i "And Sans liked my poem too, you know."
    y "He even told me he was impressed by it."
    show layer master:
        zoom 1.5 xcenter 1400 ycenter 340
    show bg club_day:
        zoom 1.5 xcenter 200 ycenter 390
    show sans_t 1 at TC:
        zoom 1.5 xcenter -7 ycenter 532
        sans_t_move(1.2)
    show sans h at TC:
        zoom 1.5 xcenter -10 ycenter 392
        sans_h_move(1.2)
    show b l at TC:
        zoom 0.5 xcenter 300 ycenter 400
    show s_text "{size=32}did i say\nthat before...?":
        xcenter 325 ycenter 316
    $ s_say("did i say that before...?")
    $ pause()
    $ s_say2("did i say that before...?")
    hide s_text
    hide b
    stop music fadeout 2
    show layer master:
        SP
        zoom 1.75 xcenter 200 ycenter 420
        1
        easein_circ 0.75 zoom 1.5 xcenter 300 ycenter 380
    show bg club_day:
        SP
        zoom 1.375 xcenter 475 ycenter 365
        1
        easein_circ 0.75 zoom 1.5 xcenter 430 ycenter 380
    $ pause(1)
    n 4y "Oh?"
    n "I didn't realize you were so invested in trying to impress our new member, Yuri."
    show layer master:
        zoom 1.5 xcenter 1050 ycenter 500
    show bg club_day:
        zoom 1.5 xcenter 310 ycenter 350
    show yuri 1n at i11:
        SP
        zoom 1.15 xcenter 384 ycenter 400 yoffset 0
        easein 0.1 yoffset -15
        easeout 0.1 yoffset 0
    play music inferno
    y "E-Eh?!"
    y "That's not what I...!"
    y 1o "Uu..."
    show layer master:
        zoom 1.5 xcenter 1400 ycenter 340
    show bg club_day:
        zoom 1.5 xcenter 200 ycenter 390
    show sans_t 1 at TC:
        zoom 1.5 xcenter -7 ycenter 532
        sans_t_move(1.2)
    show sans j at TC:
        zoom 1.5 xcenter -10 ycenter 392
        sans_h_move(1.2)
    show b l at TC:
        zoom 0.5 xcenter 300 ycenter 400
    show s_text "{size=32}nah,":
        xcenter 235 ycenter 300
    $ s_say("nah,")
    $ pause(0.4)
    show s_text "{size=32}{space=75}it's\nnothin'." as s1:
        xcenter 269 ycenter 316
    $ s_say("it's nothin'.")
    $ pause()
    $ s_say2("nah, it's nothin'.")
    hide s1
    show s_text "{size=32}keep going.":
        xcenter 289 ycenter 300
    $ s_say("keep going.")
    $ pause()
    $ s_say2("keep going.")
    hide b
    hide s_text
    show layer master:
        zoom 1.5 xcenter 1050 ycenter 500
    show bg club_day:
        zoom 1.5 xcenter 310 ycenter 350
    y "You...You're just..."
    y 2r "Maybe you're just jealous that Sans appreciates my advice more than he appreciated yours!"
    show layer master:
        zoom 1.5 xcenter 1400 ycenter 340
    show bg club_day:
        zoom 1.5 xcenter 200 ycenter 390
    show sans_t 1 at TC:
        zoom 1.5 xcenter -7 ycenter 532
        sans_t_move(1.2)
    show sans b at TC:
        zoom 1.5 xcenter -10 ycenter 392
        sans_h_move(1.2)
    show b l at TC:
        zoom 0.5 xcenter 300 ycenter 400
    show s_text "{size=32}(actually,":
        xcenter 280 ycenter 300
    $ s_say("(actually,")
    $ pause(0.4)
    show s_text "{size=32}{space=165}i\ndon't.)" as s1:
        xcenter 293 ycenter 316
    $ s_say("i don't.)")
    $ pause()
    $ s_say2("(actually, i don't.)")
    hide s_text
    hide b
    hide s1
    show layer master:
        zoom 1.5 xcenter 300 ycenter 380
    show bg club_day:
        zoom 1.5 xcenter 430 ycenter 380
    show natsuki 1e at i11:
        zoom 1.15 xcenter 910 ycenter 400 yoffset 0
        easein 0.1 yoffset -10
        easeout 0.1 yoffset 0
    n "Huh! And how do you know he didn't appreciate {i}my{/i} advice more?"
    n 2g "Hey, Sans! Let's be honest, do you prefer my advice or hers?"
    show layer master:
        zoom 1.5 xcenter 1400 ycenter 340
    show bg club_day:
        zoom 1.5 xcenter 200 ycenter 390
    show sans_t 2 at TC:
        zoom 1.5 xcenter -7 ycenter 532
        sans_t_move(1.2)
    show sans d at TC:
        zoom 1.5 xcenter -10 ycenter 392
        sans_h_move(1.2)
    show b l at TC behind sans_t:
        zoom 0.5 xcenter 300 ycenter 400
    show s_text "{size=32}i dunno,":
        xcenter 264 ycenter 300
    $ s_say("i dunno,")
    $ pause(0.4)
    show s_text "{size=32}{space=133}i\nguess both will\ndo." as s1:
        xcenter 315 ycenter 332
    $ s_say("i guess both will do.")
    $ pause()
    $ s_say2("i dunno, i guess both will do.")
    hide b
    hide s_text
    hide s1
    show layer master:
        zoom 1.5 xcenter 300 ycenter 380
    show bg club_day:
        zoom 1.5 xcenter 430 ycenter 380
    show natsuki 1o at i11:
        zoom 1.15 xcenter 910 ycenter 400
        layershake2(-5, -10)
    n "Uuu...! You're so clueless!"
    scene bg club_day:
        zoom 1.5 xcenter 200 ycenter 370
    show layer master:
        zoom 1.5 xcenter 2100 ycenter 440
    $ pause(0.1)
    show sayori 2l at i11:
        SP
        zoom 1.15 xcenter -1000 ycenter 400
        easein_circ 0.66 xcenter -350
    $ pause(0.25)
    window auto
    s "U-Um!!"
    s "Is everyone okay...?"
label ch2_poemend2:
    window hide(None)
    scene bg club_day:
        zoom 1.5 xcenter 430 ycenter 380
    show layer master:
        zoom 1.5 xcenter 300 ycenter 380
    show natsuki 1f at i11:
        zoom 1.15 xcenter 910 ycenter 400
    show yuri 2r at i11:
        zoom 1.15 xcenter 384 ycenter 400
    show sans_t 1 at TC:
        zoom 1.5 xcenter -7 ycenter 532
        sans_t_move(1.2)
    show sans h at TC:
        zoom 1.5 xcenter -10 ycenter 392
        sans_h_move(1.2)
    n "Well, you know what?!"
    n "I wasn't the one whose boobs magically grew a size bigger as soon as Sans started showing up!!"
    play sound quack2
    show layer master:
        zoom 1.5 xcenter 1050 ycenter 500
    show bg club_day:
        zoom 1.5 xcenter 310 ycenter 350
    show yuri 3p at i11:
        SP
        zoom 1.15 xcenter 384 ycenter 400 yoffset 0
        easein 0.1 yoffset -15
        easeout 0.1 yoffset 0
    y "N-Natsuki!!"
    show layer master:
        zoom 1.5 xcenter 1400 ycenter 340
    show bg club_day:
        zoom 1.5 xcenter 200 ycenter 390
    show sans_t 1 at TC:
        zoom 1.5 xcenter -7 ycenter 532
        sans_t_move(1.2)
    show sans b at TC:
        zoom 1.5 xcenter -10 ycenter 392
        sans_h_move(1.2)
    show b l at TC behind sans_t:
        zoom 0.5 xcenter 300 ycenter 400
    show s_text "{size=32}whoa there,":
        xcenter 293 ycenter 300
    $ s_say("whoa there,")
    $ pause(0.4)
    show s_text "{size=32}fella," as s1:
        xcenter 248 ycenter 336
    $ s_say("fella,")
    $ pause(0.4)
    show s_text "{size=32}{space=100}watch\nyour language." as s2:
        xcenter 315 ycenter 352
    $ s_say("watch your language.")
    $ pause()
    $ s_say2("whoa there, fella, watch your language.")
    hide s1
    hide s2
    show sans_t 1 at TC:
        zoom 1.5 xcenter -7 ycenter 532
        sans_t_move(1.2)
    show sans d at TC:
        zoom 1.5 xcenter -10 ycenter 392
        sans_h_move(1.2)
    show s_text "{size=32}you can't just\njump straight\ninto an\nargument.":
        xcenter 314 ycenter 349
    $ s_say("you can't just jump straight into an argument.")
    $ pause()
    $ s_say2("you can't just jump straight into an argument.")
    show sans_t 1 at TC:
        zoom 1.5 xcenter -7 ycenter 532
        sans_t_move(1.2)
    show sans b at TC:
        zoom 1.5 xcenter -10 ycenter 392
        sans_h_move(1.2)
    show s_text "{size=32}this is a club,":
        xcenter 314 ycenter 300
    $ s_say("this is a club,")
    $ pause(0.4)
    show s_text "{size=32}not a big fight\nshindig." as s1:
        xcenter 319 ycenter 350
    $ s_say("not a big fight shindig.")
    $ pause()
    $ s_say2("this is a club, not a big fight shindig.")
    hide s1
    hide b
    hide s_text
    show layer master:
        zoom 1.5 xcenter 300 ycenter 380
    show bg club_day:
        zoom 1.5 xcenter 430 ycenter 380
    show sans_t 1 at TC:
        zoom 1.5 xcenter -7 ycenter 532
        sans_t_move(1.2)
    show sans h at TC:
        zoom 1.5 xcenter -10 ycenter 392
        sans_h_move(1.2)
    show yuri 2n
    n 1e "But she was so mean to me!"
    n "She doesn't want to be emotionally invested in my poems!"
    show layer master:
        SP
        zoom 1.5 xcenter 300 ycenter 380
        ease_cubic 0.5 xcenter 1050 ycenter 500
    show bg club_day:
        SP
        zoom 1.5 xcenter 430 ycenter 380
        ease_cubic 0.5 xcenter 310 ycenter 350
    $ pause(0.5)
    y "W-Wait! I-I do want to...!"
    y 2o "I...I just want to evoke your emotions."
    play sound2 eq loop fadein 6
    show natsuki 1o
    show layer master:
        SP
        zoom 1.5 xcenter 1050 ycenter 500
        ease_cubic 0.5 xcenter 300 ycenter 380
    show bg club_day:
        SP
        zoom 1.5 xcenter 310 ycenter 350
        ease_cubic 0.5 xcenter 430 ycenter 380
    show vignette onlayer front:
        TC
        alpha 0
        ease 6 alpha 0.33
    $ pause(0.5)
    n "It doesn't evoke any of them when you're using irritating and complicated language!"
    show layer master:
        SP
        zoom 1.75 xcenter 200 ycenter 420
        easein_cubic 0.75 zoom 1.5 xcenter 300 ycenter 380
    show bg club_day:
        SP
        zoom 1.375 xcenter 475 ycenter 365
        easein_cubic 0.75 zoom 1.5 xcenter 430 ycenter 380
    show speedline at SL onlayer front:
        alpha 1
        easein 0.75 alpha 0
    show layer screens:
        TC
        layershake2(-20, -10, 1)
    show natsuki 1o at i11:
        zoom 1.15 xcenter 910 ycenter 400
        layershake2(-10, -10, 1)
    n "It's just an excuse to have no clarification at all!"
    hide speedline onlayer front
    hide natsuki
    show layer master:
        zoom 1.5 xcenter 1400 ycenter 340
    show bg club_day:
        zoom 1.5 xcenter 200 ycenter 390
    show sans_t 1 at TC:
        zoom 1.5 xcenter -7 ycenter 532
        sans_t_move(1.2)
    show sans e at TC:
        zoom 1.5 xcenter -10 ycenter 392
        sans_h_move(1.2)
    show b l at TC behind sans_t:
        zoom 0.5 xcenter 300 ycenter 400
    show s_text "{size=32}alright,":
        xcenter 263 ycenter 300
    $ s_say("alright,")
    $ pause(0.4)
    show s_text "{size=32}{space=125}lemme\nsweeten the\ndeal for ya." as s1:
        xcenter 309 ycenter 332
    $ s_say("lemme sweeten the deal for ya.")
    $ pause()
    $ s_say2("alright, lemme sweeten the deal for ya.")
    hide s1
    show sans_t 1 at TC:
        zoom 1.5 xcenter -7 ycenter 532
        sans_t_move(1.2)
    show sans a at TC:
        zoom 1.5 xcenter -10 ycenter 392
        sans_h_move(1.2)
    show s_text "{size=32}keep doing\nwhatever you\ndo.":
        xcenter 305 ycenter 333
    $ s_say("keep doing whatever you do.")
    $ pause()
    $ s_say2("keep doing whatever you do.")
    show sans_t 1 at TC:
        zoom 1.5 xcenter -7 ycenter 532
        sans_t_move(1.2)
    show sans d at TC:
        zoom 1.5 xcenter -10 ycenter 392
        sans_h_move(1.2)
    show s_text "{size=32}eventually,":
        xcenter 289 ycenter 300
    $ s_say("eventually,")
    $ pause(0.4)
    show s_text "{size=32}y'all gonna\nrustle up some\nsense." as s1:
        xcenter 313 ycenter 368
    $ s_say("y'all gonna rustle up some sense.")
    $ pause()
    $ s_say2("eventually, y'all gonna rustle up some sense.")
    show layer master:
        SP
        zoom 1.5 xcenter 1400 ycenter 340
        easein_circ 0.5 zoom 10 xcenter 7125 ycenter 0
    $ pause(0.35)
label ch2_poemend3:
    scene bg class_day:
        zoom 2 xcenter 0 ycenter 380
    show monika 1d at i11:
        SP
        zoom 1.25 xcenter 1100 ycenter 420
        0.25
        parallel:
            easein_quad 1.5 xcenter 875
        parallel:
            ease_quad 0.75 ycenter 400
            ease_quad 0.75 ycenter 420
    show sans_l at TC:
        zoom 1.65 xcenter 400 ycenter 775
    show sans_t 1 at TC:
        zoom 1.65 xcenter 392 ycenter 603
        sans_t_move(1.35)
    show sans d at TC:
        zoom 1.65 xcenter 390 ycenter 448
        sans_h_move(1.35)
    show layer master at TC:
        SP
        zoom 10 xcenter 3150 ycenter -525
        easeout_circ 0.75 zoom 1 xcenter 640 ycenter 360
    $ pause(0.75)
    show layer master at TC:
        layershake2(-40, -40)
    show bg class_day:
        zoom 2 xcenter 0 ycenter 380
        layershake2(17.5, 17.5)
    $ pause(0.25)
    window auto
    m 1d "Hey Sans, why can't you stop the violence over there?"
    window hide(None)
    show sans_t 1 at TC:
        zoom 1.65 xcenter 392 ycenter 603
        sans_t_move(1.35)
    show sans h at TC:
        zoom 1.65 xcenter 390 ycenter 448
        sans_h_move(1.35)
    show b m at TC behind sans_l:
        zoom 1.1 xcenter 700 ycenter 460
    show s_text "{size=32}hate to say it,":
        xcenter 715 ycenter 350
    $ s_say("hate to say it,")
    $ pause(0.4)
    show s_text "{size=32}but..." as s1:
        xcenter 645 ycenter 387
    $ s_say("but...")
    $ pause()
    $ s_say2("hate to say it, but...")
    hide s1
    show sans_t 1 at TC:
        zoom 1.65 xcenter 392 ycenter 603
        sans_t_move(1.35)
    show sans b at TC:
        zoom 1.65 xcenter 390 ycenter 448
        sans_h_move(1.35)
    show s_text "{size=32}these skunks\nare starting to\nsmell.":
        xcenter 715 ycenter 382
    $ s_say("these skunks are starting to smell.")
    $ pause()
    $ s_say2("these skunks are starting to smell.")
    show sans_t 1 at TC:
        zoom 1.65 xcenter 392 ycenter 603
        sans_t_move(1.35)
    show sans h at TC:
        zoom 1.65 xcenter 390 ycenter 448
        sans_h_move(1.35)
    show s_text "{size=32}and i have no\nidea what to do.":
        xcenter 726 ycenter 366
    $ s_say("and i have no idea what to do.")
    $ pause()
    $ s_say2("and i have no idea what to do.")
    show s_text "{size=32}can you find\na method to\nstop 'em?":
        xcenter 695 ycenter 383
    $ s_say("can you find a method to stop 'em?")
    $ pause()
    $ s_say2("can you find a method to stop 'em?")
    hide b
    hide s_text
    show monika 3l at i11:
        SP
        zoom 1.25 xcenter 875 ycenter 420
        easein 0.1 yoffset -15
        easeout 0.1 yoffset 0
    m "Ah, sorry!"
    m "Monika doesn't have any solutions! Because I'm not used at solving difficult situations."
    m 1m "As a president, it's kind of embarrassing, you know?"
    m "I'm pretty glad you should ask Sayori for help if you need her."
    stop music fadeout 2
    stop sound2 fadeout 2
    show vignette onlayer front:
        alpha 0.33
        ease 2 alpha 0
    show sans_t 1 at TC:
        zoom 1.65 xcenter 392 ycenter 603
        sans_t_move(1.35)
    show sans e at TC:
        zoom 1.65 xcenter 390 ycenter 448
        sans_h_move(1.35)
    show b m at TC behind sans_l:
        zoom 1.1 xcenter 700 ycenter 460
    show s_text "{size=32}nah,":
        xcenter 630 ycenter 350
    $ s_say("nah,")
    $ pause(0.4)
    show s_text "{size=32}{space=75}y'know\nwhat?" as s1:
        xcenter 687 ycenter 366
    $ s_say("y'know what?")
    $ pause()
    $ s_say2("nah, y'know what?")
    hide s1
    show s_text "{size=32}i'll do it.":
        xcenter 675 ycenter 350
    $ s_say("i'll do it.")
    $ pause()
    hide vignette onlayer front
    $ s_say2("i'll do it.")
    show s_text "{size=32}i'll end this\ncrap.":
        xcenter 691 ycenter 366
    $ s_say("i'll end this crap.")
    $ pause()
    $ s_say2("i'll end this crap.")
    hide b
    hide s_text
    $ pause(0.75)
    play sound ut_whoosh
    show layer master at TC:
        layershake2(0, -60)
    show bg class_day:
        zoom 2 xcenter 0 ycenter 380
        layershake2(0, 22.5)
    show white at TC:
        alpha 0.66 zoom 1.5
        linear 0.15 alpha 0
    $ pause(0.25)
    hide white
    show monika 1d at i11:
        SP
        zoom 1.25 xcenter 875 ycenter 420
        easein 0.1 yoffset -15
        easeout 0.1 yoffset 0
    play sound2 ut_hurt
    show layer screens at TC:
        layershake(-30, -30, -1.25)
    ny "Aaghk--!\"{space=1000}{w=0.5}{nw}"
    $ _history_list[-1].what = "\"Aaghk--!\""
    $ pause(0.1)
    play sound impact3
    play sound2 ice
    show layer master at TC:
        layershake2(40, -40, 1)
    show bg class_day:
        zoom 2 xcenter 0 ycenter 380
        layershake2(-18, 18, 1)
    $ pause(1.5)
    show sans_t 1 at TC:
        zoom 1.65 xcenter 392 ycenter 603
        sans_t_move(1.35)
    show sans a at TC:
        zoom 1.65 xcenter 390 ycenter 448
        sans_h_move(1.35)
    show b m at TC behind sans_l:
        zoom 1.1 xcenter 700 ycenter 460
    show s_text "{size=32}there ya go.":
        xcenter 696 ycenter 350
    $ s_say("there ya go.")
    $ pause()
    $ s_say2("there ya go.")
    show sans_t 1 at TC:
        zoom 1.65 xcenter 392 ycenter 603
        sans_t_move(1.35)
    show sans b at TC:
        zoom 1.65 xcenter 390 ycenter 448
        sans_h_move(1.35)
    show s_text "{size=32}oh gee,":
        xcenter 654 ycenter 350
    $ s_say("oh gee,")
    $ pause(0.4)
    show s_text "{size=32}{space=123}would\nya look at the\ntime." as s1:
        xcenter 711 ycenter 383
    $ s_say("would ya look at the time.")
    $ pause()
    $ s_say2("oh gee, would ya look at the time.")
    hide s1
    show sans_t 1 at TC:
        zoom 1.65 xcenter 392 ycenter 603
        sans_t_move(1.35)
    show sans h at TC:
        zoom 1.65 xcenter 390 ycenter 448
        sans_h_move(1.35)
    show s_text "{size=32}it's time for a\nslap-up meal.":
        xcenter 713 ycenter 366
    $ s_say("it's time for a slap-up meal.")
    $ pause()
    $ s_say2("it's time for a slap-up meal.")
    show sans_t 1 at TC:
        zoom 1.65 xcenter 392 ycenter 603
        sans_t_move(1.35)
    show sans j at TC:
        zoom 1.65 xcenter 390 ycenter 448
        sans_h_move(1.35)
    show s_text "{size=32}in grillby's.":
        xcenter 691 ycenter 350
    $ s_say("in grillby's.")
    $ pause()
    $ s_say2("in grillby's.")
    hide b
    hide s_text
    hide sans
    hide sans_l
    hide sans_t
    play sound disappear
    show layer master at TC:
        layershake2(15, -15)
    show bg class_day:
        zoom 2 xcenter 0 ycenter 380
        layershake2(-3.5, 3.5)
    show sans_shockwave at TC:
        zoom 0.3 xcenter 390 ycenter 590
        shockwave_zoom(0.45)
    show sans_shockwave at TC as ss1:
        zoom 0.15 xcenter 390 ycenter 590
        shockwave_zoom(0.15, 0.25)
    show white at TC:
        alpha 0.66 zoom 1.5
        linear 0.15 alpha 0
    $ pause(1.5)
    hide sans_shockwave
    hide ss1
    play sound "<from 0.6>mod_assets/sfx/leroy.ogg" fadein 1
    show sayori 4r at i11:
        SP
        zoom 1.25 xcenter 350 ycenter -750
        0.75
        parallel:
            linear 0.25 ycenter 420
        parallel:
            RG
            time 0.25
        parallel:
            0.25
            rotate 0
    $ pause(0.7)
    play audio concrete
    $ pause(0.2)
    stop sound
    $ playexplode()
    show white at TC:
        alpha 0.66 zoom 2
        linear 0.15 alpha 0
    show explode at TC:
        zoom 7.5 xcenter 350 ycenter 380
    show explodenew at TC:
        zoom 2.75 xcenter 350 ycenter 380
    show shockwave at TC behind explode:
        zoom 0.5 xcenter 360 ycenter 380
        shockwave_zoom(0.5)
    show layer master at TC:
        layershake(-40, -205, 5, 1)
    show bg class_day:
        zoom 2 xcenter 0 ycenter 380
        layershake(17.5, 95.5, -2.5, 1)
    $ pause(1)
    $ hide_explosions()
    s "What did I miss? The fight?"
label post_ch2:
    window hide(None)
    scene black
    play sound paulsans4
    show splash_warning2 "While spending time with his club members these days," at TC:
        ycenter 300
    $ pause(2.87)
    show splash_warning2 "Sans happened to learn even further about them." as s1 at TC:
        ycenter 340
    $ pause(2.79)
    show splash_warning2 "How remarkable." as s2 at TC:
        ycenter 380
    $ pause(1.34)
    scene black
    with Dissolve(0.5)
    play sound paulsans5
    show splash_warning2 "He still proceeds to create (dull) poems" at TC:
        ycenter 300
    $ pause(2.075)
    show splash_warning2 "and shares them with the club members day by day." as s1 at TC:
        ycenter 340
    $ pause(3.1)
    show splash_warning2 "Until then..." as s2 at TC:
        ycenter 380
    $ pause(1.125)
    scene black
    with Dissolve(0.5)
    return

init python:
    import math
    
    def image_loop(z=1, indefinite=False, w=1280):
        if indefinite:
            y = w / 2
            ans = ((y * z)-(y * z)- y)+ 640
            ans2 = "Left: " + str(ans - ans - ans) + " Right: " + str(ans + y) + " (Might not be the answer.)"
            return ans2
        else:
            ans = (640 * z)+((640 * z)- 640)
            ans2 = "Left: " + str(ans - ans - ans) + " Right: " + str(ans + 640)
            return ans2 