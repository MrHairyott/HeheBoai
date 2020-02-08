## This is an example scene
## It teaches you a little about making mods

# Each section needs a label, this is how we will call the scene in other parts
# of the script

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

#label example_chapter:
#    stop music fadeout 2.0

#    # setup scene with background and music
#    scene bg club_day
#    with dissolve_scene_full
#    play music t3

#    # Say statements
#    # <char name> "stuff to say"
#    m "...[player]?"

#    # show characters and positions and stuff
#    show monika 1 zorder 2 at t11
#    m "Ah! What a nice surprise!"

#    # Character images are their name followed by number and letters
#    show monika 1b zorder 2 at t11
#    m "Welcome to the club!"
#    m "The Modification Club."


#    show monika 3 zorder 2 at t11
#    m " I started this club after I had some difficulties changing code in Doki Doki Literature Club."







#    m 3l "It turns out that bad coding can really hurt people."
#    m 3j "That's why I wanted to make this club to teach people how to mod responsibly!"

#    m 2a "First, you need the right template."
#    m 2b "This template you're looking at right now!"
#    $ config.developer = "auto"
#    if config.developer:
#        m 2b "Looks like you're ahead of me on that one."
#        m "Way to take the initiative!"
#    else:
#        m 2b "You can find the source for it online at https://github.com/therationalpi/DDLCModTemplate"
#        m "If you haven't already, of course."

#    m 1a "Then you need to add files from DDLC."
#    m "You'll want to put those in the /game folder of the template."
#    if config.developer:
#        m 1b "Again, that's something you already know."
#        m 1l "Please let me know if I'm boring you!"
#    else:
#        m 1b "Kind of like what you did to make this demo work!"

#    m 1a "Finally, you're going to want to download the Ren'Py SDK."
#    m 2a "That's at https://www.renpy.org/latest.html"
#    if config.developer:
#        m 2j "I promise I'll get to the good stuff now."
#    else:
#        m 2a "You'll be using that to write and test your scripts."

#    m 4a "So now that you have everything, it's time to get started!"
#    m 4b "Start by opening up your /game folder"
#    m 4c "You'll notice there aren't a lot of files in there."
#    m 4a "Most of the data we'll be using is coming from DDLC."
#    m "Including all of the user interface and system coding."
#    m 4k "All you need to bring are the stories you want to tell!"
#    m 4c "Of course, if you really want to dig deep and change how the game works..."
#    m 4b "That's possible too."

#    m 1j "That reminds me..."
#    m 1k "I haven't asked about you or the game you want to make."
#    m 5 "Ahaha~! How silly of me!"



#    default knows_python = False
#    default knows_renpy = False


#    menu:
#        m "How experienced are you with coding?"
#        "I'm an experienced coder":

#            $ experience_level = 2
#            m 5 "Really? That's very impressive!"
#            show monika 1m zorder 2 at t11
#            with Dissolve(0.3)
#            m 1m "I'm new to this, myself, so maybe I'll end up learning more from you, instead!"
#        "I've coded before":
#            $ experience_level = 1
#            m 5 "That's good."
#            show monika 1j zorder 2 at t11
#            with Dissolve(0.3)
#            m 1j "Building a mod for DDLC should feel very natural, then!"
#        "New to coding":
#            $ experience_level = 0
#            m 5 "Really? This should be fun then!"
#            show monika 1m zorder 2 at t11
#            with Dissolve(0.3)
#            m 1m "I'm pretty new to this myself..."
#            m 1n "So it's a little a weird for me to be someone's teacher."
#            m 1k "But I'll try my best!"

#    if experience_level > 0:
#        m 2a "Since you've coded before, you might like to know that this game was built using Renpy."
#        m "It's a very popular platform for making visual novels."

#        show monika 1a zorder 2 at t11

#        menu:
#            m "Have you used Renpy before?"
#            "Yes.":
#                $ knows_renpy = True
#                m 1b "Sounds like you're ahead of the game, then."
#            "No.":
#                m 1e "Well, don't worry about that."
#                m 1b "Renpy is actually very easy once you get used to it."

#        m 3a "For more advanced coding, python might be necessary."
#        m 3c "Renpy is actually built with Python..."
#        m 3j "So the sky's the limit for modding if you know how to use it!"

