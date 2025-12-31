
import turtle
import random
# Set up the screen
screen = turtle.Screen()
screen.title("🍪 Catch the Cookie Game!")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

# Create the basket
basket = turtle.Turtle()
basket.shape("square")
basket.color("brown")
basket.shapesize(stretch_wid=1, stretch_len=5)
basket.penup()
basket.goto(0, -250)

# Create the cookie
cookie = turtle.Turtle()
cookie.shape("circle")
cookie.color("chocolate")
cookie.penup()
cookie.goto(random.randint(-280, 280), 250)
cookie.speed(0)

# Score
score = 0
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center", font=("Arial", 18, "bold"))

# Move basket
def go_left():
    x = basket.xcor()
    x -= 40
    if x < -280:
        x = -280
    basket.setx(x)

def go_right():
    x = basket.xcor()
    x += 40
    if x > 280:
        x = 280
    basket.setx(x)

screen.listen()
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# Game loop
def drop_cookie():
    global score
    y = cookie.ycor()
    y -= 20
    cookie.sety(y)

    # Check if caught
    if cookie.ycor() < -240 and abs(cookie.xcor() - basket.xcor()) < 50:
        score += 1
        cookie.goto(random.randint(-280, 280), 250)
        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Arial", 18, "bold"))

    # Missed
    elif cookie.ycor() < -280:
        cookie.goto(random.randint(-280, 280), 250)

    screen.ontimer(drop_cookie, 200)

drop_cookie()
screen.mainloop()
