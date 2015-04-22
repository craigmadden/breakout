from graphics import *

class GameArea(object):
    def __init__(self):
        self.left = 25
        self.right = 475
        self.bottom = 25
        self.top = 475
        self.rect = Rectangle(Point(25,25),Point(475,475))
        self.rect.setFill("white")

    def collision_detection(self,pt, direction):
        if pt.getX() <= self.left:
            direction[0] = 5
            return True
        elif pt.getX() >= self.right:
            direction[0] *= -1
            return True
        if pt.getY() >= self.top:
            direction[1] *= -1
            return True
        elif pt.getY() <= self.bottom:
            direction[1] = 5
            return True
        self.direction = direction


class Paddle(object):
    def __init__(self):
        self.width = 40
        self.height = 10
        self.x = 150
        self.y = 30
        self.rect = Rectangle(Point(150,30),Point(200,40))
        self.rect.setFill("Green")

    def collision_detect(self,pt, paddle_pt, direction):
        paddle_lx = paddle_pt.getX()
        paddle_rx = paddle_pt.getX() + 40
        paddle_y = paddle_pt.getY() + 10

        if pt.getY() <= paddle_y:
            if pt.getX() >= paddle_lx and pt.getX() <= paddle_rx:
                direction[1] = 5
                return True

        self.direction = direction

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
        if not (by2 < recty1 || by1 > )
        #print bx1,bx2,by1,by2,rectx1,rectx2,recty1,recty2
        # if bx1 >= rectx1 and bx1 <= rectx2:
        #     if by1 >= recty1 and by1 <= recty2:
        #         direction[1] = 5
        #         return True
        # elif bx2 >= rectx1 and bx2 <= rectx2:
        #     if(by1 >= recty1 and by1 <= recty2) or (by2 >= recty1 and by2 <= recty2):
        #         # Ball is inside rectangle
        #         direction[1]=5
        #         return True
