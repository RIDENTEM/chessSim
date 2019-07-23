# The script of the game goes in this file.
$import subprocess
init python:
    def _shout(str):
        ret = str.upper()
        return ret
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Serena", color = "#ffff00")
image sNorm = "sNorm.png"
define t = Character("Donovan", color = "#d3d3d3")
image dNorm = "images/dNorm.png"
define k = Character("Miki", color = "#000080")
image mNorm = "images/mNorm.png"
define l = Character("Leonardo")
image lNorm = "images/lNorm.png"
define u = Character("???")
define c = Character("Juno", color = "#ff0000")
image jNorm = "images/jNorm.png"
# The game starts here.
define sLove = 0
define tLove = 0
define lLove = 0
define kLove = 0
define chessLove = 0



label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene pov chess
#scene hallway

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.

    "Hey check that out over there"
    "A few tables with chairs and people surrounding them are present just ahead"
    "There are also chess boards between the people, it must be a chess club or something"
    "A perky seemingly young girl approaches me as I approach the tables"

#show s happy

#u "Hey there! Interested in playing some chess?"
#u "HELLLOOOOOOOO!!"
show sNorm with easeinleft
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
       $sLove += 1
       jump invite
label invite:
s "You wanna come and play some chess? No boards are free but you can come and watch if you like."
y "Sure why not, I love chess."
"I take a seat next to [s] and we both intently watch one of the games going on."

show sNorm at left
play music "chessClub.wav"

u "Bro you are doo doo man can't you make a good move?"

u "Yo look who's talking man you're down two pawns!"
"You lean over and whisper to [s]"
#try a whisper function here
y "Who are these two?"
s "[t] and [l], don't let them scare you, they just love giving each other crap when they play."
t "Yo hurry up and lose already we got people waiting to play."
"A couple of minutes pass and many moves are made before [t] yells out"
show dNorm
#$tCheck = _shout("Checkmate bitch!")
t "Checkmate bitch!"
#show ty as a sprite
show lNorm at right
l "Barely counted man I was distracted."
#bring up Lenny as a sprite

t "Whatever man just shake my damn hand."
"They shake hands and turn their attention towards me"

t "Hey wassup, you enjoy the game?"
y "Yeah that was a pretty impressive checkmate."
l "Don't gush he's not that good he got lucky."
t "Quit being so salty bro."
l "Yeah, yeah."
l "I gotta go study so I'll see you all later."
t "See ya."
s "Bye [l]!"
hide lNorm with easeoutright
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
s "{cps=*2}Aww thanks!{/cps}"

t "- In determining how good you are."
s "{cps=*2}What is that supposed to mean??{/cps}"
t "It means that if you get beat I'll have a pretty good idea of the skill level of our new friend here."
s "{cps=*2}Oh yeah?? Well I'm gonna win you'll see!{/cps}"
y "Hold on, I have to play a game right now?"
t "Yep, good luck"
s "Hope you're ready! <3"
$playerVersing = open("versing.txt", "w+")
$playerVersing.write("S")
$playerVersing.close()

#This is where the chess game would be played
$playerVersing = open("versing.txt","w+").close()
$playerVersing = open("versing.txt","w+")
$playerVersing.write("S")
$playerVersing.close()
#$subprocess.Popen("C:\Users\RIDENTEM\Downloads\checkOnYourHeart\checkOnMyHeart\game\chess.exe")

"THIS IS WHERE A CHESS GAME WOULD TAKE PLACE, IT IS ASSUMED THE PLAYER LOST."

#$gamesWon = open("gamesWon.txt", 'r')
#$gamesWon = open("gamesWon.txt", "r+")
#$gamesWon = open("C:\Users\RIDENTEM\Downloads\chessSim\checkOnYourHeart\checkOnMyHeart\game\gamesWon.txt", "r+")

#$game1Result = gamesWon.readline().rstrip()
$game1Result = "False"

if (game1Result == "True"):
     s "Wow you aren't bad, nice win!"
