import turtle
import time
import random
import os

#setup the screen 

wn = turtle.Screen()
wn.title("Snake Game -- MS")
wn.bgpic("Webp.net-resizeimage (11).gif")
wn.setup(width = 700 , height = 757)
wn.bgcolor("black")
wn.tracer(0) 
wn.register_shape("apple.gif")
wn.register_shape("Webp.net-resizeimage (10).gif")
wn.register_shape("right.gif")
wn.register_shape("left.gif")

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-180,-295 )

#setup head 

head = turtle.Turtle()
head.color("#002b7d")
head.shape("Webp.net-resizeimage (10).gif")
head.speed(0)
head.shapesize(1.5,1.5)
head.penup()
head.goto(0,0)
head.direction = "stop"

#setup food

food = turtle.Turtle()
food.color("#792034")
food.shape("apple.gif")	#sizq apple = 40px
food.penup()
food.goto(100,0)


#setup Movement Functions

def goUp():
	if(head.direction != "down"):
		head.direction = "up"
		head.shape("Webp.net-resizeimage (10).gif")

def goDown():
	if(head.direction != "up"):
		head.direction ="down"
		head.shape("Webp.net-resizeimage (10).gif")


def goRigth():
	if(head.direction != "left"):
		head.direction = "right"

def goLeft():
	if(head.direction != "right"):
		head.direction = "left"


def moveSnake():
	if(head.direction == "up"):
		y = head.ycor()					# set Y coordinate of head
		head.sety(y + 20)

	if(head.direction == "down"):
		head.sety(head.ycor() - 20)

	if(head.direction == "right"):		# set x coordinate of head
		head.setx(head.xcor() + 20)
		head.shape("right.gif")

	if(head.direction == "left"):
		head.setx(head.xcor() - 20)
		head.shape("left.gif")


# Add Body to the head of Snake

body = []

def addBody():
	newSegmant = turtle.Turtle()
	newSegmant.color("#86231E")
	newSegmant.shape("circle")
	newSegmant.shapesize(1.5,1.5)
	newSegmant.speed(0)
	newSegmant.penup()

	body.append(newSegmant)

# Make this fuckin body move with the head

def move_body_with_head():
	for i in range( len(body)-1 , 0 , -1) :
		x = body[i-1].xcor()
		y = body[i-1].ycor()
		body[i].goto(x,y)

	if(len(body)>0):
		body[0].goto(head.xcor(),head.ycor())


# Move Food to Random position

def moveFood():
	if(head.distance(food) < 40):	# 20 cause 1 pixel = 10 , and default size for turtle = 1 Pixel height and 1 pixel width
		xFood = random.randint(-340,340)	# cause screen = 600 == (300x + 300x under 0 , 300y + 300 y in minuse position)
		yFood = random.randint(-340,340)
		food.goto(xFood,yFood)	
		addBody()

# my game and my FUCKIN RULES

def reset():
	time.sleep(1)
	for i in range(len(body)):
		body[i].goto(1000,1000)

	body.clear()
	head.goto(0,0)
	head.direction = "stop"

def check():
	x = head.xcor()
	y = head.ycor()

	if(x > 340 or x < -340 or y > 340 or y < -340):
		reset()

	for segment in body :
		if(segment.distance(head) < 20):
			reset()

#link screen with keyboard

wn.listen()
wn.onkey(goUp,"w")
wn.onkey(goDown,"s")
wn.onkey(goRigth,"d")
wn.onkey(goLeft,"a")

#main game loop

while True :
	wn.update()		#make screen updae rapied and continously
	moveFood()
	move_body_with_head()
	moveSnake()
	check()

	#pen.clear()
    #pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


	time.sleep(.1)


turtle.done()