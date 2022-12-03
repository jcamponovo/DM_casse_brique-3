import pyxel, random


# vies/score
health_points = 3
score = 0

# screen's size
screen_width = 400
screen_height = 300
pyxel.init(screen_width, screen_height)


# variables liées à la plateforme
platform_velocity = 12
platform_color = 5
platform_sideWidth = 30
platform_width = 40
platform_height = 10
platform_downHeight = 2
platform_altitude = 10
platform_x = (screen_width/2) - (platform_width/2)
platform_y = screen_height - platform_height - platform_altitude


# variables liées à la balle
ball_x = screen_width / 2
ball_y = screen_height / 2
ball_totalVelocity = 2
ball_velocity_x = (- ball_totalVelocity)
ball_velocity_y = (- ball_totalVelocity)
ball_radius = 3
ball_color = 5
ball_run = False
ball_acceleration_x = - 1
ball_acceleration_y = - 1


# coordonnées des murs
wall_Right = screen_width
wall_Left = 0
wall_Down = screen_height
wall_Up = 0



# variables liées aux briques
# variables liées à l'apparence des briques
brick_width = 20
brick_height = 10
brick_color = 10
brick_color_2 = 3
brick_color_3 = 8
#variables des coordonnées en x des briques
b_x1 = 70
b_x2 = 110
b_x3 = 150
b_x4 = 190
b_x5 = 230
b_x6 = 270
b_x7 = 310
#variables des coordonnées en y des briques
b_y1 = 50
b_y2 = 75
b_y3 = 100
#listes des coordonnées en x et y des briques
bricks_x = [b_x1, b_x2, b_x3, b_x4, b_x5, b_x6, b_x7]
bricks_y = [b_y1, b_y2, b_y3]
bricks_niveau1 = [brick_color, brick_color, brick_color, brick_color, brick_color, brick_color, brick_color, brick_color, brick_color_2, brick_color_3, brick_color_3, brick_color_3, brick_color_2, brick_color, brick_color, brick_color, brick_color, brick_color, brick_color, brick_color, brick_color]  
bricks_niveau2 = [brick_color_2, brick_color, brick_color, brick_color, brick_color, brick_color, brick_color_2, brick_color, brick_color_3, brick_color_3, brick_color_3, brick_color_3, brick_color_3, brick_color, brick_color_2, brick_color, brick_color_2, brick_color_2, brick_color_2, brick_color, brick_color_2]
bricks_niveau3 = [brick_color_3, brick_color_3, brick_color_3, brick_color_3, brick_color_3, brick_color_3, brick_color_3, brick_color_3, brick_color_2, brick_color_2, brick_color_2, brick_color_2, brick_color_2, brick_color_3, brick_color_3, brick_color_3, brick_color_3, brick_color_3, brick_color_3, brick_color_3, brick_color_3]
rang = 0
bricks_broken = 0
#liste des briques
bricks_list = []
# variable qui permet la construction des briques une seule fois
brick_start = True


# variables liées au jeu
level_1 = True
level_2 = False
level_3 = False
game = True




#___________________________________________________________________________________#
# fonctions du casse-brique


# fonction qui définit le mouvement de la plateforme
def platform_move(x, y):

    if pyxel.btn(pyxel.KEY_RIGHT):
        if x  < (screen_width - platform_width - platform_sideWidth) :
            x = x + platform_velocity
    if pyxel.btn(pyxel.KEY_LEFT):
        if x > (platform_sideWidth) :
            x = x - platform_velocity
    
    return x, y


# fonction qui définit l'accélaration de la balle
def ball_acceleration(ball_velocity_x, ball_velocity_y, ball_acceleration_x, ball_acceleration_y):
    if (pyxel.frame_count % 2000 == 0):
        if ball_acceleration_x > 0:
            ball_acceleration_x = ball_acceleration_x + 1
            
        if ball_acceleration_x < 0:
            ball_acceleration_x = ball_acceleration_x - 1
            
        if ball_acceleration_y > 0:
            ball_acceleration_y = ball_acceleration_y + 1
            
        if ball_acceleration_y < 0:
            ball_acceleration_y = ball_acceleration_y - 1
            
    return ball_velocity_x, ball_velocity_y, ball_acceleration_x, ball_acceleration_y