if(game1Result == "False"):
     s "Yes!! I won!! Take that!"
     "[s] begins jumping up and down with elation"
     t "Alright [s] that's enough, congratulations on that win though."
"That took awhile, it's already late"
y "Crap! I got class now, I gotta go!"
s "I'll see you later!"
t "See you around."
stop music
"I head to my dull class filled with unenthusiastic students as well as others who slept through the entirety of the lecture."
"..."
"The lecture ends and I go straight home."
"Today was fun, especially the chess club. I can't wait to go back tomorrow."
"Day 2"
"I arrive at the school unharried and filled with newfound enthusiasm and excitement."
"I can't help but smile at the thought of those interesting characters playing chess again."
"I approach the chess table once again and [s] runs up and greets me just as she did yesterday."
play music "chessClub.wav"
s "Helllooooo [y]!"
y "Hello [s], how's it going?"
s "Just swell thanks, care to play some chess?"
y "Maybe later, I wanted to watch today and try to learn."
s "Then come on over! You can sit next to me."
"We both walk over to the table and see [t] well established playing some music and overseeing the group."
"As you approach [t] greets you."
t "What's up [y], good to see you."
y "Hey [t]."
"I take a seat next to [s], and watch one of the games unfold."
"Ty gets closer to me and says something, but it is inaudible among the excitement"
"You ask him to repeat himself and he moves closer, inches from your face."
t "I said, do you play chess often?"
y "N-not really, that was the first game I played in a long time."
t "Yesterday against [s]?"
y "Yeah, that one."
t "That was a pretty good game, you played well."
y "Heh, thanks."
t "Do you want to play me?"
y "I don't know, I always get nervous about facing people better than me."
t "You don't know if I'm better than you though."
y "I guess we'll have to find out won't we?"
t "That's what I like to hear, let's play some chess baby!"
#start next match
$playerVersing = open("versing.txt", 'w').close()
$playerVersing = open("versing.txt", 'w')
$playerVersing.write("T")
$playerVersing.close()

#$subprocess.Popen("C:\Users\RIDENTEM\Downloads\checkOnYourHeart\checkOnMyHeart\game\chess.exe")
"THIS IS WHERE A CHESS GAME WOULD TAKE PLACE, IT IS ASSUMED THE PLAYER LOST."

#$game2Result = gamesWon.readline().rstrip()
$game2Result = "False"

if(game2Result == "True"):
    t "Ah crap I lost."
if game2Result == "False":
    t "Good game."
u "[t] shut up you're trash."
t "Right on time, [y] this is [c], just a good friend."
c "Hey! Nice to meet you."
y "Likewise. You play chess too?"
c "Only sometimes. Nowhere near as much as these other nerds."
t "Hey! We play to win baby we're winners."
c "Exactly what someone obsessed with winning would say."
t "What EXACTLY are you doing here anyway? I thought your classes got cancelled?"
c "I came because I enjoy speaking to my good friends here [t]."
t "Well we love talking to you too, but- "
"They both pause and stare into the distance down the hallway"
c "You see that?"
t "Yeah I saw that."
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
t "We're all friends here, no need to hide anything."
c "Guys I'm gonna get going, it's getting late."
"She's right, it's getting dark out again."
t "Are you leaving too [y]?"
stop music
menu:
   "Actually...":
      jump walkMe
   "Yeah, see everyone later!":
      jump goHome

label goHome:
     "I head home and look forward to sleeping."
     jump day3
label walkMe:
     y "You wanna walk me outside?"
     t "Sure, let me grab my coat."
     s "Can I come?"
     t "No, you stay here and watch the chess stuff, you're the only trustworthy person here."
     s "UGGHH fine."
     "[t] grabs their coat and we both head outside."
#Change background to outside
t "Dammit it's cold out here."
y "Come on it's not that bad, my coat isn't even as heavy as yours."
t "There's ice and snow all over the place!"
y "Don't slip and fall, heh."
"[t] grabs your hand and holds it tight."
t "Now if I fall we both go down."
"[t]'s hand is warm in mine."
y "Heh, I suppose so."
t "I'm still freezing dude."
"[t] brings his hand along with mine to his lips and blows warm air into them"
"The warmth of his breath is comforting, and I blush slightly."
y "Ahem, I think the bus is coming."
t "By the way, I meant to ask but what made you want to stop by the club?"

