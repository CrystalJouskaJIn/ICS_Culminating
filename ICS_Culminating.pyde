'''
Title: Lancebotics Fight Club
Author: Crystal Jin
BETA Testers:
Description: Python Game Culminating
'''
from random import randint
import math

#Start Up Variables
show = "Welcome"
selected = "No"
counter = 1
answer = "None"
game_start = 0
already_calc = 0
#Reset weapon position
reset = 0 

#Vex Questions, Possible answers, and correct answers
vexq = ["The Drive gear is a 12 tooth, the driven gear is a 60 tooth. What is the ratio?", \
        "Which gear is connected directly to the motor?",\
        "How do idler gears affect your robot?",\
        "Layout for a standard Vex match",\
        "How many teams are in an alliance",\
        "Which one of the following would cause a team to fail an inspection?",\
        "Which of the following components would be in a Pneumatic Subsystem?",\
        "The ratio of output force to the input force applied to a mechanism is _____.",\
        "What is the name of the gear that mates with a pinion gear?",\
        "A motor is spinning at 50 RPM at 6 Volts, what's the speed at 9 Volts?"\ 
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
        "Strength",\
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
        "Friction",\
        "Screw",\
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

#Get random number for index of lists
x = randint(0, (len(vexq)-1))


#Shoutout to Sam's code with helped me understand how to do classes
#Player Class
class Player(object):
    #Intialize with player and weapon image, speed 
    def __init__ (self, player, weapon, player_speed):
        self.player = player
        self.weapon = weapon
        self.player_speed = player_speed 
        
        #Inital X location
        self.positionX = 100
        #Initial Y location
        self.positionY = 900
        
        #Going up
        self.up = 0
        #Going down
        self.down = 0
        #Going left
        self.left = 0
        #Going right
        self.right = 0
        
    #Function for actually showing the player
    def show(self):
        image(self.player, self.positionX, self.positionY, 100, 100)
        image(self.weapon, self.positionX + 100, self.positionY + 50, 100, 100)
        
    #Function to move. Code from Sam from Farees
    def move(self):
        self.positionX += (self.right - self.left)*self.player_speed
        self.positionY += (self.down - self.up) * self.player_speed
    
    #Function for boundary checker
    def boundary(self):
        if (self.positionX < 0):
            self.positionX = 0
        if (self.positionX > 1400):
            self.positionX = 1400
        if (self.positionY < 0):
            self.positionY = 0
        if (self.positionY > 900):
            self.positionY = 900

class Enemy(object):
    #Intialize with enemy and weapon image
    def __init__(self, enemy, enemy_speed):
        self.enemy = enemy
        self.enemy_speed = enemy_speed
        self.positionX = 750
        self.positionY = 500
        self.directionX = 1
        self.directionY = 1
        
    #Function for actually showing the enemy
    def show(self):
        image(enemy, self.positionX, self.positionY, 100, 100)
        
    #Function to move. Will go in one direction, once hit boundary switch. Update of mrv provided code
    def move(self):
        self.positionX+= self.enemy_speed * self.directionX
        self.positionY += self.enemy_speed * self.directionY
        
        if (self.positionX <= 0) or (self.positionX >= 1400):
            self.directionX *= -1
        if (self.positionY <= 100) or (self.positionY >= 900):
            self.directionY *= -1
    
class Shoot(object):
    #Intialize with weapon image, location, speed, mouse position
    def __init__(self, weapon, weapon_speed):
        self.weapon = weapon
        self.weapon_speed = weapon_speed
        #self.enemy_object = enemy_object
        self.positionPX = 0
        self.positionPY = 0
        self.positionMX = 0
        self.positionMY = 0
        
    #Check if they have enough weapons
    def enough_weapon(self, counter):
        self.counter = counter
        if (counter == 0):
            show = "Game Over"
        
    #Calculate slope of the line that weapon must follow to go to mouse clicked X,Y
    def calc(self, positionPX, positionPY, positionMX, positionMY):
        self.positionPX = positionPX
        self.positionPY = positionPY
        self.positionMX = positionMX
        self.positionMY = positionMY
        
        #Distance
        d = math.sqrt((positionPX - positionMX)**2 + (positionPY - positionMY)**2)
        #Time
        t = d / weapon_speed
        #Delta X (How much it must travel each second)
        self.deltaX = (positionMX - positionPX)/t
        #Delta Y (how much it must travel each second)
        self.deltaY = (positionMY - positionPY)/t
        
        self.currentX = self.positionPX + self.deltaX
        self.currentY = self.positionPY + self.deltaY
    
    #Showing the weapon
    def show(self):
        image(self.weapon, self.currentX, self.currentY, 100, 100)

    #Moving the weapon
    def move(self):
        self.currentX += self.deltaX
        self.currentY += self.deltaY
                
    #Boundaries    
    def boundary(self):
        is_boundary = 0
        if (self.currentX >= 1500 or self.currentX <= 0 or self.currentY >= 1000 or self.currentY <= 0):
            is_boundary = 1
        return is_boundary
        
    def hit(self, enemyX, enemyY):
        is_hit = 0
        d_WE = math.sqrt ((self.currentX - enemyX)**2 + (self.currentY - enemyY)**2)
        #Distance between weapon and enemy is less than 1
        if (d_WE <= 100):
            print("Yes")
            is_hit = 1
        return is_hit
                

def setup():
    size(1500, 1000)   
    noStroke()
    frameRate(30)

    global lancebotics_img, fightclub_img, mrv_img, crystal_img, chris_img, yannik_img, shashank_img, farees_img, sam_img 
    global metal_img, gear_img, wrench_img, screw_img, motor_img, cortex_img 
    global tp_img, explosion_img, show, game_start
    

    #Image loading
    lancebotics_img = loadImage("Lancebotics.png")
    fightclub_img = loadImage ("FightClub.png")
    #Background Images
    tp_img = loadImage("turningpoint.png")
    tp_img.resize(1500,1000)
    #Character Images
    mrv_img = loadImage("mrv.jpg")
    crystal_img = loadImage("Crystal.PNG")
    chris_img = loadImage("Chris.PNG")
    yannik_img = loadImage("Yannik.PNG")
    shashank_img = loadImage("Shashank.jpg")
    farees_img = loadImage("Farees.jpg")
    sam_img = loadImage("Sam.jpg")

    #Weapon Imagery
    metal_img = loadImage("Metal.jpg")
    gear_img = loadImage("Gear.jpg")
    wrench_img = loadImage("Wrench.jpg")
    screw_img = loadImage("Screw.jpg")
    motor_img = loadImage("Motor.png")
    cortex_img = loadImage("Cortex.jpg")
    ball_img = loadImage("ball.jpg")
    explosion_img = loadImage("explosion.png")


def welcome():
    textSize(75)
    background("#0D8B2B")
    startb()
    #Lancebotics Image
    imageMode(CENTER)
    image (lancebotics_img, 750, 150, 1143, 124)
    #Fight Club image
    image (fightclub_img, 1100, 550, 400, 400)
    
    #Character Images
    #Mrv
    image (mrv_img, 200, 400, 100, 100)
    #Crystal
    image (crystal_img, 400, 400, 100, 100)
    #Chris
    image (chris_img, 600, 400, 100, 100)
    #Yannik
    image (yannik_img, 100, 600, 100, 100)
    #Shashank
    image (shashank_img, 300, 600, 100, 100)
    #Farees
    image (farees_img, 500, 600, 100, 100)
    #Sam
    image (sam_img, 700, 600, 100, 100)
    
#Character Selection Setup
def player_setup():
    #Character Abilities
    #Chris Abilities
    fill("#FFFFFF")
    rect(60, 150, 300, 300, 10)
    image (chris_img, 210, 230, 150, 150)
    textAlign (CENTER, TOP)
    fill("#0D8B2B")
    textSize(30)
    text("Chris", 210, 310)
    textSize(20)
    text("Strengths: Strong Boi", 210, 350)
    text("Weakness: Weird ideas", 210, 390)
        
    #Crystal Abilities
    fill("#FFFFFF")
    rect(420, 150, 300, 300, 10)
    image (crystal_img, 570, 230, 150, 150)
    textAlign (CENTER, TOP)
    fill("#0D8B2B")
    textSize(30)
    text("Crystal", 570, 310)
    textSize(20)
    text("Strengths: Memorization", 570, 350)
    text("Weakness: Incoherent", 570, 390)
    
    #Yannik Abilities
    fill("#FFFFFF")
    rect(780, 150, 300, 300, 10)
    image (yannik_img, 930, 230, 150, 150)
    textAlign (CENTER, TOP)
    fill("#0D8B2B")
    textSize(30)
    text("Yannik", 930, 310)
    textSize(20)
    text("Strengths: Tall", 930, 350)
    text("Weakness: Lanky", 930, 390)
    
    #Sam Abilities
    fill("#FFFFFF")
    rect(1140, 150, 300, 300, 10)
    image (sam_img, 1290, 230, 150, 150)
    textAlign (CENTER, TOP)
    fill("#0D8B2B")
    textSize(30)
    text("Sam", 1290, 310)
    textSize(20)
    text("Strengths: Fast", 1290, 350)
    text("Weakness: Blind", 1290, 390)
    
    #Farees Abilities
    fill("#FFFFFF")
    rect(780, 550, 300, 300, 10)
    image (farees_img, 930, 630, 150, 150)
    textAlign (CENTER, TOP)
    fill("#0D8B2B")
    textSize(30)
    text("Farees", 930, 710)
    textSize(20)
    text("Strengths: Auton?", 930, 750)
    text("Weakness: Brittle Bones", 930, 790)

    #Shashank Abilities
    fill("#FFFFFF")
    rect(1140, 550, 300, 300, 10)
    image (shashank_img, 1290, 630, 150, 150)
    textAlign (CENTER, TOP)
    fill("#0D8B2B")
    textSize(30)
    text("Shashank", 1290, 710)
    textSize(20)
    text("Strengths: Talker ", 1290, 750)
    text("Weakness: Short Temper", 1290, 790)

# Weapon Selection Setup
def weapon_setup():
    #Weaponry
    #Metal
    fill("#FFFFFF")
    rect(60, 150, 300, 300, 10)
    image (metal_img, 210, 230, 150, 150)
    textAlign (CENTER, TOP)
    fill("#0D8B2B")
    textSize(30)
    text("Metal", 210, 310)
    textSize(20)
    text("Aluminum & Steel", 210, 350)
    text("Structure of the Robot", 210, 390)
        
    #Gear/Sprocket/Chain
    fill("#FFFFFF")
    rect(420, 150, 300, 300, 10)
    image (gear_img, 570, 230, 150, 150)
    textAlign (CENTER, TOP)
    fill("#0D8B2B")
    textSize(30)
    text("Gear & Sprocket", 570, 310)
    textSize(20)
    text("High Strength & Low Strength", 570, 350)
    text("Speed/Torque", 570, 390)
    
    #Wrench and Allen Keys
    fill("#FFFFFF")
    rect(780, 150, 300, 300, 10)
    image (wrench_img, 930, 230, 150, 150)
    textAlign (CENTER, TOP)
    fill("#0D8B2B")
    #If you're reading this Crystal did not check her code over
    textSize(30)
    text("Wrench & Allen Keys", 930, 310)
    textSize(20)
    text("German or L", 930, 350)
    text("Secure Screws", 930, 390)
    
    #Screws and Nylocks
    fill("#FFFFFF")
    rect(1140, 150, 300, 300, 10)
    image (screw_img, 1290, 230, 150, 150)
    textAlign (CENTER, TOP)
    fill("#0D8B2B")
    textSize(30)
    text("Screws & Nylocks", 1290, 310)
    textSize(20)
    text("Aluminum & Steel", 1290, 350)
    text("Glue of the robot", 1290, 390)
    
    #Motors
    fill("#FFFFFF")
    rect(780, 550, 300, 300, 10)
    image (motor_img, 930, 630, 150, 150)
    textAlign (CENTER, TOP)
    fill("#0D8B2B")
    textSize(30)
    text("Motors", 930, 710)
    textSize(20)
    text("Torque/Speed/Turbo", 930, 750)
    text("To power the robot", 930, 790)
    
    #Cortex
    fill("#FFFFFF")
    rect(1140, 550, 300, 300, 10)
    image (cortex_img, 1290, 630, 150, 150)
    textAlign (CENTER, TOP)
    fill("#0D8B2B")
    textSize(30)
    text("Cortex & Controller", 1290, 710)
    textSize(20)
    text("V5 or V4", 1290, 750)
    text("Brain of the robot", 1290, 790)
    
# Display pic depending on player selected
def player_select():
    fill ("#FFFFFF")
    textAlign(CENTER, BOTTOM)
    textSize(40)
    text("YOU", 570, 550)
    
    image (player, 570, 630, 150, 150)
    
# Display enemy depending on enemy selected
def enemy_select():
    global enemy
    fill ("#FFFFFF")
    textAlign(CENTER, BOTTOM)
    textSize(40)
    text("ENEMY", 570, 750)
    
    image (enemy, 570, 830, 150, 150)

# Display weapon depending on weapon selected
def weapon_select():
    global weapon
    fill ("#FFFFFF")
    textAlign(CENTER, BOTTOM)
    textSize(40)
    text("WEAPON", 325, 550)
    
    image (weapon, 325, 630, 150, 150)
    
def vexquestions():
    global counter, x, em, sm, show
    background ("#0D8B2D")
    #Timer for 2 mins
    if (em - sm <= 10000):
        fill ("#FFFFFF")
        textSize(40)
        text ("Time Left: " + str((10000-em+sm)/1000), 1000, 900)
        #Question Box
        fill("#FFFFFF")
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
        
        quit()
        fill("#FFFFFF")
        text(str(counter)+"X WEAPON", 1200, 710)
    
        
        #Display question and possible answers
        
        textAlign(CENTER, CENTER)
        fill ("#0D8B2B")
        textSize(30)
        text (vexq[x], 750, 275)
        textSize(20)
        text (vexa1[x], 400, 502)
        text (vexa2[x], 400, 632)
        text (vexa3[x], 1100, 502)
        text (vexa4[x], 1100, 632)

    else:
        show = "PrepF"        

# Start button
def startb():
    fill("#FFFFFF")
    rect(100, 710, 300, 100, 10)
    fill("#0D8B2B")
    textAlign(CENTER, CENTER)
    textSize(60)
    text("Start", 250, 760)

# Next button
def next():
    fill("#FFFFFF")
    rect(600, 850, 300, 100, 10) 
    fill("#0D8B2B")
    textAlign(CENTER, CENTER)
    textSize(40)
    text("Next Q", 750, 900)

#Help button
def help():
    fill("#FFFFFF")
    rect(100, 850, 300, 100, 10)
    fill("#0D8B2B")
    textAlign(CENTER, CENTER)
    textSize(60)
    text("Help", 250, 900)

#Exit Game Button
def exitb():
    fill("#FFFFFF")
    rect(100, 850, 300, 100, 10)
    fill("#0D8B2B")
    textAlign(CENTER, CENTER)
    textSize(40)
    text("Exit", 250, 900)
        
        
# Quit button
def quit():
    fill("#FFFFFF")
    rect(100, 850, 300, 100, 10)
    fill("#0D8B2B")
    textAlign(CENTER, CENTER)
    textSize(60)
    text("Quit", 250, 900)
    
        
def draw():  
    global selected, choice, next_quest, x, counter, answer, sm, em 
    global player, enemy, weapon, show
    global P, E, S, game_start, already_calc, reset
    background("#0D8B2B")
    
    # Welcome Screen
    if (show == "Welcome"):
        welcome()
        help()
        
    # Help Screen 
    elif (show == "Help"):
        fill("#FFFFFF")
        textAlign(CENTER, BOTTOM)
        textSize(35)
        text("How to play \n Select your character \n Select your enemy \n Select your weapon \n Answer Questions: 1 Correct answer = 1+ weapon \n Launch Weapons at Enemy \n Every player has different health/speed", 750, 100)
        quit()
    
    # Character Selection Screen
    elif (show == "Character"):
        fill("#FFFFFF")
        textAlign(CENTER, BOTTOM)
        textSize(50)
        text ("Select your character", 750, 100)
        
        player_setup()
        quit()
        
    # Enemy Selection Screen  
    elif (show == "Enemy"):
        fill("#FFFFFF")
        textAlign(CENTER, BOTTOM)
        textSize(50)
        text ("Select your Enemy", 750, 100)
    
        player_setup()
        player_select()    
        quit()
    
    # Weapon Selection Screen
    elif (show == "Weapon"):        
        fill("#FFFFFF")
        textAlign(CENTER, BOTTOM)
        textSize(50)
        text ("Select your Weapon", 750, 100)
        
        weapon_setup()
        player_select()
        enemy_select()
        quit()
    
    # Mrv Alert Screen / Explaning rules
    elif (show == "Mrv Alert"):
        fill("#FFFFFF")
        textAlign(CENTER, BOTTOM)
        textSize(50)
        text ("AVOID MRV", 750, 100)
        rect(0, 125, 1500, 300)
        fill("#0D8B2D")
        textAlign(CENTER, CENTER)
        text("AH! You're in RM.124 without supervision \n Collect as many parts as you can before MRV kicks you out! \n Gain a weapon every correct answer to a question \n You have 2 minutes good luck", 750, 275)
        image(mrv_img, 1125, 750, 500, 500)
        player_select()
        enemy_select()
        weapon_select()
        startb()
        quit()
    
    #Question Screen
    elif (show == "Questions"):
        em = millis()
        vexquestions()
        
    
    elif(show == "Correct/Wrong"):
        fill("#FFFFFF")
        textAlign (CENTER, CENTER)
        textSize(60)
        if (answer == "Correct"):
            text ("Correct", 750, 500)
        elif (answer == "Wrong"):
            text("Wrong", 750, 500)
        next()
            
    elif (show == "PrepF"):
        fill ("#FFFFFF")
        rect(0, 125, 1500, 300)
        fill("#0D8B2B")
        text ("It is time to defeat the final boss \n Ready?", 750, 275)
        fill("#FFFFFF")
        text(str(counter)+"X WEAPON", 1200, 710)
        player_select()
        enemy_select()
        weapon_select()
        startb()
        quit()
    
    elif (show == "Game"):
        background (tp_img)
        fill ("#FFFFFF")
        textSize(60)
        textAlign(CENTER, CENTER)
        text("WEAPONS LEFT:" + str(counter), 1200, 800)
        #If intialized, dont intialize the object again
        if game_start == 0:
            P = Player(player, weapon, player_speed)
            E = Enemy(enemy, enemy_speed)
            S = Shoot(weapon, weapon_speed)
            game_start = 1
        
        P.show()
        P.move()
        P.boundary()
        E.show()
        E.move()
        S.enough_weapon()
        if (already_calc == 1):
            S.show()
            S.move()
            is_hit = S.hit(E.positionX, E.positionY)
            if (is_hit == 1):
                show = "Win"
            at_boundary = S.boundary()
            if (at_boundary == 1):
                already_calc = 0
    
    elif (show == "Win"):
        fill("#FFFFFF")
        textAlign(CENTER, CENTER)
        textSize(80)
        text("WINNER \n Thanks for Playing", 750, 500)
        #exit button
        exitb()
    
    elif (show == "Game Over"):
        fill("#FFFFFF")
        textSize(80)
        textAlign(CENTER, CENTER)
        text("Game Over", 750, 500)
        #exit button
        exitb()
        
        

def mouseClicked():
    global show, player, player_speed, enemy, enemy_speed, weapon, weapon_speed, choice,  x, answer, counter, sm, speed, P, E, S, positionMX, positionMY, already_calc
    
    #Starting
    if  (mouseX> 100 and mouseX< 100 + 300 and mouseY> 700 and mouseY< 700+100 and show == "Welcome"):
        show = "Character"
    elif  (mouseX> 100 and mouseX< 100 + 300 and mouseY> 700 and mouseY< 700+100 and show == "Mrv Alert"):
        show = "Questions"
        sm=millis()
    elif (mouseX> 100 and mouseX<100 + 300 and mouseY>700 and mouseY<700+100 and show == "PrepF"):
        show = "Game"
        
    #Help Screen
    elif (mouseX > 100 and mouseX < 100 + 300 and mouseY > 850 and mouseY < 850 + 100 and show == "Welcome"):
        show = "Help"

    #Quitting 
    elif  (mouseX> 100 and mouseX< 100 + 300 and mouseY> 850 and mouseY< 850 +100) and (show == "Help" or show == "Character" or show == "Enemy" or show == "Weapon" or show == "Mrv Alert" or show == "Questions"):
        show = "Welcome"
        
    #Selecting your character
    elif  (mouseX> 60 and mouseX< 60 + 300 and mouseY> 150 and mouseY< 150 + 300 and show == "Character"):
        show = "Enemy"
        player = chris_img
        player_speed = 7
    elif  (mouseX> 420 and mouseX< 420 + 300 and mouseY> 150 and mouseY< 150 + 300 and show == "Character"):
        show = "Enemy"
        player = crystal_img
        player_speed = 15
    elif  (mouseX> 780 and mouseX< 780 + 300 and mouseY> 150 and mouseY< 150 + 300 and show == "Character"):
        show = "Enemy"
        player = yannik_img
        player_speed = 8
    elif  (mouseX> 1140 and mouseX< 1140 + 300 and mouseY> 150 and mouseY< 150 + 300 and show == "Character"):
        show = "Enemy"
        player = sam_img
        player_speed = 12
    elif  (mouseX> 780 and mouseX< 780 + 300 and mouseY> 550 and mouseY< 550 + 300 and show == "Character"):
        show = "Enemy"
        player = farees_img
        player_speed = 7
    elif  (mouseX> 1140 and mouseX< 1140 + 300 and mouseY> 550 and mouseY< 550 + 300 and show == "Character"):
        show = "Enemy"
        player = shashank_img
        player_speed = 6
    
    #Selecting your enemy
    elif  (mouseX> 60 and mouseX< 60 + 300 and mouseY> 150 and mouseY< 150 + 300 and show == "Enemy"):
        show = "Weapon"
        enemy = chris_img
        enemy_speed = 7
    elif  (mouseX> 420 and mouseX< 420 + 300 and mouseY> 150 and mouseY< 150 + 300 and show == "Enemy"):
        show = "Weapon"
        enemy = crystal_img
        enemy_speed = 15
    elif  (mouseX> 780 and mouseX< 780 + 300 and mouseY> 150 and mouseY< 150 + 300 and show == "Enemy"):
        show = "Weapon"
        enemy = yannik_img
        enemy_speed = 8
    elif  (mouseX> 1140 and mouseX< 1140 + 300 and mouseY> 150 and mouseY< 150 + 300 and show == "Enemy"):
        show = "Weapon"
        enemy = sam_img
        enemy_speed = 12
    elif  (mouseX> 780 and mouseX< 780 + 300 and mouseY> 550 and mouseY< 550 + 300 and show == "Enemy"):
        show = "Weapon"
        enemy = farees_img
        enemy_speed = 7
    elif  (mouseX> 1140 and mouseX< 1140 + 300 and mouseY> 550 and mouseY< 550 + 300 and show == "Enemy"):
        show = "Weapon"
        enemy = shashank_img
        enemy_speed = 6
        
    #Selecting your weapon
    elif  (mouseX> 60 and mouseX< 60 + 300 and mouseY> 150 and mouseY< 150 + 300 and show == "Weapon"):
        show = "Mrv Alert"
        weapon = metal_img
        weapon_speed = 40
    elif  (mouseX> 420 and mouseX< 420 + 300 and mouseY> 150 and mouseY< 150 + 300 and show == "Weapon"):
        show = "Mrv Alert"
        weapon = gear_img
        weapon_speed = 25
    elif  (mouseX> 780 and mouseX< 780 + 300 and mouseY> 150 and mouseY< 150 + 300 and show == "Weapon"):
        show = "Mrv Alert"
        weapon = wrench_img
        weapon_speed = 27
    elif  (mouseX> 1140 and mouseX< 1140 + 300 and mouseY> 150 and mouseY< 150 + 300 and show == "Weapon"):
        show = "Mrv Alert"
        weapon = screw_img
        weapon_speed = 20
    elif  (mouseX> 780 and mouseX< 780 + 300 and mouseY> 550 and mouseY< 550 + 300 and show == "Weapon"):
        show = "Mrv Alert"
        weapon = motor_img
        weapon_speed = 29
    elif  (mouseX> 1140 and mouseX< 1140 + 300 and mouseY> 550 and mouseY< 550 + 300 and show == "Weapon"):
        show = "Mrv Alert"
        weapon = cortex_img
        weapon_speed = 35
    
    #Question Period
    #Question choices. Compares if the selected answer is correct. If correct, adds to weapon counter
    #A
    elif  (mouseX> 100 and mouseX< 100 + 600 and mouseY> 450 and mouseY< 450 + 105 and show == "Questions"):
        if (vexa1[x] == vexca[x]):
            answer = "Correct"
            counter = counter + 1
        else:
            answer = "Wrong"
        show = "Correct/Wrong"
    #B
    elif  (mouseX> 100 and mouseX< 100 + 600 and mouseY> 580 and mouseY< 580 + 105 and show == "Questions"):
        if (vexa2[x] == vexca[x]):
            answer = "Correct"
            counter = counter + 1
        else:
            answer = "Wrong"
        show = "Correct/Wrong"
    #C
    elif  (mouseX> 800 and mouseX< 800 + 600 and mouseY> 450 and mouseY< 450 + 105 and show == "Questions"):
        if (vexa3[x] == vexca[x]):
            answer = "Correct"
            counter = counter + 1
        else:
            answer = "Wrong"
        show = "Correct/Wrong"
    #D
    elif  (mouseX> 800 and mouseX< 800 + 600 and mouseY> 580 and mouseY< 580 + 105 and show == "Questions"):
        if (vexa4[x] == vexca[x]):
            answer = "Correct"
            counter = counter + 1
        else: 
            answer = "Wrong"
        show = "Correct/Wrong"
    
    #Next Question. Removes previously used question from list
    elif (mouseX> 600 and mouseX< 600 + 300 and mouseY> 850 and mouseY< 850 + 100 and show == "Correct/Wrong"):
        vexq.pop(x)
        vexa1.pop(x)
        vexa2.pop(x)
        vexa3.pop(x)
        vexa4.pop(x)
        vexca.pop(x)
        if (len(vexq) == 0):
            show = "PrepF"
        else:
            x = randint(0, (len(vexq)-1))
            answer = "None"
            show = "Questions"
    
    #Actual Game
    elif (show == "Game"):
        if (already_calc == 0):
            S.calc(P.positionX, P.positionY, mouseX, mouseY)
            already_calc = 1
            counter = counter - 1

    #Exit Game 
    elif (mouseX > 100 and mouseX < 100 + 300 and mouseY > 850 and mouseY < 850 + 100) and (show == "Win" or show == "Game Over"):
        exit()
    
#Player Movement
def keyPressed(): 
    if (key == "W" or key == "w"):
        P.up=1
    if (key == "S" or key == "s"):
        P.down= 1
    if (key == "A" or key == "a"):
        P.left= 1
    if (key == "D" or key == "d"):
        P.right= 1
    # if (keyCode == "SPACE"):
        
#whenever a key is released it stops the direction      
def keyReleased():   
    if (key == "W" or key == "w"):
        P.up= 0
    if (key == "S" or key == "s"):
        P.down= 0
    if (key == "A" or key == "a"):
        P.left= 0
    if (key == "D" or key == "d"):
        P.right= 0

    
    

 
