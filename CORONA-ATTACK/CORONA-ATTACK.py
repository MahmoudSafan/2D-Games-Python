import turtle
import time
import random

score = 0
lifes = 3
level = 0
levelUpgrade = 10
difficult = 3
picEnimes = ["first.gif","second.gif","third.gif","fourth.gif","shoot.gif"]

#SCREEN

wn = turtle.Screen()
wn.setup(width = 700, height = 700)
wn.title("CORONA ATTACK -- MS")
wn.bgpic("Webp.net-resizeimage (7).gif")
wn.tracer(0)
wn.register_shape("dettol3.gif")
wn.register_shape(picEnimes[0])
wn.register_shape(picEnimes[1])
wn.register_shape(picEnimes[2])
wn.register_shape(picEnimes[3])
wn.register_shape(picEnimes[4])



# plane 

plane = turtle.Turtle()
plane.shape("dettol3.gif")
plane.color("white")
plane.penup()
plane.goto(0,-320)
plane.speed(0)
plane.direction = "stop"

# Enemy

enemies = []
selectEnemies = 0
def createEnemies():
	global selectEnemies
	enemy = turtle.Turtle()
	enemy.shape(picEnimes[selectEnemies])
	enemy.color("red")
	enemy.penup()
	enemy.goto(random.randint(-320,320),random.randint(150,320))
	enemy.speed(0)
	enemies.append(enemy)
	selectEnemies += 1
	if(selectEnemies >=4 ):
		selectEnemies = 0

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 320)

# movement functions

planeSpeed = 30
enemySpeed = 5
bulletSpeed = 20

def up():
	if(plane.ycor() < 320):
		plane.sety(plane.ycor()+planeSpeed)

def down():
	if(plane.ycor() > -320):
		plane.sety(plane.ycor()-planeSpeed)

def right():
	if(plane.xcor() < 320):
		plane.setx(plane.xcor()+planeSpeed)

def left():
	if(plane.xcor() > -320):
		plane.setx(plane.xcor()-planeSpeed)

bullets = []

def fire():
	bullet = turtle.Turtle()
	bullet.shape(picEnimes[4])
	bullet.color("yellow")
	bullet.penup()
	bullet.shapesize(.5,.5)
	bullet.goto(plane.xcor() , plane.ycor()+bulletSpeed)
	bullets.append(bullet)


# move bullet to kill the target

def moveBullets():
	global bulletSpeed , level , levelUpgrade
	for bu in range(len(bullets)):
		bullets[bu].sety(bullets[bu].ycor()+bulletSpeed)
		for em in range(len(enemies)):
			if(bullets[bu].distance(enemies[em]) < 30):
				global score
				score += 1
				enemies[em].goto(3000,3000)
				bullets[bu].goto(2000,2000)
				if(score % levelUpgrade == 0):
					level += 1
					levelUpgrade += 10
				

# move enemies 

def moveEnemies():
	global enemySpeed
	for i in range(len(enemies)):
		enemies[i].sety(enemies[i].ycor() - enemySpeed)

# check

def check():
	global lifes , score , level , difficult , enemySpeed
	for i in range(len(enemies)):
		if(plane.distance(enemies[i]) < 50 ):
			enemies[i].goto(1000,1000)
			lifes -= 1

	if(lifes == 0):
		# Pen
		pen = turtle.Turtle()
		pen.speed(0)
		pen.shape("square")
		pen.color("#05254C")
		pen.penup()
		pen.hideturtle()
		pen.goto(0, 0)
		pen.write("STAY HOME WITH ME ", align="center", font=("Courier", 24, "normal"))
		
		for i in range(len(enemies)):
			enemies[i].goto(2000,2000)

		for i in range(len(bullets)):
			bullets[i].goto(2000,2000)


		enemies.clear()
		bullets.clear()
		time.sleep(3)
		pen.clear()
		lifes = 3
		score = 0
		level = 0
		difficult = 3
		enemySpeed = 5
		createEnemies()
		createEnemies()


wn.listen()
wn.onkey(up,'w')
wn.onkey(down,'s')
wn.onkey(right,'d')
wn.onkey(left,'a')
wn.onkey(fire,'space')

createEnemies()
createEnemies()
mytime = 0
clearList = 0

while True:
	wn.update()
	moveBullets()
	moveEnemies()
	check()
	mytime += 1
	clearList += 1
	pen.clear()
	pen.write("score: {}      level: {}       lifes: {} ".format(score,level,lifes), align="center", font=("Helvetica", 16, "bold"))
			
	if(mytime > 100/difficult):
		for i in range(difficult):
			createEnemies()

		mytime = 0
	enemySpeed +=.03

	if(clearList > 200):
		clearList = 0

		for i in range(len(enemies)):
			enemies[i].goto(4000,4000)

		for i in range(len(bullets)):
			bullets[i].goto(2000,2000)

		enemies.clear()
		bullets.clear()
		difficult += 1		
		for i in range(difficult):
			createEnemies()

	time.sleep(.1)

turtle.done()