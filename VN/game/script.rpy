# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define N = Character('Nova', color="#0066FF")
define S = Character('Shawn', color="#33CC33")
define A = Character('Alex', color="#3FCCFF")
image cNova = "images/CNova.png"
image cShawn = "images/CShawn.png"
image BG = "images/BG.jpg"
image cAlex = "images/CAlex.png"
image tavernBG = "images/tavernBG.jpg"

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

    show cAlex at left
    A "idiots..."
    
    pause .5
    
    scene tavernBG
    with Dissolve(.5)
    show cShawn at right
    S "I don't see any artists anywhere... do you?"
    
    show cNova at center
    N "Nope.. why did we go to a tavern to look for talent?"
    
    show cAlex at left
    A "Hey! There's my old G rank hunter buddy! Hey let's go hunt an Agnaktor!"
    
    "SHUT THE HELL UP!!"
    
    A "ghey.."
              
    return
