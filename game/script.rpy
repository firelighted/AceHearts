# Declare characters used by this game.
define alex = Character('Alex', color="#014420")
define alexorous = Character('alexorous', color="#014420")
define sarah = Character('Sarah', color="#014420")
define debbie = Character('Debbie', color="#014420")
define gregory = Character('Gregory', color="#014420")

define jill = Character('Jillian', color="#014420")
define calvin = Character('Calvin', color="#014420")
define bobby = Character('Bobby', color="#014420")
define gwen = Character('Gwen', color="#014420")

define frannie = Character('Frannie', color="#014420")
define thomas = Character('Thomas', color="#014420")
define feeniks = Character('Feeniks', color="#014420")
define jason = Character('Jason', color="#014420")
define kaitlyn = Character('Kaitlyn', color="#014420")

define misty = Character('Melanie', color="#014420")
define zaffie = Character('Zaffie', color="#014420")
define peter = Character('Peter', color="#014420")
define nekomami = Character('nekomami', color="#014420")

image peter = "Peter.png"
image feeniks = "Feeniks.png"
image misty = "Misty.png"
image kaitlyn = "Kaitlyn.png"

define audio.Farmer = "Farmer.ogg"
#Define other variables here
define job = False #if player tell jill about job
define femaleAlex = False
define maleAlex = False
define nbAlex = False

# The game starts here.
#101
label start:

    # Start by playing some music.
    # play music  #place holder

    scene bg black #place holder
    with fade
    
    menu:
        "What gender do you identify with right now?"
        "Female":
            $ femaleAlex = True
        "Male":
            $ maleAlex = True
        "Non-binary":
            $ nbAlex = True
    
    "*Groans*"
    "I should have remembered to close the blin…"
    "Shit, what time is it?! 8:00?!"
    "Why didn’t someone wake me up?!"
    "Wait,{p=1.0} no,{p=1.0} it's summer vacation.\n Phew, thought I was going to be in a lot of trouble"
    "I need to get dressed and pack my bag. I don’t remember doing any homework."
    "Where’s my phone? Why the fuck didn’t I set an alarm? It’s---oh. Shit. It’s summer."

    menu:

        "As I realize this, I decide to..."

        "Go back to bed.":
            jump sleep

        "Get up.":
            jump wake

#102a
label sleep:

    "I guess I might as well go back to bed for a little bit…"
    "No one will be awake so early, anyways."

    jump scene_103

#102b
label wake:
    
    #bedroom bg
    "Do I smell bacon? Heck yeah! But who is making it at this time of morning?"
    "Dad should be at work, and Sarah and Mom both sleep in until the afternoon."
    "I’mma head downstairs and figure out what’s going on."

    scene bg kitchen
    show sarah relaxed at right
    debbie "Morning Alex! We’re making bacon and eggs. How do you want yours done?"
    alex "Sunnyside up? I’ll put in some toast."
    sarah "Already put it in. Mom always asks how you like yours but I know you always eat them the same way."
    alex "Uhm, thanks… But why are you up so early?"
    show sarah happy
    sarah "Mom’s taking me and my friends to the beach right after breakfast."
    debbie "Yeah, Alex would you like to come with us?"
    "I’d rather spend my day on my computer than waste it at the beach."
    alex "Nah, you two have fun."
    sarah "We will."
    debbie "I will enjoy reading my book in the sun. Oh, Alex, do you need anything before we head out?"
    alex "Nope. I’ll be alright."

    jump scene_103

label scene_103:

    scene bg club #place holder
    with fade

    scene bg black
    "It was a chill morning. I played World of Guildcraft for a few hours before I got a text from Jill."
    
    scene bg texting#place holder
    jill "wanna hang at java house? :D me n cal are goin there @ 11am"
    "Sounds better than more grinding in WoG. I should take a break."
    "I’ll get dressed and head over."
    alex "Sounds good! See u there!"
    jill "great :D:D:D"
    
label scene_104:
    
    scene bg black
    "I put on whatever is at the top of my pile of clothes and head out."
    
    #Residential street
    scene bg street
    "I hadn’t realized that summer had gotten so busy because of my schoolwork. People are out walking their dogs and running before it gets too hot."
    
    #downtown 1
    "It’s still cool in the shade but it’s warm in the sun. I still prefer spring and fall."
    
    scene bg coffeeshop
    "By the time I get to the cafe, Jill and Calvin are already there."
    jill "Hey Alex, we’re over here."
    "She waves me over vigorously. So I make my way to their table."
    calvin "Hey, Alex. What’s up?"
    alex "Nothin’ much. What did you guys have planned for today?"
    calvin "I was thinking we could go to the movies. The newest 'She Has Scales' was just released."
    jill "Have you even seen the first six?"
    alex "I haven’t. My internet friends said they were awful. Like 10 Decaying Potatoes awful."
    calvin "I haven’t. Did you have something else in mind, Princess?"
    jill "We always go to the movies. Why can’t we go play Magick at Mimic? It’ll be so much fun."
    calvin "But. You. Always. Win."
    jill "Fine. Alex you get to pick."
    calvin "You’re the tiebreaker."
    "This always happens. Why me?"
    alex "I need coffee before I can make a decision, guys."
    jill "Oh yeah. We haven’t ordered yet."
    calvin " I know what I want. Are you going to look at the menu for ten more minutes, hun?"
    "Jill glares at him."
    alex "I think I’ll have an iced coffee. It’s getting hot out there."
    "We place our orders and wait for our drinks."
    "They keep staring at me but I just ignore them until our drinks arrive."
    
    menu:
        "Where should we go after?"
        
        "Go see She Has Scales 7.":
            jump scene_105a

        "Go play Magick.":
            jump scene_105b

    
label scene_105a:

    scene bg coffeeshop
    "I don’t feel like getting crushed in Magick right now."
    alex "Let’s go see the movie."
    calvin "Wait. You actually sided with me for once?!"
    jill "You’ll never get better if you don’t play."
    alex "Or maybe I just don’t want to build a deck worth hundreds of dollars."
    "Jill shrugs."
        
    scene bg black
    "We watched the movie...much to Jill’s dismay. The movie was awful..."
    "Just terrible."
    "We all regretted seeing it and Jill was oddly quiet until we exited the theater."
    calvin "Babe, it wasn’t that bad."
    jill "I need therapy."
    calvin "There wasn’t even any beastiality."
    jill "It was implied!"
    alex "Let’s just agree to never see the first six."
    jill "You don’t have to tell me twice."
    calvin "You guys are no fun."
    jill "Well, we are some fun. If I wasn’t you wouldn’t be going out with me."
    alex "Well, I think I should head home. It’s almost dinner time. Text you guys later?"
    calvin "‘Later!"
    jill "Bye!"

    jump scene_106

