# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define N = Character('Nova', color="#0066FF")
define S = Character('Shawn', color="#33CC33")
image cNova = "images/CNova.png"
image cShawn = "images/CShawn.png"
image BG = "images/BG.jpg"

# The game starts here.
label start:
    
    scene BG
    show cNova at left
    N "Shawn! We are creating a game! ...However.."
    hide cNova
    
    show cShawn at right
    S "What? Oh ya! We need an artist!!"
    hide cShawn

    show cNova at center
    N "Ya! Let's find him/her!"
    
    show cShawn at right behind cNova
    S "Gotcha~"
    
    
    
    return
