image symbol = "mod_assets/gui/symbol2.png"
image eyesymbol = "mod_assets/gui/symbol.png"
define audio.bell = "mod_assets/sfx/s_clock.ogg"
define audio.timeeffect = "mod_assets/sfx/s_time.ogg"
define audio.eye = "mod_assets/sfx/s_eye.ogg"
define audio.bell2 = "mod_assets/sfx/bell.ogg"

define audio.slice = "mod_assets/sfx/ut/slice.wav"
define audio.release = "mod_assets/sfx/ut/release.wav"
define audio.charge = "mod_assets/sfx/ut/charge.wav"

image n_up = "mod_assets/spysuki/up.png"
image n_down = "mod_assets/spysuki/down.png"

image oneeye:
    "yuri/oneeye2.png"
    crop (371, 230, 39, 45)
image yuri ghost_base = "yuri/0a.png"

define RUBBER = Pixellate(0.425, 6)

#-------------------------------------------------# ( Goto line 255 to find the label. )
# This is a transformation test.
transform symbol_move:
    function symbol_function

init python:
    def symbol_function(trans, st, at):
        trans.xzoom = (random.random() - 0.5) * 2
        trans.yzoom = (random.random() - 0.5) * 2
        trans.rotate = (random.random() * 360)
        return 0.01
        
image symboltest2:
    SP
    "symbol"
    xcenter 640 ycenter 360
    symbol_move

image symboltest:
    SP
    "symbol"
    xcenter 640 ycenter 360
    parallel:
        rotate 0
        linear 2 rotate 360
        repeat
    parallel:
        yzoom 0.1
        easeout 1 yzoom 1.5
        easein 1 yzoom 0.1
        easeout 1 yzoom 1.5
        easein 1 yzoom 0.1
        repeat
    parallel:
        xzoom 1.5
        easein 1 xzoom 0.1
        easeout 1 xzoom 1.5
        easein 1 xzoom 0.1
        easeout 1 xzoom 1.5
        repeat
#-------------------------------------------------#
        

image death_eye:
    size (2, 2)
    xcenter 1048 ycenter 165
    Blood("blood_particle", dripChance=0.04, numSquirts=0, burstSize=0, dripTime=3600.0).sm

label dc:
    scene white:
        TC
        zoom 3
    show layer master:
        TC
        zoom 0.5 xcenter 700
    pause
    call deathcircle3 from _call_deathcircle3
    pause
    jump dc

# DeathCircle ( inspiration by Roblox Genocider script. )
label deathcircle:
    play audio bell
    show symbol as circ zorder 101:
        SP
        TC
        zoom 2 xcenter 500 ycenter 360
        additive -3
        parallel:
            rotate 0
            linear 5 rotate 360
            repeat
        parallel:
            0.6
            easein 0.1 yoffset -20
            easeout 0.1 yoffset 0
        parallel:
            easein_circ 1.5 additive -0.5
    show symbol as circ2 zorder 102:
        SP
        TC
        alpha 1
        zoom 2 xcenter 500 ycenter 360
        additive -1
        parallel:
            rotate 0
            linear 5 rotate 360
        parallel:
            easein 0.6 alpha 0 zoom 3 additive 0
    show symbol as circ3 zorder 99:
        SP
        TC
        alpha 0.25
        zoom 2.125 xcenter 500 ycenter 360
        additive -0.5
        parallel:
            rotate 0
            linear 5 rotate -360
            repeat
        parallel:
            ease 2 zoom 2.25
            ease 2 zoom 2.125
            repeat
        parallel:
            0.6
            easein 0.1 yoffset -20
            easeout 0.1 yoffset 0
    return
    
label deathcircle2:
    play audio bell
    show symbol as circ zorder 101:
        SP
        TC
        zoom 2 xcenter -55 ycenter 390
        additive -3
        parallel:
            rotate 0
            linear 5 rotate 360
            repeat
        parallel:
            0.65
            easein 0.1 yoffset -20
            easeout 0.1 yoffset 0
        parallel:
            easein_circ 1.5 additive -0.5
    show symbol as circ2 zorder 102:
        SP
        TC
        alpha 1
        zoom 2 xcenter -55 ycenter 390
        additive -1
        parallel:
            rotate 0
            linear 5 rotate 360
        parallel:
            easein 0.6 alpha 0 zoom 3 additive 0
    show symbol as circ3 zorder 99:
        SP
        TC
        alpha 0.25
        zoom 2.125 xcenter -55 ycenter 390
        additive -0.5
        parallel:
            rotate 0
            linear 5 rotate -360
            repeat
        parallel:
            ease 2 zoom 2.25
            ease 2 zoom 2.125
            repeat
        parallel:
            0.65
            easein 0.1 yoffset -20
            easeout 0.1 yoffset 0
    return
        
label deathcircle3:
    play audio bell
    show symbol as circ zorder 101:
        SP
        TC
        zoom 2 xcenter 500 ycenter 360
        additive -3
        parallel:
            rotate 0
            linear 5 rotate 360
            repeat
        parallel:
            easein_circ 1.5 additive -0.5
    show symbol as circ2 zorder 102:
        SP
        TC
        alpha 1
        zoom 2 xcenter 500 ycenter 360
        additive -1
        parallel:
            rotate 0
            linear 5 rotate 360
        parallel:
            easein 0.6 alpha 0 zoom 3 additive 0
    show symbol as circ3 zorder 99:
        SP
        TC
        alpha 0.25
        zoom 2.125 xcenter 500 ycenter 360
        additive -0.5
        parallel:
            rotate 0
            linear 5 rotate -360
            repeat
        parallel:
            ease 2 zoom 2.25
            ease 2 zoom 2.125
            repeat
    return
    
label deathcircle4:
    hide circ2
    show symbol as circ zorder 101:
        SP
        TC
        zoom 2 xcenter 500 ycenter 360
        additive -0.5
        parallel:
            rotate 0
            linear 5 rotate 360
            repeat
        parallel:
            linear 0.2 xoffset -600
    show symbol as circ3 zorder 99:
        SP
        TC
        alpha 0.25
        zoom 2.125 xcenter 500 ycenter 360
        additive -0.5
        parallel:
            rotate 0
            linear 5 rotate -360
            repeat
        parallel:
            ease 2 zoom 2.25
            ease 2 zoom 2.125
            repeat
        parallel:
            linear 0.2 xoffset -600
    return
    
    
    
