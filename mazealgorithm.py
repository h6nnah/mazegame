from visual import *

# BFS algorithm

# OBJECTS
ball = sphere(pos=(-4,4,0), radius=0.5, color=color.cyan)
ball.velocity=vector(0,0,0)
ball.material=materials.chrome

c1=Polygon([(-5.5,-5.5),(-5.5,5.5),(5.5,5.5),(5.5,-5.5)])
c2=Polygon([(-5.3,-5.3),(-5.3,5.3),(5.3,5.3),(5.3,-5.3)])
cage=extrusion(pos=[(0,0,.5),(0,0,-.5)],shape=c1-c2,material=materials.ice)

box1=box(pos=(-4,-1,0),length=2,height=.2,width=.01,material=materials.ice)
box2=box(pos=(-1,-3,0),length=4,height=.2,width=.01,material=materials.ice)
box3=box(pos=(-2,3,0),length=2,height=.2,width=.01,material=materials.ice)
box4=box(pos=(4,3,0),length=2,height=.2,width=.01,material=materials.ice)
box5=box(pos=(0,1,0),length=6,height=.2,width=.01,material=materials.ice)
box6=box(pos=(2,-1,0),length=2,height=.2,width=.01,material=materials.ice)

box7=box(pos=(1,3,0),length=.2,height=4,width=.01,material=materials.ice)
box8=box(pos=(-3,2,0),length=.2,height=2,width=.01,material=materials.ice)
box9=box(pos=(-1,0,0),length=.2,height=2,width=.01,material=materials.ice)
box10=box(pos=(1,-2,0),length=.2,height=2,width=.01,material=materials.ice)
box11=box(pos=(3,-4,0),length=.2,height=2,width=.01,material=materials.ice)
box12=box(pos=(3,0,0),length=.2,height=2,width=.01,material=materials.ice)

scene.range = 5.5
scene.background = color.white
scene.foreground = color.black
scene.userspin = False
scene.userzoom = False

# DEFINED VARIABLES
deltat = 0.005
t = 0
a = 0

# KEYBOARD INPUT FUNCTION
def keyInput(evt):
    s = evt.key
    if s == 'up':
        ball.color=color.blue
        ball.velocity=vector(0,1,0)
    elif s == 'down':
        ball.color=color.red
        ball.velocity=vector(0,-1,0)
    elif s == 'right':
        ball.color=color.yellow
        ball.velocity=vector(1,0,0)
    elif s == 'left':
        ball.color=color.green
        ball.velocity=vector(-1,0,0)
    elif s == 's':
        ball.color=color.black
        ball.velocity=vector(0,0,0)
scene.bind('click keydown', keyInput)

# UPDATE POSITION
while True:
    rate(800)
    if ball.pos.x < -4.5:
        ball.velocity=vector(a,0,0)
    if ball.pos.x > 4.5:
        ball.velocity=vector(-a,0,0)
    if ball.pos.y < -4.5:
        ball.velocity=vector(0,a,0)
    if ball.pos.y > 4.5:
        ball.velocity=vector(0,-a,0)
        
# LIMITS ON BALL POS (2) FOR ALL 12 WALLS
    if (box7.pos.x -.5) <= ball.pos.x <= (box7.pos.x + .5) and .5 < ball.pos.y < 5 and ball.velocity.x < 0:
        ball.velocity=-ball.velocity/1000
        
    if (box7.pos.x -.5) <= ball.pos.x <= (box7.pos.x + .5) and .5 < ball.pos.y < 5 and ball.velocity.x > 0:
        ball.velocity.x=-.001

    if (box1.pos.y -.5) <= ball.pos.y <= (box1.pos.y + .5) and -4.5 < ball.pos.x < -2.5 and ball.velocity.y < 0:
        ball.velocity=-ball.velocity/1000
        
    if (box1.pos.y -.5) <= ball.pos.y <= (box1.pos.y + .5) and -4.5 < ball.pos.x < -2.5 and ball.velocity.y > 0:
        ball.velocity.x=-.001
        
        
    #if <ball.pos.y<:

        
    ball.pos = ball.pos + ball.velocity * deltat
    t = t + deltat
    a = a + (deltat/1000)