menu:
      "You...":
         jump tFlirt
      "I love chess!":
         jump chessFlirt
label chessFlirt:
     $chessLove += 1
     t "Yeah me too. Chess is great, but there are some things better, you know?"
     "Before I have a chance to say something else the bus pulls up in front of us and I say goodbye."
     "I get on the bus head home."
     jump goHome
label tFlirt:
     $tLove += 1
     t "Oh shit haha."
     "[t] blushes slightly and has difficulty hiding it."
     t "Well I'm flattered."
     "The bus arrives and opens its doors"
     "[t] gives me a hug and says goodbye"
     jump goHome

label day3:
"Day 3"
"I arrive at school, excited to see all the people in the chess club once again."
"As I approach the tables [t], [s], and [l] are at the tables along with someone you have not seen yet."
"[s], as she usually does, greets me with unbridled enthusiasm."
play music "chessClub.wav"
s "Hey [y]! We were just talking about you!"
y "Oh really?"
t "We were just talking about your chess game."
t "[l] wants to play you."
u "So the prodigy finally appears!"
t "[y], this is [k], the president of the club."
k "Good to finally meet you, I've heard a lot about you."
y "All good I hope, hehe."
k "Just that you been playing some interesting games lately."
k "You wanna play me?"
l "Hell no I got first dibs."
k "Fine fine, I'll wait it out."
l "Hold on I want to get to know my enemy just a little more before we play."
l "It'll break the ice so you aren't so nervous."
l "How about some twenty questions?"
y "I'm fine with that."
l "Okay, what's your favorite food?"
y "Donuts, next."
l "Favorite flavor?"
y "Glazed."
l "What's your favorite color?"
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
"Everyone pays very close attention to the responses, as though making an extra effort to remember what I say"
l "Alright, lets try something else."
l "Out of all the people here, who would you want to kiss the most?"
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
     $tLove += 1
     s "WHAT?? I mean, I don't care pft."
     t "Damn I'm flattered hahaa."
     l "Oh I see how it is, damn I'll make sure I get you two a room."
     k "Nice."
     jump lGame
label sKiss:
    $sLove += 1
    s "OOOOOOO shit! Now I'm REALLY blushing!"
    t "Oh well."
    l "Oh I see how it is, damn I'll make sure I get you two a room."
    k "Nice."
    jump lGame
label kKiss:
    $kLove += 1
    k "Nice!"
    s "Good for you two, well [t] at least we have each other."
    t "Huh?"
    s "Oblivious as usual."
    t "Huh???"
    l "Oh I see how it is, damn I'll make sure I get you two a room."
    jump lGame
label lKiss:
    $lLove += 1
    l "Well if you insist, pucker up!"
    k "Nice."
    s "Good for you two, well [t] at least we have each other."
    t "Huh?"
    s "Oblivious as usual."
    t "Huh???"
    jump lGame

label lGame:
    y "I wasn't really expecting all this attention, do you have enough info now? Can we play [l]?"
    l "Yeah let's get it on. Hope you're ready!"
    y "As ready as I'll ever be."
    l "Cool, lets set things up then."
$playerVersing = open("versing.txt", 'w').close()
$playerVersing = open("versing.txt", 'w')
$playerVersing.write("L")
$playerVersing.close()
#$subprocess.Popen("C:\Users\RIDENTEM\Downloads\checkOnYourHeart\checkOnMyHeart\game\chess.exe")
"THIS IS WHERE A CHESS GAME WOULD TAKE PLACE, IT IS ASSUMED THE PLAYER LOST."
#$game3Result = gamesWon.readline().rstrip()
$game3Result = "False"

