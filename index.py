#welcome message thingy yippee
print("\nHello, hello everyone!! Emphasis on the one, unless there are more of you, but that feels unlikely. Welcome, you one (I assume) contestant to the Amazing Axolotl Gameshow! Now, we ran out of mon- I mean this is a quizshow special, so there are no games. Not cut due to budget issues. Deffinetly didn't spend it all on rocks... ANYWAY, let's begin our quiz with the first question. \n")

name = input("What is your name? ")

print("\nINCORRECT")
print("\nJust kidding! I don't know your acual name, so I can't say your answer was wrong. Enjoy the quiz," ,name,"! \n")

#store score in varable
score = 0

#first question
print("We'll start with something fairly simple:\n What is the most common color of axolotls?\n")
print("A: Yellow")
print("B: Pink")
print("C: Brown")
answer = input("\nYour answer, please (enter the letter): ")
answerclean = answer.upper ()

if answerclean == "C":
    print("\nCORRECT!")
    score += 1
else:
    print("\nINCORRECT")

print("\nAlthough pink ones are the ones that have recieved the most attention, that color is a result of leucism and albinism. Axolotls are naturally dark to blend in with their natural habbitat, so brown is the most common color overall.\n")

#second question yahoo
print("\nLet's move on to the sec-OUK-AWKCKGH-EHemf...Pardon me, uh...QUESTION TWO:\n What is the lifespan of axolotls?")
print("A: 10-15 years")
print("B: 6-8 years")
print("C: 2-4 years")
answer = input("\nYour answer, please (enter the letter): ")
answerclean = answer.upper ()

if answerclean == "A":
    print("\nCORRECT!")
    score += 1
else:
    print("\nINCORRECT")

print("\nAxolots usually live for 10-15 years like many other species of salamanders, and they spend their entire lives in the water despite developing lungs to-ERP...to breathe air.")