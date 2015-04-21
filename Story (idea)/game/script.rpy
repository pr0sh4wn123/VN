# You can place the script of your game in this file.
# the start label.

# Here we define the backgrounds that are used.
play music "music/memory.mp3"
    
# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define N = Character('Nova', color="#0066FF")
define Kay = Character('Kayoto', color="#000000")
define Av = Character('Ava', color ="#3FCCFF")
define Mys = Character('???', color="#000000")
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
image BGoffice = "images/BGoffice.jpg"
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
    Mys "I..."
    "( ??? breaths out, then smiles)"
    Mys "I promise, I'll come back for you"
    pause (2) 
    with Dissolve (8) 

    scene BGoffice
    "Ugh my head...."
    "What was that?"
    "Was it a dream..."
    stop music 
    pause (.5)
    "..."
    
    queue sound "music/Dingsound.mp3"
    pause (1)
    "(door rings)"
    Kay "come in!"
    Av "Commander! sorry to wake you but we have the Adm. Grey on the line"
    Av "He wishes to speak with you"
    Kay "Very well. Patch him through."
    "(Commander Kayoto pick up the phone)"
    play music "music/Background.mp3"
    
    Kay "Hello admeral, its been some time since we last spoke."
    
    "Adm. Grey - yes it i'm afraid this wont be our last."
    Kay "what seems to be the problem Admeral"
    
    "Adm. Grey - it appears we need top call upon the Sunrider and its Ryders once more"
    Kay "how can we assist?"
    
    "Adm. Grey - As you might be aware, the Alliance pushed far into PACT'S space and we are having a pesky problem that we have no doupt that the Sunrider can handle"
    
return