if(game3Result == "True"):
    "I start to notice that a lot of people have gathered around your game, and I confidently announce my win."
    y "Checkmate."
    "The crowd exclaims loudly and showers me with praise."
    t "Damn [l] you got BEAT HAHAAA!"
    s "That was a close game, well done!"
    k "Yeah seriously dude that was pretty great."
    l "Ah damn, I lost *SIGH*."
    "[l] extends his hand out and I grab it and shake"
    y "Good game."
    jump postGame3
if(game3Result == "False"):
    "I finally notice the crowd of people surrounding me when they audibly sigh at the loss you received"
    l "Tch, come on man, I just lost to myself."
    y "You really think so?"
    l "Yeah, even if you lose you still learn."
    k "That was a good game to watch."
    t "I thought you were gonna win for sure."
    "[l] extends his hand out and I grab it and shake"
    jump postGame3
    # This ends the game.

label postGame3:
y "Well after that I'm starving, who else is hungry?"
"Everyone murmurs in agreement"
y "Let's go to the cafeteria then and get some food."
stop music
"We all head to the cafeteria and try to decide what to get"
#change scene to a caf
y "I can't decide what to get guys."
k "Get pizza dude, it's always the best option."
y "Yeah but I want something sweet too, and the pizza place hasn't got anything like that."
s "Go to the donut place and get something!"
y "I would love to but is it really healthy?"
s "All I know is they are awesome."
y "Hmmmm..."
menu:
    "Get a Donut":
        $sLove += 1
        y "Alright I'll get a donut."
        s "YESSS thinking about them is making me so hungry!"
        y "Me too, I'll be right back."
        "I purchase my favorite donut, which is undoubtedly the best kind, and take a seat next to [s]"
        s "Sooo what kind did you get?"
        y "The best kind."
        s "What's that?"
        y "A donut."
        s "Yes but what KIND?"
        y "A donut that I will enjoy, that's all."
        s "IT'S GLAZED I REMEM- Ahem, I recall you saying something about that when [l] asked."
        y "Heh, yeah I guess I did mention it."
        jump gotFood

    "Get pizza":
        $kLove += 1
        y "Okay [k], I'll get some pizza."
        k "Sweet,  get some toppings dude they always have something good here."
        y "Maybe, let me see what they have."
        "I glance over the display of pies available to purchase, and get a slice of one that looks especially delicious"
        "I go back to the table where everyone is seated and sit next to [k]"
        k "That's a good-looking piece of pie."
        y "It is, but there are other things that look way better."
        k "Like what?"
        "I immediately think of saying something flirty, but in front of everyone it might be embarassing, and I can't help but giggle at the idea."
        y "Hehe, take a guess."
        k "I don't know dude, spill it!"
        y "No you have to guess!"
        k "Come on dude, uhhh me?"
        y "Hell yeah."
        "[k] blushes ever so slightly"
        k "T-thanks dude, haha."
        l "Come on I'm eating here!"
        jump gotFood



label gotFood:
    k "Hey I almost forgot, we were going to go golfing tomorrow, do you want to come with us [y]?"
    y "Yeah that sounds awesome, I wasn't doing anything anyway."
    k "Cool, it's gonna be at the end of the day, so we will all still be hanging around here for the most part."
    y "Nice, I always look forward to playing some chess during the day."
    "I glance outside and notice how late it's gotten."
    y "Crap it's almost dark, I'm gonna head home and get ready for tomorrow."
    k "See ya dude!"
    l "Later."
    t "See ya."
    s "Bye bye!"
    "I exit the school grounds and am on the way home."
    "Thinking about tomorrow makes me excited to go out with everyone and golf."
    "I should have asked, but I hope its mini golf."

