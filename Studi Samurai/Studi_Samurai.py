from pynput.keyboard import Key, Controller
import time
import random
keyboard = Controller()
inp = ""
energy  = 120
drain = 1
gain = 20 
cont = False
exit = False

#Grabs all elements from the study guide into an array
questions = []
answers = []
with open ('Cards.txt', 'rt') as myfile:
    for myline in myfile:     
        if myline.find("Starting points: ") != -1 :
            energy = int(myline[17:]) 
        if myline.find("Points drained per second: ") != -1 :
            drain = int(myline[27:]) 
        if myline.find("Points gained/lost when you answer a question") != -1 : 
            gain = int(myline[myline.find(":") + 2 :]) 
        if myline.find("Q:") != -1:
            questions.append(myline[3:myline.find("A:")])
            answers.append(myline[myline.find("A:") + 2 :])

#Begins the program
while not cont:
    print("Welcome! press enter to start")
    if (input() == ""):
        cont = True
        print("Please open another tab, this will automatically refocus when you run out of energy.")
        time.sleep(5) 
cont = False
#Main Loop
while (exit == False):
    #countdown
    keyboard.press(Key.alt)
    keyboard.press(Key.tab)
    keyboard.release(Key.alt)
    keyboard.release(Key.tab)
    time.sleep(0.1)
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    while (energy > 0):
        
        cont = False
        print("You have " + str(energy) + " energy left")
        energy = energy - drain
        time.sleep(1)
    print("Out of energy, Quiz time!")
    print("")
    #Quiz
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    time.sleep(0.1)
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    time.sleep(0.1)
    keyboard.press(Key.alt)
    keyboard.press(Key.tab)
    keyboard.release(Key.alt)
    keyboard.release(Key.tab)
    while (cont == False):

        #Assign Answers
        tempAnsArr = random.sample(range(0, len(answers)), 4)
        corrIndex = tempAnsArr[random.randint(0, 3)]
        print(questions[corrIndex])
        print("")
        for x in range(0,4):
            print(str(x+1) + ": " + answers[tempAnsArr[x]])
            #Judges you if you got it right and awards/takes away energy
        if (tempAnsArr[int(input()) - 1] == corrIndex):
            print("Good Job!, +" + str(gain) + " energy!")
            energy = energy + gain
        else:
            print("Better luck next time, -" + str(gain) + " energy")
            print("The corrent answer was " + answers[corrIndex])  
            energy = energy - gain
        print("")
        print("you now have " + str(energy))
        print("Press c to go back to your game, press anything else to answer more questions")
        if input() == "c":
            cont = True
            print("Ok, get out of here!")
            time.sleep(3)











