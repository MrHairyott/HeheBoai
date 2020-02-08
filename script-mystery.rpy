
init python:
    import subprocess
    import os
    process_list = []
    currentuser = ""
    if renpy.windows:
        try:
            process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
        except:
            pass
        try:
            for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                user = os.environ.get(name)
                if user:
                    currentuser = user
        except:
            pass

label creepy:
    if not player or not persistent.playername or player == "" or persistent.playername == "":
        $ player = "MC"
        $ persistent.playername = player
    stop music fadeout 0.5
    call clearscreens from _call_clearscreens
    if not config.developer:
        $ quick_menu = False
        $ config.allow_skipping = False
        $ allow_skipping = False
    else:
        $ quick_menu = True
        $ config.allow_skipping = True
        $ allow_skipping = True
    scene bg club_day
    with wipeleft
    play music t6
    show yuri 2y5 at t11 zorder 2
    y "Hi, [player]!"
    y "I've been waiting for you."
    y 2d "Are you ready to continue reading?"
    y "I brought my best tea today--"
    show yuri 2f
    show natsuki 4w at f33 zorder 3
    n "Monika!"
    n "I told you not to--"
    n 1g "Ugh..."
    n "Is she really late again?"
    show natsuki at t33 zorder 2
    show yuri at f32 zorder 3
    y 1h "Inconsiderate as usual, Natsuki."
    show yuri at t32 zorder 2
    show natsuki at f33 zorder 3
    n 4c "Excuse me?"
    show natsuki at t33 zorder 2
    show yuri at f32 zorder 3
    y 1r "Must you always interrupt my conversations with your incessant yelling?"
    show yuri at t32 zorder 2
    show natsuki at t33 zorder 3
    n 1o "What are you talking about?!"
    n 1q "You say that like I do it on a regular basis{nw}"
    window hide(None)
    window auto
    scene black
    show black onlayer front
    show yuri ghost_base at i32 onlayer front
    show image "mod_assets/yuhri/hair.png" as y2 onlayer front at i32 zorder 1 
    show image "mod_assets/gui/smack/circle.png" as y onlayer front:
        zoom 0.125 xcenter 607 ycenter 185 yzoom 1.125 rotate -10 xzoom 1.07
    show natsuki ghost_base at i33 zorder 2 onlayer front
    show image "mod_assets/gui/smack/circle.png" as n zorder 3 onlayer front:
        zoom 0.14 xcenter 1021 ycenter 273 yzoom 1.1 xzoom 1.05 rotate -6
    python:
        currentpos = get_pos()
        currentpos2 = get_pos() + 0.05
        audio.t6r = "<from " + str(currentpos) + " to " + str(currentpos2) + " loop " + str(currentpos) + ">bgm/6.ogg"
        renpy.music.set_volume(2.5)
    play music t6r
    pause
    pause
    pause
    stop music
    $ renpy.music.set_volume(1)
    $ quick_menu = True
    $ renpy.quit()
    return
