show = "Game"
e_radius = 50
e_xspeed = 10
e_yspeed = 10
e_xpos = 0
e_ypos = 0
xdirection = 1
e_ydirection = 1

from random import randint
s_width = 1500
s_height = 1000

class player(object):
    def __init__(self):
        self.x = 500
        self.y = 750
        self.up = 0
        self.down = 0
        self.left = 0
        self.right = 0
        self.speed = 15
        self.h = 100
        self.w = 100
    def show(self):
        image(crystal_img, self.x, self.y, self.w, self.h)
    def update(self):
        self.x = self.x + (self.right - self.left)*self.speed
        self.y = self.y + (self.down - self.up)*self.speed
        if (self.x <= 0):
            self.x = 0
        if (self.x >= (s_width - self.w)):
            self.x = (s_width - self.w)
        if (self.y <= 0):
            self.y = 0
        if (self.y >= (s_height - self.h)):
            self.y = (s_height - self.h)

def setup():
    size(1500, 1000)   #
    global e_xpos, e_ypos, yannik_img, crystal_img, p
    noStroke()
    frameRate(30)
    ellipseMode(e_radius)
    e_xpos = 500
    e_ypos = 750
    p = player()
    yannik_img = loadImage("Yannik.PNG")
    crystal_img = loadImage("Crystal.PNG")

def draw(): 
    global e_xpos, e_ypos, xdirection, e_ydirection, yannik_img
    background(102)
    
    if (show == "Game"):
            background ("#FFFFFF")
            background(100)
            p.show()
            p.update()
    
            e_xpos = e_xpos + e_xspeed * xdirection   #accumulator 
            e_ypos += e_yspeed * e_ydirection
            
            if (e_xpos < e_radius) or (s_width - e_radius < e_xpos):
                xdirection *= -1
            
            if (e_ypos < e_radius) or (s_height - e_radius < e_ypos):
                e_ydirection *= -1
            image(yannik_img, e_xpos, e_ypos, 100, 100)

def keyPressed():  #this method activates whenever a key is pressed activating the desired diretion
    if (key == "W" or key == "w"):
        p.up=1
    if (key == "S" or key == "s"):
        p.down= 1
    if (key == "A" or key == "a"):
        p.left= 1
    if (key == "D" or key == "d"):
        p.right= 1
                    
def keyReleased():   #whenever a key is released it stops the direction
    if (key == "W" or key == "w"):
        p.up= 0
    if (key == "S" or key == "s"):
        p.down= 0
    if (key == "A" or key == "a"):
        p.left= 0
    if (key == "D" or key == "d"):
        p.right= 0
