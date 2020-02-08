
screen ch3_choice():
    
    style_prefix "NYEH"
    
    vbox:
        hbox:
            frame:
                textbutton "Natsuki." action Jump("ch3_natsuki") at c_trans
            frame:
                textbutton "Yuri." action Jump("ch3_yuri") at c_trans

        hbox:
            if not help_monika:
                frame:
                    textbutton "Monika." action Jump("ch3_monika") at c_trans
            if not help_sayori:
                frame:
                    textbutton "Sayori..." action Jump("ch3_sayori") at c_trans
    
define super_pixellate = Pixellate(1, 8)
define SUPER_MARIO_WORLD_TRANSITION_YAY = ComposeTransition(super_pixellate, before=fade, after=fade)

label ch3:
    scene bg club_day at TC:
        zoom 1.75 ycenter 450
    show natsuki 3c at i11:
        zoom 1.5 xcenter 0 ycenter 450
    show monika 1a at i11:
        zoom 1.5 xcenter 640 ycenter 450
    show yuri 1e at i11:
        zoom 1.5 xcenter 1280 ycenter 450
    with wipeleft
    play music t3
    m 1a "Anyway, we need to figure out the rest of the festival preparations, so..."
    m "I'll decide what everyone will be doing this weekend."
    show layer master:
        SP
        TC2
        easein_cubic 0.5 xcenter 1120 ycenter 300
    show bg club_day:
        SP
        zoom 1.75 xcenter 640 ycenter 450
        easein_cubic 0.5 xcenter 525 ycenter 475
    m "Natsuki will be making cupcakes with different flavors."
    n 5d "You bet!"
    show layer master:
        SP
        xcenter 1120 ycenter 300
        easein_cubic 0.5 TC2
    show bg club_day:
        SP
        zoom 1.75 xcenter 525 ycenter 475
        easein_cubic 0.5 xcenter 640 ycenter 450
    m 2a "And as for myself..."
    m "I'm going to be printing and assembling all the poetry pamphlets."
    m "Sayori will be helping me design them."
    m "And as for Yuri..."
    m 1d "..."
    m 3n "Yuri, you can..."
    window hide(None)
    show layer master:
        SP
        xcenter 160 ycenter 420
        easeout 1.5 zoom 1.1 xcenter 80 ycenter 450
    show bg club_day:
        SP
        zoom 1.75 xcenter 755 ycenter 425
        easeout 1.5 zoom 1.7 xcenter 775 ycenter 415
    show natsuki 5g
    show yuri 2v
    $ pause(1.5)
    show layer master:
        SP
        xcenter 1120 ycenter 300
        easeout 1.5 zoom 1.1 xcenter 1200
    show bg club_day:
        SP
        zoom 1.75 xcenter 525 ycenter 475
        easeout 1.5 zoom 1.7 xcenter 505 ycenter 470
    $ pause(1.5)
    show layer master
    show bg club_day at TC:
        zoom 1.75 ycenter 450
    m 5a "Guys..."
    m "Can you help me come up with something for Yuri...?"
    show layer master:
        xcenter 160 ycenter 420
    show bg club_day:
        zoom 1.75 xcenter 755 ycenter 425
    y 4c "I..."
    y "I'm useless..."
    show layer master at TC:
        layershake2(0, -20, 1)
    show bg club_day at TC:
        zoom 1.75 ycenter 450
        layershake2(0, 10, 1)
    m 1g "N-No!"
    m "That's not it at all!"
    m 1d "You're the most talented person here, you know!"
    m 2a "That involves your ravishing handwriting."
    m "Besides, you should make some banners and decorations to help set the atmosphere."
    show layer master:
        xcenter 160 ycenter 420
    show bg club_day:
        zoom 1.75 xcenter 755 ycenter 425
    y 4a "Atmosphere...?"
    y "Um, about that..."
    y "I..."
    show yuri 2r at i11 as y1:
        SP
        zoom 1.5 xcenter 1280 ycenter 450 alpha 0.75
        easein_circ 1 zoom 1.75 xcenter 1283 ycenter 480 alpha 0
    y 2r "I love atmosphere!"
    show yuri 2m 
    hide y1
    show layer master
    show bg club_day at TC:
        zoom 1.75 ycenter 450
    m 2b "That's great!"
    m "You'll be a wonderful help, Yuri."
    m 2a "But anyway..."
    m "That just leaves you, Sans."
    show layer master:
        SP
        TC2
        easeout_cubic 0.5 xcenter 880
    show bg club_day at TC:
        SP
        zoom 1.75 xcenter 640 ycenter 450
        easeout_cubic 0.5 xcenter 520
    with None
