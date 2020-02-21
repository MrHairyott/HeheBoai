init -100 python:

    for archive in ['audio','images','fonts']:
        if archive not in config.archives:
            renpy.error("DDLC archive files not found in /game folder. Check installation and try again.")

init python:
    menu_trans_time = 1

    splash_message_default = "( Not affiliated with Team Salvato nor Toby Fox. )\n( Just a Fan work. )"

    splash_messages = []


image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

image splash_warning2 = ParameterizedText(style="splash_text2", xalign=0.5, yalign=0.5)

image splash_warning3 = ParameterizedText(style="splash_text3", xalign=0.5, yalign=0.5)

image splash_warning4_5 = ParameterizedText(style="splash_text4_5", xalign=0.5, yalign=0.5)

image splash_warning4 = ParameterizedText(style="splash_text4", xalign=0.5, yalign=0.5)

image splash_warning5 = ParameterizedText(style="splash_text5", xalign=0.5, yalign=0.5)


image menu_logo:
    "/mod_assets/DDLCModTemplateLogo.png"  
    subpixel True
    xcenter 240
    ycenter 180
    zoom 0.60
    menu_logo_move
    
image menu_logo2:
    "/mod_assets/DDLCModTemplateLogo.png"  
    subpixel True
    xcenter 240
    ycenter 180
    zoom 0.60
    easeout_cubic 1 xoffset -500

image menu_sans_text:
    Text("{size=37}{bl}sans the skeleton\n{space=60}{size=27}in{/bl}", style="comicsans2")
    xcenter 165 ycenter 95 rotate -50
    xoffset -350
    3.5
    parallel:
        easein_cubic 1 xoffset 0 rotate -10
    parallel:
        1
        dizzy(0.25, 1)
        
image menu_sans_text_out:
    Text("{size=37}{bl}sans the skeleton\n{space=60}{size=27}in{/bl}", style="comicsans2")
    xcenter 165 ycenter 95 rotate -10
    xoffset 0
    parallel:
        easeout_cubic 1 xcenter -185 rotate -50
    parallel:
        dizzy(0.25, 1)
        
image menu_sans_text2:
    Text("{size=37}{bl}sans the skeleton\n{space=60}{size=27}in{/bl}", style="comicsans2")
    xcenter 165 ycenter 95 rotate -50 alpha 0.33
    xoffset -350 zoom 1
    3.5
    parallel:
        easein_cubic 1 xoffset 0 rotate -10
        block:
            zoom 1 alpha 0.33
            easein 1 zoom 1.15 alpha 0
            repeat
    parallel:
        1
        dizzy(0.25, 1)

image blackout:
    Solid("#000")
    alpha 0
    2.65
    alpha 1
    0.35
    alpha 0

image menu_sans_l:
    Follow("sans_l", 9, 18).sm
    zoom 1.25 xcenter 1350 ycenter 925
    alpha 0
    2.9
    alpha 1
image menu_sans_l2:
    Follow("sans_l", 9, 18).sm
    zoom 1.25 xcenter 1350 ycenter 925

image menu_sans_t:
    Follow("sans_t 2", 9, 18).sm
    zoom 1.25 xcenter 1266 ycenter 784
    alpha 0
    2.9
    alpha 1
    sans_t_move()
image menu_sans_t2:
    Follow("sans_t 2", 9, 18).sm
    zoom 1.25 xcenter 1266 ycenter 784
    sans_t_move()

image menu_sans_h:
    Follow("sans d", 9, 18).sm
    zoom 1.25 xcenter 1374 ycenter 659
    alpha 0
    2.9
    alpha 1
    sans_h_move()
image menu_sans_h2:
    Follow("sans d", 9, 18).sm
    zoom 1.25 xcenter 1374 ycenter 659
    sans_h_move()

image menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_move

image game_menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_loop

image menu_fade:
    "white"
    menu_fadeout

image menu_art_y:
    subpixel True
    Follow("gui/menu_art_y.png", 9, 27.5).sm
    xcenter 900
    ycenter 235
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)
image menu_art_y2:
    subpixel True
    Follow("gui/menu_art_y.png", 9, 27.5).sm
    xcenter 900
    ycenter 235
    zoom 0.60
    menu_art_move2(0.54, 600, 0.60)

