import pyxel, random

# screen's size
screen_width = 300
screen_height = 300
pyxel.init(screen_width, screen_height)


# variables liées à la plateforme
platform_velocity = 10
platform_color = random.randint(0, 15)
platform_sideWidth = 40
platform_width = 50
platform_height = 16
platform_downHeight = 3
platform_altitude = 10
platform_x = (screen_width/2) - (platform_width/2)
platform_y = screen_height - platform_height - platform_altitude


# variables liées à la balle
ball_x = screen_width / 2
ball_y = screen_height / 2
ball_totalVelocity = 3
ball_velocity_x = (- ball_totalVelocity)
ball_velocity_y = (- ball_totalVelocity)
ball_radius = 5
ball_color = 5
ball_run = False


# coordonnées des murs
wall_Right = screen_width
wall_Left = 0
wall_Down = screen_height
wall_Up = 0


# vies/score
health_points = 4
score = 0


# variables liées aux briques
#variables des coordonnées en x des briques
b_x1 = 20
b_x2 = 60
b_x3 = 100
b_x4 = 140
b_x5 = 180
b_x6 = 220
b_x7 = 260
#variables des coordonnées en y des briques
b_y1 = 50
b_y2 = 75
b_y3 = 100
#listes des coordonnées en x et y des briques
bricks_x = [b_x1, b_x2, b_x3, b_x4, b_x5, b_x6, b_x7]
bricks_y = [b_y1, b_y2, b_y3]
#liste des briques
bricks_list = []
# variable qui permet la construction des briques une seule fois
brick_start = True
# variables liées à l'apparence des briques
brick_width = 20
brick_height = 10
brick_color = 8
brick_color_V = 8
brick_color_B = 8


# variables liées au jeu
menu = True
niveau_1 = False
niveau_2 = False
niveau_3 = False
game_start = False




#___________________________________________________________________________________#
# fonctions du casse-brique

# fonction qui permet le lancement du jeu
def game_start():
    if pyxel.btnr(pyxel.KEY_RIGHT):
        game_start = True


# fonction qui définit le mouvement de la plateforme
def platform_move(x, y):

    if pyxel.btn(pyxel.KEY_RIGHT):
        if ((x + platform_velocity) < (screen_width - platform_width - platform_sideWidth + 5)) :
            x = x + platform_velocity
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > platform_sideWidth) :
            x = x - platform_velocity
    
    return x, y



#fonction qui définit le mouvement de la balle
def ball_move(x, y, a, b, r, health_points, score, ball_run):
    
    if ball_run:
        x = x + a
        y = y + b
        for brick in bricks_list:
        
            if (y + r + b) >= brick[1] and (y - r + b) <= (brick[1] + brick_height) and (x + r + a) >= brick[0] and (x - r + a) <= (brick[0] + brick_width):
                if (x + r + a) > (brick[0] + r) and (x - r + a) < (brick[0] + brick_width - r):
                    b = (- b)
                else:
                    a = (- a)
                score += 1
                bricks_list.remove(brick)
                
            
        # bord droit
        if (x + r + a) >= wall_Right: 
            a = (- a)
            
        # bord gauche
        elif (x - r + a) <= wall_Left:
            a = (- a)
             
        # bord haut
        elif (y - r + b) <= wall_Up:
            b = (- b)
            
        # bord bas
        elif (y + r + b) >= wall_Down:
            ball_run = False
                
            
        # milieu platforme
        elif (y + r + b) > platform_y and (x + a - r) < (platform_x + platform_width) and (x + a + r) > platform_x :
            b = (-b)
            
        # bord droit   
        elif (y + r + b) > platform_y and (x + r + a) < (platform_x) and (x - r + a) > (platform_x - platform_sideWidth) and pyxel.pget((x + a), (y + b)) == platform_color:
            b = (- b)
        
        #bord gauche plateforme
        elif (y + r + b) > platform_y and (x + r + a) < (platform_x + platform_width + platform_sideWidth) and (x - r + a) > (platform_x + platform_width) and pyxel.pget((x + a), (y + b)) == platform_color:
            b = (- b)
    
    return x, y, a, b, r, health_points, score, ball_run



# fonction qui permet d'ajouter des briques à la liste des briques
def bricks_creation(bricks_list):
    bricks_list.append([b_x, b_y])
    
    return bricks_list 



# fonction qui gère les vies
def health_points_gestion():
    global health_points, ball_y, ball_x, ball_radius, wall_Down, ball_run
    if (ball_y + ball_radius + ball_velocity_y) >= wall_Down:
        ball_run = False
        health_points -= 1





# Update_____________________________________________________________________________________________________
def update():
    """mise à jour des variables (30 fois par seconde)"""

    # appelle les variables et les listes nécessaires
    global health_points, ball_totalVelocity, platform_x, platform_y, vies, ball_x, ball_y, ball_velocity_x, ball_velocity_y, ball_radius, b_x, b_y, bricks_list, brick_start, game_start, brick_height, brick_width, score, ball_run
    
    
    # au lancement du jeu appuyer sur espace pour commencer le déplacement de la balle
    if pyxel.btnr(pyxel.KEY_SPACE):
        ball_run = True
    
    # si la balle n'est plus en état de se déplacer (touche bord bas)
    if ball_run == False:
        ball_x = 150
        ball_y = 150
        

    # mise à jour de la position du vaisseau
    platform_x, platform_y = platform_move(platform_x, platform_y)
    
    #déplacement de la balle
    ball_x, ball_y, ball_velocity_x, ball_velocity_y, ball_radius, health_points, score, ball_run = ball_move(ball_x, ball_y, ball_velocity_x, ball_velocity_y, ball_radius, health_points, score, ball_run)
    
    #gestion des vies
    health_points_gestion()
    
    # si la construction des brique est vrai alors créer les briques 
    if brick_start :
        for i in bricks_y:
            for j in bricks_x:
                b_y = i
                b_x = j
                bricks_creation(bricks_list)
        brick_start = False


        
    

# affichage graphique___________________________________________________________________________________________________________________________
def draw():
    """création des objets (30 fois par seconde)"""
    # effacer les éléments de l'écran
    pyxel.cls(0)

    # si les vies sont supérieures à 0
    if health_points > 0:    

        # platform 
        pyxel.rect(platform_x, platform_y, platform_width, platform_height, platform_color)
        pyxel.tri(platform_x + platform_width, platform_y, platform_x + platform_width, platform_y + platform_height - 1, platform_x + platform_width + platform_sideWidth, platform_y + platform_height - 1, platform_color)
        pyxel.tri(platform_x, platform_y, platform_x, platform_y + platform_height - 1, platform_x - platform_sideWidth, platform_y + platform_height - 1, platform_color)
        pyxel.rect((platform_x - platform_sideWidth), (platform_y + platform_height), ((2 * platform_sideWidth) + platform_width), platform_downHeight, platform_color)
        # ball
        pyxel.circ(ball_x, ball_y, ball_radius, ball_color)
        
        
        for brick in bricks_list:
            pyxel.rect(brick[0], brick[1], brick_width, brick_height, brick_color)
        
        pyxel.text(10, 10,'Score: %d' % score, 7)
        
        pyxel.text(50, 10,'vies: %d' % health_points, 7)
    
    
    
    # si les vies ne sont pas supérieures à 0  
    else :

        pyxel.text(150,120, 'GAME OVER', 7)
        pyxel.text(50, 10,'vies: %d' % health_points, 7)

# lancement du jeu _____________________________________________________________________________________________________________________________
pyxel.run(update, draw)