label scene_105b:
    
    scene bg coffeeshop#morning
    alex "That movie sounds too terrible. Even for me."
    alex "I’d rather lose at Magick."
    jill "See, I knew Alex would side with me."
    calvin "As always."
    
    scene bg black
    "It’s not a long walk to The Door’s a Mimic. The store is small but it has a cozy feel. There are a few groups of people playing various games around the tables."
    jill "Let’s find a fourth and play some Supreme Leader Magick."
    calvin "Sure. I have some new tech that will allow me to defeat you."
    alex "We’ll see. I am sure she is several steps ahead of you."
    calvin "Let me have some hope…"
    "One of the workers there joined us because they weren't super busy. The staff’s cool like that. Too bad Jill knocked him out really early."
    jill "I summon my Grekolo, Goblin Warlord."
    jill "All of my goblins now get more damage and more health for each other goblin I control."
    alex "Oh no. Calvin, do you have anything to take care of that?"
    calvin "It depends. If I draw another energy source I might. Is your turn over Jill?"
    jill "Yes, unfortunately I had to attack before casting my Warlord."
    calvin "It all comes down to this."
    calvin "Alright. I got this. I play my Spooky Isle and cast a maximized Clone Army, creating ten copies of my Scarecrow King."
    jill "It is unique. You have to sacrifice them because you can only have one."
    calvin "You’re right. However, first each of them triggers its ability for each other one that came into play. I get to destroy up to one hundred cards."
    alex "Uhh..."
    jill "This one goes to you Calvin."
    calvin "Yes! Finally!"
    "We play a few more rounds. Calvin loses in all of them. Even I win one. The games take quite some time and eventually we decide to call it a day and head home."
    jill "I’m going home now. Bye!"
    calvin "‘Evening."
    alex "‘Later!"
    
    jump scene_106

label scene_106:
    
    scene bg kitchen#(evening)
    "When I got home it smelled of veggie stir fry."
    "I went to my room. Sarah apparently heard me and peeked in."
    show sarah surprised at right
    sarah "Hey. Do you know what we’re doing for dinner?"
    alex "Uh… Veggie stir fry."
    show sarah awkward
    sarah "Oh, cool… Uhh… How was your day?"
    alex "Okay. Hung out with Jill and Calvin. How about you?"
    show sarah happy
    sarah "I was playing the new video game, Undersee. It's actually really good."
    alex "Oh yeah? I'll have to check it out."
    sarah "Let me know when you do so you can add me!"
    
    scene bg black
    "She gave a quick wave before sliding out of the room. I relaxed into my chair, and turned on my computer."
    "After spending a little bit watching videos about the new meta in World of Guildcraft, Mom called us down for dinner."
    "It smells really good actually."
    
    scene bg kitchen#(evening)
    debbie "Alex, isn’t there an orientation day for your university coming up? Remind us when it is, and maybe we can give you a ride there."
    show sarah happy at right
    sarah "Oh! I want to go too!"
    gregory "I don’t see why not. Why don’t we all go?"
    debbie "That’s a great idea honey."
    gregory "Say Sarah, have you thought about what you want to do? Maybe you want you to go to med school like your brother?"
    show sarah relaxed at right
    sarah "I haven’t really put much thought into it. I'm sure they’ll pressure me enough in grade 12 to pick something."
    debbie "I’m sure you’ll find something. Alex, if you need any more furniture for your dorm, let us know."
    alex "Oh, uh, thanks. I’m hoping to get a decent desk chair with my next paycheck."
    gregory "Your grandparents have some extra furniture sitting around. We should go take a look some time."
    "It would save money but who knows how old that furniture is. Worth a look I suppose."
    alex "Sure. I think I’m off next weekend."
    gregory "That doesn’t work for me. I took some shifts for Jenny at work. Her husband is having surgery. Some other time perhaps."
    "The rest of the dinner was in comfortable silence. At the end, I cleared my dishes and excused myself."
                                                                     
    scene bg black
    "I didn’t feel like WoG, so I decided to watch some Planet Globe II before bed."
    
label scene_107:
    
    scene bg black
    "I turn off my alarm clock and sit up, stretching before I start to get ready."
    "Since there’s no special dress code, I just put on some clean clothes."
    "I brush my teeth, and head downstairs to scrounge for something to eat."
    
    scene bg kitchen
    "I’m too lazy to make anything, so I eat the leftover stir fry before I go to work."
    
    scene bg black
    "It’s a nice morning. The air is still cool and the grass is damp with dew."
    "Judging by the strength of the sun today, though, the walk home will probably be way less pleasant."
    "I make it to work just before my shift starts, jogging up to a small building tucked in the line of shops in town."
    "The large sign outside reads “Frannie’s Bakery” with a small colorful cupcake dotting the “i.”"
    "It’s a popular place, and has gotten even busier with all the new houses being built." 
    "The business is great for Frannie, and I get a ton of hours, but it can be exhausting just being the three of us."
    "As I reach the entrance, the small wooden plaque in the doorway reads “Closed / Fermé” but I enter anyways."

label scene_108:
    
    scene bg bake
    "It’s already warm inside, with the ovens going and Frannie bringing out tarts fresh from the oven."
    frannie "Hey sweetie! Could you start setting up the display?"
    alex "Sure. Just let me get my apron on."
    "We set up the store with all the fresh baked goods before we open."
    "There are already some people waiting outside. Mostly older people who want a fresh loaf in the morning. They’ve been coming here for so long that Frannie makes their orders separately to be ready for them when they show up at their usual time."
    "Frannie and Thomas chat with their regulars while managing the shop."
    "The morning is hectic and before I know it, it’s one o’clock."
    "It calms down a bit and Frannie comes out, brushing flour from her hair and face."
    frannie "How are you doing?"
    alex "Fine, but it’s getting harder to keep the displays full and handle the customers at the same time."
    frannie "Speaking of, I‘ve been thinking about bringing someone else in."
    alex "That sounds like a great idea! Oh, are there any more cinnamon rolls in the oven? We’re all out."
    frannie "You hear that Tom?"
    thomas "Yeah. I’m just putting them together now." #thomas is offscreen
    
