# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define N = Character('Nova', color="#0066FF")
define S = Character('Shawn', color="#33CC33")
define A = Character('Alex', color="#3FCCFF")
define H = Character('G Rank Hunter', color="#000000")
define Sol = Character('Sola', color="#33CC33")
image cNova = "images/CNova.png"
image cShawn = "images/CShawn.png"
image cSola = "images/cSola.png"
image BGWhose1 = "images/BGWhose1.png"
image BGWhose2 = "images/BGWhose2.png"
image BG = "images/BG.jpg"
image BGstars = "images/BGstars.jpg"
image cAlex = "images/CAlex.png"
image cHunter = "images/cHunter.png"                             
image tavernBG = "images/tavernBG.jpg"
image Agnaktor = "images/Agnaktor.png"
image volcanoBG = "images/volcanoBG.jpg"
image attack999 = "images/-999.png"
image alchemy = "images/alchemyCircle.png"

# The game starts here.
label start:
    # Start the background music playing.
    play music "music/themesong.mp3"
    
    scene BGstars
    "Promise me!!"
    "Promise me that you will come back alive."
    show cSola at right
    Sol "Please promise me this!"
    N "I..."
    "( Nova breaths out then smiles)"
    N "I promise I'll come back for you"
    pause (2) 
    with Dissolve (20) 
    
    scene BG
    "Ugh my head...."
    "What was that?"
    "Was it a dream..."
return