#fonction qui définit le mouvement de la balle
def ball_move(x, y, a, b, r, health_points, score, ball_run, ball_acceleration_x, ball_acceleration_y, bricks_broken, level_2, level_3):
    
    if ball_run:
        x = x + a + ball_acceleration_x
        y = y + b + ball_acceleration_y
        for brick in bricks_list:
        
            if (y + r + b) >= brick[1] and (y - r + b) <= (brick[1] + brick_height) and (x + r + a) >= brick[0] and (x - r + a) <= (brick[0] + brick_width):
                if (x + r + a) > (brick[0] + r) and (x - r + a) < (brick[0] + brick_width - r):
                    b = (- b)
                    ball_acceleration_y = (- ball_acceleration_y)
                    score += 1
        
                else:
                    a = (- a)
                    ball_acceleration_x = (- ball_acceleration_x)
                    score += 1
                    
                if pyxel.pget(brick[0] + 1, brick[1] + 1) == brick_color:
                    bricks_list.remove(brick)
                    bricks_broken += 1
                    print(bricks_broken)
                    if bricks_broken == 21 :
                        print("niveau2")
                        level_1 = False
                        level_2 = True
                        bricks_creation(bricks_niveau2)
                    elif bricks_broken == 42:
                        print("niveau3")
                        level_2 = False
                        level_3 = True
                        bricks_creation(bricks_niveau3)
                    
                elif pyxel.pget(brick[0] + 1, brick[1] + 1) == brick_color_2:
                    brick[2] = brick_color
                        
                elif pyxel.pget(brick[0] + 1, brick[1] + 1) == brick_color_3:
                    brick[2] = brick_color_2
                
                
            
        # bord droit
        if (x + r + a) >= wall_Right: 
            a = (- a)
            ball_acceleration_x = (- ball_acceleration_x)
            
        # bord gauche
        elif (x - r + a) <= wall_Left:
            a = (- a)
            ball_acceleration_x = (- ball_acceleration_x)
             
        # bord haut
        elif (y - r + b) <= wall_Up:
            b = (- b)
            ball_acceleration_y = (- ball_acceleration_y)
            
        # bord bas
        elif (y + r + b) >= wall_Down:
            ball_run = False
                
            
        # rebond plateforme
        elif ((y + r + b) > platform_y and (x + a - r) <= (platform_x + platform_width) and (x + a + r) >= platform_x) or ((y + r + b) > platform_y and (x + r + a) < (platform_x) and (x - r + a) > (platform_x - platform_sideWidth) and pyxel.pget((x + a), (y + b)) == platform_color) or ((y + r + b) > platform_y and (x + r + a) < (platform_x + platform_width + platform_sideWidth) and (x - r + a) > (platform_x + platform_width) and pyxel.pget((x + a), (y + b)) == platform_color):
            b = (-b)
            ball_acceleration_y = (- ball_acceleration_y)
            
    return x, y, a, b, r, health_points, score, ball_run, ball_acceleration_x, ball_acceleration_y, bricks_broken, level_2, level_3


