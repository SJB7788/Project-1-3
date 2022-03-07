while True:
    storyOpt = input("Which story would you like to play? Enter the number of the story (1, 2, or 3) or type q to quit: ")
    if storyOpt is not str:
        print("Response is invalid!")
        continue
    if storyOpt == "q":
        break
    
noun1 = input("Noun: ")
adj1 = input("Adjective: ")
pNoun1 = input("Plural noun: ")
bodyPart = input("Body part: ")
location = input("Location: ")
number = input("Number: ")
verbIng1 = input("A verb that ends with -ing: ")

story1 = "I went to the supermarket to buy some eggs. There I found a " + noun1 + " with a " + adj1 + " face. Then I saw a bunch of " + pNoun1 + ". Their " + bodyPart + " all of a \
sudden exploded and disappear into thin air. Then at " + location + ", " + str(number) + " million rats stormed out of the city pipelines and started " + verbIng1 

story2 = "Service jobs are difficult. There are so many " + pNoun1 + " that are annoying that cant read any other situation that doesn't include themselves. But there is a nice \
    coworker named " + noun1 + " that is very " + adj1 + ". Although one day he said my " + bodyPart + " looked weird and told me to lose weight. But other than that one time \
        he is pretty chill and cool. Our work place is at " + location + " and I work from 9AM to " + number + "PM. It can be tiring but at the end of the day I get payed so it \
            can be justified. Cant wait to start " + verbIng1 + " once I get home"

story3 = "Running, sleeping, working, studying, playing, and " + verbIng1 + ". Those are verbs that end in Ing. I have no idea what to write for story number3 and therefore will \
    be writing jibberish. There is no way this lazy story will reduce my marks by " + number + " percent right? I cant wait to finish this and do nothing amaright fellas. That is \
        a joke. Although writing all this is hurting my " + bodyPart + " because these keyboards kinda doo doo because i need to press harder than I normally do. And honestly I \
            am really " + adj1 + ". I want to go to " + location + " and do nothing. I just want to lay down on a bed and count to " + number + "until I fall asleep. Aight I see \
                 " + pNoun1 + " and " + noun1 + ". Time to get back to work. "

