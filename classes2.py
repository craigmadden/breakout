from graphics2 import *

class GameArea(object):
    def __init__(self):
        self.left = 25
        self.right = 475
        self.bottom = 25
        self.top = 475
        self.rect = Rectangle(Point(25,25),Point(475,475))
        self.rect.setFill("black")


class Paddle(object):
    def __init__(self):
        self.width = 40
        self.height = 10
        self.x = 150
        self.y = 30
        self.rect = Rectangle(Point(150,30),Point(200,40))
        self.rect.setFill("Green")

class Brick(object):
    def __init__(self,x,y,color):
        self.width = 40
        self.height = 10
        self.x = x
        self.y = y
        self.rect = Rectangle(Point(x-20,y-5),Point(x+20,y+5))
        self.rect.setFill(color)


class Ball(object):
    def __init__(self,x,y,r):
        self.circle = Circle(Point(x,y),r)
        self.circle.setFill("blue")
        self.x = x
        self.y = y
        # Create a hit box that consists of the four corners

    def collision_dect(self,rect,direction):
        bx1 = self.x - 2
        bx2 = self.x + 2
        by1 = self.y - 2
        by2 = self.y + 2
        rectx1 = rect.x - 15
        rectx2 = rect.x + 15
        recty1 = rect.y - 10
        recty2 = rect.y + 10
        if not (by2 < recty1 or by1 > recty2 or bx2 < rectx1 or bx1 > rectx2):
            direction[1] *= -1
            return True