label ch3_s:
    scene bg class_day:
        SP
        zoom 4 xcenter 680 ycenter 400
        0.5
        easein_cubic 0.75 xcenter 600
    show layer master at TC:
        SP
        xcenter 480
        0.5
        easein_cubic 0.75 xcenter 640
    show sans_t 1 at TC:
        zoom 2.5 xcenter 500 ycenter 600
        sans_t_move(1.75)
    show sans a at TC:
        zoom 2.5 xcenter 495 ycenter 365
        sans_h_move(1.75)
    with SUPER_MARIO_WORLD_TRANSITION_YAY
    $ pause(0.25)
    show b m at TC behind sans_t:
        zoom 1.5 xcenter 950 ycenter 380
    show s_text "{size=45}oh nice.":
        xcenter 900 ycenter 225
    $ s_say("oh nice.")
    $ pause()
    $ s_say2("oh nice.")
    show s_text "{size=45}what shall i do\nthis weekend?":
        xcenter 975 ycenter 248
    $ s_say("what shall i do this weekend?")
    $ pause()
    $ s_say2("what shall i do this weekend?")
    show bg class_day:
        SP
        zoom 4 xcenter 600 ycenter 400
        easeout_cubic 0.5 xcenter 680
    show layer master at TC:
        SP
        xcenter 640
        easeout_cubic 0.5 xcenter 480
    with None
    scene bg club_day:
        SP
        zoom 1.75 xcenter 520 ycenter 450
        0.5
        easein_cubic 0.75 xcenter 640
    show layer master at TC:
        SP
        xcenter 880 ycenter 360
        0.5
        easein_cubic 0.75 TC2
    show natsuki 3c at i11:
        zoom 1.5 xcenter 0 ycenter 450
    show monika 1b at i11:
        zoom 1.5 xcenter 640 ycenter 450
    show yuri 2m at i11:
        zoom 1.5 xcenter 1280 ycenter 450
    with SUPER_MARIO_WORLD_TRANSITION_YAY
    $ pause(0.25)
    m 1b "Both Natsuki and Yuri have some pretty heavy tasks to handle."
    m "It would probably go a long way to give one of them a hand."
    m 1m "You could always help me out, as well..."
    m 1a "I would be really appreciative of that."
    show layer master:
        SP
        TC2
        easeout_cubic 0.5 xcenter 880
    show bg club_day at TC:
        SP
        zoom 1.75 xcenter 640 ycenter 450
        easeout_cubic 0.5 xcenter 520
    with None
    scene bg class_day:
        SP
        zoom 4 xcenter 680 ycenter 400
        0.5
        easein_cubic 0.75 xcenter 600
    show layer master at TC:
        SP
        xcenter 480
        0.5
        easein_cubic 0.75 xcenter 640
    show sans_t 1 at TC:
        zoom 2.5 xcenter 500 ycenter 600
        sans_t_move(1.75)
    show sans a at TC:
        zoom 2.5 xcenter 495 ycenter 365
        sans_h_move(1.75)
    with SUPER_MARIO_WORLD_TRANSITION_YAY
    $ pause(0.25)
    show b m at TC behind sans_t:
        zoom 1.5 xcenter 950 ycenter 380
    show s_text "{size=45}...":
        xcenter 844 ycenter 225
    $ s_say("...")
    $ pause()
    $ s_say2("...")
    show sans_t 1 at TC:
        zoom 2.5 xcenter 500 ycenter 600
        sans_t_move(1.75)
    show sans b at TC:
        zoom 2.5 xcenter 495 ycenter 365
        sans_h_move(1.75)
    show s_text "{size=45}...?":
        xcenter 858 ycenter 225
    $ s_say("...?")
    $ pause()
    $ s_say2("...?")
    scene bg club_day:
        zoom 1.75 xcenter 755 ycenter 425
    show layer master:
        xcenter 160 ycenter 420
    show natsuki 3c at i11:
        zoom 1.5 xcenter 0 ycenter 450
    show monika 1a at i11:
        zoom 1.5 xcenter 640 ycenter 450
    show yuri 1u at i11:
        SP
        zoom 1.5 xcenter 1280 ycenter 450 yoffset 0
        easein 0.1 yoffset -10
        easeout 0.1 yoffset 0
    y 1u "Ah..."
    y "I...suppose I wouldn't mind a bit of help..."
    show layer master:
        SP
        xcenter 160 ycenter 420
        ease_circ 0.5 xcenter 1120 ycenter 300
    show bg club_day:
        SP
        zoom 1.75 xcenter 755 ycenter 425
        ease_circ 0.5 xcenter 525 ycenter 475
    $ pause(0.6)
    n "Well, even if you don't know how to bake, there's always some dirty work I could give to you."
    n 3q "It's not like Monika's going to give me a choice, and you shouldn't be sitting on your butt anyway..."
    scene bg class_day:
        zoom 4 xcenter 600 ycenter 400
    show sans_t 1 at TC:
        zoom 2.5 xcenter 500 ycenter 600
        sans_t_move(1.75)
    show sans b at TC:
        zoom 2.5 xcenter 495 ycenter 365
        sans_h_move(1.75)
    with Dissolve(0.5)
    $ pause(0.25)
    show b m at TC behind sans_t:
        zoom 1.5 xcenter 950 ycenter 380
    show s_text "{size=45}well...":
        xcenter 888 ycenter 225
    $ s_say("well...")
    $ pause()
    $ s_say2("well...")
    show sans_t 2 at TC:
        zoom 2.5 xcenter 500 ycenter 600
        sans_t_move(1.75)
    show sans b at TC:
        zoom 2.5 xcenter 495 ycenter 365
        sans_h_move(1.75)
    show s_text "{size=45}sounds like i\nwill replenish\nmy calcium\nagain.":
        xcenter 958 ycenter 294
    $ s_say("sounds like i will replenish my calcium again.")
    $ pause()
    $ s_say2("sounds like i will replenish my calcium again.")
    scene bg club_day at TC:
        zoom 1.75 ycenter 450
    show natsuki 3q at i11:
        zoom 1.5 xcenter 0 ycenter 450
    show monika 1a at i11:
        zoom 1.5 xcenter 640 ycenter 450
    show yuri 1u at i11:
        zoom 1.5 xcenter 1280 ycenter 450
    m "Anyways, Sans will decide how he'd like to contribute."
    m "Besides..."
    show monika 5a at i11: # I don't like this...
        SP
        zoom 1.5 xcenter 640 ycenter 450
        easein 0.1 yoffset -15
        easeout 0.1 yoffset 0
    show confess as c1 behind monika:
        zoom 2 xcenter 1850 ycenter 1225
    show confess as c2 behind monika:
        zoom 2 xcenter 1850 ycenter 1225
    show confess as c3 behind monika:
        zoom 2 xcenter 1850 ycenter 1225
    show confess as c4 behind monika:
        zoom 2 xcenter 1850 ycenter 1225
    m 5 "He hasn't really gotten the chance to spend any time with me yet, you know?"
    m "So I'm sure he's interested in--"
    hide c1
    hide c2
    hide c3
    hide c4
    show layer master:
        SP
        zoom 1.2 xcenter 1200 ycenter 300
        parallel:
            easein_elastic 1 zoom 1 xcenter 1120
        parallel:
            layershake2(-60, -40, 1)
    show bg club_day:
        SP
        zoom 1.7 xcenter 505 ycenter 470
        parallel:
            easein_elastic 1 zoom 1.75 xcenter 525 ycenter 475
        parallel:
            layershake2(30, 20, 1)
    show speedline at SL onlayer front:
        alpha 1
        easeout 0.75 alpha 0
    n 4f "Wait! You said--"
    hide speedline onlayer front
    show bg club_day:
        zoom 1.75 xcenter 755 ycenter 425
    show layer master:
        xcenter 160 ycenter 420
    y 2t "Monika, I-I'm surprised as well!"
    show bg club_day at TC:
        zoom 1.75 xcenter 640 ycenter 450
    show layer master
    show monika 1l at i11:
        SP
        zoom 1.5 xcenter 640 ycenter 450 yoffset 0
        easein 0.1 yoffset -15
        easeout 0.1 yoffset 0
    m "Sorry, sorry!"
    m "I was just saying, though..."
    show layer master:
        SP
        TC2
        easein_cubic 0.5 xcenter 1120 ycenter 300
    show bg club_day:
        SP
        zoom 1.75 xcenter 640 ycenter 450
        easein_cubic 0.5 xcenter 525 ycenter 475
    n 4x "Ugh..."
    n "Can we just settle this already?"
    show layer master:
        SP
        xcenter 1120 ycenter 300
        easein_cubic 0.5 TC2
    show bg club_day:
        SP
        zoom 1.75 xcenter 525 ycenter 475
        easein_cubic 0.5 xcenter 640 ycenter 450
    m 1e "Yeah..."
    m "Sans, you're okay with this, right?"
    m 1a "In the end, it's up to you."
    show layer master:
        SP
        TC2
        easeout_cubic 0.5 xcenter 880
    show bg club_day at TC:
        SP
        zoom 1.75 xcenter 640 ycenter 450
        easeout_cubic 0.5 xcenter 520
    with None
    scene bg class_day:
        SP
        zoom 4 xcenter 680 ycenter 400
        0.5
        easein_cubic 0.75 xcenter 600
    show layer master at TC:
        SP
        xcenter 480
        0.5
        easein_cubic 0.75 xcenter 640
    show sans_t 1 at TC:
        zoom 2.5 xcenter 500 ycenter 600
        sans_t_move(1.75)
    show sans a at TC:
        zoom 2.5 xcenter 495 ycenter 365
        sans_h_move(1.75)
    with SUPER_MARIO_WORLD_TRANSITION_YAY
    $ pause(0.25)
    show b m at TC behind sans_t:
        zoom 1.5 xcenter 950 ycenter 380
    show s_text "{size=45}ok,":
        xcenter 847 ycenter 225
    $ s_say("ok,")
    $ pause(0.4)
    show s_text "{size=45}{space=85}lemme\nsweeten this\nup." as s1:
        xcenter 945 ycenter 270
    $ s_say("lemme sweeten this up.")
    $ pause()
    $ s_say2("ok, lemme sweeten this up.")
    hide s1
    show sans_t 1 at TC:
        zoom 2.5 xcenter 500 ycenter 600
        sans_t_move(1.75)
    show sans b at TC:
        zoom 2.5 xcenter 495 ycenter 365
        sans_h_move(1.75)
    show s_text "{size=45}y'all lookin\ngreat,":
        xcenter 939 ycenter 247
    $ s_say("y'all lookin great,")
    $ pause(0.4)
    show s_text "{size=45}{space=150}by the\nway." as s1:
        xcenter 956 ycenter 294
    $ s_say("by the way.")
    $ pause()
    $ s_say2("y'all lookin great, by the way.")
    hide s1
    show sans_t 1 at TC:
        zoom 2.5 xcenter 500 ycenter 600
        sans_t_move(1.75)
    show sans e at TC:
        zoom 2.5 xcenter 495 ycenter 365
        sans_h_move(1.75)
    show s_text "{size=45}i reckon i'll\nprefer...":
        xcenter 945 ycenter 247
    $ s_say("i reckon i'll prefer...")
    $ pause()
    $ s_say2("i reckon i'll prefer...")
    $ help_monika = False
    $ help_sayori = False
    hide b
    hide s_text
    play audio whoosh
    show layer screens:
        TC
        SP
        ycenter 600
        easein_elastic 1 ycenter 360
    # show splash_warning4_5 "(End of demo.)" onlayer screens:
        # xcenter 1000 ycenter 700
    call screen ch3_choice()
    return

