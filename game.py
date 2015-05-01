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
        self.y = 300

        # Initialize game area
        self.gamearea = GameArea()
        self.gamearea.rect.draw(self.win)

    def reset(self):
        self.ball.circle.undraw()
         # Create circle (ball x, y and radius)
        self.ball = Ball(self.x, self.y, 8)
        self.ball.circle.draw(self.win)
        # Starting point of ball
        self.x = 50
        self.y = 300

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

        # Create circle (ball x, y and radius)
        self.ball = Ball(self.x, self.y, 8)
        self.ball.circle.draw(self.win)

        # The direction values determine amount of movement of ball
        direction = [BALL_SPEED, BALL_SPEED]
        while True:
            if self.ball.is_below_paddle(paddle):
                self.reset()
            self.ball.hits_wall(self.gamearea, direction)

            self.ball.hits_paddle(paddle, direction)

            for item, brick in enumerate(bricks):
                self.ball.hits_brick(brick, direction, bricks, item)

            # Move ball to new location
            self.ball.move(direction[0], direction[1])

            # Check for mouse click on play area
            if self.win.checkMouse(): # pause for click in window
                break
            user_event = self.win.checkKey()
            if user_event == "Left":
                paddle.move(-10)
            elif user_event == "Right":
                paddle.move(10)

            # Wait for next loop
            time.sleep(.003)

        win.close()

g = GameApp()
g.main()
