# The script of the game goes in this file.
$import subprocess

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Serena", color = "#ffff00")
define t = Character("Donovan", color = "#d3d3d3")
define k = Character("Miki")
define l = Character("Leroy")
define u = Character("???")
define c = Character("Juno", color = "0xff0000")
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
#scene hallway

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.


    "Hey check that out over there"
    "*A few tables with chairs and people surrounding them are present just ahead*"
    "*There are also chess boards between the people, it must be a chess club or something*"
    "*A perky seemingly young girl approaches you as you approach the tables*"

#show s happy

#u "Hey there! Interested in playing some chess?"
#u "HELLLOOOOOOOO!!"
u "Hey there, what's your name?"
$mainCharacter = renpy.input("What is your name?")
define y = Character("[mainCharacter]")

s "Nice to meet you [y], I'm [s]. I love your shoes by the way!"
y "Thanks, I like your..."
"Like her what? Say something witty!"
menu:
   "Shoes":
       jump shoes
   "Outfit":
       jump outfit
   "Eyes":
       jump eyes

label shoes:
     s "Aww thanks! I just bought them the other day!"
     jump invite
label outfit:
      s "Oh this old thing? I just threw it on."
      jump invite
label eyes:
       s "Aww stop you're gonna make me blush!"
       jump invite
label invite:
s "You wanna come and play some chess? No boards are free but you can come and watch if you like."
y "Sure why not, I love chess."
"*You take a seat next to [s] and you both intently watch one of the games going on.*"

u "Bro you are doo doo man can't you make a good move?"
u "Yo look who's talking man you're down two pawns!"
"*You lean over and whisper to [s]"
y "Who are these two?"
s "[t] and [l], don't let them scare you, they just love giving each other crap when they play."
t "Yo hurry up and lose already we got people waiting to play."
"*A couple of minutes pass and many moves are made before [t] yells out"
t "Checkmate bitch!"
l "Barely counted man I was distracted."
t "Whatever man just shake my damn hand."
"*They shake hands and turn their attention towards you*"
show ty question
show lenny listening

t "Hey wassup, you enjoy the game?"
y "Yeah that was a pretty impressive checkmate."
l "Don't gush he's not that good he got lucky."
t "Quit being so salty bro."
l "Yeah, yeah."
l "I gotta go study so I'll see you all later."
t "See ya."
s "Bye [l]!"
y "He seems nice."
t "Only when he's winning."
t "Anyway sorry about that, uhh."
s "[y]!"
t "Right, [y], good to meet you."
t "Oh, and welcome to the chess club."
s "Yayy new member!"
y "Well thanks, I'm happy to be a part of it, but don't I have to play chess to be in the club?"
t "Actually yeah, after all this is the chess club, not the loiterers club."
y "Damn, well after that display I'm not sure how good I would do."
t "It's alright, everyone here sucks their fair share of ass."
t "Start off against [s], she will give you a good game-"
s "Aww thanks!"
t "- In determining how good you are."
s "What is that supposed to mean??"
t "It means that if you get beat I'll have a pretty good idea of the skill level of our new friend here."
s "Oh yeah?? Well I'm gonna win you'll see!"
y "Hold on, I have to play a game right now?"
t "Yep, good luck"
s "Hope you're ready! <3"
$ playerWon = false
$subprocess.Popen("C:\Users\RIDENTEM\Downloads\checkOnYourHeart\checkOnMyHeart\game\chess.exe")

$gamesWon = open("gamesWon.txt", 'r')
$game1Result = gamesWon.readline().rstrip()
if (game1Result == "true"):
     s "Wow you aren't bad, nice win!"
if(game1Result == "false"):
     s "Yes!! I won!! Take that!"
     "[s] begins jumping up and down with elation"
     t "Alright [s] that's enough, congratulations on that win though"
"That took awhile, it's already late"
y "Crap! I got class now, I gotta go!"
s "I'll see you later!"
t "See you around"
"*You head to a dull class filled with unenthusiastic students as well as others who slept through the entirety of the lecture*"
"*...*"
"*The lecture ends and you go straight home*"
"Today was fun, especially the chess club. I can't wait to go back tomorrow"
"*The next day*"
"*You arrive at the school unharried and with newfound enthusiasm and excitement*"
"*You can't help but smile at the thought of those interesting characters playing chess again*"
"*You approach the chess table once again and [s] runs up and greets you just as she did yesterday*"
s "Helllooooo [y]!"
y "Hello [s], how's it going?"
s "Just swell thanks, care to play some chess?"
y "Maybe later, I wanted to watch today and try to learn."
s "Then come on over! You can sit next to me."
"*You both walk over to the table and see [t] well established playing some music and overseeing the group.*"
"*As you approach [t] greets you*"
t "What's up [y], good to see you."
y "Hey [t]."
"*You take a seat next to [s], and watch one of the games unfold.*"
"*Ty gets closer to you and says something, but it is inaudible among the excitement*"
"*You beckon him to repeeat himself and he moves closer, inches from your face*"
t "I said, do you play chess often?"
y "N-not really, that was the first game I have played in a long time."
t "Yesterday against [s]?"
y "Yeah, that one."
t "That was a pretty good game, you played well."
y "Heh, thanks."
t "Do you want to play me?"
y "I don't know, I always get nervous about facing people better than me."
t "You don't know if I am better than you though."
y "I guess we will have to find out won't we?"
t "That's what I like to hear, let's play some chess baby!"
#start next match

