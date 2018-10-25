# Lauren & Jia Qi He

import random

story = "Once upon a/an time there were three little <ANIMAL> s. The first little <ANIMAL> was very <ADJECTIVE> and he built a house for himself out of <PNOUN> . The second <ANIMAL> was <ADJECTIVE> and he built a house out of <PNOUN> . But the third little <ANIMAL> was very <ADJECTIVE> and he built his house out of genuine <PNOUN> . Well, one day, a mean old wolf came along and saw the houses. ' <SOUND> !!!' he said, 'I'll <VERB> and I'll <VERB> and I'll blow your house down.' And he blew down the first <ANIMAL> 's <NOUN> and the second <ANIMAL> 's <NOUN> . The two <ANIMAL> s ran to the third <ANIMAL> 's house. Thereupon, the wolf began blowing, but he couldn't blow down the third <ANIMAL> 's <ADJECTIVE> house. So he <PVERB> off into the forest and the three <ADJECTIVE> <ANIMAL> s moved to <PLACE> and went into the <FOOD> business."
animal_list = ["pig", "dog", "cat", "cow", "armadillo"] #this one doe n't change
noun_list = ["light" "apple juice", "leg", "pencil", "house"] #nouns
adj_list = ["freaky", "scary", "funny", "strong", "weak"] #adjectives
pnoun_list = ["bricks", "socks", "papers", "ice cream tubs", "cards"] #plural nouns
sound_list = ["woof", "oof", "pft", "awoo", "tch"] #sounds
verb_list = ["jump", "blow", "throw", "pounce", "break"] #verbs
pverb_list = ["jumped", "rolled", "slinked", "ran", "teleported"] #past tense verbs
place_list = ["Japan", "Paris", "Chicago", "New York", "Texas"]
food_list = ["jalepenos", "kimchi", "sausage", "pie", "macaroni and cheese"]

def madlibs(s):
    mad_story = []
    animal = random.choice(animal_list)
    for item in s.split():
        if item == '<ANIMAL>':
            mad_story.append(animal)
        elif item == '<ADJECTIVE>':
            mad_story.append(random.choice(adj_list))
        elif item == '<NOUN>':
            mad_story.append(random.choice(noun_list))
        elif item == '<PNOUN>':
            mad_story.append(random.choice(pnoun_list))
        elif item == '<SOUND>':
            mad_story.append(random.choice(sound_list).upper())
        elif item == '<VERB>':
            mad_story.append(random.choice(verb_list))
        elif item == '<PVERB>':
            mad_story.append(random.choice(pverb_list))
        elif item == '<PLACE>':
            mad_story.append(random.choice(place_list))
        elif item == '<FOOD>':
            mad_story.append(random.choice(food_list))
        else:
            mad_story.append(item)
    return ' '.join(mad_story)
print(madlibs(story))