image menu_art_n:
    subpixel True
    Follow("gui/menu_art_n.png", 9, 22.5).sm
    xcenter 1050
    ycenter 285
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)
image menu_art_n2:
    subpixel True
    Follow("gui/menu_art_n.png", 9, 22.5).sm
    xcenter 1050
    ycenter 285
    zoom 0.58
    menu_art_move2(0.58, 750, 0.58)

image menu_art_s:
    subpixel True
    Follow("gui/menu_art_s.png", 9, 21).sm
    xcenter 810
    ycenter 400
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)
image menu_art_s2:
    subpixel True
    Follow("gui/menu_art_s.png", 9, 21).sm
    xcenter 810
    ycenter 400
    zoom 0.68
    menu_art_move2(0.68, 510, 0.68)

image menu_art_m:
    subpixel True
    Follow("gui/menu_art_m.png", 9, 19.5).sm
    xcenter 1300
    ycenter 440
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)
image menu_art_m2:
    subpixel True
    Follow("gui/menu_art_m.png", 9, 19.5).sm
    xcenter 1300
    ycenter 440
    zoom 1.00
    menu_art_move2(1.00, 1000, 1.00)

image menu_art_y_ghost:
    subpixel True
    "gui/menu_art_y_ghost.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n_ghost:
    subpixel True
    "gui/menu_art_n_ghost.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s_ghost:
    subpixel True
    "gui/menu_art_s_ghost.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m_ghost:
    subpixel True
    "gui/menu_art_m_ghost.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_s_glitch:
    subpixel True
    "gui/menu_art_s_break.png"
    xcenter 470
    ycenter 600
    zoom 0.68
    menu_art_move(.8, 470, .8)

image menu_nav:
    "gui/overlay/main_menu.png"
    menu_nav_move
image menu_nav2:
    SP
    "gui/overlay/main_menu.png"
    xoffset 0
    easeout_cubic 1 xoffset -500

image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=40, particleTime=2.0, particleXSpeed=3, particleYSpeed=3).sm
    particle_fadeout
    

transform particle_fadeout:
    easeout 1.5 alpha 0

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

transform menu_logo_move:
    subpixel True
    yoffset -400
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0
        
transform menu_art_move2(z, x, z2):
    subpixel True
    yoffset 0 xoffset 0
    zoom z2

image intro:
    truecenter
    "white"
    0.5
    "bg/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image tos = "bg/warning.png"
image tos2 = "bg/warning2.png"

image zawarudo = "mod_assets/gui/zawarudo.png" 
#ZA WARUDO! TOKI WO TOMARE!!!