def bricks_creation(niveau):
    for i in bricks_y:
        for j in bricks_x:
            b_y = i
            b_x = j
            if bricks_y.index(b_y) == 0:
                rang = bricks_x.index(b_x)
                    
            elif bricks_y.index(b_y) == 1:
                rang = bricks_x.index(b_x) + 7
                    
            elif bricks_y.index(b_y) == 2:
                rang = bricks_x.index(b_x) + 14
                    
            brick_level = niveau[rang]
            bricks_list.append([b_x, b_y, brick_level])
                
    return niveau    




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
    global health_points, rang, brick_level, ball_totalVelocity, platform_x, platform_y, vies, ball_x, ball_y, ball_velocity_x, ball_velocity_y, ball_radius, b_x, b_y, bricks_list, brick_start, brick_height, brick_width, score, ball_run, ball_acceleration_x, ball_acceleration_y, bricks_broken, bricks_niveau1, bricks_niveau2, level_2, level_3
    
    
    # au lancement du jeu appuyer sur espace pour commencer le déplacement de la balle
    if pyxel.btnr(pyxel.KEY_SPACE):
        ball_run = True
    
    # si la balle n'est plus en état de se déplacer (touche bord bas)
    if ball_run == False:
        ball_x = screen_width/2
        ball_y = screen_height/2
        

    # mise à jour de la position du vaisseau
    platform_x, platform_y = platform_move(platform_x, platform_y)
    
    ball_velocity_x, ball_velocity_y, ball_acceleration_x, ball_acceleration_y = ball_acceleration(ball_velocity_x, ball_velocity_y, ball_acceleration_x, ball_acceleration_y)
    
    #déplacement de la balle
    ball_x, ball_y, ball_velocity_x, ball_velocity_y, ball_radius, health_points, score, ball_run, ball_acceleration_x, ball_acceleration_y, bricks_broken, level_2, level_3 = ball_move(ball_x, ball_y, ball_velocity_x, ball_velocity_y, ball_radius, health_points, score, ball_run, ball_acceleration_x, ball_acceleration_y, bricks_broken, level_2, level_3)
    
    
    #gestion des vies
    health_points_gestion()
    
    # si la construction des brique est vrai alors créer les briques 
    if brick_start :
        bricks_creation(bricks_niveau1)
        brick_start = False
        
    

        
    

# affichage graphique___________________________________________________________________________________________________________________________
def draw():
    global level_1, level_2, level_3, game
    """création des objets (30 fois par seconde)"""
    # effacer les éléments de l'écran
    pyxel.cls(0)

    # si les vies sont supérieures à 0
    if health_points > 0 and game == True:    

        # platform 
        pyxel.rect(platform_x, platform_y, platform_width, platform_height, platform_color)
        pyxel.tri(platform_x + platform_width, platform_y, platform_x + platform_width, platform_y + platform_height - 1, platform_x + platform_width + platform_sideWidth, platform_y + platform_height - 1, platform_color)
        pyxel.tri(platform_x, platform_y, platform_x, platform_y + platform_height - 1, platform_x - platform_sideWidth, platform_y + platform_height - 1, platform_color)
        pyxel.rect((platform_x - platform_sideWidth), (platform_y + platform_height), ((2 * platform_sideWidth) + platform_width), platform_downHeight, platform_color)
        # ball
        pyxel.circ(ball_x, ball_y, ball_radius, ball_color)
        
        
        for brick in bricks_list:
            pyxel.rect(brick[0], brick[1], brick_width, brick_height, brick[2])
        
        pyxel.text(10, 10,'Score: %d' % score, 7)
        
        pyxel.text(360, 10,'vies: %d' % health_points, 7)
        
        if level_1:
            pyxel.text(186,10, 'NIVEAU 1', 7)
            
            if level_2:
                level_1 = False
                pyxel.text(186,10, 'NIVEAU 2', 7)
        
            elif level_3:
                level_1 = False
                pyxel.text(186,10, 'NIVEAU 3', 7)
   
        if level_2:
            pyxel.text(186,10, 'NIVEAU 2', 7)
            if level_3:
                level_2 = False
                pyxel.text(186,10, 'NIVEAU 3', 7)
                
        if level_3:
            pyxel.text(186,10, 'NIVEAU 3', 7)
        
        if bricks_broken == 63:
            game = False
    
    elif game == False: 
        pyxel.text(142,150, 'BRAVO TU AS REUSSI LES 3 NIVEAUX', 7)
        
    # si les vies ne sont pas supérieures à 0  
    elif health_points <= 0:

        pyxel.text(180,150, 'GAME OVER', 7)
        
        

# lancement du jeu _____________________________________________________________________________________________________________________________
pyxel.run(update, draw)

