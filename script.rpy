# Declare characters used by this game.
define alex = Character('Alex', color="#014420")
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

#Define other variables here
default job = False #if player tell jill about job

# The game starts here.
#101
label start:

    # Start by playing some music.
    # play music  #place holder

    scene bg lecturehall #place holder
    with fade
    
    "*Groans*"
    "I should have remembered to close the blin…"
    "Shit, what time is it?! 8:00?!"
    "Why didn’t someone wake me up?!"
    #"Wait,{p=1.0} no,{p=1.0} it's summer vacation.\n Phew, thought I was going to be in a lot of trouble"
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

    #kitchen bg
    debbie "Morning Alex! We’re making bacon and eggs. How do you want yours done?"
    alex "Sunnyside up? I’ll put in some toast."
    sarah "Already put it in. Mom always asks how you like yours but I know you always eat them the same way."
    alex "Uhm, thanks… But why are you up so early?"
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

    #bedroom bg
    "It was a chill morning. I played World of Guildcraft for a few hours before I got a text from Jill."
    
    #phone bg===============================================================================================================================
    #how should we write phone texts
    jill "wanna hang at java house? :D me n cal are goin there @ 11am"
    "Sounds better than more grinding in WoG. I should take a break."
    "I’ll get dressed and head over."
    alex "Sounds good! See u there!"
    jill "great :D:D:D"
    
label scene_104:
    
    #bedroom bg
    "I put on whatever is at the top of my pile of clothes and head out."
    
    #Residential street
    "I hadn’t realized that summer had gotten so busy because of my schoolwork. People are out walking their dogs and running before it gets too hot."
    
    #downtown 1
    "It’s still cool in the shade but it’s warm in the sun. I still prefer spring and fall."
    
    #java house
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

    #java house
    "I don’t feel like getting crushed in Magick right now."
    alex "Let’s go see the movie."
    calvin "Wait. You actually sided with me for once?!"
    jill "You’ll never get better if you don’t play."
    alex "Or maybe I just don’t want to build a deck worth hundreds of dollars."
    "Jill shrugs."
        
    #Outside of Rockridge Cinema#
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
    
    #Java House (morning)
    alex "That movie sounds too terrible. Even for me."
    alex "I’d rather lose at Magick."
    jill "See, I knew Alex would side with me."
    calvin "As always."
    
    #The Door’s a Mimic
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
    
    #Kitchen (evening)
    "When I got home it smelled of veggie stir fry."
    "I went to my room. Sarah apparently heard me and peeked in."
    sarah "Hey. Do you know what we’re doing for dinner?"
    alex "Uh… Veggie stir fry."
    sarah "Oh, cool… Uhh… How was your day?"
    alex "Okay. Hung out with Jill and Calvin. How about you?"
    sarah "I was playing the new video game, Undersee. It's actually really good."
    alex "Oh yeah? I'll have to check it out."
    sarah "Let me know when you do so you can add me!"
    
    #Bedroom (evening)
    "She gave a quick wave before sliding out of the room. I relaxed into my chair, and turned on my computer."
    "After spending a little bit watching videos about the new meta in World of Guildcraft, Mom called us down for dinner."
    "It smells really good actually."
    
    #Kitchen (evening)
    debbie "Alex, isn’t there an orientation day for your university coming up? Remind us when it is, and maybe we can give you a ride there."
    sarah "Oh! I want to go too!"
    gregory "I don’t see why not. Why don’t we all go?"
    debbie "That’s a great idea honey."
    gregory "Say Sarah, have you thought about what you want to do? Maybe you want you to go to med school like your brother?"
    sarah "I haven’t really put much thought into it. I'm sure they’ll pressure me enough in grade 12 to pick something."
    debbie "I’m sure you’ll find something. Alex, if you need any more furniture for your dorm, let us know."
    alex "Oh, uh, thanks. I’m hoping to get a decent desk chair with my next paycheck."
    gregory "Your grandparents have some extra furniture sitting around. We should go take a look some time."
    "It would save money but who knows how old that furniture is. Worth a look I suppose."
    alex "Sure. I think I’m off next weekend."
    gregory "That doesn’t work for me. I took some shifts for Jenny at work. Her husband is having surgery. Some other time perhaps."
    "The rest of the dinner was in comfortable silence. At the end, I cleared my dishes and excused myself."
                                                                     
    #Bedroom (night)
    "I didn’t feel like WoG, so I decided to watch some Planet Globe II before bed."
    
label scene_107:
    
    #Bedroom (morning)
    "I turn off my alarm clock and sit up, stretching before I start to get ready."
    "Since there’s no special dress code, I just put on some clean clothes."
    "I brush my teeth, and head downstairs to scrounge for something to eat."
    
    #Kitchen (morning)
    "I’m too lazy to make anything, so I eat the leftover stir fry before I go to work."
    
    #Downtown (2, morning)
    "It’s a nice morning. The air is still cool and the grass is damp with dew."
    "Judging by the strength of the sun today, though, the walk home will probably be way less pleasant."
    "I make it to work just before my shift starts, jogging up to a small building tucked in the line of shops in town."
    "The large sign outside reads “Frannie’s Bakery” with a small colorful cupcake dotting the “i.”"
    "It’s a popular place, and has gotten even busier with all the new houses being built." 
    "The business is great for Frannie, and I get a ton of hours, but it can be exhausting just being the three of us."
    "As I reach the entrance, the small wooden plaque in the doorway reads “Closed / Fermé” but I enter anyways."

