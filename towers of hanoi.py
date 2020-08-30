from turtle import *
#tutorial,rings,movement,rules,endcheck,recursive function 
print("")
a1x = 45
y1 = 40
a2x = 50
y2 = 30
a3x = 55
y3 = 15
b1x = 115
b2x = 120
b3x = 125
c1x = 185
c2x = 190
c3x = 195
a1s = "occupied by blue"
a2s = "occupied by green"
a3s = "occupied by red"
b1s = "vacant"
b2s = "vacant"
b3s = "vacant"
c1s = "vacant"
c2s = "vacant"
c3s = "vacant"
class ring:
    def __init__(self,color1,color2,color3,thickness,lenght):
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.thickness = thickness
        self.lenght = lenght
    def draw (self):
        colormode(255)
        pencolor(self.color1,self.color2,self.color3)
        pensize(self.thickness)
        fd(self.lenght)
    def erase(self):
        colormode(255)
        pencolor(255,255,255)
        fd(self.lenght)
blue_ring = ring(0,0,255,4,20)
red_ring = ring(255,0,0,4,30)
green_ring = ring(0,255,0,4,40)
def set_towers():
    for _ in range(3):
        speed(0)
        pensize(4)
        fd(35)
        lt(90)
        fd(50)
        rt(180)
        fd(50)
        lt(90)
        fd(35)    
def draw_setup():
    set_towers()
    pu()
    goto(a1x,y1)
    pd()
    rt(180)
    blue_ring.draw()
    pu()
    goto(a2x,y2)
    pd()
    red_ring.draw()
    pu()
    goto(a3x,y3)
    pd()
    green_ring.draw()
draw_setup()
def move():
    fro = input("enter a,b or c in small letters:")
    to = input("enter a,b or c in small letters:")
    if fro == "a":
        if a1s == "occupied by blue":
            goto(a1x,y1)
            blue_ring.erase()
            a1s == "vacant"
#                if to ==
        elif a1s == "vacant":
            if a2s == "occupied by blue":
                goto(a1x,y2)
                blue_ring.erase()
#                if to ==
            elif a2s == "occupied by red":
                goto(a2x,y2)
                green_ring.erase()
#                if to ==             
            elif a2s == "vacant":
                if a3s == "occupied by blue":
                    goto(a1x,y3)
                    blue_ring.erase()
#                if to ==
                elif a3s == "occupied by red":
                    goto(a2x,y3)
                    green_ring.erase()
#                if to ==              
                elif a3s == "occupied by green":
                    goto(a3x,y3)
                    red_ring.erase()
#                if to ==                  
    elif fro == "":
        a = 36538
    elif fro == "":
        r = 7385478305
    else:
        print("you can't cheat :)") 
move()
        
        
        