label scene_109:
    
    #Frannie’s Bakery
    "The store finally quiets down once it’s a bit past lunch, and I’m cleaning up from the rush when the bell on the door rings."
    frannie "Welcome!"
    alex "Welcome!"
    bobby "Hey!"
    alex "Hey Bobby, are you getting something?"
    bobby "Yeah! Why else would I be here? Just to see your beautiful face?"
    alex "Ha-ha, very funny. What can I get for you?"
    bobby "How about some cinnamon rolls?"
    alex "Hmmm. We’re all out right now but Tom is making more right now. If you don’t mind waiting, you could have some straight from the oven."
    bobby "Hell yeah! I’ll pay for ‘em now."
    "{p=1.0}"#Register sounds, tapping. It’s a pause. (code in the pause, SV)(maybe later -SV)
    bobby "You still excited for university?" 
    bobby "Maybe finally get a girlfriend after...y’know?"
    alex "I’m excited to start my bachelor degree, I’m not going there for a relationship."
    bobby "I’m just looking out for you, dude! You better remember me when you leave. I’ll miss you."
    alex "Of course not. We’ve known each other since elementary school."
    frannie "Here are the cinnamon rolls."
    bobby "Oh, man! That smells so good."
    frannie "Thank you!"
    bobby "Cool!"
    bobby "Hey, are you busy after work? I have something to show you."
    
    menu:
        "What should I do?"
        
        "Hang out with Bobby.":
            jump scene_110a

        "Go home.":
            jump scene_110b
        
label scene_110a:
    scene bg bake
    alex "Sure! We haven’t hung out in ages. Where do you wanna go?"
    bobby "Let’s go to the skate park! I found a cat there recently."
    bobby "I don’t think it’s got a home. I’ve been feeding it for a week and wanted to show you."
    alex "Ummm, do cats eat cinnamon rolls?"
    bobby "I’m not giving the cat cinnamon rolls, dummy. I’m going to bring a can of tuna."
    bobby "When are you done?"
    alex "At three."
    bobby "I’ll go get the tuna and swing by around then."
    
    scene bg black
    "After work, we head over to Gary’s Skatepark. I look around for the cat, but don’t see anything."
    alex "I don’t know Bobby, I don’t see any cats."
    bobby "Should be by the tree over there. At least that’s where I last saw it."
    "I look over to where he is pointing, and see the flash of a black tail as a small cat runs behind the tree."
    alex "Oh! I think I see it!"
    bobby "Come here kitty. I brought you some yummy food."
    "The kitten refused to come out from behind the tree."
    "Bobby opened the can of tuna and put it down, and then both of us backed away slowly."
    "After we were a good four meters away, the kitten slowly walked up to the food and started eating."
    bobby "Oh no! They are so tiny! I wonder why they are out here alone."
    alex "I don’t know… It looks really skinny too. I’m glad you’re feeding it."
    "The kitten ate the entire can. Then growled softly at us and scampered away. Bobby picked up the can and sighed."
    bobby "I hope they warm up to me someday."
    alex "I’m sure they appreciate the food!"
    "We leave the park and eventually head home, promising to talk again soon."
    
    jump scene_112
    
label scene_110b:
    
    scene bg bake
    alex "Sorry, I really wanna just go home today. I’m exhausted."
    bobby "Oh, alright. I’ll talk to you later then."
    "After I clocked out and said bye to Frannie and Thomas, I left the bakery."
    
    scene bg black
    "On the way home, I see Jill running up the street toward me, arms full of papers, and one escapes her grip. She jumps up to grab it and pauses in front of me."
    jill "Oh, hey Alex! What’s up? Did your shift just end?"
    alex "Yeah. What’s with the stack of paper?"
    jill "Oh, these? My mom helped me put together a resume to give to places around town."
    jill "She said I need to get a job if I wanna keep spending money on Magick cards and books."
    alex "Don’t you spend money on anything else?"
    jill "Eheh. Well, I wasn’t planning on moving out. But I do need to start saving."

    menu:
        "Tell her Frannie’s hiring.":
            $ job = True #set telling jill about job to true
            jump scene_111a

        "Wish her luck.":
            jump scene_111b
            
label scene_111a:
    
    scene bg black
    alex "Hey, we’ve been swamped at the bakery lately. I know Frannie has been wanting to hire someone. If you want, you can drop a resume off there."
    jill"Really?! I’m gonna give her my resume now! Hope I get the job."
    alex "Don’t worry. I think Frannie will hire you."
    jill "Thanks for letting me know. See you later!"
    "I wave at Jill and watch as she skips her way towards the bakery. I hope she gets the job. Working with a friend is better than some other stranger."
    
    jump scene_112

label scene_111b:

    scene bg black
    alex "Good luck on the job hunt! I’m sure you’ll find something."
    jill "Thanks! Whoops, I really gotta run. I’m almost late for my next interview. See you later!"
    alex "See ya! Hope you do well on that interview!"
    "Jill sure seems busy. I continue my walk home."
    
    jump scene_112

label scene_112:

    scene bg kitchen
    alex "Mom, dad, I’m home!"
    "After greeting my family, I changed into comfortable clothes and sat down to unwind in front of the TV. Soon after, my mom walked into the room."
    debbie "Alex, sweetheart. I know you just got home, but could you please go to the store? Your father forgot to pick up the milk and potatoes on the way home."
    "I really don’t wanna go, but I know I’ll just upset her if I say no. Plus, I hadn’t really found anything interesting to watch, yet."
    alex "Alright."
    debbie "Love you sweetheart."
    "I grab the car keys and my wallet and head to the grocery store."

label scene_113:
    
    scene bg black
    "The store isn’t far from our house, so I get there rather quickly." 
    "I went straight for what I needed. I got a bag of homogenized milk and got a small sack of potatoes."
    "I get to the checkout and find myself in line beside someone from my school, Peter."
    show peter
    play music Farmer
    "I don’t know him well, just that he lives on a farm."
    "He recognizes me, too, but we stand in an awkward silence."
    
    menu:
        "Talk to Peter.":
            jump scene_114a

        "Remain silent.":
            jump scene_114b
            
label scene_114a:
    
    scene bg black
    show peter
    "Peter was a pretty nice guy in school, and talking to him can pass the time waiting in line. I decide to break the awkward silence."
    alex "H-"
    peter "H-"
    "Before I can finish my sentence, Peter also starts speaking." 
    peter "Hey Alex, sorry to interrupt you. What were you going to say?"
    alex "I was just saying hi."
    
    jump scene_115
    
label scene_114b:
    
    show peter
    "We don’t know each other very well. I don’t really wanna bother him."
    peter "Hey Alex."
    "Oh, apparently he wants to talk to me."
    alex "Hey Peter."
    
    jump scene_115
    