init python:
    if not persistent.do_not_delete:

        import os
        try:
            if not os.access(config.basedir + "/characters/", os.F_OK):
                os.mkdir(config.basedir + "/characters")
        except:
            pass
        
        try: renpy.file("../characters/monika.chr")
        except: open(config.basedir + "\\characters\\monika.chr", "wb").write(renpy.file("monika.chr").read())
        try: renpy.file("../characters/natsuki.chr")
        except: open(config.basedir + "\\characters\\natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
        try: renpy.file("../characters/yuri.chr")
        except: open(config.basedir + "\\characters\\yuri.chr", "wb").write(renpy.file("yuri.chr").read())
        try: renpy.file("../characters/sayori.chr")
        except: open(config.basedir + "\\characters\\sayori.chr", "wb").write(renpy.file("sayori.chr").read())


label splashscreen:
    $ renpy.music.set_volume(1)
    $ renpy.sound.set_volume(1)


    python:
        firstrun = ""
        try:
            firstrun = renpy.file("firstrun").read(1)
        except:
            with open(config.basedir + "/game/firstrun", "wb") as f:
                pass
    if not firstrun:
        if persistent.first_run and not persistent.do_not_delete:
            $ quick_menu = False
            scene black
            menu:
                "A previous save file has been found. Would you like to delete your save data and start over?"
                "Yes, delete my existing data.":
                    "Deleting save data...{nw}"
                    python:
                        delete_all_saves()
                        renpy.loadsave.location.unlink_persistent()
                        renpy.persistent.should_save_persistent = False
                        renpy.utter_restart()
                "No, continue where I left off.":
                    pass

        python:
            if not firstrun:
                with open(config.basedir + "/game/firstrun", "w") as f:
                    f.write("1")
            filepath = renpy.file("firstrun").name
            open(filepath, "a").close()


    default persistent.first_run = False
    if config.developer:
        scene white
        if renpy.random.randint(0,3) == 0:
            call screen confirm("Jotaro?", Return(True), Return(False))
        else:
            call screen confirm("Intro?", Return(True), Return(False))
        if _return:
            $ eee = True
        else:
            $ eee = False
    else:
        $ eee = False
    if not persistent.first_run or eee:
        $ quick_menu = False
        scene white
        pause 0.5
        scene tos
        show sans_l at TC:
            zoom 1.15 xcenter 1100 ycenter 660
        show sans_t 1 at TC:
            zoom 1.15 xcenter 1095 ycenter 537
            sans_t_move2(0.925)
        show sans e at TC:
            zoom 1.15 xcenter 1093 ycenter 428
            sans_h_move2(0.925)
        with Dissolve(1.0)
        pause 1.0

        "[config.name] is a Doki Doki Literature Club fan mod that is not affiliated with Team Salvato and Toby Fox."
        "It is designed to be played after the official game {i}and{/i} Undertale have been completed, and contains spoilers for the two games."
        "You can play DDLC for free at: {a=http://ddlc.moe}{color=#99f}http://ddlc.moe{/color}{/a}, and puchase Undertale at: {a=http://undertale.com}{color=#99f}http://undertale.com{/color}{/a}"

        menu:
            "By playing [config.name], you agree that you have completed DDLC and Undertale; and accept any spoilers contained within."
            "I agree.":

                pass
        show tos2 behind sans_l
        with Dissolve(1.5)
        hide tos
        $ pause(1)
        
        show zawarudo at TC:
            zoom 0.8 xzoom 1.015 nearest True
        play sound ut_snap
        show sans_t 1 at TC:
            zoom 1.15 xcenter 1095 ycenter 537
        show sans e at TC:
            zoom 1.15 xcenter 1093 ycenter 428
        $ pause(1.25)
        
        show b m at TC:
            zoom 0.75 xcenter 810 ycenter 440 xzoom -1
        show s_text "{size=27}welp,":
            xcenter 746 ycenter 370
        $ s_say("welp,")
        $ pause(0.4)
        show s_text "{size=27}{space=69}let's\nget this over\nwith." as s1:
            xcenter 795 ycenter 398
        $ s_say("let's get this over with.")
        
        $ pause(1.5)
        
        scene white
        with Dissolve(1)

        $ persistent.first_run = True

    python:
        basedir = config.basedir.replace('\\', '/')

    if persistent.autoload and not _restart:
        jump autoload

    $ config.allow_skipping = False

    show white
    $ config.mouse = None
    $ persistent.ghost_menu = False
    $ splash_message = splash_message_default
    $ config.main_menu_music = audio.t1
    $ renpy.music.play(config.main_menu_music)
    show intro with Dissolve(0.5, alpha=True):
        SP
        TC
        zoom 1
        parallel:
            linear 3.5 zoom 1.15
        parallel:
            3
            linear 0.5 alpha 0
    pause 3
    hide intro
    if persistent.playthrough == 2 and renpy.random.randint(0, 3) == 0:
        $ splash_message = renpy.random.choice(splash_messages)
    show splash_warning "[splash_message]" with Dissolve(0.5, alpha=True):
        SP
        TC
        zoom 1
        linear 3 zoom 1.15
    pause 2.0
    hide splash_warning with Dissolve(0.5, alpha=True)
    $ config.allow_skipping = True
    return

label warningscreen:
    hide intro
    show warning
    pause 3.0

label after_load:
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = False
    $ style.say_dialogue = style.normal

    if anticheat != persistent.anticheat:
        stop music
        scene black
        "The save file could not be loaded."
        "Are you trying to cheat?"


        $ renpy.utter_restart()
    return


label autoload:
    python:

        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()


        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None



    $ renpy.pop_call()
    jump expression persistent.autoload

label before_main_menu:
    python:
        try: renpy.file("../characters/monika.chr")
        except: open(config.basedir + "\\characters\\monika.chr", "wb").write(renpy.file("monika.chr").read())
        try: renpy.file("../characters/natsuki.chr")
        except: open(config.basedir + "\\characters\\natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
        try: renpy.file("../characters/yuri.chr")
        except: open(config.basedir + "\\characters\\yuri.chr", "wb").write(renpy.file("yuri.chr").read())
        try: renpy.file("../characters/sayori.chr")
        except: open(config.basedir + "\\characters\\sayori.chr", "wb").write(renpy.file("sayori.chr").read())
        config.main_menu_music = audio.t1
    return
    
label extras:
    $ config.mouse = None
    $ config.skipping = False
    $ config.allow_skipping = False
    $ quick_menu = False
    $ renpy.music.set_volume(1)
    $ renpy.sound.set_volume(1)
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"
    call hidefront from _call_hidefront_2
    hide red onlayer front
    stop music fadeout 1.25
    scene white
    show vignette:
        alpha 0.35
    with Dissolve(1)
    $ pause(0.25)
    play music ambience
    scene black
    show splash_warning5 "You're not supposed to see this."
    show splash_warning5 "{size=10}Also there's a secret button somewhere." as sp1:
        TC
        ycenter 600 alpha 0.25
    show white onlayer screens
    show vignette onlayer screens:
        SP
        alpha 0.35
        block:
            ease 10 alpha 0.65
            ease 10 alpha 0.35
            repeat
    show rays onlayer screens:
        TC
        SP
        alpha 0 zoom 2.5
        parallel:
            rotate 0
            linear 35 rotate 360
            repeat
        parallel:
            ease 1 alpha 0.2
    show splash_warning4_5 "{size=50}Extras" onlayer screens:
        ycenter 70
    show image "mod_assets/bobyori/a.png" as s1 onlayer screens:
        SP
        zoom 0.35 xcenter 325 ycenter 250
        dizzy(0.5, 1)
    show image "mod_assets/bobyori/a.png" as s2 onlayer screens behind s1:
        SP
        zoom 0.35 xcenter 325 ycenter 250 alpha 0.25
        0.5
        dizzy(0.5, 1)
    show image "yuri/a.png" as y1 onlayer screens:
        zoom 0.35 xcenter 950 ycenter 375
    show image "yuri/a.png" as y2 onlayer screens behind y1:
        SP
        zoom 0.35 xcenter 950 ycenter 375 alpha 0.35
        block:
            ease 1.5 zoom 0.4 ycenter 388
            ease 1.5 zoom 0.35 ycenter 375
            repeat
    show eyesymbol as eye onlayer screens:
        SP
        zoom 0.075 xcenter 920 ycenter 292
        block:
            rotate 0
            linear 5 rotate 360
            repeat
label extras2:
    show screen creepy
    python:
        madechoice = renpy.display_menu([("The Joy of Painting with Bobyori Ross!", "bobyori"), ("Yuri, The Supernatural Genocider", "darkyuri"), ("Exit", "exit")], screen="choice_t")
    if madechoice == "bobyori":
        $ quick_menu = True
        stop music fadeout 0.5
        hide screen creepy
        call clearscreens from _call_clearscreens_1
        jump bobyori
    elif madechoice == "darkyuri":
        if persistent.playername == None or player == None:
            call screen name_input("Please enter your name\n{size=15}(If none, \"MC\" will be chosen.)", Return(True))
            if _return:
                $ FinishEnterName()
                if not player:
                    $ player = "MC"
                    $ persistent.playername = player
        $ quick_menu = True
        stop music fadeout 0.5
        hide screen creepy
        call clearscreens from _call_clearscreens_2
        jump darkyuri
    elif madechoice == "exit":
        call screen confirm("Are you sure you want to return to the main menu?", Return(True), Return(False))
        if _return:
            $ quick_menu = True
            return
        else:
            call extras2 from _call_extras2
            
    return

label clearscreens:
    hide splash_warning5
    hide sp1
    with None
    hide vignette onlayer screens
    hide white onlayer screens
    hide splash_warning4_5 onlayer screens
    hide rays onlayer screens
    hide s1 onlayer screens
    hide s2 onlayer screens
    hide y1 onlayer screens
    hide y2 onlayer screens
    hide eye onlayer screens
    with wipeleft
    return
    
label quit:
    return
