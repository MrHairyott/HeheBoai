init python:
    import subprocess

    def m_msgbox():
        if not renpy.windows: return
        if renpy.game.preferences.fullscreen: renpy.game.preferences.fullscreen = False
        pause(0.5)
        try:
            msgbox = subprocess.Popen( basedir + "/game/submods2/ATL.vbs.vbs", shell=True)
            msgbox.wait()
        except: return renpy.error("Directory not found. (Don't change anything in the submods2 folder!)")
        return

# Entry point
label start:

    # ID of this playtrhoguh
    $ config.mouse = None
    $ anticheat = persistent.anticheat

    # keep track of chapter
    $ chapter = 0

    # if they quit during a pause, we have to set _dismiss_pause to false again
    $ _dismiss_pause = config.developer

    # girl names
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"

    $ quick_menu = False
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True
    $ renpy.music.set_volume(1)
    $ renpy.sound.set_volume(1)

    ###########################
    
    call start_transition from _call_start_transition
    $ pause(0.75)
    
    if persistent.playthrough == 0:

        call badtime_e from _call_sans
        call ch2 from _call_sans2
        call ch3 from _call_sans3

    return

label start_transition:
    $ quick_menu = False
    scene black
    show game_menu_bg
    show menu_art_y2
    show menu_art_n2
    show menu_art_s2
    show menu_art_m2
    show menu_sans_l2
    show menu_sans_t2
    show menu_sans_h2
    show menu_nav2
    show menu_logo2
    show menu_sans_text_out
    show layer master:
        zoom 1 rotate 0
        TC
        SP
        0.75
        easeout_cubic 0.75 zoom 1.5 rotate 10
    return

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