label scene_115:
    
    scene bg black
    show peter at right
    peter "It’s been awhile!!"
    "I awkwardly smile back at him."
    alex "Yeah, it has. How have you been?"
    peter "Pretty good. The farm’s pretty busy at this time of year." 
    alex "I’m glad to see your family still owns the farm."
    peter "Yeah! We’ve actually been doing very well this season."
    alex "Thats good to hear!"
    peter "You’re buying milk here? It’s getting so expensive."
    alex "Yeah. It really sucks."
    peter "Hey, my family sells it quite a bit cheaper.  A lot of people come directly to our farm to buy." 
    peter "You should come over to buy some, I promise we won’t gouge you like this place does."
    "The price of milk is regulated by the government isn’t it?"
    alex "Really? Where is your farm again?"
    peter "Oh, its at 4567 Wallaby street. We’re the long dead end road down past the school."
    "I finish paying for my two items and pause with Peter outside the grocery store."
    alex "Alright, I’ll keep that in mind. It was nice seeing you again Peter! I should head home. I’m holding up dinner right now."
    peter "Alright, see you around Alex! It was nice catching up!"
    "It was pretty nice to see him. I should tell Mom about his offer."
    stop music
label scene_116:
    
    scene bg black
    alex "I’m back! Here Mom, I got the milk and potatoes."
    debbie "Thank you!"
    "I help out by making the mashed potatoes, and we talk about our days as we cook."
    "Soon it’s time to eat."
    gregory "Mmmm mashed potatoes. My favourite!"
    debbie "So how’s everyone doing tonight?"
    show sarah happy at right
    sarah "I found out that the new season of How To Go Out With A Murderer is coming out this next Thursday. I’m so excited! I’m going to rewatch the first season."
    debbie "How To Go Out With A Murderer? I don’t know if you should be watching a show like that."
    show sarah awkward at right
    sarah "Mom, I’m 15."
    gregory "Yeah, our children are both growing up now. Also I really like that show too! You should watch it with us, Deb!"
    debbie "I will not. How about your day, Alex?"
    alex "Well, I had a really busy day at work. Frannie’s looking to hire someone, and I hope that happens soon. We could really use the extra help for the summer at least."
    alex "Oh also, I saw one of my high school classmates at the grocery store just now, Peter. His family owns the big farm not too far outside of town."
    alex "He said his family is selling milk, and we can buy milk from them for a cheaper price."
    gregory "That’s great! Milk has really-- heck, everything has gone up in price for some time now."
    gregory "I think I know this kid’s dad. Tyler, right? Yeah, we used to hang out all the time."
    debbie "A trip out there just for some milk?"
    gregory "They have eggs too, and vegetables sometimes! I should talk to Tyler some more. He’s a nice guy."
    
    scene bg black
    "After dinner, I go to my room to play some WoG."
    "It’s a nice way to relax and can make time fly by."
    "I do a few quests and gain a level but I have work in the morning. Best to get enough sleep."
    
    #if alex told jill about job
    if job == True:
        jump scene_117a
        
    #else (wish her luck/hang out with bobby)
    else:
        jump scene_117b

label scene_117a:
    
    scene bg bake
    "I get to work in the morning and start setting up. About thirty minutes before we open, the bell rings and I look up to see who’s here."
    "We aren’t open yet. Who’s..."
    "Jill is poking her head through the door, looking around nervously. When she sees me, she smiles and comes inside."
    jill "Hey Alex!"
    frannie "Hey Jill. Put on an apron and have Alex show you what you need to do."
    jill "Yes ma'am!"
    alex "That’s awesome! You got the job!"
    jill "Yeah, and it’s thanks to you!"
    "I spend the morning showing Jill what to do."
    "She is nervous at the start and drops a few muffins. Though by noon, she handles the register pretty well."
    "{p=1.0}"
    "The bell rings as someone leaves. As they leave someone else slips in through the open door."
    calvin "Hey Jill!"
    jill "Calvin?"
    calvin "I came to see you on your first day of work!"
    jill "Aww thanks, boo."
    calvin "Wait wait wait, lemme take a picture of you. You look great in that apron."
    jill "Please don’t. I’m covered in flour."
    "I see Calvin take some pictures anyway. They act cutesie, and Calvin has her pose in front of the display case and holding a tray of muffins. It’s grossly adorable."
    alex "Get a room you two."
    calvin "But we’re already in a room."
    "I get out of the way as Jill walks up to him and throws a handful of flour at his head."
    calvin "Hey."
    frannie "Haha. I remember those days, eh Tom?"
    "Tom was already standing behind her with a handful of flour. As soon as she turned around he tossed it in her face."
    frannie "Tom!"
    thomas "Haha."
    "Tom likely didn’t see the tube of icing she was holding behind her back."
    "Soon everyone was covered in flour, icing, and sprinkles-- even me."
    "I’m so glad that Jill enjoyed her first day, and that Frannie and Tom look happier without all the stress from being understaffed."

    jump scene_118
    
label scene_117b:
    
    "Work was insane. It seemed that the ovens couldn’t cook fast enough and I had to ask people to wait constantly." 
    "By the end of the day, I’m exhausted. I hope Frannie finds someone to help out soon."
    "They also gave me some fresh bread and other baked goods to take home for the trouble."
    
    jump scene_118
    
label scene_118:
    
    scene bg black
    "After a long day at work, I guess I could spend some time playing World of Guildcraft. NekoMami37 should be online around this time."
    scene bg copmuter
    "Alexorous: Hey. You up for some questing?"
    "NekoMami37: one sec, parents left me to scrounge dinner"
    "Alexorous: All right, I’ll meet you at Wildland Outpost."
    "NekoMami37: lets go"
    "Alexorous: Did you find something to eat?"
    "NekoMami37: peanut butter and a spoon"
    "We get through the frontier area and reached the western ocean."
    "NekoMami37: u got 2 work in the morning?"
    "Alexorous: Not tomorrow. Onward! The ocean beckons."
  
label scene_119:
    
    scene bg black
    "Nothing exciting happened for the next few days."
    "Should I try to get some of my friends to hang out later?"
    "{p=1.0}"
    scene bg texting
    jill "hey i signed us up 4 pottery classes! :D:D:D"
    calvin "wh...pottery classes?"
    alex "why?"
    jill "bc u 2 never do anything but play video games"
    calvin "baaaaabe"
    jill "we’re going" 
    alex "...When?"
    jill "tonight >.>"
    calvin "way to give us a warning babe"
    jill "just come 2 the town square @ 7! Or i’ll hunt you down >:("
    alex "See you at seven."
    calvin "pottery it is"
 
