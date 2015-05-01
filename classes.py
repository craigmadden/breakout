from graphics import *

BALL_SPEED = 1

class GameArea(object):
    def __init__(self):
        self.left = 25
        self.right = 475
        self.bottom = 25
        self.top = 475
        self.rect = Rectangle(Point(25,25),Point(475,475))
        self.rect.setFill("black")

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

class Paddle(object):
    def __init__(self):
        self.width = 40
        self.height = 10

        # X and Y are the lower left of paddle and starting position
        self.x = 250
        self.y = 30
        self.left = self.x - 20
        self.right = self.x + 20
        self.top = self.y + self.height
        self.rect = Rectangle(Point(self.x, self.y), Point(self.x + self.width, self.y + self.height))
        self.rect.setFill("Green")

    def move(self, x, y=0):
        # Move paddle to new position and update the current location of the paddle
        self.rect.move(x, y)
        self.x += x
        self.y += y
        self.left = self.x - 20
        self.right = self.x + 20

class Brick(object):
    def __init__(self,x,y,color):
        self.width = 40
        self.height = 10
        self.x = x
        self.y = y
        self.top = self.y + 10
        self.left = self.x - 20
        self.right = self.x + 20
        self.rect = Rectangle(Point(self.x, self.y), Point(self.x + self.width, self.y + self.height))
        self.rect.setFill(color)

class Ball(object):
    def __init__(self, x, y, radius):
        self.circle = Circle(Point(x, y), radius)
        self.circle.setFill("blue")

        # X and Y is the center of the ball
        self.x = x
        self.y = y
        self.radius = radius
        # Create a hit box that consists of the four corners

    def move(self, x, y):
        # Move ball to new position and update the current location
        self.circle.move(x, y)
        self.x += x
        self.y += y

    def hits_paddle(self, paddle, direction):
        # Bottom of ball is self.y - self.radius
        if (self.y - self.radius) <= paddle.top and (self.x - 23) > paddle.left and (self.x - 23) < paddle.right:
            print self.x, paddle.left, paddle.right
            direction[1] *= -1

    def hits_brick(self, brick, direction, bricks, item):
        if not ((self.y + self.radius) < brick.y or (self.y - self.radius) > brick.top or (self.x + self.radius) < brick.left or (self.x - self.radius) > brick.right):
            direction[1] *= -1
            bricks.pop(item)
            brick.rect.undraw()

    def is_below_paddle(self, paddle):
        # The bottom of the ball is self.y - self.radius
        return (self.y - self.radius) < paddle.top

    def hits_wall(self, gamearea, direction):
        if (self.x - self.radius) <= gamearea.left:
            direction[0] = BALL_SPEED
        elif (self.x + self.radius) >= gamearea.right:
            direction[0] = -BALL_SPEED
        elif (self.y + self.radius) >= gamearea.top:
            direction[1] = -BALL_SPEED