# A dark scene using the DeathCircle
# The Third Eye is drawing closer. (Well, not really...)
# OW THE EDGE 
label darkyuri:
    if not config.developer:
        $ allow_skipping = False
        $ config.allow_skipping = False
    $ style.say_dialogue = style.normal
    window hide(None)
    $ renpy.sound.set_volume(1)
    play music t2 fadein 1
    scene bg club_day:
        SP
        zoom 1.5 xcenter 750 ycenter 425
        easein_back 1.5 ycenter 400
    show mc 2a at i11:
        SP
        zoom 1.25 xcenter 400 ycenter 525
        xzoom -1
        easein_back 1.5 ycenter 450
    show sayori 2x at i11:
        SP
        zoom 1.25 xcenter 850 ycenter 525
        easein_back 1.5 ycenter 450
    show black zorder 10:
        alpha 1
        linear 1 alpha 0
    $ pause(0.75)
    s "By the way, [player]. I'm kinda hungry..."
    s "Will you come with me to buy a snack?"
    mc 5e2 "Sorry, but no thanks."
    show sayori 4h at i11:
        SP
        zoom 1.25 xcenter 850 ycenter 450
        easein 0.1 yoffset -20
        easeout 0.1 yoffset 0
    s "Eh??"
    s "T-That's not like you at all!!"
    window hide(None)
    window auto
    stop music fadeout 1
    $ pause(0.15)
    play sound closet_open
    $ pause(0.5)
    show mc 1d2 at i11:
        SP
        zoom 1.25 xcenter 400 ycenter 450
        xzoom -1
        easein 0.1 yoffset -20
        easeout 0.1 yoffset 0
    show sayori 1b at i11:
        SP
        zoom 1.25 xcenter 850 ycenter 450
        easein 0.1 yoffset -20
        easeout 0.1 yoffset 0
    $ pause(0.9)
    scene bg class_day:
        zoom 4.5 xcenter -450 ycenter 100
    show dark onlayer front:
        alpha 0.5
    show vignette onlayer front:
        alpha 0.5
        ease 2 alpha 0.7
        ease 2 alpha 0.5
        repeat
    with dissolve_cg
    show noise onlayer front behind vignette:
        alpha 0
        block:
            ease 1.5 alpha 0.1
            ease 1.5 alpha 0.05
            repeat
    play music lullaby fadein 0.5
    show yuri 1l at i11 behind dark:
        SP
        zoom 2.5 xcenter 2000 ycenter -215
        parallel:
            easein 2 xcenter 640
        parallel:
            easein 2 ycenter -150
    $ pause(1.8)
    play sound step
    $ pause(0.5)
    show yuri 1l at i11 behind dark:
        SP
        zoom 2.5 xcenter 640 ycenter -150
        parallel:
            ease 2 ycenter 800
        parallel:
            1.8
            ease 1 yoffset -10
            ease 1 yoffset 0
    show bg class_day:
        SP
        zoom 4.5 xcenter -450 ycenter 100
        ease 2 ycenter 500
    $ pause(3.25)
    scene bg club_day:
        zoom 1.5 xcenter 750 ycenter 400
    show mc 1d2 at i11:
        zoom 1.25 xcenter 400 ycenter 450
        xzoom -1
    show sayori 1b at i11:
        zoom 1.25 xcenter 850 ycenter 450
    show dark as d1 zorder 110:
        alpha 0.45 zoom 3
        TC
    show vignette onlayer front:
        alpha 0.45
        ease 2 alpha 0.65
        ease 2 alpha 0.45
        repeat
    show noise onlayer front behind vignette:
        alpha 0.05
        ease 1.5 alpha 0.1
        ease 1.5 alpha 0.05
        repeat
    hide dark onlayer front
    with dissolve_cg
    $ pause(0.5)
    show sayori 1b at i11:
        SP
        zoom 1.25 xcenter 850 ycenter 450
        parallel:
            ease 1.5 zoom 1.5 xcenter 825
        parallel:
            0.1
            ease 0.75 ycenter 405
            ease 0.65 ycenter 425
    $ pause(0.5)
    s "...Yuri?"
    s 3c "Can you tell [player] to buy snacks for us?"
    window hide(None)
    scene bg class_day:
        zoom 4.5 xcenter -450 ycenter 500
    show dark onlayer front:
        alpha 0.5
    show vignette onlayer front:
        alpha 0.5
        ease 2 alpha 0.7
        ease 2 alpha 0.5
        repeat
    show noise onlayer front behind vignette:
        alpha 0.05
        ease 1.5 alpha 0.1
        ease 1.5 alpha 0.05
        repeat
    show yuri 1l at i11 behind dark:
        SP
        zoom 2.5 xcenter 640 ycenter 800
        ease 1 yoffset -10
        ease 1 yoffset 0
        parallel:
            easeout 2 xcenter -1000
        parallel:
            ease 1 ycenter 750
    with dissolve_cg
    $ pause(3)
    play sound step
    $ pause(1)
    hide dark onlayer front
    scene bg club_day:
        zoom 1.5 xcenter 750 ycenter 400
    show mc 2d2 at i11:
        zoom 1.25 xcenter 400 ycenter 450
        xzoom -1
    show sayori 1b at i11:
        zoom 1.5 xcenter 825 ycenter 425
    show dark as d1 zorder 110:
        alpha 0.45 zoom 3
        TC
    show vignette onlayer front zorder 2:
        alpha 0.45
        ease 2 alpha 0.65
        ease 2 alpha 0.45
        repeat
    show noise onlayer front zorder 1:
        alpha 0.05
        ease 1.5 alpha 0.1
        ease 1.5 alpha 0.05
        repeat
    with dissolve_cg
    $ pause(0.5)
    show yuri 1l at i11 behind dark:
        SP
        zoom 1.5 xcenter -200 ycenter 425
        xzoom -1
        parallel:
            linear 4 xcenter 1650
        parallel:
            ease 1 yoffset -40
            ease 1 yoffset 0
            repeat 2
    show sayori at i11:
        SP
        zoom 1.5 xcenter 825 ycenter 425
        1
        "sayori 4g"
        zoom 1.2
        parallel:
            linear 0.3 zoom 1 xcenter 850
        parallel:
            easein 0.15 ycenter 400
            easeout 0.15 ycenter 450
    $ pause(1.65)
    play sound step
    $ pause(1.85)
    play sound step
    $ pause(1)
    s "[player]..."
    show sayori 4g at i11:
        SP
        zoom 1.25 xcenter 850 ycenter 450
        dizzy(0.1, 0.03)
    hide yuri
    s "I-Is there something wrong with her...? I'm a bit scared..."
    show sayori 4g at i11:
        SP
        zoom 1.25 xcenter 850 ycenter 450
        easein 1 xoffset 0 yoffset 0
    show mc 2d2 at i11 zorder 1:
        SP
        zoom 1.25 xcenter 400 ycenter 450 xzoom -1
        ease 0.5 xcenter 600
    show mc 2a at i11 as mc1 zorder 1:
        SP
        zoom 1.25 xcenter 400 ycenter 450 xzoom -1
        alpha 0
        ease 0.5 xcenter 600 alpha 1
    mc "Don't worry, Sayori."
    hide mc1
    mc 2a "Nothing is happening to her. I hope."
    mc "It's up to me to save this situation."
    window hide(None)
    show mc 2a at i11 zorder 1:
        SP
        zoom 1.25 xcenter 600 ycenter 450 xzoom -1
        parallel:
            easeout 1.75 xcenter 1500
        parallel:
            ease 0.875 yoffset -40
            ease 0.875 yoffset 0
    with None
    show sayori 4b at i11:
        SP
        zoom 1.25 xcenter 850 ycenter 450
        0.15
        parallel:
            ease 0.4 xcenter 870 zoom 1.1 ycenter 455
        parallel:
            ease 0.2 yoffset -20
            ease 0.2 yoffset 0
    with Dissolve(0.2)
    $ pause(2.25)
    show mc 1d2 at i11:
        SP
        zoom 1.25 xcenter 1650 ycenter 450
        ease 1.5 xoffset -1200
    show bg club_day:
        SP
        zoom 1.5 xcenter 750 ycenter 400
        ease 1.5 xcenter 425
    show sayori at i11:
        SP
        zoom 1.1 xcenter 870 ycenter 455
        ease 1.5 xoffset -1035
    show yuri 1l at i44 zorder 1 behind dark:
        SP
        zoom 1.5 xcenter 2150 ycenter 465 xzoom -1
        parallel:
            ease 1.5 xoffset -1100
        parallel:
            ease 2 yoffset -10
            ease 2 yoffset 0
            repeat
    $ pause(2)
    mc "Yuri, are you feeling alright?"
    show mc 1d at i11:
        SP
        zoom 1.25 xcenter 1650 ycenter 450 xoffset -1200
        parallel:
            ease 0.5 xoffset -1150
    show mc 1t at i11 as mc1 zorder 1 behind yuri:
        SP
        alpha 0
        zoom 1.25 xcenter 1650 ycenter 450 xoffset -1200 xzoom -1
        parallel:
            ease 0.5 xoffset -1150 alpha 1
    mc "I'm worried that you seem a little odd recently."
    show mc 1t
    hide mc1
    show layer master:
        SP
        TC
        xcenter 640 ycenter 360
        ease 6 zoom 2 xcenter -200 ycenter 700
    show bg club_day:
        SP
        zoom 1.5 xcenter 425 ycenter 400
        ease 6 zoom 1 xcenter 775 ycenter 275
    show vignette onlayer front zorder 2:
        ease 6 alpha 0.9
    show dark as d1 zorder 110:
        alpha 0.45 zoom 3 
        TC
        ease 6 alpha 0.75
    mc "Are you listening to me, Yuri?"
    show yuri 1l at i44 zorder 1:
        SP
        zoom 1.5 xcenter 2150 ycenter 465 xzoom -1 xoffset -1100
        ease 1.5 yoffset 0
    mc "You should rest if you feel exhausted or something."
    $ pause(0.85)
    show yuri 1m
    with Dissolve(0.5)
    $ renpy.sound.set_volume(1.75)
    $ pause(1)
    play sound eye
    show layer master:
        SP
        zoom 2 xcenter -200 ycenter 700
        easein_circ 0.85 zoom 2.75 xcenter -550 ycenter 825
    with None
    show yuri 1a
    show eyesymbol zorder 3:
        SP
        zoom 0.15 xcenter 1053 ycenter 170 alpha 0.65
        parallel:
            rotate 0
            linear 1 rotate 360
            repeat
        parallel:
            zoom 0.15
            ease 1 zoom 0.175
            ease 1 zoom 0.15
            repeat
    show eyesymbol zorder 3 as eye1:
        SP
        zoom 0.15 xcenter 1053 ycenter 170 alpha 0
        parallel:
            rotate 0
            linear 1 rotate 360
            repeat
        parallel:
            0.75
            block:
                alpha 0.65 zoom 0.15
                easein_circ 0.75 zoom 0.5 alpha 0
                0.1
                repeat
    show layer master:
        zoom 2 xcenter -200 ycenter 700
    show death_eye zorder 4
    with Dissolve(0.75)
    $ pause(1.1)
    show vignette onlayer front:
        alpha 0.7
        ease 2 alpha 0.65
        ease 2 alpha 0.7
        repeat
    $ renpy.sound.set_volume(1)
    show yuri 1l at i44 zorder 1 behind dark:
        zoom 1.5 xcenter 2150 ycenter 465 xzoom -1 xoffset -400
    show bg club_day:
        zoom 1.15 xcenter 500 ycenter 325
    show layer master:
        topleft
        zoom 1.3
    show sayori at i11:
        zoom 1.1 xcenter 870 ycenter 455 xoffset -1050
    show mc 1h at i11:
        SP
        zoom 1.25 xcenter 1650 ycenter 450 xoffset -1150 xzoom -1
        easein 0.1 yoffset -20
        easeout 0.1 yoffset 0
    hide eye1
    mc "Huh?! I-Is that a glowing eye?"
    window hide(None)
    window auto
    $ renpy.sound.set_volume(1.5)
    show mc 1h at i11:
        SP
        zoom 1.25 xcenter 1650 ycenter 450 xoffset -1150 xzoom -1
        0.6
        "mc 1j"
        zoom 1
        easein 0.1 yoffset -20
        easeout 0.1 yoffset 0
        0.35
        ease 0.2 xzoom 1
        0.2
        ease 0.2 xzoom -1
    call deathcircle from _call_deathcircle
    $ pause(0.6)
    window show(None)
    window auto
    mc "{cps=*1.5}Ah--! W-What's happening to me?!{/cps}"
    window hide(None)
    show layer master:
        SP
        zoom 1.3 xcenter 832 ycenter 467
        ease 0.75 xcenter 1100
    show sayori 4h at i11:
        SP
        zoom 1.1 xcenter 870 ycenter 410 xoffset -1050
        ease 0.75 xoffset -850
    show bg club_day:
        SP
        zoom 1.15 xcenter 500 ycenter 325
        ease 0.75 xcenter 400
    $ pause(0.75)
    hide yuri
    hide eyesymbol
    hide death_eye
    s "[player]...Look around you...!"
    s "W-What kind of magic is this!?"
    $ renpy.sound.set_volume(1)
    s "And why is she doing this--!"
    play sound [ "<silence 0.05>", whoosh2 ]
    show mc 1j at i11 zorder 6:
        SP
        zoom 1.25 xcenter 1650 ycenter 450 xoffset -1150 xzoom -1
        ease 0.2 xzoom 1
    mc "I don't know, Sayori!"
    mc "Something is controlling her soul!"
    $ style.say_dialogue = style.normal
    mc "She lost control to herself!"
    $ renpy.sound.set_volume(1.1)
    play sound timeeffect
    show yuri 1a at i11:
        zoom 1.25 xcenter 750 ycenter 425
    show yuri 1a at i11 as y1 zorder 5 behind mc:
        SP
        zoom 1.25 xcenter 750 ycenter 425 alpha 1
        easein_circ 0.75 zoom 2.25 ycenter 525 alpha 0
    show eyesymbol zorder 3:
        SP
        zoom 0.15 xcenter 665 ycenter 187 alpha 0.65
        parallel:
            rotate 0
            linear 1 rotate 360
            repeat
        parallel:
            zoom 0.15
            ease 1 zoom 0.175
            ease 1 zoom 0.15
            repeat
    show eyesymbol zorder 3 as eye1 behind mc:
        SP
        zoom 0.15 xcenter 665 ycenter 187 alpha 0
        parallel:
            rotate 0
            linear 1 rotate 360
            repeat
        parallel:
            0.75
            block:
                alpha 0.65 zoom 0.15
                easein_circ 0.75 zoom 0.5 alpha 0
                0.1
                repeat
    show death_eye zorder 4:
        xcenter 661 ycenter 181
    $ pause(0.4)
    show mc 1shock at i11 zorder 6:
        SP
        zoom 1.25 xcenter 1650 ycenter 450 xoffset -1150
        easein 0.1 yoffset -20
        easeout 0.1 yoffset 0
    show sayori 4v at i11:
        SP
        zoom 1.1 xcenter 870 ycenter 410 xoffset -850
        easein 0.1 yoffset -20
        easeout 0.1 yoffset 0
    $ pause(0.9)
    show layer master:
        zoom 2 xcenter 750 ycenter 600
    show bg club_day:
        zoom 1 xcenter 450 ycenter 300
    show mc 1shock at i11 zorder 6:
        SP
        zoom 1.25 xcenter 500 ycenter 450 xoffset 0
        dizzy(0.175, 0.01)
    with dissolve_cg
    $ pause(0.35)
    show eyesymbol zorder 3:
        SP
        zoom 0.15 xcenter 665 ycenter 187 alpha 0.65
        parallel:
            rotate 0
            linear 1 rotate 360
        parallel:
            zoom 0.15
            ease 1 zoom 0.175
            ease 1 zoom 0.15
        parallel:
            linear 0.35 alpha 0 xoffset -17
    show eyesymbol zorder 3 as eye1 behind mc:
        SP
        zoom 0.15 xcenter 665 ycenter 187 alpha 0
        parallel:
            rotate 0
            linear 1 rotate 360
        parallel:
            block:
                alpha 0.65 zoom 0.15
                easein_circ 0.75 zoom 0.5 alpha 0
        parallel:
            linear 0.35 alpha 0 xoffset -17
    show death_eye zorder 4:
        SP
        xcenter 661 ycenter 181
        linear 0.35 alpha 0 xoffset -17
    show yuri 1a at i11:
        SP
        zoom 1.25 xcenter 750 ycenter 425
        easein_expo 2.25 xcenter 735
    show yuri 1l at i11 as y1 zorder 2:
        SP
        zoom 1.25 xcenter 750 ycenter 425 alpha 0
        parallel:
            easein_expo 2.25 xcenter 735
        parallel:
            linear 0.35 alpha 1
    $ style.say_dialogue = style.edited
    window show(None)
    y "{cps=15}I can feel it...{/cps}"
    hide y1
    hide eyesymbol
    hide eye1
    hide death_eye
    y 1l "{cps=15}I can feel the fresh {color=#FAA}blood{/color} coursing through my skin.{/cps}"
    y "{cps=15}Do you feel it, [player]?{/cps}"
    $ _history_list.pop()
    show eyesymbol zorder 3:
        SP
        zoom 0.15 xcenter 654 ycenter 188 alpha 0
        parallel:
            linear 0.5 alpha 0.65
        parallel:
            rotate 0
            linear 1 rotate 360
            repeat
        parallel:
            zoom 0.15
            ease 1 zoom 0.175
            ease 1 zoom 0.15
            repeat
    show eyesymbol zorder 3 as eye1 behind mc:
        SP
        zoom 0.15 xcenter 654 ycenter 188 alpha 0
        parallel:
            rotate 0
            linear 1 rotate 360
            repeat
        parallel:
            0.5
            block:
                alpha 0.65 zoom 0.15
                easein_circ 0.75 zoom 0.5 alpha 0
                0.1
                repeat
    show death_eye zorder 4:
        xcenter 650 ycenter 182 alpha 0
        linear 0.5 alpha 1
    show yuri 1y4 as y1 at i11 zorder 2:
        zoom 1.25 xcenter 735 ycenter 425 alpha 0
        linear 0.5 alpha 1
    extend "\"{fast}{cps=15} \"{color=#F77}Do you?{/color}{/cps}"
    hide y1
    show yuri 1y1 at i11 zorder 2:
        SP
        zoom 1.25 xcenter 735 ycenter 425
        linear 0.1 yoffset -10
        easein 0.15 yoffset 0
        0.1
        linear 0.1 yoffset -10
        easein 0.15 yoffset 0
        0.1
        linear 0.1 yoffset -20
        easein 0.5 yoffset 0
    show eyesymbol zorder 3:
        SP
        zoom 0.15 xcenter 654 ycenter 188
        parallel:
            rotate 0
            linear 1 rotate 360
            repeat
        parallel:
            zoom 0.15
            ease 1 zoom 0.175
            ease 1 zoom 0.15
            repeat
        parallel:
            linear 0.1 yoffset -10
            easein 0.15 yoffset 0
            0.1
            linear 0.1 yoffset -10
            easein 0.15 yoffset 0
            0.1
            linear 0.1 yoffset -20
            easein 0.5 yoffset 0
    show eyesymbol zorder 3 as eye1 behind mc:
        SP
        zoom 0.15 xcenter 654 ycenter 188 alpha 0.65
        parallel:
            rotate 0
            linear 1 rotate 360
            repeat
        parallel:
            block:
                alpha 0.65 zoom 0.15
                easein_circ 0.75 zoom 0.5 alpha 0
                0.1
                repeat
        parallel:
            linear 0.1 yoffset -10
            easein 0.15 yoffset 0
            0.1
            linear 0.1 yoffset -10
            easein 0.15 yoffset 0
            0.1
            linear 0.1 yoffset -20
            easein 0.5 yoffset 0
    show death_eye zorder 4:
        SP
        xcenter 650 ycenter 182
        parallel:
            linear 0.1 yoffset -10
            easein 0.15 yoffset 0
            0.1
            linear 0.1 yoffset -10
            easein 0.15 yoffset 0
            0.1
            linear 0.1 yoffset -20
            easein 0.5 yoffset 0
    $ style.say_dialogue = style.edited
    y "{cps=15}Ha{w=0.075} ha{w=0.055} ha.{/cps}"
    window hide(None)
    show layer master:
        SP
        zoom 2 xcenter 750 ycenter 600
        ease 0.75 zoom 2.5 xcenter 1000 ycenter 700
    show bg club_day:
        SP
        zoom 1 xcenter 450 ycenter 300
        ease 0.75 zoom 0.9 xcenter 415 ycenter 290
    $ pause(1)
    $ style.say_dialogue = style.normal
    mc "Help...{w=0.2}Me...{w=0.2}Sayori..."
    window hide(None)
    show sayori 1g
    show layer master:
        SP
        zoom 2.5 xcenter 1000 ycenter 700
        ease 0.45 zoom 1.75 xcenter 1750 ycenter 450
    show bg club_day:
        SP
        zoom 0.9 xcenter 415 ycenter 290
        ease 0.45 zoom 1.15 xcenter 250 ycenter 325
    $ pause(0.5)
    show sayori 4v at i11:
        SP
        zoom 1.1 xcenter 870 ycenter 410 xoffset -850
        easein 0.1 yoffset -20
        easeout 0.1 yoffset 0
    s "Ah--"
    show sayori at i11:
        SP
        zoom 1.1 xcenter 20 ycenter 410
        dizzy(0.25, 0.02)
    s "Ummm...!"
    show natsuki 4c at i11 behind sayori:
        SP
        zoom 1.1 xcenter -600 ycenter 410
        easein_expo 0.5 xcenter -200
    show sayori at i11:
        SP
        zoom 1.1 xcenter 20 ycenter 410 xoffset -2.5 yoffset -1.25
        easein_elastic 1.5 xoffset 0 yoffset 0
    n "Hey, what's going on here?"
    show natsuki 1k at i11 behind sayori:
        SP
        zoom 1.1 xcenter -200 ycenter 410
        easein 0.1 yoffset -20
        easeout 0.1 yoffset 0
    n "Oh-- [player] and Yuri?"
    n 1m "With this d-dark magic?"
    show natsuki at i11 behind sayori:
        SP
        zoom 1.1 xcenter -200 ycenter 410
        parallel:
            ease 0.5 zoom 0.85 xcenter -220 ycenter 385
        parallel:
            ease 0.25 yoffset -10
            ease 0.25 yoffset 0
    n "W-What the heck is going on?!"
    show natsuki at i11 behind sayori:
        SP
        zoom 0.85 xcenter -220 ycenter 385
        easein_elastic 1.25 zoom 0.8 xcenter -208 ycenter 375
    show layer master:
        SP
        zoom 1.75 xcenter 1750 ycenter 450
        easein_elastic 1.25 zoom 2 xcenter 1910 ycenter 525
    show bg club_day:
        SP
        zoom 1.15 xcenter 250 ycenter 325
        easein_elastic 1.25 zoom 1.075 xcenter 235 ycenter 315
    s 4h "Natsuki! Yuri has been acting really weird!"
    s "She got psychic powers for no reason!"
    s "You gotta help [player] before she releases her super destruction!"
    s "Please, do something Natsuki!"
    show natsuki 1n at i11 behind sayori:
        SP
        zoom 0.8 xcenter -208 ycenter 375
        ease 1 zoom 0.85 xcenter -220 ycenter 385
    show layer master:
        SP
        zoom 2 xcenter 1910 ycenter 525
        ease 1 zoom 1.75 xcenter 1750 ycenter 450
    show bg club_day:
        SP
        zoom 1.075 xcenter 235 ycenter 315
        ease 1 zoom 1.15 xcenter 250 ycenter 325
    n "Umm.."
    show natsuki at i11 behind sayori:
        SP
        zoom 0.85 xcenter -220 ycenter 385
        ease 0.5 xcenter 20 xzoom -1 zoom 1.1
    show sayori 4g at i11:
        SP
        zoom 1.1 xcenter 20 ycenter 410
        0.15
        easein_elastic 1.25 xcenter -200
    n "A-Alright..."
    window hide(None)
    show yuri 1y3
    with None
    show layer master:
        zoom 2 xcenter 750 ycenter 600
    show bg club_day:
        zoom 1 xcenter 450 ycenter 300
    with dissolve_cg
    $ pause(0.9)
    n "Hey, Yuri!"
    window hide(None)
    show yuri 1y7 at i11 zorder 2:
        SP
        zoom 1.25 xcenter 735 ycenter 425
        easein 0.1 yoffset -20
        easeout 0.1 yoffset 0
    show eyesymbol zorder 3:
        SP
        zoom 0.15 xcenter 654 ycenter 188
        parallel:
            rotate 0
            linear 1 rotate 360
            repeat
        parallel:
            zoom 0.15
            ease 1 zoom 0.175
            ease 1 zoom 0.15
            repeat
        parallel:
            easein 0.1 yoffset -20
            easeout 0.1 yoffset 0
    show eyesymbol zorder 3 as eye1 behind mc:
        SP
        zoom 0.15 xcenter 654 ycenter 188 alpha 0.65
        parallel:
            rotate 0
            linear 1 rotate 360
            repeat
        parallel:
            block:
                alpha 0.65 zoom 0.15
                easein_circ 0.75 zoom 0.5 alpha 0
                0.1
                repeat
        parallel:
            easein 0.1 yoffset -20
            easeout 0.1 yoffset 0
    show death_eye zorder 4:
        SP
        xcenter 650 ycenter 182
        parallel:
            easein 0.1 yoffset -20
            easeout 0.1 yoffset 0
    $ pause(0.6)
    hide sayori
    show natsuki 5g at i11:
        xcenter -40 ycenter 385 xzoom -1 zoom 1.1
    show layer master:
        SP
        zoom 2 xcenter 750 ycenter 600
        ease 1 zoom 1.5 xcenter 1700 ycenter 400
    show bg club_day:
        SP
        zoom 1 xcenter 450 ycenter 300
        ease 1 zoom 1.15 xcenter 240 ycenter 300
    $ pause(1.2)
    n "Leave [player] alone!"
    $ renpy.sound.set_volume(1.5)
    n "Or else I'll--!"
    window hide(None)
    call deathcircle2 from _call_deathcircle2
    show natsuki 5g at i11:
        SP
        xcenter -40 ycenter 385 xzoom -1 zoom 1.1
        0.65
        "natsuki 1f"
        zoom 0.88
        easein 0.1 yoffset -20
        easeout 0.1 yoffset 0
    $ pause(0.6)
    n "--!!"
    n 1s "Umm..."
    n 1u "..."
    n 1n "S-Sorry there Yuri...I wasn't shouting! Please don't hurt me..."
    hide eye1
    window hide(None)
    show layer master:
        SP
        zoom 1.5 xcenter 1700 ycenter 400
        ease 0.5 zoom 2.5 xcenter 500 ycenter 750
    show bg club_day:
        SP
        zoom 1.15 xcenter 240 ycenter 300
        ease 0.5 zoom 0.95 xcenter 510 ycenter 290
    show eyesymbol zorder 3:
        SP
        zoom 0.15 xcenter 654 ycenter 188
        rotate 0
        easeout 0.8 rotate 360
        rotate 0
        easein 1 rotate 405
    $ renpy.sound.set_volume(1)
    $ pause(2.15)
    show eyesymbol zorder 3:
        SP
        zoom 0.15 xcenter 654 ycenter 188 rotate 405 additive -0.5
        easein_circ 2.75 zoom 0.225 additive 0
    show symbol zorder 3 behind eyesymbol as eye2:
        SP
        zoom 0.15 xcenter 654 ycenter 188 alpha 1 additive -1
        easein_circ 2.75 zoom 0.225 rotate 45
    show symbol zorder 3 behind mc as eye3:
        SP
        zoom 0.15 xcenter 654 ycenter 188 alpha 0.65
        easein_circ 2.75 zoom 0.55 alpha 0.05 rotate 45
    show eyesymbol zorder 3 as eye1 behind mc:
        SP
        zoom 0.15 xcenter 654 ycenter 188 rotate 45
        alpha 0.65
        easein_circ 2.75 zoom 0.55 alpha 0.2
    play sound bell2
    show yuri 1y7 at i11 as y1 zorder 1 behind mc:
        SP
        zoom 1.25 xcenter 735 ycenter 425 alpha 1
        easein_circ 1.5 zoom 2.25 xcenter 745 ycenter 575 alpha 0.25 additive 1
    show red zorder 9:
        alpha 0 additive 1
        easein_expo 0.75 alpha 0.35
        ease 1.25 alpha 0.3
    show layer master:
        SP
        zoom 2.5 xcenter 500 ycenter 750
        easein_circ 1.5 zoom 2.25 xcenter 525 ycenter 715
    show vignette onlayer front zorder 2:
        easein_expo 0.75 alpha 1 additive -0.1
        block:
            ease 2 alpha 0.45 additive 0
            ease 2 alpha 0.65
            repeat
    show bg club_day:
        SP
        zoom 0.95 xcenter 510 ycenter 290
        easein_circ 1.5 zoom 0.75 xcenter 550 ycenter 275
    $ pause(1.5)
    hide eye2
    hide eye3
    hide eyesymbol
    hide eye1
    hide death_eye
    hide y1
    hide red
    show layer master:
        zoom 1.5 xcenter 1700 ycenter 400
    show bg club_day:
        zoom 1.15 xcenter 240 ycenter 300
    show natsuki 1o at i11:
        SP
        xcenter -40 ycenter 385 xzoom -1 zoom 1.1
        easein 0.1 yoffset -20
        easeout 0.1 yoffset 0
    n "GHK--!"
    show natsuki 1o at i11:
        SP
        xcenter -40 ycenter 385 xzoom -1 zoom 1.1
        xoffset -10 yoffset -5
        parallel:
            easein_elastic 0.5 xoffset 0
        parallel:
            0.1
            easein_elastic 0.5 yoffset 0
    show layer master:
        SP
        zoom 1.75 xcenter 1875 ycenter 400
        easein_circ 0.5 zoom 1.5 xcenter 1700 ycenter 400  
    show bg club_day:
        SP
        zoom 1.05 xcenter 210 ycenter 305
        easein_circ 0.5 zoom 1.15 xcenter 240 ycenter 300
    n "UGHK--!"
    show layer master:
        zoom 1.5 xcenter 1700 ycenter 400
        dizzy(0.75, 0.01)
    show natsuki 1p at i11:
        SP
        xcenter -40 ycenter 385 xzoom -1 zoom 1.1
        dizzy(1.5, 0.01)
    n "AAAAAAAAAAAAAAAHHHH!!!"
    $ renpy.sound.set_volume(1)
    window hide(None)
    show white onlayer front zorder 10:
        alpha 0
        easeout 0.25 alpha 1
    $ pause(0.375)
    show white onlayer front zorder 10:
        alpha 1
        easein_circ 1 alpha 0
    call hidefront from _call_hidefront
    show layer master
    hide circ
    hide circ2
    hide circ3
    show white zorder 10:
        TC
        zoom 1.25
    show n_up at i11 zorder 11:
        zoom 1 ycenter 371
    show n_down at i11 zorder 11
    $ pause(0.75) #                      R.I.P Ratsuki
    play sound slice
    show layer master:
        SP
        TC
        0.075
        linear 0.01 xoffset -10 yoffset 10
        easein_elastic 1.35 xoffset 0 yoffset 0
    show red zorder 12:
        SP
        xcenter 1200 ycenter -90 zoom 0.05 rotate -45
        parallel:
            linear 0.1 xzoom 50
        parallel:
            easeout 0.5 yzoom 0
    $ pause(1.15)
    hide red
    show n_up at i11 zorder 11:
        zoom 1 ycenter 371
        dizzy(0.35, 0.01)
    show n_down at i11 zorder 11:
        zoom 1
        dizzy(0.35, 0.01)
    $ pause(0.9)
    play sound release
    show n_up at i11 zorder 11:
        SP
        zoom 1 ycenter 371 xcenter 640 xoffset 0 yoffset 0 rotate 0
        easein_circ 2 rotate -15 xcenter 570 ycenter 320
    show n_down at i11 zorder 11:
        SP
        zoom 1 xcenter 640 ycenter 557 xoffset 0 yoffset 0 rotate 0
        easein_circ 2 rotate 10 xcenter 675 ycenter 585
    $ pause(0.9)
    show white onlayer front zorder 10:
        alpha 0
        easeout 0.75 alpha 1
    $ pause(0.85)
    show white onlayer front zorder 10:
        alpha 1
        easein_circ 1 alpha 0
    hide white
    hide n_up
    hide n_down
    call showfront from _call_showfront
    show layer master:
        zoom 2 xcenter 2100 ycenter 550
        dizzy(0.5, 0.01)
    show sayori 4w at i11:
        zoom 1.1 xcenter -100 ycenter 385
        dizzy(0.75, 0.01)
    hide natsuki
    $ delete_character("natsuki")
    s "NOOOOOOOOOOOOOOOO!!!"
    show layer master:
        zoom 2.5 xcenter 1050 ycenter 700 xoffset 0 yoffset 0
    show bg club_day:
        zoom 1 xcenter 400 ycenter 300
    show mc 1shock at i11 zorder 6:
        SP
        zoom 1.25 xcenter 500 ycenter 450 xoffset 0
        parallel:
            dizzy(0.175, 0.01)
        parallel:
            easein 0.1 ycenter 430
            easeout 0.1 ycenter 450
    show yuri 1m
    $ style.say_dialogue = style.normal
    mc "NATSUKI!!!"
    hide sayori
    $ renpy.sound.set_volume(1.5)
    $ style.say_dialogue = style.edited
    window hide(None)
    show layer master:
        SP
        zoom 2.5 xcenter 1050 ycenter 700
        ease 1 zoom 2 xcenter 750 ycenter 600
    show bg club_day:
        SP
        zoom 1 xcenter 400 ycenter 300
        ease 1 xcenter 440 ycenter 315 zoom 1.15
    $ pause(1)
    y "{cps=15}Finally.{/cps}"
    call deathcircle3 from _call_deathcircle3_1
    $ pause(0.75)
    show eyesymbol zorder 3:
        SP
        zoom 0.15 xcenter 651 ycenter 189 alpha 0
        parallel:
            linear 0.5 alpha 0.65
        parallel:
            rotate 0
            linear 1 rotate 360
            repeat
        parallel:
            zoom 0.15
            ease 1 zoom 0.175
            ease 1 zoom 0.15
            repeat
    show eyesymbol zorder 3 as eye1 behind mc:
        SP
        zoom 0.15 xcenter 651 ycenter 189 alpha 0
        parallel:
            rotate 0
            linear 1 rotate 360
            repeat
        parallel:
            0.5
            block:
                alpha 0.65 zoom 0.15
                easein_circ 0.75 zoom 0.5 alpha 0
                0.1
                repeat
    show death_eye zorder 4:
        xcenter 646 ycenter 181 alpha 0
        linear 0.5 alpha 1
    show yuri 1s as y1 at i11 zorder 2:
        zoom 1.25 xcenter 735 ycenter 425 alpha 0
        linear 0.5 alpha 1
    y "{cps=15}This is really all I wanted.{/cps}"
    hide y1
    $ style.say_dialogue = style.edited
    y 1s "{cps=15}The whole day, with just the two of us...{/cps}"
    show eyesymbol zorder 3:
        SP
        zoom 0.15 xcenter 654 ycenter 188 alpha 0.65
        parallel:
            rotate 0
            linear 1 rotate 360
            repeat
        parallel:
            zoom 0.15
            ease 1 zoom 0.175
            ease 1 zoom 0.15
            repeat
        parallel:
            dizzy(0.075, 0.015)
    show eyesymbol zorder 3 as eye1 behind mc:
        SP
        zoom 0.15 xcenter 654 ycenter 188
        parallel:
            rotate 0
            linear 1 rotate 360
            repeat
        parallel:
            block:
                alpha 0.65 zoom 0.15
                easein_circ 0.75 zoom 0.5 alpha 0
                0.1
                repeat
        parallel:
            dizzy(0.075, 0.015)
    show death_eye zorder 4:
        xcenter 650 ycenter 182
        dizzy(0.075, 0.015)
    show layer master:
        SP
        zoom 2 xcenter 750 ycenter 600 xoffset -20 yoffset 10
        parallel:
            easein_back 0.25 zoom 2.5 xcenter 700 ycenter 700
        parallel:
            easein_elastic 0.5 xoffset 0
        parallel:
            0.1
            easein_elastic 0.5 yoffset 0
    show bg club_day:
        SP
        zoom 1.15 xcenter 440 ycenter 315
        easein_back 0.25 zoom 1.0 xcenter 470 ycenter 300
    show layer screens:
        SP
        xcenter 640 ycenter 360
        xoffset -13 yoffset 10 rotate 1
        parallel:
            easein_elastic 0.75 xoffset 0
        parallel:
            0.1
            easein_elastic 0.75 yoffset 0
        parallel:
            easein_elastic 0.85 rotate 0
    show yuri 1y3 at i11 zorder 2:
        zoom 1.25 xcenter 735 ycenter 425
        dizzy(0.075, 0.015)
    y "Let's destroy everything in this wretched world.\"{fast}{space=5000}{w=2}"
    show layer master:
        SP
        zoom 2.5 xcenter 700 ycenter 700 xoffset -20 yoffset 10
        parallel:
            easein_back 0.25 zoom 3 xcenter 650 ycenter 800 
        parallel:
            easein_elastic 0.5 xoffset 0
        parallel:
            0.1
            easein_elastic 0.5 yoffset 0
    show bg club_day:
        SP
        zoom 1.0 xcenter 470 ycenter 300
        easein_back 0.25 zoom 0.85 xcenter 500 ycenter 285
    show layer screens:
        SP
        xcenter 640 ycenter 360
        xoffset -13 yoffset 10 rotate 1
        parallel:
            easein_elastic 0.75 xoffset 0
        parallel:
            0.1
            easein_elastic 0.75 yoffset 0
        parallel:
            easein_elastic 0.85 rotate 0
    show yuri stab_2 at i11 zorder 2:
        zoom 1.25 xcenter 735 ycenter 425
        dizzy(0.175, 0.015)
    show eyesymbol zorder 3:
        SP
        zoom 0.15 xcenter 654 ycenter 188 alpha 0.65
        parallel:
            rotate 0
            linear 1 rotate 360
            repeat
        parallel:
            zoom 0.15
            ease 1 zoom 0.175
            ease 1 zoom 0.15
            repeat
        parallel:
            dizzy(0.175, 0.015)
    show eyesymbol zorder 3 as eye1 behind mc:
        SP
        zoom 0.15 xcenter 654 ycenter 188
        parallel:
            rotate 0
            linear 1 rotate 360
            repeat
        parallel:
            block:
                alpha 0.65 zoom 0.15
                easein_circ 0.75 zoom 0.5 alpha 0
                0.1
                repeat
        parallel:
            dizzy(0.175, 0.015)
    show death_eye zorder 4:
        xcenter 650 ycenter 182
        dizzy(0.175, 0.015)
    y "{color=#FAA}AND CREATE OUR NEW ATMOSPHERE WITH YOU AND ME BEYOND THE GLEAMING CRIMSON TWILIGHT.{/color}\"{fast}{space=5000}{w=2}"
    window hide(None)
    show layer master:
        SP
        zoom 3 xcenter 650 ycenter 800 
        ease 0.5 zoom 2 xcenter 600 ycenter 600
    show bg club_day:
        SP
        zoom 0.85 xcenter 500 ycenter 285
        ease 0.5 zoom 1.15 xcenter 460 ycenter 315
    show yuri stab_2 at i11 zorder 2:
        zoom 1.25 xcenter 735 ycenter 425 xoffset 0 yoffset 0
    show yuri ghost_base at i11 as y1 zorder 2:
        zoom 1.25 xcenter 735 ycenter 425 alpha 0
        ease 0.5 alpha 1
    show eyesymbol zorder 3:
        SP
        zoom 0.15 xcenter 654 ycenter 188 alpha 0.65 xoffset 0 yoffset 0
        parallel:
            ease 0.5 alpha 0
        parallel:
            rotate 0
            linear 1 rotate 360
            repeat
        parallel:
            zoom 0.15
            ease 1 zoom 0.175
            ease 1 zoom 0.15
            repeat
    show eyesymbol zorder 3 as eye1 behind mc:
        SP
        zoom 0.15 xcenter 654 ycenter 188 alpha 0.65 xoffset 0 yoffset 0
        parallel:
            rotate 0
            linear 1 rotate 360
        parallel:
            block:
                zoom 0.15
                easein_circ 0.75 zoom 0.5
        parallel:
            easein_circ 0.5 alpha 0
    show death_eye zorder 4:
        xcenter 650 ycenter 182 alpha 1 xoffset 0 yoffset 0
        ease 0.5 alpha 0
    stop music fadeout 2
    $ pause(0.8)
    $ renpy.sound.set_volume(1)
    play sound [ "<silence 1.25>", charge ] 
    show yuri ghost_base
    hide yuri as y1
    hide eyesymbol
    hide eye1
    hide death_eye
    show oneeye zorder 2:
        SP
        xcenter 690 ycenter 215 yzoom 0
        parallel:
            ease_quart 0.4 yzoom 1
            0.25
            ease 0.1 yzoom -0.05
            ease 0.1 yzoom 1
            1.6
            easeout 0.3 yzoom 0
            0.3
            easeout 0.1 yzoom 1.3 ycenter 218
    show symbol as eye1 zorder 3:
        SP
        zoom 0.5 xcenter 690 ycenter 205 alpha 0 additive -1
        1.25
        alpha 1
        parallel:
            rotate 0
            linear 0.5 rotate 360
            repeat 2
        parallel:
            zoom 0.65
            linear 0.3 zoom 0.1
            repeat 2
        parallel:
            0.6
            alpha 0
    show symbol as eye2 zorder 3:
        SP
        zoom 0.5 xcenter 690 ycenter 205 alpha 0 additive -1
        1.35
        alpha 1
        parallel:
            rotate 0
            linear 0.5 rotate 360
            repeat 2
        parallel:
            zoom 0.65
            linear 0.3 zoom 0.1
            repeat 2
        parallel:
            0.6
            alpha 0
    show symbol as eye3 zorder 3:
        SP
        zoom 0.5 xcenter 690 ycenter 205 alpha 0 additive -1
        1.45
        alpha 1
        parallel:
            rotate 0
            linear 0.5 rotate 360
            repeat 2
        parallel:
            zoom 0.65
            linear 0.3 zoom 0.1
            repeat 2
        parallel:
            0.6
            alpha 0
    show yuri ghost_base at i11 as y1:
        SP
        zoom 3 xcenter 765 ycenter 760 alpha 0
        1.25
        parallel:
            linear 0.75 alpha 0.75
            alpha 0
        parallel:
            easeout_quart 0.75 zoom 1.25 xcenter 735 ycenter 425 
    $ pause(3.1)
    hide eye1
    hide eye2
    hide eye3
    hide y1
    show oneeye zorder 2:
        SP
        xcenter 690 ycenter 218 yzoom 1.3
        dizzy(2, 0.01)
    show white onlayer front zorder 3:
        alpha 1
        linear 0.25 alpha 0
    show red onlayer front:
        alpha 0.35 additive 1
    show dark as d1 zorder 110:
        zoom 3 alpha 0.9
        TC
    show layer master:
        zoom 2 xcenter 600 ycenter 600
        dizzy(5, 0.01)
    show bg club_day:
        SP
        zoom 1.15 xcenter 460 ycenter 315
        dizzy(-1.25, 0.01)
    show bg club_day_blur as bl behind yuri:
        zoom 1.15 xcenter 460 ycenter 315 alpha 0.25 additive -0.25
        parallel:
            dizzy(-1.25, 0.01)
        parallel:
            ease 1 alpha 0.5
            ease 1 alpha 0.25
            repeat
    show eyesymbol zorder 3:
        SP
        zoom 0.15 xcenter 690 ycenter 205 alpha 0.65
        parallel:
            rotate 0
            linear 0.75 rotate 360
            repeat
        parallel:
            ease 0.35 additive -0.5
            ease 0.35 additive 0
            repeat
        parallel:
            dizzy(2, 0.01)
        parallel:
            zoom 0.15
            linear 0.35 zoom 0.65
            repeat
    show eyesymbol as eye1:
        SP
        zoom 1 xcenter 690 ycenter 205 alpha 0.35
        parallel:
            rotate 0 zoom 0
            linear 0.75 rotate 360 zoom 4
            repeat
        parallel:
            ease 0.35 additive -0.5
            ease 0.35 additive 0
            repeat
        parallel:
            dizzy(2.5, 0.01)
    show eyesymbol as eye2:
        SP
        zoom 1 xcenter 690 ycenter 205 alpha 0.35
        0.375
        parallel:
            rotate 0 zoom 0
            linear 0.75 rotate 360 zoom 4
            repeat
        parallel:
            ease 0.35 additive -0.5
            ease 0.35 additive 0
            repeat
        parallel:
            dizzy(2.5, 0.01)
    show yuri ghost_base at i11 zorder 2:
        zoom 1.25 xcenter 735 ycenter 425
        dizzy(2, 0.01)
    show mc 1shock at i11 zorder 6:
        SP
        zoom 1.25 xcenter 500 ycenter 450 xoffset 0 yoffset 0
        parallel:
            linear 0.15 xcenter 100 rotate -20
    call deathcircle4 from _call_deathcircle4
    show vignette onlayer front zorder 2:
        alpha 0.65
        block:
            ease 0.5 alpha 0.85
            ease 0.5 alpha 0.65
            repeat
    show noise onlayer front zorder 1:
        alpha 0.05
        block:
            ease 0.25 alpha 0.2
            ease 0.5 alpha 0.1
            ease 1 alpha 0.125
            ease 0.25 alpha 0.1
            repeat
    show dark behind yuri:
        alpha 0.3 zoom 10 xcenter 640
    play music loud
    $ pause(0.35)
    hide white onlayer front
    hide circ
    hide circ3
    hide mc
    $ pause(0.25)
    show layer front
    with RUBBER
    $ pause(0.75)
    show layer master:
        zoom 1.5 xcenter 1450 ycenter 400
        dizzy(2, 0.01)
    show layer screens:
        dizzy(0.25, 0.01)
    show bg club_day:
        zoom 1.125 xcenter 340 ycenter 340
        dizzy(-0.7, 0.01)
    show bg club_day_blur as bl behind yuri:
        zoom 1.125 xcenter 340 ycenter 340 alpha 0.25 additive -0.25
        parallel:
            dizzy(-0.7, 0.01)
        parallel:
            ease 1 alpha 0.5
            ease 1 alpha 0.25
            repeat
    show sayori 4w at i11:
        xcenter -75 ycenter 380 zoom 0.65
        dizzy(-0.45, 0.01)
    show mc 3shock at i11:
        SP
        zoom 1 xcenter -100 ycenter 750 rotate -90
        0.5
        easein 0.5 xcenter 100 ycenter 425 rotate 0
    $ style.say_dialogue = style.normal
    $ pause(0.75)
    $ renpy.sound.set_volume(1.25)
    show layer front
    with RUBBER
    s "OH MY GOD!!!"
    window hide(None)
    play sound bang
    show noise onlayer front zorder 1:
        alpha 0.75
        block:
            ease 0.25 alpha 0.2
            ease 0.5 alpha 0.1
            ease 1 alpha 0.125
            ease 0.25 alpha 0.1
            repeat
    show white onlayer front zorder 10:
        alpha 0.6
        linear 0.25 alpha 0
    $ pause(0.55)
    play sound bang2
    show noise onlayer front zorder 1:
        alpha 0.75
        block:
            ease 0.25 alpha 0.2
            ease 0.5 alpha 0.1
            ease 1 alpha 0.125
            ease 0.25 alpha 0.1
            repeat
    show white onlayer front zorder 10:
        alpha 0.6
        linear 0.25 alpha 0
    with None
    show layer front
    with RUBBER
    show monika 1d at i11:
        SP
        zoom 1 xcenter -750 ycenter 425
        easein_circ 0.5 xcenter -150
    m "[player]? Did something happen just now?"
    hide white onlayer front
    show monika 1d at i11:
        SP
        zoom 1 xcenter -150 ycenter 425
        easein 0.1 yoffset -30
        easeout 0.1 yoffset 0
    m "Ah..."
    show layer master:
        zoom 1.5 xcenter 1450 ycenter 400
        dizzy(2, 0.01)
    show bg club_day:
        zoom 1.125 xcenter 340 ycenter 340
        dizzy(-0.7, 0.01)
    show bg club_day_blur as bl behind yuri:
        zoom 1.125 xcenter 340 ycenter 340 alpha 0.25 additive -0.25
        parallel:
            dizzy(-0.7, 0.01)
        parallel:
            ease 1 alpha 0.5
            ease 1 alpha 0.25
            repeat
    show sayori 4w at i11:
        xcenter -75 ycenter 380 zoom 0.65
        dizzy(-0.45, 0.01)
    show mc 3shock at i11:
        SP
        zoom 1 xcenter 100 ycenter 425
        parallel:
            dizzy(-0.45, 0.01)
        parallel:
            0.1
            ease 0.4 zoom 0.65 xcenter 260
        parallel:
            0.1
            ease 0.2 ycenter 350
            ease 0.2 ycenter 380
    show monika 1h at i11:
        SP
        zoom 1 xcenter -150 ycenter 425
        ease_quart 0.5 xcenter 100
    m "Stand back, [player]. I got this."
    window hide(None)
    $ consolehistory = []
    call updateconsolefront("os.remove(\"characters/yuri.chr\")", "yuri.chr deleted successfully.") from _call_updateconsolefront
    $ delete_character("yuri")
    $ pause(0.25)
    call hideconsolefront from _call_hideconsolefront
    show layer master:
        zoom 2 xcenter 600 ycenter 600
        dizzy(5, 0.01)
    show bg club_day:
        SP
        zoom 1.15 xcenter 460 ycenter 315
        dizzy(-1.25, 0.01)
    show bg club_day_blur as bl behind yuri:
        zoom 1.15 xcenter 460 ycenter 315 alpha 0.25 additive -0.25
        parallel:
            dizzy(-1.25, 0.01)
        parallel:
            ease 1 alpha 0.5
            ease 1 alpha 0.25
            repeat
    $ pause(0.25)
    show layer front
    with RUBBER
    $ pause(0.425)
    show layer screens
    hide yuri
    hide eyesymbol
    hide eye1
    hide eye2
    hide oneeye
    hide dark
    hide red onlayer front
    hide bl
    call hidefront from _call_hidefront_1
    $ renpy.sound.set_volume(1)
    play sound "<from 0.9>mod_assets/sfx/squeak.ogg"
    show mc 1shock at i11:
        zoom 0.65 xcenter 260 ycenter 380 xoffset 0 yoffset 0
    show layer master:
        zoom 2 xcenter 600 ycenter 600 xoffset 0 yoffset 0
    show bg club_day:
        zoom 1.15 xcenter 460 ycenter 315 xoffset 0 yoffset 0
    show sayori 4m at i11:
        xcenter -75 ycenter 380 zoom 0.65 xoffset 0 yoffset 0
    play music t8
    show monika 2a
    $ pause(1.5)
    show layer master:
        zoom 1.5 xcenter 1450 ycenter 400
    show bg club_day:
        zoom 1.125 xcenter 340 ycenter 340
    with dissolve_cg
    m "There we go!"
    show monika 2a at i11:
        SP
        zoom 1 xcenter 100 ycenter 425
        ease 0.5 xcenter 525
    show monika 2m at i11 as m1:
        SP
        zoom 1 xcenter 100 ycenter 425 alpha 0
        ease 0.5 xcenter 525 alpha 1
    show layer master:
        SP
        zoom 1.5 xcenter 1450 ycenter 400
        ease 0.5 xcenter 1150
    show bg club_day:
        SP
        zoom 1.125 xcenter 340 ycenter 340
        ease 0.5 xcenter 480
    show sayori 4m at i11:
        SP
        zoom 0.65 xcenter -75 ycenter 380
        ease 0.5 xcenter -10
    show mc 1shock at i11:
        SP
        zoom 0.65 xcenter 260 ycenter 380
        ease 0.5 xcenter 350
    show mc 1h at i11 as mc1 behind monika:
        SP
        zoom 0.65 xcenter 260 ycenter 380 alpha 0
        parallel:
            ease 0.5 xcenter 350
        parallel:
            0.25
            alpha 1
    m "Sorry about that... Ahaha..."
    hide m1
    hide mc1
    show mc 1h at i11:
        SP
        zoom 0.65 xcenter 350 ycenter 380
        easein_circ 1 zoom 0.55 xcenter 390 ycenter 360
    show sayori 4m at i11:
        SP
        zoom 0.65 xcenter -10 ycenter 380
        easein_circ 1 zoom 0.55 xcenter 95 ycenter 360
    show bg club_day:
        SP
        zoom 1.125 xcenter 480 ycenter 340
        easein_circ 1 zoom 0.925 xcenter 505 ycenter 327
    show monika 2n at i11:
        SP
        zoom 1 xcenter 525 ycenter 425
        easein_circ 1 zoom 1 xcenter 525 ycenter 415
    show layer master:
        SP
        zoom 1.5 xcenter 1150 ycenter 400
        easein_circ 1 zoom 2 xcenter 1150 ycenter 450
    m "You know...I was checking through the mod assets to test out new features."
    m "It's quite a few of them. Some of which are related to a friendly skeleton."
    m 2p "So, I keep searching on and I discovered an unused feature that is leftover for months."
    m "It's a well scripted feature, but I might not know what it'll eventually do."
    m "{cps=*0.5}I...{/cps}{w=0.5}accidentally implemented it to Yuri."
    m "Causes her to have supernatural powers that are even worse than amplifying her obsessiveness."
    m 2g "So...I'm really sorry if she hurts one of your club members."
    mc "Umm..."
    show mc 1h at i11:
        SP
        zoom 0.55 xcenter 390 ycenter 360
        parallel:
            ease 0.35 yoffset -10
            ease 0.35 yoffset 0
        parallel:
            ease 0.7 zoom 0.65 xcenter 370 ycenter 370
    mc "What are you talking about, Monika?"
    show layer master:
        SP
        zoom 2 xcenter 1150 ycenter 450
        easein_elastic 1 zoom 2.25 xcenter 1100 ycenter 515
    show monika 2l at i11:
        SP
        zoom 1 xcenter 525 ycenter 415
        easein_elastic 1 zoom 1.15 xcenter 510 ycenter 445
    show bg club_day:
        SP
        zoom 0.925 xcenter 505 ycenter 327
        easein_elastic 1 zoom 0.9 xcenter 520 ycenter 315
    m "Ahaha! Never mind, It's was nothing really..."
    show monika 2b
    m "Anyways, that's how I lost my {i}presidential license{/i}." # ...ARCHIMEDIES! NO!!
    show monika 2a
    m "So please stay back, while I'm going to bring them back, okay?"
    show layer master:
        SP
        zoom 2.25 xcenter 1100 ycenter 515
        ease 1.5 zoom 2 xcenter 1000 ycenter 475
        2
        ease 2 xcenter 250
    show monika 2a at i11:
        SP
        zoom 1.15 xcenter 510 ycenter 445
        ease 1.5 zoom 1.025 xcenter 485 ycenter 420
        2
        ease 2 xcenter 295
    show bg club_day:
        SP
        zoom 0.9 xcenter 520 ycenter 315
        ease 1.5 zoom 0.925 xcenter 530 ycenter 317
        2
        ease 2 xcenter 650
    show natsuki 1c at i11:
        SP
        zoom 0 ycenter 340 xcenter 725
        4.5
        easein_elastic 0.75 zoom 0.65
    show yuri 1e at i11:
        SP
        zoom 0 xcenter 950 ycenter 340
        7.5
        easein_elastic 0.75 zoom 0.65
    window hide(None)
    $ consolehistory = []
    call updateconsolefront("{size=-2}open(\"characters/natsuki.chr\", \"wb\")\n.write(renpy.file(\"natsuki.chr\").read()){/size}", "natsuki.chr written successfully.", 0.5) from _call_updateconsolefront_1
    python:
        try: renpy.file("../characters/natsuki.chr")
        except: open(config.basedir + "\\characters\\natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
    call updateconsolefront("{size=-2}open(\"characters/yuri.chr\", \"wb\")\n.write(renpy.file(\"yuri.chr\").read()){/size}", "yuri.chr written successfully.", 0.5) from _call_updateconsolefront_2
    python:
        try: renpy.file("../characters/yuri.chr")
        except: open(config.basedir + "\\characters\\yuri.chr", "wb").write(renpy.file("yuri.chr").read())
    $ pause(1.25)
    call hideconsolefront from _call_hideconsolefront_1
    hide natsuki
    hide yuri
    show layer master:
        zoom 1.5 xcenter 1150 ycenter 400
    show bg club_day:
        zoom 1.125 xcenter 480 ycenter 340
    show monika 2a at i11:
        zoom 1 xcenter 525 ycenter 425
    show sayori 4w at i11:
        SP
        zoom 0.65 xcenter -10 ycenter 380
        easein 0.1 yoffset -20
        easeout 0.1 yoffset 0
        0.6
        easeout 0.25 xcenter -810
    show mc 1shock at i11:
        SP
        zoom 0.65 xcenter 350 ycenter 380
        easein 0.1 yoffset -20
        easeout 0.1 yoffset 0
        0.6
        easeout 0.25 xcenter -450
    "{size=-2}Sayori &\n[player]{/size}" "{cps=55}{size=32}\"AAAHHHH!! RUN AWAY!\"{/size}{w=0.75}{/cps}{nw}"
    hide sayori
    hide mc
    show monika 1g at i11:
        SP
        zoom 1 xcenter 525 ycenter 425
        easein 0.1 yoffset -20
        easeout 0.1 yoffset 0
    m "Hey! Don't run..! There's absolutely nothing to worry about!"
    window hide(None)
    show layer master:
        SP
        zoom 1.5 xcenter 1150 ycenter 400
        ease 0.65 xcenter 0
    show natsuki 1k at i11:
        zoom 0.75 xcenter 950 ycenter 360 
    show yuri 1e at i11:
        zoom 0.75 xcenter 1250 ycenter 360
    show monika 1g at i11:
        SP
        zoom 1 xcenter 525 ycenter 425
        ease 0.65 xcenter 400
    show bg club_day:
        SP
        zoom 1.125 xcenter 480 ycenter 340
        ease 0.65 xcenter 800
    $ pause(0.8)
    show natsuki 4c
    hide monika
    hide m1
    n "What the heck just happened?"
    show natsuki 4c at i11:
        SP
        zoom 0.75 xcenter 950 ycenter 360 xzoom 1
        ease 0.25 xzoom -1
    n "Why are they--"
    show layer master:
        SP
        zoom 1.5 xcenter 0 ycenter 400
        easein_elastic 0.75 zoom 2 ycenter 450
    show bg club_day:
        SP
        zoom 1.125 xcenter 800 ycenter 340
        easein_elastic 0.75 zoom 0.975 xcenter 790 ycenter 330
    n 1o "GHK--!"
    show yuri 1e at i11:
        SP
        zoom 0.75 xcenter 1250 ycenter 360 
        0.425
        "yuri 3n"
        zoom 0.6
        easein 0.1 yoffset -10
        easeout 0.1 yoffset 0
    show natsuki 1p at i11:
        SP
        zoom 0.75 xcenter 950 ycenter 360 xzoom -1
        xoffset -10 yoffset -10
        parallel:
            easein_elastic 0.75 xoffset 0
        parallel:
            0.1
            easein_elastic 0.75 yoffset 0
    show layer master:
        SP
        zoom 2 xcenter 0 ycenter 450 xoffset -3 yoffset -3
        parallel:
            easein_elastic 0.75 xoffset 0
        parallel:
            0.1
            easein_elastic 0.75 yoffset 0
    n "GET AWAY FROM ME--!"
    show natsuki 1p at i11:
        SP
        zoom 0.75 xcenter 950 ycenter 360 xzoom -1
        parallel:
            easein 0.1 yoffset -30
            easeout 0.1 yoffset 0
            easeout_circ 0.25 xcenter 500
        parallel:
            ease 0.2 xzoom 1
    window hide(None)
    $ pause(0.9)
    hide natsuki
    show layer master:
        SP
        zoom 2 xcenter 0 ycenter 450
        ease_quint 2 xcenter -350 ycenter 500
    show bg club_day:
        SP
        zoom 0.975 xcenter 790 ycenter 330
        ease_quint 2 xcenter 865 ycenter 315
    show yuri 3n at i11:
        SP
        zoom 0.75 xcenter 1250 ycenter 360
        1
        block:
            ease 1.75 yoffset -5
            ease 1.75 yoffset 0
            repeat
    $ pause(1)
    y "W-What happened?"
    y "W-Why am I hated so much?"
    show monika 5a at i11:
        SP
        zoom 0.75 xcenter 600 ycenter 370 xzoom -1 rotate 7
        parallel:
            easein_quint 1 xcenter 900
        parallel:
            easein_cubic 1 ycenter 360 rotate 0
    m "Don't worry Yuri~"
    m "You didn't do anything bad."
    m "I promise they'll turn back to normal."
    window hide(None)
    stop music fadeout 0.5
    $ pause(0.2)
    play sound knock
    $ pause(1.25)
    show layer master:
        SP
        zoom 2 xcenter -350 ycenter 500
        easein_cubic 0.5 zoom 1.75 xcenter -150 ycenter 450
    show bg club_day:
        SP
        zoom 0.975 xcenter 865 ycenter 315
        easein_cubic 0.5 zoom 1.05 xcenter 835
    show monika 1d at i11 behind yuri:
        zoom 0.75 xcenter 900 ycenter 360 xzoom 1
    show yuri 3n at i11:
        SP
        zoom 0.75 xcenter 1250 ycenter 360
        ease 1.75 yoffset 0
    m "Is someone knocking on the door?"
    m "Yuri, you go open it."
    y 3o "..."
    show yuri 1w at i11:
        SP
        zoom 0.75 xcenter 1250 ycenter 360
        easein_circ 1 yoffset 5
    y "A..Alright.."
    show yuri 1w at i11:
        SP
        zoom 0.75 xcenter 1250 ycenter 360 yoffset 5
        parallel:
            easeout 3 xcenter 500
        parallel:
            ease 0.75 yoffset -10
            ease 0.75 yoffset 5
            repeat 2
    window hide(None)
    $ pause(1.1)
    play sound step
    $ pause(1.35)
    play sound step
    $ pause(0.75)
    scene bg class_day:
        zoom 4 xcenter -100 ycenter 360
    with dissolve_cg
    show yuri 1w at i11:
        SP
        zoom 1.5 ycenter 500 xcenter -250 xzoom -1 rotate 0 yoffset -15
        parallel:
            linear 2 xcenter 640
        parallel:
            ease 1 yoffset 0
            ease 1 yoffset -15
        parallel:
            2
            "yuri 3p"
            zoom 1.2
            linear 0.3 rotate -90 ycenter 1100 xoffset -100
    show layer master:
        SP
        TC
        1.95
        xoffset -50 yoffset -50
        parallel:
            easein_elastic 0.75 xoffset 0
        parallel:
            0.1
            easein_elastic 0.75 yoffset 0
    show india:
        SP
        zoom 1.2 xcenter 1750 ycenter 360
        1.95
        easein_back 0.5 xcenter 640
    $ pause(0.85)
    play sound step
    $ pause(1.1)
    play music [ "<silence 0.25>", kerobobs ]
    play sound wood
    $ pause(0.5)
    scene bg class_day:
        SP
        zoom 4 xcenter -100 ycenter 360
        parallel:
            dizzy(0.25, 0.5)
        parallel:
            0.1
            block:
                zoom 3.75 xcenter -50
                easein_quart 0.675 zoom 4 xcenter -100
                repeat
    show india:
        SP
        zoom 1.2 xcenter 640 ycenter 360
        dizzy(0.5, 0.5)
    show layer master:
        SP
        TC
        zoom 1
        0.1
        block:
            zoom 1.1
            easein_quart 0.675 zoom 1
            repeat
    hide yuri
    "Indian Man" "helo bitch lasagnas"
    scene bg club_day:
        zoom 2.5 xcenter 0 ycenter 450
    show monika 1i at i11:
        zoom 2 xcenter 700 ycenter 600
    with Dissolve(0.25)
    $ pause(0.2)
    show monika 1q at i11:
        SP
        zoom 2 xcenter 700 ycenter 600
        easein 0.5 rotate -7.5 xcenter 675 ycenter 650
    m "Oh Jesus Christ..."
    stop music
    window hide(None)
    scene black
    show splash_warning5 "AND THUS,\nDOKI DOKI INDIA-MAN TIME WAS\nBORN AGAIN."
    show splash_warning2 "(Credits to Childish-N for protagonist sprites)" at sub:
        zoom 0.5 alpha 0.5
    $ pause()
    return

label hidefront:
    hide dark as d1
    hide vignette onlayer front
    hide noise onlayer front
    return
    
label showfront:
    show vignette onlayer front zorder 2:
        alpha 0.45
        block:
            ease 2 alpha 0.45
            ease 2 alpha 0.65
            repeat
    show dark as d1 zorder 110:
        alpha 0.75 zoom 3
        TC
    show noise onlayer front zorder 1:
        alpha 0.05
        ease 1.5 alpha 0.1
        ease 1.5 alpha 0.05
        repeat
    return