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
platform_sideWidth = 30
platform_width = 50
platform_height = 15

# variables linked to the ball 
ball_x = screen_width / 2
ball_y = screen_height / 2
ball_totalVelocity = 5
ball_velocity_x = (- ball_totalVelocity)
ball_velocity_y = (- ball_totalVelocity)
ball_radius = 4
ball_color = 5
ball_run = False

# definition of the walls for ball's rebound
wall_Right = screen_width
wall_Left = 0
wall_Down = screen_height
wall_Up = 0


# nombres de vies
health_points = 1
score = 0

b_x1 = 20
b_x2 = 60
b_x3 = 100
b_x4 = 140
b_x5 = 180
b_x6 = 220
b_x7 = 260

b_y1 = 50
b_y2 = 75
b_y3 = 100

bricks_x = [b_x1, b_x2, b_x3, b_x4, b_x5, b_x6, b_x7]
bricks_y = [b_y1, b_y2, b_y3]
bricks_list = []

brick_start = True

brick_width = 20
brick_height = 3
brick_color = 8
brick_color_V = 8
brick_color_B = 8


menu = True
niveau_1 = False
niveau_2 = False
niveau_3 = False
game_start = False

def game_start():
    if pyxel.btnr(pyxel.KEY_RIGHT):
        game_start = True


# fonction which defines de movement of the platform : key right/left
def platform_move(x, y):

    if pyxel.btn(pyxel.KEY_RIGHT):
        if ((x + platform_velocity) < (screen_width - platform_width - platform_sideWidth + 5)) :
            x = x + platform_velocity
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > platform_sideWidth) :
            x = x - platform_velocity
    
    return x, y


def ball_move(x, y, a, b, r, health_points, score, ball_run):
    
    
    
    x = x + a
    y = y + b
    for brick in bricks_list:
        
        #if (x + r + a) >= brick[0] and (y - r + b) <= (brick[1] + brick_height) and (y + r + b) >= brick[1]:
            #a = (- a)
            #bricks_list.remove(brick)
        
        #if (x - r + a) <= (brick[0] + brick_width) and (y - r + b) <= (brick[1] + brick_height) and (y + r + b) >= brick[1]:
            #a = (- a)
            #bricks_list.remove(brick)
            
        if (y - r + b) <= (brick[1] + brick_height) and (x + r + a) >= brick[0] and (x - r + a) <= (brick[0] + brick_width):
            b = (- b)
            score += 1
            bricks_list.remove(brick)
        
        #elif (y + r + b) >= brick[1] and (x + r + a) >= brick[0] and (x - r + a) <= (brick[0] + brick_width):
            #b = (- b)
            #bricks_list.remove(brick)
            
        
        # bord droit
        elif (x + r + a) >= wall_Right: 
            a = (- a)
        
        # bord gauche
        elif (x - r + a) <= wall_Left:
            a = (- a)
         
        # bord haut
        elif (y - r + b) <= wall_Up:
            b = (- b)
        
        # bord bas
        elif (y + r + b) >= wall_Down:
            health_points -= 1
            ball_run = False
        
        # milieu platforme
        elif (y + r + b) >= platform_y and (x + a) <= (platform_x + platform_width + r/2) and (x + a) >= (platform_x - r/2) :
            b = (-b)
        
        # bord droit plateforme
        elif (y + r + b) >= platform_y and (x + r + a) <= (platform_x) and (x - r + a) >= (platform_x - platform_sideWidth) and pyxel.pget((x + a), (y + b)) == platform_color:
            a = (- a)
            b = (- b)
        
        #bord gauche plateforme
        elif (y + r + b) >= platform_y and (x + r + a) <= (platform_x + platform_width + platform_sideWidth) and (x - r + a) >= (platform_x + platform_width) and pyxel.pget((x + a), (y + b)) == platform_color:
            a = (- a)
            b = (- b)
            
    
    return x, y, a, b, r, health_points, score, ball_run


def bricks_creation(bricks_list):
    bricks_list.append([b_x, b_y])
    
    return bricks_list 



def update():
    """mise à jour des variables (30 fois par seconde)"""

    global health_points, ball_totalVelocity, platform_x, platform_y, vies, ball_x, ball_y, ball_velocity_x, ball_velocity_y, ball_radius, b_x, b_y, bricks_list, brick_start, game_start, brick_height, brick_width, score, ball_run
    

    if pyxel.btnr(pyxel.KEY_SPACE) :
        ball_run is True
        
    while ball_run == True :
        ball_x, ball_y, ball_velocity_x, ball_velocity_y, ball_radius, health_points, score, ball_run = ball_move(ball_x, ball_y, ball_velocity_x, ball_velocity_y, ball_radius, health_points, score, ball_run)
    
    if ball_run is False :
        ball_x = screen_width / 2
        ball_y = screen_height / 2
    
    # mise à jour de la position du vaisseau
    platform_x, platform_y = platform_move(platform_x, platform_y)
    
    #déplacement de la balle
    
    
    if brick_start :
        for i in bricks_y:
            for j in bricks_x:
                b_y = i
                b_x = j
                bricks_creation(bricks_list)
        brick_start = False
    
        
        
    


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
        pyxel.circ(ball_x, ball_y, ball_radius, ball_color)
        
        
        for brick in bricks_list:
            pyxel.rect(brick[0], brick[1], brick_width, brick_height, brick_color)
        
        pyxel.text(10, 10,'Score: %d' % score, 7)
    
       
    else:

        pyxel.text(150,120, 'GAME OVER', 7)

pyxel.run(update, draw)
