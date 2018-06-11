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

# class enemy(object):
#     def __init__(self):
#         self.x = 1000
#         self.y = 500
#         self.w = 100
#         self.h = 100
#         self.r = 50
#         self.xspeed = 10
#         self.yspeed = 10
#         self.xdirection = 1
#         self.ydirection = 1
        
#     def show(self):
#         fill(0)
#         image(yannik_img, self.x, self.y, self.w, self.h)
        
#     def update(self):
#         self.x = self.x + self.xspeed * self.xdirection
#         self.y = self.y + self.yspeed * self.ydirection

#         if (self.x < self.r) or (self.w - self.r < self.x):
#             self.xdirection *= -1
#         if (self.x < self.r) or (self.h - self.r < self.y):
#             self.ydirection *= -1
        
show = "Game"

def setup():  
    size (s_width, s_height)
    noStroke()
    frameRate(30)
    global p, xpos, ypos
    p = player()
    global crystal_img, p
    crystal_img = loadImage("Crystal.PNG")
       
def draw():  
    if (show == "Game"):
        background ("#FFFFFF")
        background(100)
        p.show()
        p.update()


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
            
            
  
