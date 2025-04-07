image bg space = Movie(play="gui/pp1.webm", loop=True)
image bg space2 = Movie(play="gui/pp2.webm", loop=True)
image bg space3 = Movie(play="gui/pp3.webm", loop=True)
image bg space4 = Movie(play="gui/end.webm", loop=True)


image bg dystopia = Movie(play="gui/1door.webm", loop=True)
image bg born     = Movie(play="gui/2door.webm", loop=True)
image bg sunrise = Movie(play="gui/3door.webm", loop=True)

image sylus happy = Movie(play="gui/1door.webm", loop=True)
image 1 normal = "images/1_normal.png"
image 2 o = "images/2_o.png"
image 3 hmm = "images/3_hmm.png"

# Define Characters
define s = Character("Sylus", color="#8A2BE2")
define a = Character("Aeris", color="#00CED1")
define u = Character("Unknown Voice", color="#FF4500")


# --- Main Menu ---
label start:
    window show
    scene bg space with fade
    menu:
        "Login":
            jump login
        "Register":
            jump register
        "Exit":
            jump start

# --- Login Flow ---
label login:
    scene bg space with fade
    s "Please enter your username and password."

    $ username = renpy.input("Enter your username:")
    $ password = renpy.input("Enter your password:", mask="*")

    # Sample stored credentials (replace this with actual storage logic)
    $ correct_username = "mariam"
    $ correct_password = "sylus"

    if (username == correct_username and password == correct_password) or (username == new_username and password == new_password):
        s "Login successful!"
        jump start2
    else:
        s "Invalid username or password. Returning to the main menu."
        jump start

# --- Register Flow ---
label register:
    scene bg space with fade
    s "Create a new account."

    $ new_username = renpy.input("Enter a new username:")
    $ new_password = renpy.input("Enter a new password:", mask="*")

    # Validation: Username must be at least 4 characters, Password at least 6
    if len(new_username) < 4:
        s "Username must be at least 4 characters long. Try again."
        jump register
    elif len(new_password) < 6:
        s "Password must be at least 6 characters long. Try again."
        jump register
    else:
        s "Account created successfully! You can now log in."
        return


label exit:
    return