label ch3_natsuki:
    $ pause(0.5)
    show sans_t 1 at TC:
        zoom 2.5 xcenter 500 ycenter 600
        sans_t_move(1.75)
    show sans a at TC:
        zoom 2.5 xcenter 495 ycenter 365
        sans_h_move(1.75)
    show b m at TC behind sans_t:
        zoom 1.5 xcenter 950 ycenter 380
    # 
    return
label ch3_yuri:
    "Not done yet."
    return
label ch3_monika:
    $ help_monika = True
    $ pause(0.5)
    show sans_t 1 at TC:
        zoom 2.5 xcenter 500 ycenter 600
        sans_t_move(1.75)
    show sans a at TC:
        zoom 2.5 xcenter 495 ycenter 365
        sans_h_move(1.75)
    show b m at TC behind sans_t:
        zoom 1.5 xcenter 950 ycenter 380
    show s_text "{size=45}guess i'll\nassist the club\npresident.":
        xcenter 972 ycenter 272
    $ s_say("guess i'll assist the club president.")
    $ pause()
    $ s_say2("guess i'll assist the club president.")
    scene bg club_day at TC:
        zoom 1.75 ycenter 450
    show monika 5a at i11: # I still don't like this...
        SP
        zoom 1.5 xcenter 640 ycenter 450
        easein 0.1 yoffset -15
        easeout 0.1 yoffset 0
    show confess as c1 behind monika:
        zoom 2 xcenter 1850 ycenter 1225
    show confess as c2 behind monika:
        zoom 2 xcenter 1850 ycenter 1225
    show confess as c3 behind monika:
        zoom 2 xcenter 1850 ycenter 1225
    show confess as c4 behind monika:
        zoom 2 xcenter 1850 ycenter 1225
    show natsuki 3g at i11:
        zoom 1.5 xcenter 0 ycenter 450
    show yuri 1e at i11:
        zoom 1.5 xcenter 1280 ycenter 450
    m "Yay, you picked me!"
    hide c1
    hide c3
    hide c3
    hide c4
    show layer master:
        SP
        zoom 1.2 xcenter 1200 ycenter 300
        parallel:
            easein_elastic 1 zoom 1 xcenter 1120
        parallel:
            layershake2(-60, -40, 1)
    show bg club_day:
        SP
        zoom 1.7 xcenter 505 ycenter 470
        parallel:
            easein_elastic 1 zoom 1.75 xcenter 525 ycenter 475
        parallel:
            layershake2(30, 20, 1)
    show speedline at SL onlayer front:
        alpha 1
        easeout 0.75 alpha 0
    n 3e "Hold on one second!"
    hide speedline onlayer front
    show bg club_day:
        zoom 1.75 xcenter 755 ycenter 425
    show layer master:
        xcenter 160 ycenter 420
    y 2r "Y-Yeah!"
    show layer master:
        zoom 1 xcenter 1120 ycenter 300
    show bg club_day:
        zoom 1.75 xcenter 525 ycenter 475
    n "Monika, you're the one who needs the least help out of all of us!"
    show layer master:
        SP
        xcenter 1120 ycenter 300
        easein_cubic 0.5 TC2
    show bg club_day:
        SP
        zoom 1.75 xcenter 525 ycenter 475
        easein_cubic 0.5 xcenter 640 ycenter 450
    m 1d "Eh? But..."
    show bg club_day:
        SP
        xcenter 640 ycenter 450
        easein_cubic 0.5 zoom 1.75 xcenter 755 ycenter 425
    show layer master at TC2:
        SP
        easein_cubic 0.5 xcenter 160 ycenter 420
    y "I agree with Natsuki."
    y 1l "Not only is your work already most suitable for one person..."
    y "But you already have Sayori as well."
    show layer master:
        SP
        xcenter 160  ycenter 420
        easein_cubic 0.5 TC2
    show bg club_day:
        SP
        zoom 1.75 xcenter 755 ycenter 425
        easein_cubic 0.5 xcenter 640 ycenter 450
    m 1p "But Sans was the one who..."
    m "Ah..."
    show layer master:
        SP
        TC2
        easeout_cubic 0.5 xcenter 880
    show bg club_day at TC:
        SP
        zoom 1.75 xcenter 640 ycenter 450
        easeout_cubic 0.5 xcenter 520
    with None
    scene bg class_day:
        SP
        zoom 4 xcenter 680 ycenter 400
        0.5
        easein_cubic 0.75 xcenter 600
    show layer master at TC:
        SP
        xcenter 480
        0.5
        easein_cubic 0.75 xcenter 640
    show sans_t 1 at TC:
        zoom 2.5 xcenter 500 ycenter 600
        sans_t_move(1.75)
    show sans a at TC:
        zoom 2.5 xcenter 495 ycenter 365
        sans_h_move(1.75)
    with SUPER_MARIO_WORLD_TRANSITION_YAY
    $ pause(0.25)
    show b m at TC behind sans_t:
        zoom 1.5 xcenter 950 ycenter 380
    show s_text "{size=45}it's fine bud.":
        xcenter 960 ycenter 225
    $ s_say("it's fine bud.")
    $ pause()
    $ s_say2("it's fine bud.")
    show s_text "{size=45}i already\nchanged up my\nmind.":
        xcenter 963 ycenter 272
    $ s_say("i already changed up my mind.")
    $ pause()
    $ s_say2("i already changed up my mind.")
    show s_text "{size=45}having sayori\ndoesn't require\nmy assistance.":
        xcenter 975 ycenter 272
    $ s_say("having sayori doesn't require my assistance.")
    $ pause()
    $ s_say2("having sayori doesn't require my assistance.")
    show sans_t 21 at TC:
        zoom 2.5 xcenter 500 ycenter 600
        sans_t_move(1.75)
    show sans b at TC:
        zoom 2.5 xcenter 495 ycenter 365
        sans_h_move(1.75)
    show bone at TC:
        SP
        zoom 3 xcenter 195 ycenter 325 xzoom 4 alpha 0
        0.25
        easein_cubic 0.5 alpha 1 xzoom 2
        block:
            ease 1 yoffset -10
            ease 1 yoffset 0
            repeat
    show splash_warning "(Adrenaline)":
        SP
        zoom 1 xcenter 195 ycenter 325 rotate -90 yzoom 2 alpha 0
        0.25
        easein_cubic 0.5 alpha 1 yzoom 1
        block:
            ease 1 yoffset -10
            ease 1 yoffset 0
            repeat
    show s_text "{size=45}unless you\nneed it.":
        xcenter 925 ycenter 248
    $ s_say("unless you need it.")
    $ pause()
    $ s_say2("unless you need it.")
    show sans_t 2 at TC:
        zoom 2.5 xcenter 500 ycenter 600
        sans_t_move(1.75)
    show sans i at TC:
        zoom 2.5 xcenter 495 ycenter 365
        sans_h_move(1.75)
    show s_text "{size=45}so i can stand\nthere and do\nnothing.":
        xcenter 966 ycenter 272
    $ s_say("so i can stand there and do nothing.")
    $ pause()
    $ s_say2("so i can stand there and do nothing.")
    scene bg club_day:
        zoom 1.75 xcenter 525 ycenter 475
    show layer master:
        zoom 1 xcenter 1120 ycenter 300
    show natsuki 4b at i11:
        zoom 1.5 xcenter 0 ycenter 450
    show monika 1p at i11:
        zoom 1.5 xcenter 640 ycenter 450
    n 4e "Hello?!"
    n "What about us?"
    scene bg class_day:
        zoom 4 xcenter 600 ycenter 400
    show sans_t 2 at TC:
        zoom 2.5 xcenter 500 ycenter 600
        sans_t_move(1.75)
    show sans a at TC:
        zoom 2.5 xcenter 495 ycenter 365
        sans_h_move(1.75)
    show bone at TC:
        SP
        zoom 3 xcenter 195 ycenter 325 xzoom 2
        parallel:
            ease 1 yoffset -10
            ease 1 yoffset 0
        parallel:
            0.75
            easeout_cubic 0.5 alpha 0 xzoom 4
    show splash_warning "(Adrenaline)":
        SP
        zoom 1 xcenter 195 ycenter 325 rotate -90
        parallel:
            ease 1 yoffset -10
            ease 1 yoffset 0
        parallel:
            0.75
            easeout_cubic 0.5 alpha 0 yzoom 2
    with Dissolve(0.5)
    $ pause(0.25)       
    show b m at TC behind sans_t:
        zoom 1.5 xcenter 950 ycenter 380
    show s_text "{size=45}whoops,":
        xcenter 894 ycenter 225
    $ s_say("whoops,")
    $ pause(0.4)
    show s_text "{size=45}sorry," as s1:
        xcenter 1055 ycenter 225
    $ s_say("sorry,")
    $ pause(0.4)
    show s_text "{size=45}i forgot." as s2:
        xcenter 912 ycenter 275
    hide bone
    hide splash_warning
    $ s_say("i forgot.")
    $ pause()
    $ s_say2("whoops, sorry, i forgot.")
    hide s1
    hide s2
    show sans_t 1 at TC:
        zoom 2.5 xcenter 500 ycenter 600
        sans_t_move(1.75)
    show sans d at TC:
        zoom 2.5 xcenter 495 ycenter 365
        sans_h_move(1.75)
    show s_text "{size=45}i can also\nhelp ya by\ndoing nothing,":
        xcenter 965 ycenter 272
    $ s_say("i can also help ya by doing nothing,")
    $ pause(0.4)
    show s_text "{size=45}too." as s1:
        xcenter 856 ycenter 367
    $ s_say("too.")
    $ pause()
    $ s_say2("i can also help ya by doing nothing, too.")
    scene bg club_day:
        zoom 1.75 xcenter 525 ycenter 475
        layershake2(-25, 22.5, 1)
    show layer master:
        xcenter 1120 ycenter 300
        layershake2(50, -45, 1)
    show natsuki 1o at i11:
        zoom 1.5 xcenter 0 ycenter 450
    show monika 1f at i11:
        zoom 1.5 xcenter 640 ycenter 450
    show yuri 1l at i11:
        zoom 1.5 xcenter 1280 ycenter 450
    show smack at TC:
        zoom 1.25 xcenter -175 ycenter 175
    play sound crit
    n 1o "Hey--!"
    hide smack
    n "Quit saying these shenanigans, seriously!"
    show layer master:
        SP
        xcenter 1120 ycenter 300
        easein_cubic 0.5 TC2
    show bg club_day:
        SP
        zoom 1.75 xcenter 525 ycenter 475
        easein_cubic 0.5 xcenter 640 ycenter 450
    m "Sans..."
    show bg club_day at TC:
        SP
        zoom 1.75 xcenter 640 ycenter 450
        easeout 20 zoom 1.625 ycenter 400
    show layer master at TC:
        SP
        TC2
        easeout 20 zoom 1.25 ycenter 450
    m "This isn't the time to fool around."
    m 1e "It's up to you to pick what you prefer."
    m 1m "We are all being serious here, so please..."
    scene bg class_day:
        zoom 4 xcenter 600 ycenter 400
    show sans_t 1 at TC:
        zoom 2.5 xcenter 500 ycenter 600
        sans_t_move(1.75)
    show sans e at TC:
        zoom 2.5 xcenter 495 ycenter 365
        sans_h_move(1.75)
    with Dissolve(0.5)
    $ pause(0.25)       
    show b m at TC behind sans_t:
        zoom 1.5 xcenter 950 ycenter 380
    show s_text "{size=45}ok,":
        xcenter 847 ycenter 225
    $ s_say("ok,")
    $ pause(0.4)
    show s_text "{size=45}{space=75}no promises\nthough." as s1:
        xcenter 973 ycenter 248
    $ s_say("no promises though.")
    $ pause()
    $ s_say2("ok, no promises though.")
    hide s_text
    hide s1
    hide b
    show layer screens:
        TC
        SP
        ycenter 600
        easein_elastic 1 ycenter 360
    call screen ch3_choice()
    return
    
