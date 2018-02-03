from visual import *

# OBJECTS
ball = sphere(pos=(-2,2,0), radius=0.5, color=color.green)
ball.velocity=vector(0,0,0)
ball.material=materials.chrome

#c1 = Polygon([(-5.5,-5.5), (-5.5,5.5), (5.5,5.5), (5.5,-5.5)])
#c2 = Polygon([(-5.3,-5.3), (-5.3,5.3),(5.3,5.3),(5.3,-5.3)])
#cage = extrusion(pos = [(0,0,.5), (0,0,-.5)], shape = c1 - c2, material = materials.ice)

c1 = Polygon([(-n-.5,-n-.5), (-n-.5,-n-.5), (n+.5,n+.5), (n+.5,-n-.5)])
c2 = Polygon([(-n-.3,-n-.3), (-n-.3,n+.3),(n+.3,n+.3),(n+.3,-n-.3)])
cage = extrusion(pos = [(0,0,.5), (0,0,-.5)], shape = c1 - c2, material = materials.ice)


box1 = box(pos = (-4,-1,0), length = 2, height = .2, width=.01, material = materials.ice)
box2 = box(pos = (-1,-3,0), length = 4, height = .2, width=.01, material = materials.ice)
box3 = box(pos = (-2,3,0), length = 2, height = .2, width=.01, material = materials.ice)
box4 = box(pos = (4,3,0), length = 2, height = .2, width=.01, material = materials.ice)
box5 = box(pos = (0,1,0), length = 6, height = .2, width=.01, material = materials.ice)
box6 = box(pos = (2,-1,0), length = 2, height = .2, width=.01, material = materials.ice)

box7 = box(pos = (1,3,0), length = .2, height = 4, width = .01, material = materials.ice)
box8 = box(pos = (-3,2,0), length = .2, height = 2, width = .01, material = materials.ice)
box9 = box(pos = (-1,0,0), length = .2, height = 2, width = .01, material = materials.ice)
box10 = box(pos = (1,-2,0), length = .2, height = 2, width = .01, material = materials.ice)
box11 = box(pos = (3,-4,0), length = .2, height = 2, width = .01, material = materials.ice)
box12 = box(pos = (3,0,0), length = .2, height = 2, width = .01, material = materials.ice)

start = box(pos = (-2,2,0), length = 1.8, height = 1.8, width = .01, material = materials.unshaded, color = color.green, opacity = 0.2)
stop = box(pos = (4.1,4.1,0), length = 2, height = 2, width = .01, material = materials.unshaded, color = color.red, opacity = 0.2)
startl = text(text = 'START', align = 'center', depth = -0.01, color = color.green, pos = (-2,2,.5), height = .3, width = .8)
stopl = text(text = 'FINISH', align = 'center', depth = -0.01, color = color.red, pos = (4,4,.5), height = .3, width = .8)

scene.visible = False
scene.title = 'MAZE'
scene.range = 5.5
scene.background = color.white
scene.foreground = color.black
#scene.userspin = False
#scene.userzoom = False
scene.fullscreen = 1


# DEFINED VARIABLES
deltat = 0.005
t = 0
a = 0


# KEYBOARD INPUT FUNCTION
def keyInput(evt):
    s = evt.key
    if s == 'up':
        ball.color = color.blue
        ball.velocity = vector(0,1,0)
    elif s == 'down':
        ball.color = color.red
        ball.velocity = vector(0,-1,0)
    elif s == 'right':
        ball.color = color.yellow
        ball.velocity = vector(1,0,0)
    elif s == 'left':
        ball.color = color.green
        ball.velocity = vector(-1,0,0)
    elif s == 's':
        ball.color = color.black
        ball.velocity = vector(0,0,0)
    elif s == 'd':
        ball.color = color.white
        ball.materials = materials.rough

scene.bind('click keydown', keyInput)


# UPDATE POSITION
while True:
    rate(800)
    if ball.pos.x < -4.5:
        ball.velocity = vector(a,0,0)
    if ball.pos.x > 4.5:
        ball.velocity = vector(-a,0,0)
    if ball.pos.y < -4.5:
        ball.velocity = vector(0,a,0)
    if ball.pos.y > 4.5:
        ball.velocity = vector(0,-a,0)
#    if ball.pos.y < -3.5:
#        ball.color = color.white

# victory
#    if 3 < ball.pos.x < 4:
#        scene.background = color.blue
#    if 2 < ball.pos.x < 3:
#        scene.background = color.red
#    if -4 < ball.pos.x < -2:
#        scene.background = color.yellow
#    if -2 < ball.pos.x < 2:
#        scene.background = color.green
    if 4 < ball.pos.x and 4 < ball.pos.y:
        victory = text(text='YOU WON!', align='center', depth=-0.05, color=color.black, pos = (0,0,1), height = 1, width = .5)

# LIMITS ON BALL POS (2) FOR ALL 12 WALLS

# horizontal walls
#1 #########################
    if (box1.pos.y -.3) <= ball.pos.y <= (box1.pos.y + .5) and -4.5 < ball.pos.x < -2.5 and ball.velocity.y < 0:
        ball.velocity.y = a
    if (box1.pos.y -.5) <= ball.pos.y <= (box1.pos.y + .3) and -4.5 < ball.pos.x < -2.5 and ball.velocity.y > 0:
        ball.velocity.y = -a