label scene_120:
    scene bg black
    "I meet up with Jill and Calvin at seven, where the two are huddled under a tree. Jill’s bouncing with energy and has a big grin."
    jill "Alex!! There you are!! Are ya excited?"
    alex "Yeah, sure. I honestly know nothing about pottery though."
    calvin "Isn’t it cute that she’s so pumped about something?"
    "Jill shoves Calvin’s arm, who just grins." 
    jill "Alex, you don’t seem all too interested about this."
    alex "Can’t say I’m pumped for pottery. I just enjoy spending time with my friends."
    jill "Aaaw!"
    jill "This will be super fun! I promise!"
    alex "Where is it anyway?"
    jill "Not too far from here!"
    "Jill leads us to a messy art studio."
    "The place was full of retired women in their 60s seated at various tables."
    "We stick out like a sore thumb, considering the age difference."
    "We went for table in a corner and waited for the instructor to give everyone instructions."
    alex "Well jeez, I’m glad we aren’t the only ones who thought this was an awesome way to spend a Saturday night."
    jill "Come on, Alex. This is gonna be so much fun!"
    "The instructor begins by showing the newbies, us, how to prepare our clay and start making pots."
    "About an hour into the class, I noticed a weird sight - another younger person around our age, helping the older ladies."
    "He looks really comfortable with pottery rather than awkward like Calvin and me."
    "Jill, who was getting aggravated at her clay, eventually notices us staring, and looks up, raising an eyebrow."
    jill "Is that Jason Todd?"
    calvin "Jason?"
    jill "Yeah, Jason Todd from school. You know, the guy on the hockey team."
    calvin "Is that why he looks familiar? The Jason Todd?"
    jill "Yeah. This is the last place I would’ve expected him to be." 
    alex "He looks so in his element too."
    "Jason glances over with a small smile, probably expecting there to be more cute little old ladies. His smile disappears when he sees us instead."
    "Jill gives me a shrug, her face full of confusion. Calvin snickers a little, but we decide to go back inside and focus on our projects, making pots not even our own grandmothers could be proud of."
    "When the class was over, we cleaned our hands and went outside."
    
    scene bg black
    "We leave the studio. Before we can leave the area Jason catches up to us."
    jason "So… Listen… About this… you can’t tell anyone you saw me here. You got that?"
    jill "Umm what?"
    
    menu:
        "Promise to tell no one.":
            jump scene_121a
            
        "Tell him you will do what you want.":
            jump scene_121b
            
label scene_121a:
    #Downtown 2 (night)
    alex "I mean, yeah. We don’t even hang out with the same people. What you do is your business."
    calvin "Sure, not like we talk about you anyways."
    jill "Yeah, chill, man. We’ve got better things to do with our lives."
    "Any sign of threat vanishes when he smiles and claps Calvin on the shoulder."
    jason "Thanks! I owe ya one!"
    "With a grin and a small wave, he goes back into the studio and helps one of the old ladies."
    jill "That was weird."
    calvin "Yeah, why does he want to be all secretive about being here?"
    alex "Can’t say I know."
    
    jump scene_122
    
label scene_121b:
    #Downtown 2 (night)
    alex "Come on, it’s just a pottery class. Besides, you can’t tell me what to do."
    jason "You’d better not tell anyone--."
    jill "Why?"
    jason "That would be very bad."
    jill "Are you freaking threatening us?!"
    alex "Seriously, dude. It’s not that big of a deal. Who would we even tell?"
    calvin "We don’t even know your friends."
    jason "Please just don’t tell anyone."
    "He walks away looking agitated."
    jill "What’s his problem?"
    calvin "Guy probably thinks doing pottery ruins his reputation or some shit."
    jill "Well I don’t care if he thinks he’s too cool for pottery, that was just rude."

label scene_122:
    #Downtown 2 (night)
    jill "Anyways, pottery was great! Look at my amazing work!"
    "Calvin holds up his pot beside Jill’s."
    calvin "At least my lid fits on properly."
    jill "Hey! Mine is just aesthetic."
    alex "Is that what they call that now?"
    "We exchange blows with each other about our shitty pottery."
    jill "Have a safe walk home!"
    calvin "I’ll text you later!"
    alex "See you two later. I had fun tonight!"

label scene_123:
    #Residential street (night)
    "I start heading home. The streets look really different at night."
    "It was so weird seeing Jason at the pottery class, but he does seem to genuinely enjoy himself there. In fact, his skills are pretty good and I don’t think the teacher can teach him any more."
    "What made him so interested in pottery and interacting with the old ladies?"
    "Also, why does he want to keep it a secret? He’s really sweet and kind to the people there."
    "I decide to drop the topic of Jason when I walk into my house."
    
    #Bedroom (night)
    "Pottery is weirdly exhausting. After cleaning my hands some more and changing my clothes, I browsed some pottery pieces on Falln until I couldn’t keep my eyes open anymore."

label scene_124:
    #Bedroom
    "I wake up in the morning, and take my time getting out of bed."
    "After playing on my computer for a little while, I try and figure out something to do instead of being home all day."
    
    scene bg texting
    "As if on cue, I got a text from Bobby."
    bobby "meet me at the skate park right now? I need to ask you something :P"
    "That’s strange and I don’t know how to feel about that :P face."
    alex "Sure Bobby. See you there."

label scene_125:
    scene bg black
    "Bobby was boarding in the park when I arrived. He came over as soon as he saw me."
    bobby "Yo Alex!"
    alex "What’s up? Why did you asked me to come here so early?"
    bobby "So, I met this really cute girl the other day."
    alex "Oh yeah?"
    bobby "And I actually got her to give mer her phone number!"
    "He didn’t drag me all the way out here just to tell me about his date did he?"
    bobby "So I’m going on a date with her this Friday. But here's the thing..."
    bobby "She has a friend who kind of has difficulty getting dates."
    "I stare blankly at him, clearly not getting his point."
    bobby "So she’s bringing them too…"
    bobby "And I need to bring someone too. Like a double date."
    "A double date…?"
    alex "I… I don’t think that’s a good idea."
    bobby "Please Alex! It’s just a date! It’s not like you have to kiss or marry her friend."
    bobby "Hell, you don’t have to hold hands. I just need to bring someone with me."
    "I sigh, seeing how eager he is. I mean, I guess it wouldn’t be too bad."
    bobby "Please Alex. For me?"
    "For a friend like Bobby, sure. And who knows, I might make a new friend too."
    alex "Alright."
    bobby "Thank you so much dude! I owe you so much! Anything you need dude, I got you!"
    
label scene_126:
    #Residential Street
    scene bg street
    "After saying goodbye to Bobby, I begin my walk back home."
    "I’m filled with a weird amount of excitement, and a bit of nervousness. It’s been years since I’ve been on a date."
    "Yet this is the kind of nervousness I knew I shouldn’t be feeling about a double date."
    "I honestly didn’t expect that from Bobby, but at least it’s not anything seriously bad." 
    
    scene bg kitchen
    "I watch TV for most of the day until dinner. After I enjoyed another meal with family, I went back upstairs to play WoG."
    
    #Bedroom (night)
    "After gaming well into the middle of the night, my eyes start to ache, so I log off and get into bed."
    "As I lie in bed, I can’t help but think about the double date."
    "I have never really gotten into the huge hype about dating."
    "Do people really feel an intense urge to date someone?"
    "I mean it’ll be great to have someone you trust and can lean on, but that didn’t end well last time."
    "I guess it may have been my fault. I feel kinda clueless about this stuff."
    "I wish I could ask Calvin or Jill about this stuff. But how do I do that without the whole conversation being awkward?"
    "Those two have been together forever. As long as I have known them. They probably never feel awkward about their relationship."
    "My thoughts quickly become less and less coherent until I fall asleep."

