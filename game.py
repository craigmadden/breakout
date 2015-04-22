from graphics import *
import time
from classes import GameArea, Paddle, Ball, Brick


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

        # Create bricks
        bricks = []
        for i in range(60,460,45):
            x = i
            y1 = 400
            y2 = 385
            y3 = 370
            bricks.append(Brick(x,y1,"#99FF99"))
            bricks.append(Brick(x,y2,"#FF6600"))
            bricks.append(Brick(x,y3, "#6699FF"))
        for brick in bricks:
            brick.rect.draw(win)

        # Create paddle
        # Paddle size is 40 wide by 10 high
        paddle = Paddle()
        paddle.rect.draw(win)
        # Use a similar process for creating bricks

        # Create circle (ball x, y and radius)
        ball = Ball(x,y,8)
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
            if ball.y <= 30:
                pass
            elif gamearea.collision_detection(ball_pt,direction):
                    direction = gamearea.direction

            if ball.collision_dect(paddle, direction):
                print "Hit paddle"
            for item,brick in enumerate(bricks):
                if ball.collision_dect(brick, direction):
                    bricks.pop(item)
                    brick.rect.undraw()
                    if not bricks:
                        print "ALL BRICKS ARE GONE"

            # if paddle.collision_detect(ball_pt,paddle_pt,direction):
            #     print "Hit paddle!!"
            #     direction = paddle.direction

            x = direction[0]
            y = direction[1]

            ball.circle.move(x, y)

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
            elif user_event == "Right":
                paddle.rect.move(10,0)
                paddle.x += 10
            # Get the bottom left point of rectangle (P1)
            paddle_pt = paddle.rect.getP1()
            # Print the x of the bottom left corner
        win.close()

g = GameApp()
g.main()