#        show monika 1a zorder 2 at t11
#        menu:
#            m "Are you familiar with python?"
#            "Yes.":
#                $ knows_python = True
#                if not knows_renpy:
#                    m 1a "That might help you pick up Renpy a little quicker, then."
#                    m 3a "But there are some things that makes Renpy's python a bit different."
#                    m 3j "I'll try to call them out when they come up."
#                else:
#                    m 1b "Sounds like you're in great shape for this!"
#                    m 1j "You have all the skills you need to make whatever you want."
#                    m 1k "I'm excited to see what you come up with."
#            "No.":
#                if not knows_renpy:
#                    m 2c "Well, any coding experience will help a lot."
#                    m 2a "Python is made to be an easy language to pick up, after all."
#                else:
#                    m 2d "Don't sell yourself short, [player]."
#                    m 2a "I'm sure you picked up a few tricks from Renpy already."
#                    m 2j "But I'll be sure to share a few I've picked up with you, too."

#    m 1c "Now, about the mod you want to make."
#    m "How difficult of a project is it going to be?"
#    m 1d "Is it mostly going to be standard scripts with a few choices and special effects..."
#    m 5 "...or will you be creating lots of new systems to really change the game?"

#    menu:
#        m "So, which do you plan on making?"
#        "Basic.":
#            $ advanced = False
#            m 5 "Starting off with something simple?"
#            show monika 3b zorder 2 at t11
#            with Dissolve(0.3)
#            m 3b "I think that's a good way to go."
#            m 3a "Making a simple script is a lot like writing a play."
#            m 1a "But the actors are us characters, and we'll always do just what you direct from us..."
#            m 1m "..for better or worse."
#        "Advanced.":
#            $ advanced = True
#            m 5 "Trying for something a little more complicated?"
#            show monika 1e zorder 2 at t11
#            with Dissolve(0.3)
#            m 1e "Well, I'll try to share all the tools I have with you."
#            m 1k "Hopefully you'll find what you need to make your perfect game!"

#    m 2b "Now that I know more about you and your project, we're really ready to get started!"
#    m "I've prepared a few lessons to help get you started!"
#    m 2a "And when we're done, you'll have made your first mod."


#    $ persistent.playthrough = 1

#    jump tutorial_selection

#    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

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


init python:
    
    tch0 = []
    def translate_it():
        with renpy.file('advanced_scripts/shittytranslate.txt') as scriptfile:
            for lines in scriptfile:
                lines = lines.strip()

                if lines == '' or lines[0] == '#': continue
                lines = lines.replace('^^^', persistent.playername)
                z = lines.split('*^*^*')
                tch0.append(str(z[1]))
            return

