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
    N "{color=#000000}Shawn! We are creating a game! ...However.."
    hide cNova
    
    # Start the background music playing.
    play music "music/Calmme.mp3" 
    
    show cShawn at right
    S "{color=#000000}What? Oh ya! We need an artist!!"
    hide cShawn

    show cNova at center
    N "{color=#000000}Ya! Let's find him/her!"
    
    show cShawn at right behind cNova
    S "{color=#000000}Gotcha~"

    show cAlex at left behind cNova
    A "{color=#000000}idiots..."
    
label tavern:
    
    pause .5
    
    scene tavernBG
    with Dissolve(.5)
    show cShawn at right
    S "{color=#000000}I don't see any artists anywhere... do you?"
    
    show cNova at center
    N "{color=#000000}Nope.. why did we go to a tavern to look for talent?"
    
    show cAlex at left behind cNova
    A "{color=#000000}Hey! There's my old G rank hunter buddy! Hey let's go hunt an Agnaktor!"
    
    "SHUT THE HELL UP!!"
    
    A "{color=#000000}ghey.."
    hide cAlex
    hide cNova
    hide cShawn
    stop music 
                                                        
    pause .5                                                    
   
   # Start the background music playing.
    play music "music/battle.mp3"
   
    show cHunter:
        xalign -0.2
        yalign 2.0
    H "{color=#000000}you guys wanna go?"
    
    pause .5
    stop music
    
    scene BG
    with Dissolve(.5)
    play music "music/Calmme.mp3"
    show cShawn at right
    S "{color=#000000}Well.. that didn't go to well..."
    
    show cNova at center
    N "{color=#000000}Ya that kind of sucked... Should we keep trying?"
    
    menu:
        "{color=#000000}Yes, let's find an artist!":
            jump choice1_yes
        
        "{color=#000000}No... I give up.":
            jump choice1_no
        
label choice1_yes:
    $menu_flag = True
    
    show cAlex at left behind cNova
    A "{color=#000000}Ughh... of course you want to keep trying..."
    
    jump choice1_done
    
label choice1_no:
    $menu_flag = False
    
    show cAlex at left behind cNova
    A "{color=#000000}Thank you! Now let's go back to monster hunter!"
    
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
        A "{color=#000000}AGNAKTOR!! I'M COMING FOR YOU BITCH!!"
        
        show cHunter at right
        H "{color=#000000}YA MOTHER FUCKER, LETS GO!!"
        
        stop music
        scene BGWhose1
        with Dissolve(.5)
        play sound "music/Swhosethat1.mp3"
        
        "{color=#000000}Who's that Pokemon?"
        
        pause .5
        
        stop sound
        scene BGWhose2
        with Dissolve(.5)
        play sound "music/Swhosethat2.mp3"
        
        "{color=#000000}It's Ahhggammeeruuaahhgggaaughh!!"
        
        pause .5
        
        scene volcanoBG
        with Dissolve(.5)
        
        play music "music/AgnaktorBattle.mp3"
        
        pause .5
        
        play sound "music/AgnaktorRoar.mp3"
        
        show Agnaktor at left
        "{color=#000000}Agnaktor" "{color=#000000}ROOOOOAAARRRR!"
        
        pause .5
        
        show cAlex at right
        show cHunter at right behind cAlex, Agnaktor:
            xalign .8 yalign .3
        A "{color=#000000}Here we go, cool drinks up buddy!"
        H "{color=#000000}Already on it!"
        
        show Agnaktor:
            xalign 0.0 yalign 0.5
            linear 0.5 xalign 0.5
            linear 0.5 xalign 0.0
            xalign 0.0
            
        pause 1.0
        show attack999:
            xalign .8 yalign .1
        pause .5
            
        H "{color=#000000}Aghh!..."
            
        show cHunter behind cAlex, Agnaktor:
            linear 2.0 xalign 2.0
        hide attack999
        
        H "{color=#000000}FUCK...sorry bud... i'm done... ugh.."
        
        A "{color=#000000}Pshh.. call yourself G rank?... "
        
        A "{color=#000000}I'll show you how it's done."
        
        show alchemy:
            xalign 0.5 yalign 0.5
            zoom 1.0 alpha 0.25 rotate 0 xanchor 0.5 yanchor 0.5
            linear 1.0 zoom 1.3 alpha 1.0 rotate 180
            linear 1.0 zoom 1.0 alpha 0.25 rotate 360
            repeat
        
        A "{color=#000000}Shingarau No Pistaratta Mischal Porava!"
        
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
    "{color=#000000}Agnaktor" "{color=#000000}RAAGGHHHH!!!"
    
    show alchemy:
        alpha 1.0
        linear 2.0 zoom 3.0
        
    A "{color=#000000}DIEE!!!"
    
    show Agnaktor:
        linear 1.0 xalign -2.0
        
    play sound "music/AgnaktorRoar.mp3"
    "{color=#000000}Agnaktor" "{color=#000000}Grrraahhh!"
    
    hide alchemy
    hide cHunter
    hide Agnaktor
    
    A "{color=#000000}Alright... now we can actually find an artist..."
        
return
















