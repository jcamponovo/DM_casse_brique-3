import pyxel, random


# screen's size
screen_width = 300
screen_height = 300
pyxel.init(screen_width, screen_height)

# variables linked to the platform
platform_x = 180
platform_y = 260
platform_velocity = 10
platform_color = 5
platform_sideWidth = 20
platform_width = 60
platform_height = 20

# variables linked to the ball 
ball_x = 150
ball_y = 150
ball_totalVelocity = -8
ball_velocity_x = ball_totalVelocity
ball_velocity_y = ball_totalVelocity
ball_radius = 7

# definition of the walls for ball's rebound
wall_Right = screen_width
wall_Left = 0
wall_Down = screen_height
wall_Up = 0


# nombres de vies
health_points = 1

bricks_x = [20, 50, 80, 110, 140]
bricks_y = [50, 100]
bricks_list = []




# fonction which defines de movement of the platform : key right/left
def platform_move(x, y):

    if pyxel.btn(pyxel.KEY_RIGHT):
        if ((x + platform_velocity) < (screen_width - platform_width - platform_sideWidth + 5)) :
            x = x + platform_velocity
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > platform_sideWidth) :
            x = x - platform_velocity
    
    return x, y


def ball_move(x, y, a, b, r):
    
    x = x + a
    y = y + b
    if (x + r + a) > wall_Right or (x - r + a) < wall_Left:
        a = (- a)
        
    elif (y - r + b) < wall_Up or (y + r + b) > wall_Down:
        b = (- b)
    
    elif (y + r + b) > platform_y and (x + r + a) < (platform_x + platform_width) and (x - r + a) > platform_x:
        b = (- b)
    
    elif (y - r + b) > platform_y and (x - r + a) < (platform_x + platform_width) and (x + r + a) > platform_x:
        b = (- b)
    
    elif (y + r + b) > platform_y and (x + r + a) < (platform_x) and (x - r + a) > (platform_x - platform_sideWidth):
        a = (- a)
        b = (- b)
    
    elif (y + r + b) > platform_y and (x + r + a) < (platform_x + platform_width + platform_sideWidth) and (x - r + a) > (platform_x + platform_width):
        a = (- a)
        b = (- b)
    
    return x, y, a, b, r





def update():
    """mise à jour des variables (30 fois par seconde)"""

    global platform_x, platform_y, vies, ball_x, ball_y, ball_velocity_x, ball_velocity_y, ball_radius

    # mise à jour de la position du vaisseau
    platform_x, platform_y = platform_move(platform_x, platform_y)
    
    #déplacement de la balle
    ball_x, ball_y, ball_velocity_x, ball_velocity_y, ball_radius = ball_move(ball_x, ball_y, ball_velocity_x, ball_velocity_y, ball_radius)


def draw():
    """création des objets (30 fois par seconde)"""
    
    # erase the screen
    pyxel.cls(0)

    # if the player still have health points
    if health_points > 0:    

        # platform 
        pyxel.rect(platform_x, platform_y, platform_width, platform_height, platform_color)
        pyxel.tri(platform_x + platform_width, platform_y, platform_x + platform_width, platform_y + platform_height - 1, platform_x + platform_width + platform_sideWidth, platform_y + platform_height - 1, platform_color)
        pyxel.tri(platform_x, platform_y, platform_x, platform_y + platform_height - 1, platform_x - platform_sideWidth, platform_y + platform_height - 1, platform_color)

        # ball
        pyxel.circ(ball_x, ball_y, ball_radius, 5)
        
        for i in bricks_y:
            for j in bricks_x:
                pyxel.rect(j, i, 8, 8, 8)
        
    
       
    # else: GAME OVER
    else:

        pyxel.text(50,64, 'GAME OVER', 7)

pyxel.run(update, draw)
