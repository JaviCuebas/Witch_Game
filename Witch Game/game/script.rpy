# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define l = Character(_("Lottie"), color="#e60073")
define lu = Character(_("Lucina"), color="#00cc44")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg forest
    with fade

    "WitchCon 2020. This was the most anticipated witch gathering of the year.
    Magick-casters all over the world come to a hidden island in the Carribean
    to learn from the best and brightest witches around."

    "And me? I was fortunate enough to be one of the
    select few to open up a stand at their festival."

    "My family is very well renowned among all witches."

    "Due to them, on top of my actual magickal prowess I was permitted
    to set my very own pop-up tarot reading tent."

    " While I was only 18, I’ve been practicing the
    occult (focusing on divination in particular) ever since I was born."

    "I was considered a magickal prodigy by all of my peers and relatives."

    "I wonder what kind of stories I’ll hear and people I’ll meet during my time here…"

    "All I know is that I’ll do my best to give them the clarity they need."

    scene bg first day
    with fade

    "I made sure to get up early to have my tent ready by 7am.
    I wanted to have some spare time to mentally prepare and meditate."

    scene bg tent2
    with fade

    "I sat criss-cross on the floor cushion inside my tent and closed my eyes."

    "I imagined the energy already flowing inside my body flowing downward, passing
    through the floor of the tent and attaching to the earth beneath me."

    scene bg black
    with fade

    "I rooted myself and began my descent into nothingness."

    scene bg tent2
    with fade

    "Before I knew it, my first client showed up."

    lu "Great, I’m the first one here"

    l "Indeed you are. Please take a seat."

    show lucina sad
    with dissolve

    l "speak."

    show lucina shocked
    with dissolve

    lu "what?"

    l "Well you’re obviously here because you have a problem."

    l "That’s kind of the whole point."

    show lucina angry
    with dissolve

    lu "And you expect me to open up with that attitude?"

    l "I don’t exactly get paid to be your friend."

    lu "A little better customer service wouldn’t hurt though"

    l "You either pay me or leave bud.
    Not my fault your problems got so bad you had to
    resort to damn tarot readings."

    show lucina embarassed happy
    with dissolve

    lu "yeet!."

    lu "fuck you Lottie!."

    lu "fuck you mamahuevo."
















    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    lu "You've created a new Ren'Py game."

    lu "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
