from graphics import *
import time
from classes import GameArea, Paddle, Ball


class GameApp(object):
    def main(self):
        # Create game area
        win = GraphWin("Game Area", 500, 500)
        win.setCoords(0,0,500,500)

        # Initialize game area
        gamearea = GameArea()
        gamearea.rect.draw(win)

        # Starting point of ball
        x = 100
        y = 50

        # Create paddle
        # Paddle size is 40 wide by 10 high
        paddle = Paddle()
        paddle.rect.draw(win)
        # Use a similar process for creating bricks

        # Create circle (ball x, y and radius)
        ball = Ball(x,y,5)
        ball.circle.draw(win)

        left = 30
        right = 470
        top = 470
        bottom = 30
        # The direction values determine amount of movement of ball
        direction = [5,5]
        while True:
            ball_pt = ball.circle.getCenter()
            paddle_pt = paddle.rect.getCenter()
            #print paddle.x, paddle.x -10, paddle.x +10

            if gamearea.collision_detection(ball_pt,direction):
                print "Hit wall"
                direction = gamearea.direction
            if ball.collision_dect(paddle,direction):
                print "Hit paddle"
            # if paddle.collision_detect(ball_pt,paddle_pt,direction):
            #     print "Hit paddle!!"
            #     direction = paddle.direction

            x = direction[0]
            y = direction[1]

            ball.circle.move(x,y)

            ball.x += x
            ball.y += y

            time.sleep(.02)
            # Check for mouse click on play area
            if win.checkMouse(): # pause for click in window
                break
            user_event = win.checkKey()
            if user_event == "Left":
                paddle.rect.move(-10,0)
                paddle.x += -10
                print paddle.x
            elif user_event == "Right":
                paddle.rect.move(10,0)
                paddle.x += 10
                print paddle.x
            # Get the bottom left point of rectangle (P1)
            paddle_pt = paddle.rect.getP1()
            # Print the x of the bottom left corner
        win.close()

g = GameApp()
g.main()