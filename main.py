# ------------------- Import Modules ------------------- #
from turtle import Screen
import time
from snake import Snake
from food import Food

# ------------------- Screen Setup ------------------- #
screen = Screen()
screen.setup(width=600, height=600)           # Set screen dimensions
screen.bgcolor("black")                        # Set background color
screen.title("My Snake Game")                  # Set window title
screen.tracer(0)                               # Turn off auto screen updates

# ------------------- Create Game Objects ------------------- #
snake = Snake()                                # Initialize Snake
food = Food()                                  # Initialize Food

# ------------------- Keyboard Controls ------------------- #
screen.listen()                                # Start listening for keystrokes
screen.onkey(snake.up, "Up")                   # Bind Up arrow key
screen.onkey(snake.down, "Down")               # Bind Down arrow key
screen.onkey(snake.left, "Left")               # Bind Left arrow key
screen.onkey(snake.right, "Right")             # Bind Right arrow key

# ------------------- Main Game Loop ------------------- #
game_is_on = True

while game_is_on:
    screen.update()                            # Refresh screen
    time.sleep(0.1)                            # Control snake speed
    snake.move()                               # Move the snake forward

    # ----------- Detect Collision with Food ----------- #
    if snake.head.distance(food) < 15:         # If snake touches food
        food.refresh()                         # Generate new food

# ------------------- Exit on Click ------------------- #
screen.exitonclick()