label ch3_sayori:
    $ help_sayori = True
    $ pause(0.5)
    show sans_t 1 at TC:
        zoom 2.5 xcenter 500 ycenter 600
        sans_t_move(1.75)
    show sans a at TC:
        zoom 2.5 xcenter 495 ycenter 365
        sans_h_move(1.75)
    show b m at TC behind sans_t:
        zoom 1.5 xcenter 950 ycenter 380
    show s_text "{size=45}i'll bottle up\nwith my little\nfella sayori...":
        xcenter 975 ycenter 272
    $ s_say("i'll bottle up with my little fella sayori...")
    $ pause()
    $ s_say2("i'll bottle up with my little fella sayori...")
    show s_text "{size=45}y'know,":
        xcenter 896 ycenter 225
    $ s_say("y'know,")
    $ pause(0.4)
    show s_text "{size=45}{space=170}we're\ngood ol' pals." as s1:
        xcenter 963 ycenter 247
    $ s_say("we're good ol' pals.")
    $ pause()
    $ s_say2("y'know, we're good ol' pals.")
    scene bg club_day:
        zoom 1.75 xcenter 755 ycenter 425
    show layer master:
        xcenter 160 ycenter 420
    show natsuki 4w at i11:
        zoom 1.5 xcenter 0 ycenter 450
    show monika 1a at i11:
        zoom 1.5 xcenter 640 ycenter 450
    show yuri 2f at i11:
        zoom 1.5 xcenter 1280 ycenter 450
    y "But Monika said--"
    show layer master:
        SP
        xcenter 160 ycenter 420
        easein_back 0.75 xcenter 1120 ycenter 300
    show bg club_day:
        SP
        zoom 1.75 xcenter 755 ycenter 425
        easein_back 0.75 xcenter 525 ycenter 475
    $ pause(0.5)
    n "Monika said that Sayori was helping her!"
    n "Jeez..."
    n 4h "Do you really hate us that much?"
    scene bg class_day:
        zoom 4 xcenter 600 ycenter 400
    show sans_t 1 at TC:
        zoom 2.5 xcenter 500 ycenter 600
        sans_t_move(1.75)
    show sans a at TC:
        zoom 2.5 xcenter 495 ycenter 365
        sans_h_move(1.75)
    with Dissolve(0.5)
    $ pause(0.25)
    show b m at TC behind sans_t:
        zoom 1.5 xcenter 950 ycenter 380
    show s_text "{size=45}nah,":
        xcenter 858 ycenter 225
    $ s_say("nah,")    
    $ pause(0.4)
    show s_text "{size=45}not much." as s1:
        xcenter 1025 ycenter 225
    $ s_say("not much.")
    $ pause()
    $ s_say2("nah, not much.")
    hide s1
    show sans_t 1 at TC:
        zoom 2.5 xcenter 500 ycenter 600
        sans_t_move(1.75)
    show sans b at TC:
        zoom 2.5 xcenter 495 ycenter 365
        sans_h_move(1.75)
    show s_text "{size=45}especially when\nyou're acting\nsnarky like\nthat.":
        xcenter 977 ycenter 294
    $ s_say("especially when you're acting snarky like that.")
    $ pause()
    $ s_say2("especially when you're acting snarky like that.")
    scene bg club_day:
        zoom 1.75 xcenter 525 ycenter 475
        layershake2(0, 15, 1)
    show layer master:
        xcenter 1120 ycenter 300
        layershake2(0, -30, 1)
    show natsuki 1o at i11:
        zoom 1.5 xcenter 0 ycenter 450
    show monika 1a at i11:
        zoom 1.5 xcenter 640 ycenter 450
    show yuri 2f at i11:
        zoom 1.5 xcenter 1280 ycenter 450
    n 1o "H-Hey!"
    n "I'm not snarky, you stupid!"
    scene bg class_day:
        zoom 4 xcenter 600 ycenter 400
    show sans_t 1 at TC:
        zoom 2.5 xcenter 500 ycenter 600
        sans_t_move(1.75)
    show sans d at TC:
        zoom 2.5 xcenter 495 ycenter 365
        sans_h_move(1.75)
    with Dissolve(0.5)
    show b m at TC behind sans_t:
        zoom 1.5 xcenter 950 ycenter 380
    show s_text "{size=45}heheh,":
        xcenter 879 ycenter 225
    $ s_say("heheh,")
    $ pause(0.4)
    show s_text "{size=45}{space=150}just\nkidding." as s1:
        xcenter 931 ycenter 247
    $ s_say("just kidding.")
    $ pause()
    $ s_say2("heheh, just kidding.")
    hide s1
    show sans_t 1 at TC:
        zoom 2.5 xcenter 500 ycenter 600
        sans_t_move(1.75)
    show sans b at TC:
        zoom 2.5 xcenter 495 ycenter 365
        sans_h_move(1.75)
    show s_text "{size=45}you sound like\na fun kid,":
        xcenter 967 ycenter 247
    $ s_say("you sound like a fun kid,")
    $ pause(0.4)
    show s_text "{size=45}huh?" as s1:
        xcenter 1100 ycenter 270
    $ s_say("huh?")
    $ pause()
    $ s_say2("you sound like a fun kid, huh?")
    hide s1
    show sans_t 1 at TC:
        zoom 2.5 xcenter 500 ycenter 600
        sans_t_move(1.75)
    show sans a at TC:
        zoom 2.5 xcenter 495 ycenter 365
        sans_h_move(1.75)
    show s_text "{size=45}i don't blame\npeople more\noften.":
        xcenter 954 ycenter 272
    $ s_say("i don't blame people more often.")
    $ pause()
    $ s_say2("i don't blame people more often.")
    show bg class_day:
        SP
        zoom 4 xcenter 600 ycenter 400
        easeout_cubic 0.5 xcenter 680
    show layer master at TC:
        SP
        xcenter 640
        easeout_cubic 0.5 xcenter 480
    with None
    scene bg club_day:
        SP
        zoom 1.75 xcenter 520 ycenter 450
        0.5
        easein_cubic 0.75 xcenter 640
    show layer master at TC:
        SP
        xcenter 880 ycenter 360
        0.5
        easein_cubic 0.75 TC2
    show natsuki 1g at i11:
        zoom 1.5 xcenter 0 ycenter 450
    show monika 1e at i11:
        zoom 1.5 xcenter 640 ycenter 450
    show yuri 2e at i11:
        zoom 1.5 xcenter 1280 ycenter 450
    with SUPER_MARIO_WORLD_TRANSITION_YAY
    $ pause(0.25)
    m "...Well, I didn't mean for this to be difficult..."
    m "Just think of the club, okay?"
    show layer master:
        SP
        TC2
        easeout_cubic 0.5 xcenter 880
    show bg club_day at TC:
        SP
        zoom 1.75 xcenter 640 ycenter 450
        easeout_cubic 0.5 xcenter 520
    with None
    scene bg class_day:
        SP
        zoom 4 xcenter 680 ycenter 400
        0.5
        easein_cubic 0.75 xcenter 600
    show layer master at TC:
        SP
        xcenter 480
        0.5
        easein_cubic 0.75 xcenter 640
    show sans_t 1 at TC:
        zoom 2.5 xcenter 500 ycenter 600
        sans_t_move(1.75)
    show sans e at TC:
        zoom 2.5 xcenter 495 ycenter 365
        sans_h_move(1.75)
    with SUPER_MARIO_WORLD_TRANSITION_YAY
    $ pause(0.25)
    show layer screens:
        TC
        SP
        ycenter 600
        easein_elastic 1 ycenter 360
    call screen ch3_choice()
    return