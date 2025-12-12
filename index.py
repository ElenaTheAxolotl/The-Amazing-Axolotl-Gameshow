#welcome message thingy yippee
print("\nHello, hello everyone!! Emphasis on the one, unless there are more of you, but that feels unlikely. Welcome, you one (I assume) contestant, to the Amazing Axolotl Gameshow! Now, we ran out of mon- I mean this is a quizshow special, so there are no games. Not cut due to budget issues. Definetly didn't spend it all on rocks... ANYWAY, let's begin our quiz with the first question:\n")

name = input("What is your name? ")

print("\nINCORRECT")
print("\nJust kidding! I don't know your actual name, so I can't say your answer was wrong. Enjoy the quiz," ,name,"!\n")

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

print("\nAlthough pink ones are the ones that have received the most attention, that color is a result of leucism and albinism. Axolotls are naturally dark to blend in with their natural habitat, so brown is the most common color overall.\n")

#second question yahoo
print("\nLet's move on to the sec-OUK-AWKCKGH-EHemf...Pardon me, uh...QUESTION TWO:\n What is the lifespan of axolotls?\n")
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

print("\nAxolots usually live for 10-15 years like many other species of salamanders. They spend their entire lives in the water despite developing lungs to-ERP...to breathe air.\n")

#question threehehehehehehehe
print("\nMoving right along to the third question:\n Which country are ACk-axolotls native to?...AHem...\n")
print("A: Mexico")
print("B: Indonesia")
print("C: Rwanda")
print("D: All of the above")
answer = input("\nYour answer, please (enter the letter): ")
answerclean = answer.upper ()

if answerclean == "A":
    print("\nCORRECT!")
    score += 1
else:
    print("\nCORRE-\nINCORRECT")

print("\nMexico is the only native home of axolotls in the world, specifically Lake Xochimilco in Mexico City. The Azetec god of fire and lightning, Xolotl, is the origin of the name 'axolotl', which means 'water dog' in Nahuatl.\n")

#fourthhhh questionnnnn
print("\nSpeaking of names, it's time for the-URp-the fourth question:\n What is a common name for axolotls in Japan?\n")
print("A: Rōtoru")
print("B: Wooper Looper")
print("C: Ahobaka")
answer = input("\nYour answer, please (enter the letter): ")
answerclean = answer.upper ()

if answerclean == "B":
    print("\nCORRECT!")
    score += 1
else:
    print("\nINCORRECT")

print("\nUghh...maybe I shouldn't have eaten all those rocks...OH! UH-YOU KNOW NOTHING! AHEM! The term 'Wooper Looper' (ウーパールーパー) comes from the name of an axolotl character created to advertise UFO instant noodles and is the namesake for the axolotl-like Pokémon, Wooper. The transliteration of 'axolotl' in Japanese, ahorōtoru (アホロートル), is the same as saying 'stupid old fart', so Wooper Looper is a much nicer name.\n")

#final score reveal
print("\nOKAY, NOW QUES...tion...huh? Hang on-\n...\nWhat? That's all we have the budget for?? Cus of the...I don't know what 'rocks' you're talking about...Fine! I get it!\n...\nSo, it seems as though this is the end of the quizshow special because of...reasons...LET'S SEE THE RESULTS!!\n")
input("\nDrum roll, please... (type a drum roll) ")
print("\n\nFinal score:", score)
if score == 4:
    print("\nWOW!! You got all of the questions correct," ,name,"! I dub thee an honorary axolotl for the next 42 hours (This term does not apply to any who looked up the answers).\n")
if score == 3:
    print("\nNoice! You got the majority of the questions correct," ,name,". Imaginary high five!\n")
if score == 2:
    print("\nYou got half of the questions correct," ,name,". A valiant effort deserving of an imaginary pat on the back!\n")
if score == 1:
    print("\nHey, at least that's something," ,name,". Hopefully you learned a fact or two about axolotls!\n")
if score == 0:
    print("\nOh...welp, you tried," ,name,". You get a participation award!!\n")
input("Any last words before we end our show? ")

#ending message YAHOOOOOO
print("\nAlright, that's all for the quizshow special of the Amazing Axolotl Gameshow!! Thank you," ,name,", for being our contestant. I hope you had fun, and I am being told we are really short on time, so HAVE A GREAT REST OF YOUR DAY IDEFINITELYDIDN'TEATALLTHOSEROCKSOKAYBYYEE-")
print("\n[CONNECTION LOST]\n")