$game2Result = gamesWon.readline().rstrip()
if(game2Result == "true"):
    t "Good game."
if game2Result == "false":
    t "Ah fuck I lost."


u "[t] shut up you're trash."
t "Right on time, [y] this is [c], just a good friend."
c "Hey! Nice to meet you."
y "You too. You play chess too?"
c "Eh only sometimes, nowhere near as much as these other nerds."
t "Hey! We play to win baby we're winners."
c "Exactly what someone obsessed with winning would say."
t "What EXACTLY are you doing here anyway? I thought your classes got cancelled?"
c "I came because I enjoy speaking to my good friends here [t]"
t "Well we love talking to you too, but- "
"*They both pause and stare into the distance down the hallway*"
c "You see that?"
t "Yeah I saw that"
t "What do you think?"
#"*[s] shoots you and [t] a dirty look*"
c "10, for sure."
t "No way bump a few down for the hair."
c "The hair is the best part what's wrong with you."
y "Uh am I missing something?"
c "Sorry I can't help myself sometimes."
c "Honesty is the best policy you know?"
t "True."
y "It's interesting, usually people aren't so honest."
t "We are all friends here, no need to hide anything."
c "Guys I'm gonna get going, it's getting late."
"She is right, it's getting dark out again."
t "Are you leaving too [y]?"
menu:
   "Actually...":
      jump walkMe
   "Yeah, see everyone later!":
      jump goHome

label goHome:
     "*You head home and look forward to sleeping*"
     jump day3
label walkMe:
     y "You wanna walk me outside?"
     t "Sure, let me grab my coat."
     s "Can I come?"
     t "No, you stay here and watch the chess stuff, you are the only trustworthy person here."
     s "UGGHH fine."
     "*[t] grabs their coat and you both head outside"
#Change background to outside
t "Dammit it's cold out here."
y "Come on it's not that bad, my coat isn't even as heavy as yours."
t "There's ice and snow all over the place!"
y "Don't slip and fall, heh."
"*[t] grabs your hand and holds it tight*"
t "Now if I fall we both go down."
"*[t]'s hand is warm in yours*"
y "Heh, I suppose so."
t "I'm still freezing dude."
"*[t] brings your hand to his lips and blows warm air and rubs your hand in his.*"
"*The warmth of his breath is comforting, and you blush slightly."
y "Ahem, I think the bus is coming."
"*You see the bus approaching in the distance*"
t "By the way, I meant to ask but what made you want to stop by the club?"

menu:
      "You..":
         jump tFlirt
      "I love chess!":
         jump chessFlirt
label chessFlirt:
     t "Yeah me too. Chess is great, but there are some things better, you know?"
     "*Before you have a chance to say something else the bus pulls up in front of you both and you say goodbye.*"
     "*You get on the bus and are headed home.*"
     jump goHome
label tFlirt:
     t "Oh shit haha."
     "*[t] blushes slightly and has difficulty hiding it*"
     t "Well I'm flattered"
     "*The bus arrives and opens its doors"
     "*[t] gives you a hug and says goodbye*"
     jump goHome

    #block of code to run

label day3:
"*You arrive at school yet again, excited to see all the people in the chess club once again.*"
"*As you approach the tables [t], [s], and [l] are at the tables along with someone you have not seen yet*"
"*[s], as she usually does, greets you with unbridled enthusiasm*"
s "Hey [y]! We were just talking about you!"
y "Oh really? Good things I hope haha."
t "Nothing but good things, we were talking about your chess game."
t "[l] wants to play you."
u "So the prodigy finally appears!"
t "[y], this is [k], the president of the club."
k "Good to finally meet you, I've heard a lot about you."
y "All good I hope, hehe."
k "Just that you been playing some interesting games lately."
k "You wanna play me?"
l "Hell no I got first dibs"
k "Fine fine, I'll wait it out."
l "Hold on I want to get to know my enemy just a little more before we play."
l "It will break the ice so you aren't so nervous."
l "How about some twenty questions?"
y "I'm fine with that."
l "Okay, what's your favorite food?"
y "Donuts, next"
l "Favorite flavor?"
y "Glazed, next"
l "What is your favorite color?"
menu:
    "Blue":
        jump colorQuestion

    "Yellow":
        jump colorQuestion

    "Green":
        jump colorQuestion

    "Red":
        jump colorQuestion
label colorQuestion:
"*Everyone pays very close attention to your responses, as though making an extra effort to remember what you say*"
l "Alright, lets try something else."
l "Out of all the people here, who would you want to kiss?"
k "Whoa [l]! That's too personal! Don't put them on the spot like that."
l "Hey we're all friends here, no need to hide anything is there?"
y "Well..."
menu:
      "[t]":
         jump tKiss
      "[s]":
         jump sKiss
      "[k]":
         jump kKiss
      "[l]":
         jump lKiss

label tKiss:
     s "WHAT?? I mean, I don't care pft."
     t "Damn I'm flattered hahaa."
     l "Oh I see how it is, damn I'll make sure I get you two a room."
     k "Nice."

label lGame:
    y "I wasn't really expecting all this attention, do you have enough info now? Can we play [l]?"
    l "Yeah let's get it on. Hope you're ready!"
    y "As ready as I'll ever be"
    l "Cool, lets set things up then."
    $subprocess.Popen("C:\Users\RIDENTEM\Downloads\checkOnYourHeart\checkOnMyHeart\game\chess.exe")

    # This ends the game.

return