label translated_ch0: # Translated ch1 is located in overides.rpy
    if persistent.playername == '':
        $ persistent.playername = 'MC'
        $ player = persistent.playername
    elif player == '':
        $ player = 'MC'
        $ persistent.playername = player
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    $ s_name = "???"
    $ y_name = "Girl 1"
    $ n_name = "Girl 2"
    $ m_name = "Girl 3"
    $ translate_it()
    
    s "[tch0[0]]"
    "[tch0[1]]"
    "[tch0[2]]"
    "[tch0[3]]"
    "[tch0[4]]"
    "[tch0[5]]"
    "[tch0[6]]"
    $ s_name = "Sayori"
    show sayori 4p zorder 2 at t11
    s 4p "[tch0[7]]"
    s "[tch0[8]]"
    s "[tch0[9]]"
    mc "[tch0[10]]"
    show sayori at s11
    s 5c2 "[tch0[11]]"
    s "[tch0[12]]"
    mc "[tch0[13]]"
    show sayori zorder 2 at t11
    s 1a2 "[tch0[14]]"
    s "[tch0[15]]"
    s "[tch0[16]]"
    mc "[tch0[17]]"
    s 1q "[tch0[18]]"
    show sayori zorder 1 at thide
    hide sayori
    "[tch0[19]]"
    "[tch0[20]]"
    show sayori 3a2 zorder 2 at t11
    s "[tch0[21]]"
    s "[tch0[22]]"
    mc "[tch0[23]]"
    mc "[tch0[24]]"
    mc "[tch0[25]]"
    show sayori at s11
    s 4h "[tch0[26]]"
    s "[tch0[27]]"
    mc "[tch0[28]]"
    "[tch0[29]]"
    "[tch0[30]]"
    s 4j "[tch0[31]]"
    s "[tch0[32]]"
    s "[tch0[33]]"
    s "[tch0[34]]"
    s 4g "[tch0[35]]"
    s "[tch0[36]]"
    mc "[tch0[37]]"
    mc "[tch0[38]]"
    mc "[tch0[39]]"
    s 1h "[tch0[40]]"
    mc "[tch0[41]]"
    show sayori zorder 2 at t11
    s 4r "[tch0[42]]"
    "[tch0[43]]"
    "[tch0[44]]"
    "[tch0[45]]"
    
    scene bg class_day
    with wipeleft_scene

    "[tch0[46]]"
    "[tch0[47]]"
    mc "[tch0[48]]"
    "[tch0[49]]"
    "[tch0[50]]"
    
    s "[tch0[51]]"
    show sayori 1b zorder 2 at t11
    mc "[tch0[52]]"
    "[tch0[53]]"
    "[tch0[54]]"
    s 1a2 "[tch0[55]]"
    s "[tch0[56]]"
    mc "[tch0[57]]"
    s 1y "[tch0[58]]"
    mc "[tch0[59]]"
    s 1a2 "[tch0[60]]"
    mc "[tch0[61]]"
    s 4r "[tch0[62]]"
    mc "[tch0[63]]"
    show sayori at s11
    s 5d "[tch0[64]]"
    "[tch0[65]]"
    "[tch0[66]]"
    "[tch0[67]]"
    "[tch0[68]]"
    "[tch0[69]]"
    mc "[tch0[70]]"
    show sayori zorder 2 at t11
    s 1g "[tch0[71]]"
    mc "[tch0[72]]"
    s 5b2"[tch0[73]]"
    s "[tch0[74]]"
    s "[tch0[75]]"
    s "[tch0[76]]"
    mc "[tch0[77]]"
    "[tch0[78]]"
    "Take a deep breath ..." # This line is missing in the tch0, so i made one.
    mc "[tch0[79]]"
    show sayori at h11
    s 4r "[tch0[80]]"

    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene

    "[tch0[81]]"
    "[tch0[82]]"
    "[tch0[83]]"

    scene bg club_day
    with wipeleft
    play music t3
    show sayori 4 at l41
    s "[tch0[84]]"
    mc "[tch0[85]]"
    show sayori at lhide
    hide sayori
    "[tch0[86]]"
    show yuri 1a zorder 2 at t11
    y "[tch0[87]]"
    y "[tch0[88]]"
    show yuri zorder 2 at t22
    show natsuki 4c zorder 2 at t21
    n "[tch0[89]]"
    n "[tch0[90]]"
    show yuri zorder 2 at t33
    show natsuki zorder 2 at t32
    show monika 1k zorder 2 at t31
    m "[tch0[91]]"
    m "[tch0[92]]"
    show monika 1a
    mc "..." # Nothing is changed in this line. The tch0[93] line stays the same. 
    "[tch0[94]]"
    "[tch0[95]]"
    "{i}[tch0[96]]{/i}"

    show monika zorder 1 at thide
    show yuri zorder 1 at thide
    show natsuki zorder 3 at f32
    hide monika
    hide yuri

    n 2c "[tch0[97]]"
    n "[tch0[98]]"
    mc "[tch0[99]]"
    show natsuki zorder 2 at t32
    show yuri 2l zorder 3 at f33
    y "[tch0[100]]"
    $ n_name = 'Natsuki'
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f32
    n 5s "[tch0[101]]"
    show natsuki zorder 2 at t32

    "[tch0[102]]"
    "[tch0[103]]"
    "[tch0[104]]"

    show sayori 2q zorder 3 at f31
    s "[tch0[105]]"
    "[tch0[106]]"
    s 1x "[tch0[107]]"
    s "[tch0[108]]"
    $ y_name = 'Yuri'
    show sayori zorder 2 at t31
    show yuri zorder 3 at f33
    y 4b "[tch0[109]]"
    "[tch0[110]]"
    show yuri zorder 2 at t33
    mc "[tch0[111]]"
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    hide yuri
    hide natsuki
    show sayori zorder 3 at f31
    s 1a2 "[tch0[112]]"
    $ m_name = 'Monika'
    show sayori zorder 2 at t31
    show monika 2a zorder 3 at f32
    m "[tch0[113]]"
    m "[tch0[114]]"
    show monika 5a at hop
    "[tch0[115]]"
    "[tch0[116]]"
    "[tch0[117]]"
    "[tch0[118]]"
    "[tch0[119]]"
    mc "[tch0[120]]"
    show monika zorder 1 at thide
    hide monika
    show sayori zorder 3 at f31
    s 4x "[tch0[121]]"
    s "[tch0[122]]"
    show sayori zorder 2 at t31
    show natsuki 1e zorder 3 at f32
    n "[tch0[123]]"
    show natsuki zorder 2 at t32
    show sayori zorder 3 at f31
    s 5a2 "[tch0[124]]"
    show sayori zorder 2 at t31
    show yuri 1a zorder 3 at f33
    y "[tch0[125]]"
    hide sayori
    hide natsuki
    hide yuri
    with wipeleft
    "[tch0[126]]"
    "[tch0[127]]"
    "[tch0[128]]"
    "[tch0[129]]"
    "[tch0[130]]"
    show natsuki 2z zorder 2 at t32
    n "[tch0[131]]"
    n "[tch0[132]]"
    show sayori 4m zorder 2 at t31
    show monika 2d zorder 2 at t33
    s "[tch0[133]]"
    "[tch0[134]]"
    "[tch0[135]]"
    show sayori zorder 3 at f31
    s 4r "[tch0[136]]"
    show sayori zorder 2 at t31
    show monika zorder 3 at f33
    m 2b "[tch0[137]]"
    show monika zorder 2 at t33
    show natsuki zorder 3 at f32
    n 2d "[tch0[138]]"
    n "[tch0[139]]"
    "[tch0[140]]"
    show natsuki zorder 2 at t32
    show sayori zorder 3 at f31
    s 4q "[tch0[141]]"
    "[tch0[142]]"
    "[tch0[143]]"
    show sayori zorder 1 at thide
    show monika zorder 1 at thide
    hide sayori
    hide monika
    show natsuki 1c zorder 2 at t32
    "[tch0[144]]"
    "[tch0[145]]"
    "[tch0[146]]"
    "[tch0[147]]"
    "[tch0[148]]"
    mc "[tch0[149]]"
    mc "[tch0[150]]"
    n 5h "[tch0[151]]"
    "{i}[tch0[152]]{/i}"
    show natsuki at s32
    n 5s "[tch0[153]]"
    mc "[tch0[154]]"
    show natsuki zorder 2 at t32
    n 12c "[tch0[155]]"
    n "[tch0[156]]"
    mc "[tch0[157]]"
    show natsuki zorder 1 at thide
    hide natsuki
    "[tch0[158]]"
    "[tch0[159]]"
    "[tch0[160]]"
    show yuri 1a zorder 2 at t21
    mc "[tch0[161]]"
    y "[tch0[162]]"
    y "[tch0[163]]"
    mc "[tch0[164]]"
    show monika 4a zorder 2 at t22
    m "[tch0[165]]"
    show yuri at h21
    y 3n "[tch0[166]]"
    "[tch0[167]]"
    y 4b "[tch0[168]]"
    mc "[tch0[169]]"
    mc "[tch0[170]]"
    y 2u "[tch0[171]]"
    "[tch0[172]]"
    "[tch0[173]]"
    show yuri zorder 1 at thide
    hide yuri
    show monika zorder 2 at t11
    m 1 "[tch0[174]]"
    mc "[tch0[175]]"
    "[tch0[176]]"
    "[tch0[177]]"
    mc "[tch0[178]]"
    m 1j "[tch0[179]]"
    m 1b "[tch0[180]]"
    m "[tch0[181]]"
    show monika 1a
    mc "[tch0[182]]"
    mc "[tch0[183]]"
    mc "[tch0[184]]"
    mc "[tch0[185]]"
    m 5 "[tch0[186]]"
    m "[tch0[187]]"
    m "[tch0[188]]"
    m "[tch0[189]]"
    m 1b "[tch0[190]]"
    show monika 1a
    show sayori 3q zorder 2 at t31
    s "[tch0[191]]"
    show yuri 1 zorder 2 at t33
    "[tch0[192]]"
    show sayori zorder 1 at thide
    show yuri zorder 1 at thide
    hide sayori
    hide yuri
    mc "[tch0[193]]"
    mc "[tch0[194]]"
    m 3b "[tch0[195]]"
    m "[tch0[196]]"
    m "[tch0[197]]"
    m "[tch0[198]]"
    m "[tch0[199]]"
    m 2k "[tch0[200]]"
    m "[tch0[201]]"
    show monika 2a zorder 2 at t22
    show sayori 4r zorder 2 at t21
    s "[tch0[202]]"
    show monika zorder 2 at t33
    show sayori zorder 2 at t32
    show yuri 1a zorder 2 at t31
    y "[tch0[203]]"
    show monika zorder 2 at t44
    show sayori zorder 2 at t43
    show yuri zorder 2 at t42
    show natsuki 4d zorder 2 at t41
    n "[tch0[204]]"
    "[tch0[205]]"
    "[tch0[206]]"
    "[tch0[207]]"
    "[tch0[208]]"
    "[tch0[209]]"
    show sayori zorder 1 at thide
    show monika zorder 1 at thide
    show natsuki zorder 1 at thide
    show yuri zorder 2 at t32
    hide sayori
    hide monika
    hide natsuki
    y "[tch0[210]]"
    mc "[tch0[211]]"
    "[tch0[212]]"
    mc "[tch0[213]]"
    "[tch0[214]]"
    show natsuki 1c zorder 2 at t41
    "[tch0[215]]"
    "[tch0[216]]"
    show natsuki zorder 1 at thide
    hide natsuki
    y 3u "[tch0[217]]"
    mc "[tch0[218]]"
    "[tch0[219]]"
    "[tch0[220]]"
    mc "[tch0[221]]"
    y 1l "[tch0[222]]"
    "[tch0[223]]"
    y 1a "[tch0[224]]"
    y "[tch0[225]]"
    y 1f "[tch0[226]]"
    "[tch0[227]]"
    "[tch0[228]]"
    y 2m "[tch0[229]]"
    y "[tch0[230]]"
    y 2a "[tch0[231]]"
    y "[tch0[232]]"
    mc "[tch0[233]]"
    "[tch0[234]]"
    "[tch0[235]]"
    show monika 1d zorder 3 at f33
    m "[tch0[236]]"
    m "[tch0[237]]"
    show monika zorder 2 at t33
    show yuri zorder 3 at f32
    y 1a "[tch0[238]]"
    y "[tch0[239]]"
    y "[tch0[240]]"
    show yuri zorder 2 at t32
    show natsuki 5q zorder 3 at f31
    n "[tch0[241]]"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f32
    y 1f "[tch0[242]]"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5c "[tch0[243]]"
    "[tch0[244]]"
    n 5q "[tch0[245]]"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 1a "[tch0[246]]"
    show monika zorder 2 at t33
    show natsuki 1o zorder 3 at f31
    n "[tch0[247]]"
    n "[tch0[248]]"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 3b "[tch0[249]]"
    m "[tch0[250]]"
    show monika zorder 2 at t33
    show natsuki 1p zorder 3 at f31
    n "[tch0[251]]"
    n "[tch0[252]]"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 1j "[tch0[253]]"
    show monika zorder 1 at thide
    show yuri zorder 1 at thide
    hide monika
    hide yuri
    show natsuki 1r zorder 2 at t42
    show sayori 4q behind natsuki at l41
    s "[tch0[254]]"
    s "[tch0[255]]"
    show sayori behind natsuki at t21
    "[tch0[256]]"
    show natsuki at h42
    n 1v "{i}[tch0[257]]{/i}"
    show natsuki zorder 2 at t11
    show sayori zorder 1 at thide
    hide sayori
    mc "[tch0[258]]"
    n 1c "[tch0[259]]"
    n "[tch0[260]]"
    mc "[tch0[261]]"
    mc "[tch0[262]]"
    n 5q "[tch0[263]]"
    "[tch0[264]]"
    n "[tch0[265]]"
    mc "[tch0[266]]"
    show yuri 2f zorder 2 at t31
    y "[tch0[267]]"
    y "[tch0[268]]"
    y 2k "[tch0[269]]"
    y "[tch0[270]]"
    show natsuki zorder 1 at thide
    hide natsuki
    show monika 2a zorder 2 at t33
    m "[tch0[271]]"
    m "[tch0[272]], [tch0[273]]" # The 2 lines split off together, so i merged them.
    show yuri at s31
    y 3o "..." # Nothing is changed in this line. The tch0[274] line stays the same.
    mc "[tch0[275]]"
    show sayori 2g zorder 2 at t32
    s "[tch0[276]]"
    show sayori zorder 1 at thide
    show yuri zorder 1 at thide
    show monika zorder 1 at thide
    hide sayori
    hide yuri
    hide monika
    "[tch0[277]]"
    show monika 5a zorder 3 at f32
    m "[tch0[278]]"
    m "[tch0[279]]"
    show yuri 3e zorder 2 at t31
    show natsuki 2k zorder 2 at t33
    ny "...?" # Nothin is changed in this line. The tch0[280] line stays the same.
    "[tch0[281]]"
    m 2b "[tch0[282]]"
    m "[tch0[283]]"
    m "[tch0[284]]"
    show monika 2a zorder 2 at t32
    show natsuki zorder 3 at f33
    n 5q "[tch0[285]]"
    show natsuki zorder 2 at t33
    show yuri 3v zorder 3 at f31
    y "..." # nothin is changed in this line. same goes to above.
    show natsuki zorder 2 at t44
    show monika zorder 2 at t43
    show yuri zorder 2 at t42
    show sayori 4r at l41
    s "[tch0[287]]"
    show monika zorder 3 at f43
    m 1a "[tch0[288]]"
    m "[tch0[289]]"
    show monika zorder 2 at t43
    "[tch0[290]]"
    mc "[tch0[291]]"
    show monika zorder 3 at f43
    m 1d "[tch0[292]]"
    "[tch0[293]]"
    show monika zorder 2 at t43
    mc "[tch0[294]]"
    mc "[tch0[295]]"
    mc "[tch0[296]]"
    show monika 1g
    show sayori 1g
    show natsuki 4g
    show yuri 2e
    "[tch0[297]]"
    "[tch0[298]]"
    show monika at s43
    m 1p "[tch0[299]]"
    show yuri at s42
    y 2v "[tch0[300]]"
    show natsuki at s44
    n 5s "[tch0[301]]"
    show sayori at s41
    s 1k "[tch0[302]]"
    mc "[tch0[303]]"
    "[tch0[304]]"
    "[tch0[305]]"
    "[tch0[306]]"
    mc "[tch0[307]]"
    mc "[tch0[308]]"
    mc "[tch0[309]]"
    show monika 1e zorder 2 at t43
    show yuri 3f zorder 2 at t42
    show natsuki 1k zorder 2 at t44
    show sayori 4b zorder 2 at t41
    "[tch0[310]]"
    show sayori at h41
    s 4r "[tch0[311]]"
    "[tch0[312]]"
    mc "[tch0[313]]"
    show yuri zorder 3 at f42
    y 1m "[tch0[314]]"
    show yuri zorder 2 at t42
    show natsuki zorder 3 at f44
    n 5q "[tch0[315]]"
    show natsuki zorder 2 at t44
    show monika zorder 3 at f43
    m 5 "[tch0[316]]"
    m "[tch0[317]]"
    show monika zorder 2 at t43
    mc "[tch0[318]]"
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    show sayori zorder 1 at thide
    show monika zorder 2 at t11
    hide yuri
    hide natsuki
    hide sayori
    m 3b "[tch0[319]]"
    m "[tch0[320]]"
    m "[tch0[321]]"
    m "[tch0[322]]"
    "[tch0[323]]"
    m 1a "[tch0[324]]"
    show monika 5 at hop
    m "[tch0[325]]"
    mc "[tch0[326]]"
    show monika zorder 1 at thide
    hide monika
    "[tch0[327]]"
    "[tch0[328]]"
    "[tch0[329]]"
    show sayori 1a2 zorder 2 at t11
    s "[tch0[330]]"
    "[tch0[331]]"
    mc "[tch0[332]]"
    s 4q "[tch0[333]]"

    scene bg residential_day
    with wipeleft_scene

    "[tch0[334]]"
    "[tch0[335]]"
    show sayori 1a2 zorder 2 at t41
    "Sayori," # Nothing is changed
    show natsuki 4 zorder 2 at t42
    "Natsuki," # ^ same as above ^
    show yuri 1 zorder 2 at t43
    "Yuri," # ^ same as above ^
    show monika 1 zorder 2 at t44
    "[tch0[339]]"
    "[tch0[340]]"
    "[tch0[341]]"
    hide sayori
    hide natsuki
    hide yuri
    hide monika
    with wipeleft
    "[tch0[342]]"
    "[tch0[343]]"
    "[tch0[344]]"
     

    return