label scene_108:
    
    #Frannie’s Bakery
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
    #Register sounds, tapping. It’s a pause.
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
    #Frannie’s Bakery
    alex "Sure! We haven’t hung out in ages. Where do you wanna go?"
    bobby "Let’s go to the skate park! I found a cat there recently."
    bobby "I don’t think it’s got a home. I’ve been feeding it for a week and wanted to show you."
    alex "Ummm, do cats eat cinnamon rolls?"
    bobby "I’m not giving the cat cinnamon rolls, dummy. I’m going to bring a can of tuna."
    bobby "When are you done?"
    alex "At three."
    bobby "I’ll go get the tuna and swing by around then."
    
    #Gary’s Skatepark
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
    
    #Frannie’s Bakery (evening)
    alex "Sorry, I really wanna just go home today. I’m exhausted."
    bobby "Oh, alright. I’ll talk to you later then."
    "After I clocked out and said bye to Frannie and Thomas, I left the bakery."
    
    #Downtown (evening)
    "On the way home, I see Jill running up the street toward me, arms full of papers, and one escapes her grip. She jumps up to grab it and pauses in front of me."
    jill "Oh, hey Alex! What’s up? Did your shift just end?"
    alex "Yeah. What’s with the stack of paper?"
    jill "Oh, these? My mom helped me put together a resume to give to places around town."
    jill "She said I need to get a job if I wanna keep spending money on Magick cards and books."
    alex "Don’t you spend money on anything else?"
    jill "Eheh. Well, I wasn’t planning on moving out. But I do need to start saving."

    menu:
        "Tell her Frannie’s hiring.":
            jump scene_111a

        "Wish her luck.":
            jump scene_111b
            
label scene_111a:
    
    #Downtown (evening)
    #set telling jill about job to true
    $ job = True
    alex "Hey, we’ve been swamped at the bakery lately. I know Frannie has been wanting to hire someone. If you want, you can drop a resume off there."
    jill"Really?! I’m gonna give her my resume now! Hope I get the job."
    alex "Don’t worry. I think Frannie will hire you."
    jill "Thanks for letting me know. See you later!"
    "I wave at Jill and watch as she skips her way towards the bakery. I hope she gets the job. Working with a friend is better than some other stranger."
    
    jump scene_112

label scene_111b:

    #Downtown (evening)
    alex "Good luck on the job hunt! I’m sure you’ll find something."
    jill "Thanks! Whoops, I really gotta run. I’m almost late for my next interview. See you later!"
    alex "See ya! Hope you do well on that interview!"
    "Jill sure seems busy. I continue my walk home."
    
    jump scene_112

label scene_112:

    #Kitchen (evening)
    alex "Mom, dad, I’m home!"
    "After greeting my family, I changed into comfortable clothes and sat down to unwind in front of the TV. Soon after, my mom walked into the room."
    debbie "Alex, sweetheart. I know you just got home, but could you please go to the store? Your father forgot to pick up the milk and potatoes on the way home."
    "I really don’t wanna go, but I know I’ll just upset her if I say no. Plus, I hadn’t really found anything interesting to watch, yet."
    alex "Alright."
    debbie "Love you sweetheart."
    "I grab the car keys and my wallet and head to the grocery store."

label scene_113:
    
    #Grocery store inside
    "The store isn’t far from our house, so I get there rather quickly." 
    "I went straight for what I needed. I got a bag of homogenized milk and got a small sack of potatoes."
    "I get to the checkout and find myself in line beside someone from my school, Peter. I don’t know him well, just that he lives on a farm."
    "He recognizes me, too, but we stand in an awkward silence."
    
    menu:
        "Talk to Peter.":
            jump scene_114a

        "Remain silent.":
            jump scene_114b
            
label scene_114a:
    
    #Grocery store
    "Peter was a pretty nice guy in school, and talking to him can pass the time waiting in line. I decide to break the awkward silence."
    alex "H-"
    peter "H-"
    "Before I can finish my sentence, Peter also starts speaking." 
    peter "Hey Alex, sorry to interrupt you. What were you going to say?"
    alex "I was just saying hi."
    
    jump scene_115
    
label scene_114b:
    
    "We don’t know each other very well. I don’t really wanna bother him."
    peter "Hey Alex."
    "Oh, apparently he wants to talk to me."
    alex "Hey Peter."
    
    jump scene_115
    
label scene_115:
    
    #Grocery store
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

label scene_116:
    
    #Kitchen (evening)
    alex "I’m back! Here Mom, I got the milk and potatoes."
    debbie "Thank you!"
    "I help out by making the mashed potatoes, and we talk about our days as we cook."
    "Soon it’s time to eat."
    gregory "Mmmm mashed potatoes. My favourite!"
    debbie "So how’s everyone doing tonight?"
    sarah "I found out that the new season of How To Go Out With A Murderer is coming out this next Thursday. I’m so excited! I’m going to rewatch the first season."
    debbie "How To Go Out With A Murderer? I don’t know if you should be watching a show like that."
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
    
    #Bedroom (night)
    "After dinner, I go to my room to play some WoG."
    "It’s a nice way to relax and can make time fly by."
    "I do a few quests and gain a level but I have work in the morning. Best to get enough sleep."
    
    #if alex told jill about job
        #jump scene_117a
        
    #else (wish her luck/hang out with bobby)
        #jump scene_117b

label scene_117a:
    
    #Frannie’s Bakery (morning)
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
    
    #Frannie’s Bakery (afternoon)
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
    
    #Bedroom (night)
    "After a long day at work, I guess I could spend some time playing World of Guildcraft. NekoMami37 should be online around this time."
    
    #Computer Screen=======================================================================================================================================
    #how should we write computer messages?
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
    
    #Bedroom (morning)
    "Nothing exciting happened for the next few days."
    "Should I try to get some of my friends to hang out later?"
                                                                               
    #Phone==================================================================================================================================================
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
    
    "120"
 