#2 #########################
    if (box2.pos.y -.3) <= ball.pos.y <= (box2.pos.y + .5) and -3.5 < ball.pos.x < 1.5 and ball.velocity.y < 0:
        ball.velocity.y = a
    if (box2.pos.y -.5) <= ball.pos.y <= (box2.pos.y + .3) and -3.5 < ball.pos.x < 1.5 and ball.velocity.y > 0:
        ball.velocity.y = -a
#3 ############################
    if (box3.pos.y -.3) <= ball.pos.y <= (box3.pos.y + .5) and -3.5 < ball.pos.x < -.5 and ball.velocity.y < 0:
        ball.velocity.y = a
    if (box3.pos.y -.5) <= ball.pos.y <= (box3.pos.y + .3) and -3.5 < ball.pos.x < -.5 and ball.velocity.y > 0:
        ball.velocity.y = -a
#4 ##########################
    if (box4.pos.y -.3) <= ball.pos.y <= (box4.pos.y + .5) and 2.5 < ball.pos.x < 4.5 and ball.velocity.y < 0:
        ball.velocity.y = a
    if (box4.pos.y -.5) <= ball.pos.y <= (box4.pos.y + .3) and 2.5 < ball.pos.x < 4.5 and ball.velocity.y > 0:
        ball.velocity.y = -a
#5
    if (box5.pos.y -.3) <= ball.pos.y <= (box5.pos.y + .5) and -3.5 < ball.pos.x < 3.5 and ball.velocity.y < 0:
        ball.velocity.y = a
    if (box5.pos.y -.5) <= ball.pos.y <= (box5.pos.y + .3) and -3.5 < ball.pos.x < 3.5 and ball.velocity.y > 0:
        ball.velocity.y = -a
#6
    if (box6.pos.y -.3) <= ball.pos.y <= (box6.pos.y + .5) and .5 < ball.pos.x < 3.5 and ball.velocity.y < 0:
        ball.velocity.y = a
    if (box6.pos.y -.5) <= ball.pos.y <= (box6.pos.y + .3) and .5 < ball.pos.x < 3.5 and ball.velocity.y > 0:
        ball.velocity.y = -a

# vertical walls
#7
    if (box7.pos.x -.3) <= ball.pos.x <= (box7.pos.x + .5) and .5 < ball.pos.y < 5 and ball.velocity.x < 0:
        ball.velocity.x = a
    if (box7.pos.x -.5) <= ball.pos.x <= (box7.pos.x + .3) and .5 < ball.pos.y < 5 and ball.velocity.x > 0:
        ball.velocity.x = -a
#8
    if (box8.pos.x -.3) <= ball.pos.x <= (box8.pos.x + .5) and .5 < ball.pos.y < 3.5 and ball.velocity.x < 0:
        ball.velocity.x = a
    if (box8.pos.x -.5) <= ball.pos.x <= (box8.pos.x + .3) and .5 < ball.pos.y < 3.5 and ball.velocity.x > 0:
        ball.velocity.x = -a
#9 ########################
    if (box9.pos.x -.3) <= ball.pos.x <= (box9.pos.x + .5) and -1.5 < ball.pos.y < 1.5 and ball.velocity.x < 0:
        ball.velocity.x = a
    if (box9.pos.x -.5) <= ball.pos.x <= (box9.pos.x + .3) and -1.5 < ball.pos.y < 1.5 and ball.velocity.x > 0:
        ball.velocity.x = -a
#10
    if (box10.pos.x -.3) <= ball.pos.x <= (box10.pos.x + .5) and -3.5 < ball.pos.y < -.5 and ball.velocity.x < 0:
        ball.velocity.x = a
    if (box10.pos.x -.5) <= ball.pos.x <= (box10.pos.x + .3) and -3.5 < ball.pos.y < -.5 and ball.velocity.x > 0:
        ball.velocity.x = -a       
#11 #######################
    if (box11.pos.x -.3) <= ball.pos.x <= (box11.pos.x + .5) and -4.5 < ball.pos.y < -2.5 and ball.velocity.x < 0:
        ball.velocity.x = a
    if (box11.pos.x -.5) <= ball.pos.x <= (box11.pos.x + .3) and -4.5 < ball.pos.y < -2.5 and ball.velocity.x > 0:
        ball.velocity.x = -a
#12
    if (box12.pos.x -.3) <= ball.pos.x <= (box12.pos.x + .5) and -1.5 < ball.pos.y < 1.5 and ball.velocity.x < 0:
        ball.velocity.x = a
    if (box12.pos.x -.5) <= ball.pos.x <= (box12.pos.x + .3) and -1.5 < ball.pos.y < 1.5 and ball.velocity.x > 0:
        ball.velocity.x = -a
        
        
    #if <ball.pos.y<:
        
    ball.pos = ball.pos + ball.velocity * deltat
    t = t + deltat
    a = a + (deltat/100)



# Depth First Search
#Nodes-specific points/locations
    #edges/transitions-connections between the nodes
    #forward edges vs. tree edges vs. directed edges
#matrices