label day4:
"Day 4"
"The day begins just as the last few, and I am out of the house and on the way to school."
"Once I get there I see that there are many more people at the chess club than usual."
play music "chessClub.wav"
"I see [s], [t], and [l] amidst the crowd and approach them."
y "Why are there so many people here today?"
l "It's a rare occasion, our president is playing a game right now."
y "Seriously? I didn't even know this club had a president."
s "Every club has a president silly! Our president is just humble about their position."
y "What does that mean?"
t "[s] is just saying that the president doesn't come around often and when they do you would never know that they are the president."
"The crowd starts to disperse and a victor sits on the other side of the table, it's [k]!"
k "Hey [y]! Check out my checkmate!"
y "That's a good one, but [k], you're the president of the club?"
k "Yeah, it's no big deal, I just take care of a bunch of boring club stuff."
y "So how did you get to be the president? Were you voted in?"
k "Yeah, I came around here so much last semester that everyone knew me and noticed when I helped around all the time."
k "Based on that and I guess a bunch of other factors, here I am, the president."
t "We voted on you because you were best suited for the role, like the rest of us."
l "Best suited?? Anyone can do what you do [t]."
y "Why what does [t] do?"
s "[t] is the secretary"
y "Chess club has a secretary? What do you need that for?"
t "For beating people at chess hahaa."
s "The secretary is SUPPOSED to clean up chess boards and pieces, which ours does most of the time."
t "Hey I do my job and I do it good."
k "Uh-huh, so hey [y], are you coming out with us tonight?"
y "Yeah, I dont have anything better to do, and I'm sure it will be fun."
k "Hell yeah!"
s "Hey [y], you haven't played chess with [k] have you?"
y "No I haven't, should I?"
t "Dude [k] is the best here, I would love to see this."
l "She is also the only one out of us you haven't played yet."
k "Yeah and I have been dying to play you after what everyone else has said."
k "So how about it? You wanna go a round?"
y "Bring it on, I'm ready."
k "Awesome, I'll just set us up then."
$playerVersing = open("versing.txt", 'w')
$playerVersing.write("K")
$playerVersing.close()
#$subprocess.Popen("C:\Users\RIDENTEM\Downloads\checkOnYourHeart\checkOnMyHeart\game\chess.exe")
"THIS IS WHERE A CHESS GAME WOULD TAKE PLACE. IT IS ASSUMED THE PLAYER LOST"
#$game4Result = gamesWon.readline().rstrip()
$game4Result = "False"

$gamesWon.close()
if(game4Result == "True"):
    "Everyone begins exclaiming loudly."
    l "Well done, you defeated our president!"
    t "I didn't think it would happen."
    s "[y] is a force to be reckoned with!"
    k "Guys, guys everyone wins and everyone learns, it's just part of the cycle."
    jump postgame4
if(game4Result == "False"):
    k "That was well played [y], I'm glad I finally got the chance to see you in action!"
    l "Well played on both sides I say."
    s "I honestly love watching you play [y], it's interesting seeing how you play."
    y "Thanks guys, I did my best and that's that. Maybe we will play again someday."
    k "I hope so!"
    jump postGame4