label start2:
    play music "gui/mp1.mp3"
    scene bg space with fade
    pause 1

    s "I wake up in darkness. The air is thick with silence, my body feels weightless, translucent. "
    s " My mind is a blank slate—no memories, no name, no originas I search through my flickering consciousness."

    s "I look up and see a circle of light, realizing I am trapped in a tunnel within these walls. To the side, I notice a door. "
    s "Since I have no purpose, no name, and no recollection of who I am, I know I need to get out."

    s "Suddenly, a figure emerges from the shadows—a robot with a health gauge. I freeze in fear, but then I realize it’s weak."

    s "The robot, Kara, doesn’t know why it’s here either. The only thing it knows is the way out. Kara explains that we must go through different floors to reach the top."

    s "I think to myself—if I can escape, maybe I’ll find answers. But there’s a catch. Kara’s health gauge is programmed to receive feedback based on a series of questions."
    s "To keep Kara functioning, I must answer them. It’s a give-and-take situation for both of us."

    s"I agree, and together, we set off"

    s"As soon as we step through, my whole body morphs—I become a knight. I have no idea what’s happening, "
    s"but I find myself trapped in a pixelated world. Suddenly, from the side, a massive figure emerges—our first challenge:"
    s" 'FASES : The Ten Piedad Boss'"
    
    
    
    

    # General Questions
    menu:
        s "Been able to concentrate on whatever you’re doing?'"
        "Better than usual":
            $ choice1 = "Better than usual "
        "Same as usual":
            $ choice1 = "Same as usual"
        "Less than usual":
            $ choice1 = "Less than usual"
        "Much less than usual":
            $ choice1 = "Much less than usual"
    menu:
        s "Been having restless, disturbed nights"
        "Not at all":
            $ choice2 = "Not at all"
        "No more than usual":
            $ choice2 = "No more than usual"
        "Rather more than usual":
            $ choice2 = "Rather more than usual"
        "Much more than usual":
            $ choice2 = "much more than usual"       

    menu:
        s "Felt on the whole you were doing things well?"
        "Better than usual":
            $ choice3 = "Better than usual"
        "About the same":
            $ choice3 = "About the same"
        "Less well than usual" :
            $ choice3 = "Less well than usual"  
        "much Less well than usual" :
            $ choice3 = " Much Less well than usual"     
    

    window hide
    stop music 
    scene bg dystopia with fade
    pause 160
    window show 
    play music "gui/mp2.mp3"
    scene bg space2 with fade
    pause 1
    
    
    s "After answering, we move forward. The door creaks open, revealing a new world—another floor. "
    s "This time, we find ourselves in the midst of a zombie apocalypse."
    s "My body shifts, morphing into a man named Joel, a survivor hardened by the horrors of this world." 
    s "The air is thick with decay, the distant groans of the undead echoing through the ruins. Suddenly, a monstrous figure emerges from the shadow."

    s "This grotesque, towering creature is covered in hardened fungal growths, its body a terrifying fusion of decay and resilience. The battle for survival begins"
    s "CISSC : the bloater boss"
    
    # General Questions
    menu:
        s "Been feeling reasonably happy, all things considered?"
        "More so than usual":
            $ choice4 = "Better than usual "
        "Same as usual":
            $ choice4 = "Same as usual"
        "Less than usual":
            $ choice4 = "Less than usual"
        "Much less than usual":
            $ choice4 = "Much less than usual"
    menu:
        s "Been feeling unhappy and depressed?"
        "Not at all":
            $ choice5 = "Not at all"
        "No more than usual":
            $ choice5 = "No more than usual"
        "Rather more than usual":
            $ choice5 = "Rather more than usual"
        "Much more than usual":
            $ choice5 = "much more than usual"       

    menu:
        s "Been losing confidence in yourself?"
        "Better than usual":
            $ choice6 = "Better than usual"
        "About the same":
            $ choice6 = "About the same"
        "Less well than usual" :
            $ choice6 = "Less well than usual"  
        "Much Less well than usual" :
            $ choice6 = " Much Less well than usual" 
    

    window hide
    stop music
    scene bg born with fade
    pause 62
    window show 
    play music "gui/mp1.mp3"
    scene bg space3 with fade


    
    menu:
        s "Felt that life is entirely hopeless?"
        "Better than usual":
            $ choice4 = "Better than usual "
        "Same as usual":
            $ choice4 = "Same as usual"
        "Less than usual":
            $ choice4 = "Less than usual"
        "Much less than usual":
            $ choice4 = "Much less than usual"
    menu:
        s "Been able to feel warmth and affection for those near to you?"
        "Not at all":
            $ choice5 = "Not at all"
        "No more than usual":
            $ choice5 = "No more than usual"
        "Rather more than usual":
            $ choice5 = "Rather more than usual"
        "Much more than usual":
            $ choice5 = "much more than usual"       

    menu:
        s "Felt that life isn’t worth living?"
        "not at all":
            $ choice6 = "not at all"
        "About the same":
            $ choice6 = "About the same"
        "Less well than usual" :
            $ choice6 = "Less well than usual"  
        "much more well than usual" :
            $ choice6 = " Much Less well than usual" 
    
    window hide
    stop music
    scene bg sunrise with fade
    pause 53
    window show
    


    play music "gui/lol.mp3"
    scene bg space4


    show text "Finally, we reach the last door. Kara and I exchange a glance—we’ve become close."
    pause 6

    show text "As we step through, we see a breathtaking world: a solarpunk, sustainable future."
    pause 6

    show text "Kara turns to me and reveals the truth. This entire journey was inside my mind—a manifestation."
    pause 6
    show text "The bosses at each door were my inner obstacles,"
    pause 6
    show text "and Kara was my positive side guiding me through them."
    pause 6

    show text "Finally kara reveals that its my mind my manifestation just like the bosses at the door which manifested my obstacles in life my positive"
    pause 6
    show text "side gave birth to a sustainable future and kara was manifestation of the positive side of myself "
    pause 6
 
    show text "So why don't you give urself a chance and move forward with positive outlook for :"  

    pause 6

    show text " Your existence is valid "

    pause 6
     

    

    show text "Follow us on {a=https://www.instagram.com/kymera_raiden.x}Instagram{/a} | {a=https://discord.gg/example}Join our Discord{/a}" with dissolve
    
    label start4:
    s "Vent box : Feel free to write anything"
    $ vent_input = renpy.input("Write your thoughts here...")  # Player types their response
    $ vent_input = vent_input.strip()  # Removes extra spaces

    if vent_input:
        s "I see. Thank you for sharing: [vent_input]"
    else:
        s "It's okay if you don't want to say anything."

    return

    pause 90
    
    return