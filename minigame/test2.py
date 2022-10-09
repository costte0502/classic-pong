import turtle
import winsound
#window
win = turtle.Screen()
win.title("Jacky's first game")
win.bgcolor("yellow")
win.setup(width = 800,height = 600)
win.tracer(0)
#score
score_a = 0
score_b = 0
#paddleA
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("black")
paddleA.shapesize(stretch_wid = 5,stretch_len = 1)
paddleA.penup()
paddleA.goto(-350,0)
# paddleB
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("black")
paddleB.shapesize(stretch_wid = 5,stretch_len = 1)
paddleB.penup()
paddleB.goto(350,0)
#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("cyan")
ball.shapesize(1,1)
ball.penup()
ball.goto(0,0)
ball.dx = 0.05
ball.dy = 0.05
#Pen
pen  = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0 Player B:0",align = "center",font = ("Courier",24,"normal"))
#FUNC
def paddleA_up():
    y = paddleA.ycor()
    y+= 20
    paddleA.sety(y)
def paddleA_down():
    y = paddleA.ycor()
    y-= 20
    paddleA.sety(y)
def paddleB_up():
    y = paddleB.ycor()
    y+= 20
    paddleB.sety(y)
def paddleB_down():
    y = paddleB.ycor()
    y-= 20
    paddleB.sety(y)
    
#binding
win.listen()
win.onkeypress(paddleA_up,"w")
win.onkeypress(paddleA_down,"s")
win.onkeypress(paddleB_up,"Up")
win.onkeypress(paddleB_down,"Down")
#ball game loop
while True: 
    win.update()
    #ball move
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #collision
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *=-1
        winsound.PlaySound("pond.wav",winsound.SND_ASYNC)
    if ball.ycor() <-290:
        ball.sety(-270)
        ball.dy *=-1
        winsound.PlaySound("pond.wav",winsound.SND_ASYNC)
    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx *=-1
        score_a +=1
        pen.clear()
        pen.write("Player A:{} Player B: {}".format(score_b,score_a),align = "center",font = ("Courier",24,"normal"))
    
    if ball.xcor() <-390:
        ball.goto(0,0)
        ball.dx *=-1
        score_b +=1
        pen.clear()
        pen.write("Player A:{} Player B: {}".format(score_b,score_a),align = "center",font = ("Courier",24,"normal"))

    if (ball.xcor()>340 and ball.xcor()<350) and(ball.ycor() < paddleB.ycor()+50 and ball.ycor()>paddleB.ycor()-50):
        ball.setx(340)
        winsound.PlaySound("paddles.wav",winsound.SND_ASYNC)
        ball.dx*=-1
    if (ball.xcor()<-340 and ball.xcor()>-350) and(ball.ycor() < paddleA.ycor()+50 and ball.ycor()>paddleA.ycor()-50):
        ball.setx(-340)
        winsound.PlaySound("paddles.wav",winsound.SND_ASYNC)
        ball.dx*=-1