label scene_127:
    #Downtown 1
    "Today is the day of the date. Bobby and I agreed to meet early. He is probably as nervous as I am."
    "I head downtown, feeling a nervous knot growing in my stomach."
    "Finally, I see Bobby in the crowd. Is that a cat hanging over his shoulder?"
    bobby "Hey! If it’s not the guest of honor."
    alex "Oh man… Don’t say that."
    bobby "I’m only joking dude."
    alex "A cat?"
    bobby "Yeah! Look how big she is. I figured she could break the ice on our date!"
    alex "Hm. Yeah, I mean… Not a lot of people bring a cat on a date."
    bobby "Well, after feeding her for a while she wouldn’t leave me alone. So I’ve kept her with me since."
    alex "You’re a dork. You know that right?"
    bobby "Yup. A true dork. You ready for this?"
    alex "I’m only here because you asked me to come."
    "Bobby looked like he was happy that he was able to find someone to bring to the double date, but upset that I wouldn’t be having a good time." 
    bobby "Well, thank you for coming! It honestly means a lot to me!"
    "Honestly, I’m still kinda on the fence about this whole dating thing, but I’m happy that Bobby is looking forward to this. I don’t think he’s ever had a date before."
    alex "Bobby, you’ve never been on a date before have you?"
    bobby "No. Is it that obvious?"
    alex "Yeah. Remember that time poor little Leah asked you out and you turned her down?"
    bobby "That was a long time ago. She was too girly. Flowers and dresses all the time."
    alex "And how about your date today?"
    bobby "Gwen? She’s punk. She likes all my favourite bands."
    if (femaleAlex):
        jump scene_128a
    else:
        jump scene_128b
    
label scene_128a: # Female Alex
    alex "We arrived at the restaurant. It’s a cute pizza and milkshake parlour."
    alex "They have an ice cream freezer showing off flavors, and the pizza smells incredible."
    alex "Bobby eventually flags down two girls. One smiles broadly and waves back. That must be Gwen."
    alex "I look at the girl next to her and the knot in my stomach gets a little tighter."
    alex "I know her."
    alex "Very well in fact."
    bobby "Hey Gwen!"
    gwen "Hey Bobby! It’s nice to see you again!"
    kaitlyn "Alex?"
    alex "Oh… Hi Kaitlyn."
    gwen "You two know each other?"
    kaitlyn "Yeah. We went to school together."
    gwen "Sorry if this is a bit weird, Kaitlyn. I’ve always thought that Alex is a boy’s name."
    bobby "What? Alex is a girl’s name. The only Alex I know is a girl! I’ve never heard of a boy called Alex."
    kaitlyn "Alex is both a girl’s and boy’s name. How did you not know?"
    bobby "Sorry. I thought it would be obvious by the name."
    gwen "It’s all right. We can all have a great time together!"
    gwen "Why do you have a cat?"
    bobby "Her name is Dusty!"
    alex "Bobby started telling Gwen about how he befriended the kitten. I glanced awkwardly Kaitlyn, catching her giving me a quick glance as well."
    alex "We have been classmates for many years and well… She’s been annoyingly, just a little bit better. A little faster, a little more talented, a little smarter, a little more helpful."
    kaitlyn "So Alex. Are you excited for the film?"
    alex "Sure but we both know it won’t be as good as the book."
    kaitlyn "Of course. But the book is missing some aspects the film has."
    alex "Good music and filmography can make up the gap for sure."
    alex "After we finish eating, Kaitlyn speaks up."
    kaitlyn "Looks like everyone is about done. How about we start going to the theatre? The movie is starting soon."
    gwen "Oh right! Good thing someone was keeping time."
    bobby "Time really flies by when you’re having fun huh?"
    alex "Yeah, let’s get going. I wouldn’t want to miss Lord of Thrones."

    #Rockridge Cinemas
    alex "We arrive at the theatre just in time to get some good seats."
    alex "As commercials play, Kaitlyn and I talk quietly about what reviews and some internet bloggers have said about the movie."
    alex "We quiet down when the movie starts and watch intently."
    alex "Then there are the sex scenes. They were in the book too yes, but that’s different than seeing it on the big screen."
    alex "Why do movies have these scenes? Apparently, sex sells, but I don’t think these scenes are necessary."
    alex "They don’t add anything to the plot or anything."
    alex "It was awkward. Really awkward. To the point I still felt awkward when we walked out of theater.    "

    alex "Bobby and Gwen continue to talk to each other. They seem to like each other a lot."
    bobby "Hey, you kids have fun. I’m going to walk Gwen home. Stay safe."
    alex "And with that, he walked off with Gwen into the night."
    alex "I smiled awkwardly at Kaitlyn, who looked back at me. I finally decided to break the silence."
    jump scene_129a #? (this is for female alex, i assume scene_129a is for male/NB - SV)

