# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define N = Character('Nova', color="#0066FF")
define S = Character('Shawn', color="#33CC33")
define A = Character('Alex', color="#3FCCFF")
define H = Character('G Rank Hunter', color="#000000")
image cNova = "images/CNova.png"
image cShawn = "images/CShawn.png"
image BGWhose1 = "images/BGWhose1.png"
image BGWhose2 = "images/BGWhose2.png"
image BG = "images/BG.jpg"
image cAlex = "images/CAlex.png"
image cHunter = "images/cHunter.png"                             
image tavernBG = "images/tavernBG.jpg"
image Agnaktor = "images/Agnaktor.png"
image volcanoBG = "images/volcanoBG.jpg"
image attack999 = "images/-999.png"
image alchemy = "images/alchemyCircle.png"

# The game starts here.
label start:
    
    scene BG
    show cNova at left
    N "Shawn! We are creating a game! ...However.."
    hide cNova
    
    # Start the background music playing.
    play music "music/Calmme.mp3" 
    
    show cShawn at right
    S "What? Oh ya! We need an artist!!"
    hide cShawn

    show cNova at center
    N "Ya! Let's find him/her!"
    
    show cShawn at right behind cNova
    S "Gotcha~"

    show cAlex at left behind cNova
    A "idiots..."
    
label tavern:
    
    pause .5
    
    scene tavernBG
    with Dissolve(.5)
    show cShawn at right
    S "I don't see any artists anywhere... do you?"
    
    show cNova at center
    N "Nope.. why did we go to a tavern to look for talent?"
    
    show cAlex at left behind cNova
    A "Hey! There's my old G rank hunter buddy! Hey let's go hunt an Agnaktor!"
    
    "SHUT THE HELL UP!!"
    
    A "ghey.."
    hide cAlex
    hide cNova
    hide cShawn
    stop music 
                                                        
    pause .5                                                    
   
   # Start the background music playing.
    play music "music/battle.mp3"
   
    show cHunter at center
    H "you guys wanna go?"
    
    pause .5
    stop music
    
    scene BG
    with Dissolve(.5)
    play music "music/Calmme.mp3"
    show cShawn at right
    S "Well.. that didn't go to well..."
    
    show cNova at center
    N "Ya that kind of sucked... Should we keep trying?"
    
    menu:
        "Yes, let's find an artist!":
            jump choice1_yes
        
        "No... I give up.":
            jump choice1_no
        
label choice1_yes:
    $menu_flag = True
    
    show cAlex at left behind cNova
    A "Ughh... of course you want to keep trying..."
    
    jump choice1_done
    
label choice1_no:
    $menu_flag = False
    
    show cAlex at left behind cNova
    A "Thank you! Now let's go back to monster hunter!"
    
    jump choice1_done

label choice1_done:
    if menu_flag:
        jump tavern
    else :
        pause .5
        scene BG
        with Dissolve(.5)
        stop music
        play music "music/battle.mp3"
        show cAlex at left
        A "AGNAKTOR!! I'M COMING FOR YOU BITCH!!"
        
        show cHunter at right
        H "YA MOTHER FUCKER, LETS GO!!"
        
        stop music
        scene BGWhose1
        with Dissolve(.5)
        play sound "music/Swhosethat1.mp3"
        
        "Who's that Pokemon?"
        
        pause .5
        
        stop sound
        scene BGWhose2
        with Dissolve(.5)
        play sound "music/Swhosethat2.mp3"
        
        "It's Ahhggammeeruuaahhgggaaughh!!"
        
        pause .5
        
        scene volcanoBG
        with Dissolve(.5)
        
        play music "music/AgnaktorBattle.mp3"
        
        pause .5
        
        play sound "music/AgnaktorRoar.mp3"
        
        show Agnaktor at left
        "Agnaktor" "ROOOOOAAARRRR!"
        
        pause .5
        
        show cAlex at right
        show cHunter at right behind cAlex, Agnaktor:
            xalign .8 yalign .3
        A "Here we go, cool drinks up buddy!"
        H "Already on it!"
        
        show Agnaktor:
            xalign 0.0 yalign 0.5
            linear 0.5 xalign 0.5
            linear 0.5 xalign 0.0
            xalign 0.0
            
        pause 1.0
        show attack999:
            xalign .8 yalign .1
        pause .5
            
        H "Aghh!..."
            
        show cHunter behind cAlex, Agnaktor:
            linear 2.0 xalign 2.0
        hide attack999
        
        H "FUCK...sorry bud... i'm done... ugh.."
        
        A "Pshh.. call yourself G rank?... "
        
        A "I'll show you how it's done."
        
        show alchemy:
            xalign 0.5 yalign 0.5
            zoom 1.0 alpha 0.25 rotate 0 xanchor 0.5 yanchor 0.5
            linear 1.0 zoom 1.3 alpha 1.0 rotate 180
            linear 1.0 zoom 1.0 alpha 0.25 rotate 360
            repeat
        
        A "Shingarau No Pistaratta Mischal Porava!"
        
        show Agnaktor:
            block:
                choice:
                    linear 0.5 xalign 0.0
                choice:
                    linear 0.5 xalign 0.1
                choice:
                    linear 0.5 yalign 0.5
                choice:
                    linear 0.5 yalign 0.6
                choice:
                    linear 0.5 yalign 0.4
                repeat
    play sound "music/AgnaktorRoar.mp3"
    "Agnaktor" "RAAGGHHHH!!!"
    
    show alchemy:
        alpha 1.0
        linear 2.0 zoom 3.0
        
    A "DIEE!!!"
    
    show Agnaktor:
        linear 1.0 xalign -2.0
        
    play sound "music/AgnaktorRoar.mp3"
    "Agnaktor" "Grrraahhh!"
    
    hide alchemy
    hide cHunter
    hide Agnaktor
    
    A "Alright... now we can actually find an artist..."
        
return
