label postGame4:
    "The sun is just about setting now."
    k "Hey are we going to mini golf?"
    y "Yeah but, I have no idea where it is."
    k "I can take you! It'll just be us for the ride."
    y "It's either that or I take a bus so..."
    stop music
    menu:
        "Catch a ride":
            y "Are you sure it would be okay to ride with you [k]?"
            k "Sure dude, let's go!"
            s "I coulda given you a ride."
            t "[s] you don't have a car."
            s "So??? Life finds a way [t]."
            k "Alright everyone get a move on! [y] and I will meet you guys there."
            "Everyone tells [k] to drive safe."
            "[k] and I go to the car and get in."
            "It's a nice car and it has a lot of cool features."
            k "Hold on while I get the heat up, I know it's freezing right now."
            y "Yeah you don't have to tell me twice. My nose feels frozen and we weren't even walking that long."
            k "Weather gets more and more brutal every year, nothing we can do about it I guess except stay warm."
            y "Yeah, do you mind if I put the radio on?"
            k "Go for it."
            "Pushing a button and turning a couple dials makes music come through the speakers."
            "The music currently on appears to be something with a noticeable beat and catchy rythm."
            k "I hope you don't mind, I love this stuff."
            menu:
                "So do I!":
                    $kLove += 1
                    k "That's awesome! I like a lot of music but the kind of stuff you can just bump to is my favorite."
                    "[k] starts speaking passionately about the kind of music she likes, why it intrigues her and what drives her to listen to it."
                    k "Haha sorry, I get really into it when I talk about something I like."
                    k "What about you? Why do you like this kind of stuff?"
                    y "I noticed it's what we listen to at chess club, it's got a great beat."
                    k "Yeah it does, that's one of the big reasons I like it too."
                    k "I didn't know you had good taste in music [y]."
                    y "Just so happens that you and I have the same taste."
                    k "Yeah, I'm glad."
                    jump postMusic

                "Eh, not really":
                    $kLove -= 1
                    k "Aw, what kind of music do you like?"
                    y "Anything else honestly, this just never clicked with me."
                    k "Ah, I see."
                    "[k] sadly tunes the radio to another station, and some classical comes on."
                    k "Uh, how about this?"
                    y "Yeah this'll do."
                    k "I know nothing about classical music, I think some of Beethoven is alright though."
                    jump postMusic

            label postMusic:
                    "[k] has been driving for quite a bit, I wonder when we will reach the place."
                    y "Hey [k], how far away are we?"
                    "[k] looks distracted."
                    y "[k]?"
                    k "Huh? Sorry I was just thinking, we are a few minutes away."
                    "[k] looks distraught."
                    "You both ride for a few minutes in silence until you reach the parking lot."
                    y "Okay, you ready to go inside?"
                    k "Wait."
                    "[k] reaches out to hold your hand."
                    k "[y], I've been thinking..."
                    y "Yeah?"
                    k "Uh, well, would you-"
                    "Before [k] can get the words out [t] walks up and knocks on the window."
                    t "Took you long enough! C'mon let's go!"
                    k "We better get out there."
                    y "Wait what did you want to say?"
                    k "Ah it's not important, I can tell you later."
                    y "Alright, let's head inside then."
                    jump toGolf

        "Take a bus":
            $chessLove += 1
            "[k] gives me the directions and I walk to the bus stop."
            "The bus arrives and I get on."
            "It's warm, yet cold and unforgiving."
            "I have no friends here, and unfortunately it will be awhile before the bus gets to the golf place."
            "To take my mind off of things, I can play that new chess app I got."
            "Maybe with some practice I can get better, then I'll be able to challenge better players."
            "The time flies by and the bus reaches the golfing place."
            "Everyone must be here by now, so I'll just meet them inside I guess."
            jump toGolf
label toGolf:
    "Once inside, I see the rest of the group beckoning to me."
    "After everything is setup and ready, we grab clubs and prepare to golf."
    "Each hole we get through is another memory made with everyone."
    "As the hours pass we all enjoy ourselves, laughing and smiling the entire time."
    "I'm growing more aware of how much I like everyone, especially..."
    menu:
        "[k]":
            $kLove += 1
            jump endGame
        "[l]":
            $lLove += 1
            jump endGame
        "[t]":
            $tLove += 1
            jump endGame
        "[s]":
            $sLove += 1
            jump endGame

label endGame:
    #end game check who is the lover
$loveRating = [sLove, tLove, lLove, kLove, chessLove]

$most = loveRating[0]
$counter = 0
while(counter < 5):
    if(loveRating[counter] > most):
        $most = loveRating[counter]
    $counter += 1

if(most == 0):
    $finalLover = s
elif(most == 1):
    $finalLover = t
elif(most == 2):
    $finalLover = l
elif(most == 3):
    $finalLover = k
elif(most == 4):
    $finalLover = c
    #$most = loveRating[1]
    #$if loveRating[l] > most:
    #$else:
        #continue

if(most < 4):
    "After a long night of having fun with everyone and getting to know them all more, I ask to speak to [finalLover] alone."
    "I confessed my feelings, and we kissed."
    "In those next few moments, I marvelled and wondered at what the future held in store for us."
else:
    "I decided to leave the gathering early, I didn't really feel like golfing anymore, an itch came over me."
    "I can't stop thinking about chess, and playing another game."
    "I head for the bus station and I wait for one going back to my town."
    "I pull out my phone and start up the chess app I got, and I play it the whole ride home."
return
