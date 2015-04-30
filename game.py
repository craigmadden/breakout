from graphics import *
import time
from classes import GameArea, Paddle, Ball, Brick, BALL_SPEED


class GameApp(object):
    def __init__(self):
        # Create game area
        self.win = GraphWin("Game Area", 500, 500)
        self.win.setCoords(0, 0, 500, 500)
        # Create circle (ball x, y and radius)
        self.x = 50
        self.y = 350

        # Initialize game area
        self.gamearea = GameArea()
        self.gamearea.rect.draw(self.win)


        self.ball = Ball(self.x, self.y, 8)
        self.ball.circle.draw(self.win)
        # Starting point of ball

    def reset(self):
        self.ball.circle.undraw()
         # Create circle (ball x, y and radius)
        self.ball = Ball(self.x, self.y, 8)
        self.ball.circle.draw(self.win)
        # Starting point of ball
        self.x = 50
        self.y = 350

    def main(self):
        # Create bricks
        bricks = []
        for i in range(60, 460, 45):
            x1 = i
            y1 = 400
            y2 = 385
            y3 = 370
            bricks.append(Brick(x1, y1, "#99FF99"))
            bricks.append(Brick(x1, y2, "#FF6600"))
            bricks.append(Brick(x1, y3, "#6699FF"))
        for brick in bricks:
            brick.rect.draw(self.win)

        # Create paddle
        # Paddle size is 40 wide by 10 high
        paddle = Paddle()

        paddle.rect.draw(self.win)
        # Use a similar process for creating bricks

        # Create circle (ball x, y and radius)
        self.ball = Ball(self.x, self.y, 8)
        self.ball.circle.draw(self.win)

        left = 30
        right = 470
        top = 470
        bottom = 30
        # The direction values determine amount of movement of ball
        direction = [BALL_SPEED, BALL_SPEED]
        while True:
            ball_pt = self.ball.circle.getCenter()
            paddle_pt = paddle.rect.getCenter()
            if self.ball.is_below_paddle(paddle):
                self.reset()
            self.ball.hits_wall(self.gamearea, direction)

            self.ball.hits_paddle(paddle, direction)

            # if self.ball.collision_dect(paddle, direction):
            #     print "Hit paddle"
            for item,brick in enumerate(bricks):
                if self.ball.collision_dect(brick, direction):
                    bricks.pop(item)
                    brick.rect.undraw()
                    if not bricks:
                        print "ALL BRICKS ARE GONE"

            x = direction[0]
            y = direction[1]

            # Move ball to new location
            self.ball.move(x, y)

            # Check for mouse click on play area
            if self.win.checkMouse(): # pause for click in window
                break
            user_event = self.win.checkKey()
            if user_event == "Left":
                paddle.move(-10)
            elif user_event == "Right":
                paddle.move(10)
            # # Get the bottom left point of rectangle (P1)
            # paddle_pt = paddle.rect.getP1()
            # Wait for next loop
            time.sleep(.005)

        win.close()

g = GameApp()
g.main()