label scene_128b: # Male, NB Alex
    alex "We arrived at the restaurant, it’s a cute pizza and milkshake parlour."
    alex "They have an ice cream freezer showing off flavors, and the pizza smells incredible."
    alex "Bobby eventually flags down two girls, one smiles broadly and waves back. That must be Gwen."
    alex "I look at the girl next to her and the knot in my stomach gets a little tighter."
    alex "I know her."
    alex "Very well in fact."
    bobby "{Happy" #what is this supposed to do?
    gwen "{Happy" #this too, jeepers people, it's not hard, it's scripting not coding :P
    kaitlyn "Alex?"
    alex "Oh… Hi Kaitlyn."
    alex "I can feel my face heat up. I’m really nervous now."
    gwen "You two know each other?"
    kaitlyn "Yeah. We had a lot of classes together in school."
    gwen "Oh good, no awkward introductions then. We can all have a great time together!"
    gwen "Also Bobby, why do you have a cat?"
    bobby "Her name is Dusty!"
    alex "Bobby started telling Gwen about how he befriended the kitten. I glanced awkwardly Kaitlyn, catching her giving me a quick glance as well."
    alex "We have been classmates for many years and well… She’s been annoyingly, just a little bit better. A little faster, a little more talented, a little smarter, a little more helpful."
    kaitlyn "So Alex. Are you excited for the film?"
    alex "Uhh… Yeah but we both know it won’t be as good as the book."
    kaitlyn "Yeah, you’re right. But the book is missing some aspects the film has."
    alex "Good music and filmography can make up the gap for sure."
    kaitlyn "If the trailers were any indication then the music is going to be great."
    alex "After we finish eating, Kaitlyn speaks up."
    kaitlyn "Looks like everyone is about done. How about we start going to the theatre? The movie is starting soon."
    gwen "Oh right! Good thing someone was keeping time."
    bobby "Time really flies by when you’re having fun huh?"
    alex "Yeah, let’s get going. I wouldn’t want to miss Lord of Thrones."
    #Rockridge Cinemas
    alex "We arrive at the theatre just in time to get some good seats."
    alex "As commercials play, Kaitlyn and I talk quietly about what reviews and some internet bloggers have said about the movie."
    alex "We quiet down when the movie starts and watch intently."
    alex "Then there are the sex scenes. They were in the book too yes, but that’s different than seeing it on the big screen."
    alex "Why do movies have these scenes? Apparently, sex sells, but I don’t think these scenes are necessary."
    alex "They don’t add anything to the plot or anything."
    alex "I see Kaitlyn beside me. She also seems uncomfortable."
    alex "It was awkward. Really awkward. To the point I still felt awkward when we walked out of theater.    "
    #Rockridge Outside
    alex "Bobby and Gwen continue to talk to each other. They seem to like each other a lot."
    bobby "Hey, you kids have fun. I’m going to walk Gwen home. Stay safe."
    alex "And with that, he walked off with Gwen into the night."
    alex "I smiled awkwardly at Kaitlyn, who also stared at me awkwardly.  I finally decided to break the silence."
    menu:
        "That was fun.":
            jump scene_130
            # jump scene_128b_1 #look idk what the script says, i didn't read it past like, scene 20, but if there's supposed to be extra scenes here---
        "We should do this again sometime.":
            jump scene_130
            # jump scene_128b_2 #eiter put them in on the next push or so, or tell me i need to do this. This breaks it, rn, gonna fix

label scene_129a: #female Alex
    # Downtown, night
    kaitlyn "Oh! That’s good."
    alex "Yeah I really enjoy these fantasy movies!"
    kaitlyn "They are my favourite! Maybe we should watch the sequel together when it comes out."
    alex "That’s probably not going to be out for a while."
    kaitlyn "I know, but I’m still going to watch it."
    alex "Same."
    alex "We spent quite a while talking about the movie and comparing it to the book. Then, we exchanged phone numbers."
    alex "We decided to walk each other home, talking along the way until we went our separate ways."
    
    jump scene_130
    

label scene_130: #130\[c\]\[d\]
    # [Add attraction compatibility based scenes]
    # [Alex goes to bed but thinks about relationships. Katelyn has been really sweet all this time--but what if their past relationship is how each one ends?[e][f]]
    # Bedroom
    scene bg bedroom
    alex "I really enjoyed tonight more than I thought I would. Kaitlyn seems really sweet."
    alex "I’ve only seen her as a classmate and friend up until this point, but do I really want to see her as more than that?"
    alex "Do I want a relationship? I mean, Bobby seems to be very happy with Gwen and vice versa. Jill and Calvin also. Idk, I think I’m gonna sleep on it."

label scene_131: #131 July 13
    # Kitchen
    scene bg black
    alex "Tomorrow is the university tour, and my whole family is coming along."
    debbie "Alex! Are you all prepared for tomorrow? Get all your questions and whatever you need ready!"
    alex "It’s just a tour ma. You don't have to all come."
    show sarah relaxed
    sarah "Hey! I want to go. I want to see what your university is like."
    sarah "I’ve got like nothing to do anyways. It’s the summer, and I’m bored."
    gregory "We’re ALL GOING! We have to support our baby."
    alex "Stop."
    gregory "Well I’m driving the whole gang there tomorrow."
    debbie "c: Remember we’re heading out early so don’t stay up too late, children."
    alex "We made sure to pack some water and food in a bag for our trip. Then, we all went to our rooms for the rest of the day."
    # Bedroom
    scene bg bedroom
    alex "I’m kinda excited for tomorrow. Lemme set an alarm and go to bed."

label scene_132: #132 July 14\[g\]
    # Campus 1
    scene bg black
    alex "The whole family got to the university campus early morning."
    alex "We were given the tour of the a lecture hall, dorms, dining hall, gym, yeah."
    # Campus 2
    scene bg black
    alex "After the tour, we are allowed to go wherever we liked."
    alex "I remembered reading about a tabletop club on the school’s website. Maybe I should go check that out."
    alex "Or maybe I should find out where Sarah wants to go first."
    alex "What should I do?"

    menu:
        "1: Go to the tabletop club.":
            jump scene_133a

        "2: Find out where Sarah wants to go.":
            jump scene_133b

label scene_133a: #133a
    # Campus 2
    scene bg black
    alex "My family decided to go somewhere else while I make my way towards the club room."
    # Campus 1
    scene bg black
    alex "As I make my way there, I see a group of people who seems to be playing something…"
    alex "And one of them is dressed up as a wizard? interesting"

label scene_134b: #134b (this formatting i swear to josh)
        # [Gregory has disappeared. Sarah wants to go to do yoga. The room for yoga is off the same space as the tabletop and LGBT clubs.
        #The rooms are unlabeled but Alex sees a group playing in one of the rooms. Sarah says she is going to yoga and Debbie is going to find Gregory.
        #They will pick Alex up when they are done. Sarah leads this scene.[h]]
    # Campus 2
    scene bg black
    sarah "Hey I really want to go check out the yoga club. Do you remember where it is?"
    alex "Yeah I can take you there,"
    alex "The yoga club should be in the same direction as the tabletop and club. I’m not really interested in yoga, so i guess i can just drop Sarah off then leave."
    debbie "I think Gregory went off to get some food. I’ll go look for him. We’ll meet up later when we’re about to leave, so about 1 hr."
    sarah "Just text dad and ask him where he is. Anyway, see you in an hour mom."
    alex "bye mom"
    debbie "see you, my cutie patooties. ::>"
    # Campus 1
    scene bg black
    alex "I walk Sarah to the yoga club and leave to go to the tabletop room. I passed a room, in which there is a group of people playing something… and one of them is dressed up as a wizard? interesting."

