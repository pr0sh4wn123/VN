# You can place the script of your game in this file.
# the start label.
    
# Declare images below this line, using the image statement.
image cNova = "images/CNova.png"
image cShawn = "images/CShawn.png"
image cSola = "images/cSola.png"
image BGWhose1 = "images/BGWhose1.png"
image BGWhose2 = "images/BGWhose2.png"
image BG = "images/BG.jpg"
image BGtheme = "images/Sunrider.jpg"
image BGstars = "images/BGstars.jpg"
image BGoffice = "images/BGoffice.jpg"
image cAlex = "images/CAlex.png"
image cHunter = "images/cHunter.png"                             
image tavernBG = "images/tavernBG.jpg"
image Agnaktor = "images/Agnaktor.png"
image volcanoBG = "images/volcanoBG.jpg"
image attack999 = "images/-999.png"
image alchemy = "images/alchemyCircle.png"
image sunriderx = "images/SunriderX.png"

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
define slowdissolve = Dissolve(1.0)

# The game starts here.
scene BGtheme
label start:
    scene BGtheme
    # Start the background music playing.
    play music "music/themeMyHeart.mp3"
    "EPISODE 1A - THE SAGA CONTINUES"
    stop music 
    pause (.5)
    
    # Start the background music playing.
    play music "music/themesong.mp3"
    
    scene BGstars
    with Dissolve(.5) 
    "Promise us!!"
    "Promise us that you will come back alive."
    show cSola at right
    Sol "Please atleast promise me this!"
    Mys "I..."
    "( ??? breaths out, then smiles)"
    Mys "I promise, I'll come back"
    pause (.5)

    scene BGoffice
    with Dissolve(.5) 
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
    Av "Commander! sorry to wake you but we have the Admiral Grey on the line"
    Av "He wishes to speak with you"
    Kay "Very well. Patch him through."
    "(Commander Kayoto picks up the phone)"
    play music "music/Background.mp3"
    
    Kay "Hello Admiral, its been some time since we last spoke."
    
    "Adm. Grey -yes, and i'm afraid this wont be our last."
    Kay "What seems to be the problem Admeral"
    
    "Adm. Grey -It appears we need to call upon the Sunrider and its Ryders once more"
    Kay "how can we assist?"
    
    "Adm. Grey -As you might be aware, the Alliance pushed far into PACT'S space. However, we are having a pesky problem that we have no doupt that the Sunrider can handle"
    "Adm. Grey -We, here in the Alliance, will pay you and your crew just as we had before."
    
    Kay "Alright Admiral you have my attention."
    "adm. Grey -I'm sending you some documents now."
    "these photos contain an image of an elite fleet that has no doubt been troubling our fleet for a few weeks now."
    Kay "I thought the Legion was the last of the PACTS elite force"
    "Adm. Grey -As did we."
    "Adm. Grey -It appears that out of desperation, The PACT pulled one last trick out of their sleeves."
    Kay "How come intel hasnt notice this fleet sooner?"
    "Adm. Grey -They must have kept them in hiding untill now."
    Kay "What do we know of them so far?"
    "Adm. Grey -Sadly nothing, every encounter we had with this fleet turns out to be a disaster."
    "Adm. Grey -We have no intel on it other than they exist and are causing havoc on out main lines."
    Kay "This fleet looks like an ordinary PACT fleet to me."
    Kay "How can they be causing ou trouble?"
    "Adm. Grey -Thats not all of them."
    "Adm. Grey -The next image may spark your intrest."
    show sunriderx at left
    "(Kayoto's heart sinks down his chest, while he clenches his fist.)"
    Kay "how is this possible? (he mumbles)."
return 