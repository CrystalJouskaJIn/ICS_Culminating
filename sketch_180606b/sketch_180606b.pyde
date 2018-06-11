from random import randint
choice = ""

show = "Questions"

def setup():
    size(1500, 1000)   
    noStroke()
    frameRate(30)
    

def vexquestion():
    global vexq, vexa1, vexa2, vexa3, vexa4, vexca, counter, show, choice, x
    choice = ""
    #Vex Question, Possible answers, and correct answers
    vexq = ["The Drive gear is a 12 tooth, the driven gear is a 60 tooth. What is the ratio?", \
            "Which gear is connected directly to the motor?",\
            "How do idler gears affect your robot?",\
            "Layout for a standard Vex match",\
            "How many teams are in an alliance",\
            "Which one of the following would cause a team to fail an inspection?",\
            "Which of the following components would be in a Pneumatic Subsystem?",\
            "The ratio of output force to the input force applied to a mechanism is _____.",\
            "What is the name of the gear that mates with a pinion gear?",\
            "If a motor is spinning at 50 RPM at 6 Volts, what would be the speed if the voltage was increased to 9 Volts?"\ 
            ]
    
    vexa1 = ["1:5", \
             "The driving gear", \
             "They don’t",\
             "15 Second Auton. 1:45 Second Driver Control",\
             "3",\
             "Soldering the VEX metal",\
             "Elastic tubing",\
             "Mechanical advantage",\
             "Planetary",\
             "25 RPM",\
             ]
    
    vexa2 = ["5:1",\
             "The driven gear",\
             "They change the speed",\
             "30 Second Auton. 1:45 Second Driver Control",\
             "2",\
             "Taping down the VEXnet key",\
             "Piston",\
             "Power",\
             "Spur",\
             "50 RPM"\
             ]
    
    vexa3 = ["1:7",\
             "The small gear",\
             "They change the torque",\
             "15 Second Auton. 1:30 Second Driver Control",\
             "4",\
             "Mounting the flag holder too low",\
             "Motor",\
             "Power",\
             "Rack",\
             "75 RPM"\
             ]
    
    vexa4 = ["3:1",\
             "The big gear",\
             "They change the rotation",\
             "30 Second Auton. 1:30 Second Driver Control",\
             "1",\
             "Cutting a gear in half",\
             "Gear",\
             "Power",\
             "Rack",\
             "100 RPM"\
             ]
    
    vexca = ["1:5",\
             "The driving gear",\
             "They change the rotation",\
             "15 Second Auton. 1:45 Second Driver Control",\
             "2",\
             "Soldering the VEX metal",\
             "Piston",\
             "Mechanical advantage",\
             "Rack",\
             "75 RPM"\
             ]

    counter = 1
    start_time = millis()
    while True:
        if (len(vexq) == 0):
            break
        m = millis()
        if (m - start_time > 120000):
            break
        else:
            x = randint(0, (len(vexq)-1))
            textAlign(CENTER, CENTER)
            fill ("#0D8B2B")
            #Display question and possible answers
            text (vexq[x], 750, 275)
            text (vexa1[x], 400, 502)
            text (vexa2[x], 400, 632)
            text (vexa3[x], 1100, 502)
            text (vexa4[x], 100, 632)
        
        while True:
            m = millis()
            if (m - start_time > 120000):
                break
            
            #User selects a box
            if (choice == "A"):
                if (vexa1[x] == vexca[x]):
                    textAlign(CENTER,CENTER)
                    text ("Correct", 800, 900)
                    counter = counter + 1
                    text (counter, "X" , 650, 900)
                else:
                    text("Wrong", 800, 900)
                
                break
            
            elif (choice == "B"):
                if (vexa2[x] == vexca[x]):
                    textAlign(CENTER,CENTER)
                    text ("Correct", 800, 900)
                    counter = counter + 1
                    text (counter, "X" , 650, 900)
                else:
                    text("Wrong", 800, 900)
                break
                
            elif (choice == "C"):
                if (vexa3[x] == vexca[x]):
                    textAlign(CENTER,CENTER)
                    text ("Correct", 800, 900)
                    counter = counter + 1
                    text (counter, "X" , 650, 900)
                else:
                    text("Wrong", 800, 900)
                break
                    
            elif (choice == "D"):
                if (vexa4[x] == vexca[x]):
                    textAlign(CENTER,CENTER)
                    text ("Correct", 800, 900)
                    counter = counter + 1
                    text (counter, "X" , 650, 900)
                else:
                    text("Wrong", 800, 900)
                break
                    
            #Remove the question from list
            vexq.pop(x)
            vexa1.pop(x)
            vexa2.pop(x)
            vexa3.pop(x)
            vexa4.pop(x)
            vexca.pop(x)
        
        show = "PrepF"
        
def draw():  
    global show, choice
    if (show == "Questions"):
        global counter
        background ("#0D8B2D")
        fill("#FFFFFF")
        #Question Box
        rect(0, 125, 1500, 300)  
        #Answer Box
        #vexa1
        rect(100, 450, 600, 105, 10)
        #vexa2
        rect(100, 580, 600, 105, 10)
        #vexa3
        rect(800, 450, 600, 105, 10)
        #vexa4
        rect(800, 580, 600, 105, 10)
        
        vexquestion()
            
        
    elif (show == "PrepF"):
        background ("#0D8B2B")
        fill ("#FFFFFF")
        rect(0, 125, 1500, 300)
        fill("#0D8B2B")



def mouseClicked():
    global choice
    
    #Question choices
    if  (mouseX> 100 and mouseX< 100 + 600 and mouseY> 450 and mouseY< 450 + 105 and show == "Questions"):
        choice = "A"
    elif  (mouseX> 100 and mouseX< 100 + 600 and mouseY> 580 and mouseY< 580 + 105 and show == "Questions"):
        choice = "B"
    elif  (mouseX> 800 and mouseX< 800 + 600 and mouseY> 450 and mouseY< 450 + 105 and show == "Questions"):
        choice = "C"
    elif  (mouseX> 800 and mouseX< 800 + 600 and mouseY> 580 and mouseY< 580 + 105 and show == "Questions"):
        choice = "D"
    