label scene_135: #135
        # [Alex looks into the room with the people playing D&D.
        #They realize that the room has the pride flag in it and turns to leave but the wizard runs up and grabs them to come play D&D.
        #The party is missing a key role. What will Alex be?]
    # LGBT Club
    scene bg black
    alex "Hmm, I wonder what they are doing."
    alex "Looking into the room, I see a pride flag on the wall. Maybe this is the LGBT club?"
    feeniks "HEY!"
    feeniks "Sorry, didn't mean to startle you or anything, but we need another person in our party."
    alex "Umm, party?"
    show zaffie relaxed
    zaffie "Yeah, join us! I’m Zaffie, and the wizard is Feeniks by the way."
    alex "Hi im alex. What are y’all doing anyways?"
    misty "We’re just playing D&D, Alex. My name is Melanie, but everyone calls me Misty."
    misty "Are you one of the new people on the uni tour?"
    alex "Yeah! I’m most likely coming for school."
    zaffie "Cool, what program did you apply for?"
    alex "bachelors in biology."
    zaffie "Ahh! Ok, I hope you like it. But yeah, we need another person for our game."
    feeniks "We have a couple of characters you can choose from. Would you rather be Feligri the half-orc cleric of the sun goddess or Colm the kind hearted rogue?"
    alex "Uhh..."

    menu:
        "1: Cleric.":
            jump scene_136a

        "2: Rogue.":
            jump scene_136b

label scene_136a: #136a (who keeps labeling these twice? -SV)
    # Fantasy world
    scene bg black
    feeniks "The party opens the huge double doors. Inside is a giant chamber lit by large fires. Dwarven runes line the walls and pillars."
    zaffie "I look for the dwarves."
    feeniks "You don’t find any. You find a thick layer of dust covering many of the surfaces."
    misty "This isn’t good. Why are there no dwarves here?"
    feeniks "A wind blows through the room."
    misty "We are deep underground!"
    feeniks "You hear something behind you. When you turn around, you see that an immense scaled creature has snuck up on you. A black dragon. Roll initiative."
    alex "The fight goes on for a while trading hits with the dragon."
    feeniks "You can tell that the dragon is weakening. It opens its mouth and releases a stream of acid. Make Dexterity saves."
    misty "19."
    alex "20."
    zaffie "Uhh… 7."
    feeniks "Misty and Alex you manage to dodge the acid unscathed. Sorry Zaffie but you take 43 points of acid damage."
    zaffie "Help. I’m unconscious and dying. I liked this character too."
    alex "I got this. It’s my turn next right? I pull out my holy symbol and run over to Zaffie. I cast Breath of Life."
    zaffie "Thanks Alex. I enter my barbarian rage, grab my spear, and thrust it into the dragon’s heart!"
    feeniks "Roll for it."
    zaffie "Natural 20. I finish off the beast!"

label scene_136b: #136b
    feeniks "The party is walking down a narrow passageway lit by torches."
    zaffie "Are there any doorways?"
    misty "Hidden doorways?"
    feeniks "Roll perception checks."
    feeniks "You don’t find any."
    feeniks "Upon turning the corner you find a large room with a raised dais in the middle."
    zaffie "I approach the dais."
    feeniks "You step up onto the platform and hear the distinct sound of a pressure plate being pressed."
    alex "Oh no."
    feeniks "The doors close and you can see water begin to seep through the cracks of the walls. It begins to pour in faster filling the room."
    misty "I open the closest door."
    feeniks "You try but it is locked."
    alex "I can open that but can’t swim very well."
    zaffie "I grab Alex and swim over to the door."
    alex "I pick the lock. 18 plus 6. 24."
    feeniks "You feel the tumblers click into place. The door opens and you are pulled out of the room as the water rushes into the hallway."

label scene_137: #137
    # Fantasy World*[i (What is this for? -SV)
    scene bg black
    zaffie "Misty, you’ve gotta cast Charm Person!"
    misty "What?"
    zaffie "We have to get past that guard. Just cast Charm Person and seduce him away from the doorway."
    misty "But my character’s asexual."
    feeniks "I dont think an asexual can cast that spell."
    alex "Asexual?"
    zaffie "Can’t your character just pretend?"
    misty "Yeah but she’s asexual. Asexuals don’t experience sexual attraction."
    zaffie "The guard probably isn’t."
    alex "Interesting, didn’t know about that."
    zaffie "Fine. I take out my club and beat him over the head. Drag him into an alley."
    feeniks "Alright."
    zaffie "Oh, and I take his coin purse."
    feeniks "Of course you do."
    # LGBT Club
    scene bg black
    misty "That was fun! Alex, you’re going to be coming here in september right? We should all exchange phone numbers."
    misty "We can tell you upcoming club stuff. Also maybe meet up again before school starts."
    alex "Sure that sounds great."
    zaffie "Cool! Well I’m really looking forward to seeing you in the fall term. If you have any questions, feel free to ask us."
    alex "I’m excited to start uni here. Talk to y’all later. My family is probably waiting for me somewhere."
    feeniks "Alright! See you in september! Enjoy the rest of your summer."

label scene_138: #138
    # Campus 1
    scene bg black
    alex "As I was leaving the clubroom, I see my family walking towards my direction."
    gregory "Alex, we were just looking for you. Are you all done? Ready to leave?"
    alex "Yeah, what perfect timing, I was just coming to find y’all."
    show sarah relaxed
    sarah "Great, let’s go home. I’m tired from yoga."
    alex "We make our way to the parking lot to get in our car. Then, we went straight home."

label scene_139: #139
        # [Alex’s thoughts fill us in on the drive back and such. They decide to investigate asexuality on the computer.]
    # Bedroom
    scene bg bedroom
    alex "On the way back home, everyone shared their thoughts on the tour of the university."
    alex "They all had fun it seems. That’s good."
    alex "I’m really looking forward to go to St. Paul’s I also enjoyed the company of those weird people playing some DnD stuff today."
    alex "Speaking of… Misty’s character really resonated with me. This is the first time I've heard of asexuality."
    alex "I have to go do some research on this topic ASAP."

label scene_140: #140
    # [Alex searches asexuality on Goggle and finds AVEN and Reddit. They fall asleep thinking that asexuality fits them very well.]
    # Bedroom
    scene bg bedroom
    alex "I booted up my PC and search “asexual” on Goggle."
    alex "First thing that I stumbled upon was a website called AVEN, and I browsed through many of the forum threads about how people find out they are asexuals. It seems very much like how I am as well."
    alex "Apparently, there is a subreddit for asexuality. The internet really has everything now doesn’t it. I need to subscribe and read up on other people’s experiences to compare to my own."
    alex "After what felt like 5 hours of research on the internet, my life now makes sense. I am asexual."
    # [a]More talking, less thinking. More development. MOAR!
    # [b]In particular the scenes while they are watching the movie need work.
    # [c]we prob need to make a male/female version of this. unless alex just talks about relationships in general/
    # [d]or just have this scene play out if alex is male
    # [e]im kinda confuzzled. what does this mean?
    # [f]Alex had a traumatic relationship when they were younger. They think all of the relationships will end that way as a result.
    # [g]shouldnt we know where sarah wants to go before deciding?
    # [h]im not 100% sure what this means
    # [i]what does this look like?

    jump end

label end:
    "Thank you for playing Summer Horizon!"
    return