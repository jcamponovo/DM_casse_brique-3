import pyxel, random


# vies/score
health_points = 3
score = 0



# screen's size
screen_width = 400
screen_height = 300
pyxel.init(screen_width, screen_height)



# variables liées à la plateforme
platform_velocity = 5
platform_color = 5
platform_sideWidth = 25
platform_width = 50
platform_height = 15
platform_downHeight = 5
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
acceleration = True



# coordonnées des murs
wall_Right = screen_width
wall_Left = 0
wall_Down = screen_height
wall_Up = 0



# variables liées aux briques:

# variables liées à l'apparence des briques
brick_width = 20
brick_height = 10
brick_color = 10
brick_color_2 = 3
brick_color_3 = 8
remove = 0

# variables des coordonnées en x des briques
b_x1 = 70
b_x2 = 110
b_x3 = 150
b_x4 = 190
b_x5 = 230
b_x6 = 270
b_x7 = 310

# variables des coordonnées en y des briques
b_y1 = 50
b_y2 = 75
b_y3 = 100

# listes des coordonnées en x et y des briques
bricks_x = [b_x1, b_x2, b_x3, b_x4, b_x5, b_x6, b_x7]
bricks_y = [b_y1, b_y2, b_y3]

bricks_niveau1 = [brick_color, brick_color, brick_color, brick_color, brick_color, brick_color, brick_color, \
                  brick_color, brick_color_2, brick_color_3, brick_color_3, brick_color_3, brick_color_2, brick_color, \
                  brick_color, brick_color, brick_color, brick_color, brick_color, brick_color, brick_color]

bricks_niveau2 = [brick_color_2, brick_color, brick_color, brick_color, brick_color, brick_color, brick_color_2,\
                  brick_color, brick_color_3, brick_color_3, brick_color_3, brick_color_3, brick_color_3, brick_color,\
                  brick_color_2, brick_color, brick_color_2, brick_color_2, brick_color_2, brick_color, brick_color_2]

bricks_niveau3 = [brick_color_3, brick_color_3, brick_color_3, brick_color_3, brick_color_3, brick_color_3, brick_color_3,\
                  brick_color_3, brick_color_2, brick_color_2, brick_color_2, brick_color_2, brick_color_2, brick_color_3, \
                  brick_color_3, brick_color_3, brick_color_3, brick_color_3, brick_color_3, brick_color_3, brick_color_3]

rang = 0
bricks_broken = 0

# liste des briques
bricks_list = []

# variable qui permet la construction des briques une seule fois
brick_start = True




# variables liées au jeu
level_1 = True
level_2 = False
level_3 = False
game = True
level_change = True





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
def ball_acceleration(ball_velocity_x, ball_velocity_y, ball_acceleration_x, ball_acceleration_y, acceleration):
    
    if ball_run:
        if (pyxel.frame_count % 1500 == 0) and acceleration:
            if ball_acceleration_x > 0 and ball_acceleration_x < 3:
                ball_acceleration_x = ball_acceleration_x + 1
                
            elif ball_acceleration_x < 0 and ball_acceleration_x > (- 3):
                ball_acceleration_x = ball_acceleration_x - 1
                
            if ball_acceleration_y > 0 and ball_acceleration_y < 3:
                ball_acceleration_y = ball_acceleration_y + 1
                
            elif ball_acceleration_y < 0 and ball_acceleration_x > (- 3):
                ball_acceleration_y = ball_acceleration_y - 1
                
            if ball_acceleration_x == 3 or ball_acceleration_x == -3 or ball_acceleration_y == 3 or ball_acceleration_y == - 3:
                acceleration = False
                
    return ball_velocity_x, ball_velocity_y, ball_acceleration_x, ball_acceleration_y, acceleration




# fonction qui définit le mouvement de la balle
def ball_move(x, y, a, b, r, health_points, score, ball_run, ball_acceleration_x, ball_acceleration_y, level_2, level_3, bricks_broken):
    
    # si le joueur à lancé le mouvement de la balle
    if ball_run:
        # mouvement de la balle
        x = x + a + ball_acceleration_x
        y = y + b + ball_acceleration_y
        # rebond de la balle sur les briques
        # on parcourt la liste des briques
        for brick in bricks_list:            
            
            # si la balle rencontre les coordonnées de la brique
            if (y + b) >= (brick[1] - r) and (y + b) <= (brick[1] + brick_height + r) and (x + a) >= (brick[0] - r) and (x + a) <= (brick[0] + brick_width + r):
                
                # dans le cas où la balle descend vers la droite
                if a > 0 and b > 0:
                    if (x + a) > (brick[0] - r) and (x + a) < (brick[0] + brick_width + r) and (y + b) > (brick[1] - r) and (y + b) < (brick[1] + r):
                        if pyxel.pget(brick[0], brick[1]) == brick_color:                            
                            bricks_list.remove(brick)
                            bricks_broken = bricks_broken + 1
                            print(bricks_broken)                        
                                
                                
                        elif pyxel.pget(brick[0], brick[1]) == brick_color_2:                            
                            brick[2] = brick_color
                                
                                
                        elif pyxel.pget(brick[0], brick[1]) == brick_color_3:
                            brick[2] = brick_color_2
                            
                        b = (- b)
                        ball_acceleration_y = (- ball_acceleration_y)
                        score += 10                     
                        
                    elif (y + b) > (brick[1] - r) and (y + b) < (brick[1] + brick_height + r) and (x + a) > (brick[0] - r) and (x + a) < (brick[0] + r):
                        if pyxel.pget(brick[0], brick[1]) == brick_color:                            
                            bricks_list.remove(brick)
                            bricks_broken = bricks_broken + 1
                            print(bricks_broken)                        
                                
                                
                        elif pyxel.pget(brick[0], brick[1]) == brick_color_2:                            
                            brick[2] = brick_color
                                
                                
                        elif pyxel.pget(brick[0], brick[1]) == brick_color_3:
                            brick[2] = brick_color_2
                        a = (- a)
                        ball_acceleration_x = (- ball_acceleration_x)
                        score += 10
                        
                        
                        
                # dans le cas où la balle descend vers la gauche       
                elif a < 0 and b > 0:
                    if (x + a) > (brick[0] - r) and (x + a) < (brick[0] + brick_width + r) and (y + b) > (brick[1] - r) and (y + b) < (brick[1] + r):
                        if pyxel.pget(brick[0], brick[1]) == brick_color:                            
                            bricks_list.remove(brick)
                            bricks_broken = bricks_broken + 1
                            print(bricks_broken)                        
                                
                                
                        elif pyxel.pget(brick[0], brick[1]) == brick_color_2:                            
                            brick[2] = brick_color
                                
                                
                        elif pyxel.pget(brick[0], brick[1]) == brick_color_3:
                            brick[2] = brick_color_2
                            
                        b = (- b)
                        ball_acceleration_y = (- ball_acceleration_y)
                        score += 10
                        
                        
                    elif (y + b) > (brick[1] - r) and (y + b) < (brick[1] + brick_height + r) and (x + a) < (brick[0] + brick_width + r) and (x + a) > (brick[0] + brick_width - r):
                        if pyxel.pget(brick[0], brick[1]) == brick_color:                            
                            bricks_list.remove(brick)
                            bricks_broken = bricks_broken + 1
                            print(bricks_broken)                        
                                
                                
                        elif pyxel.pget(brick[0], brick[1]) == brick_color_2:                            
                            brick[2] = brick_color
                                
                                
                        elif pyxel.pget(brick[0], brick[1]) == brick_color_3:
                            brick[2] = brick_color_2
                            
                        a = (- a)
                        ball_acceleration_x = (- ball_acceleration_x)
                        score += 10
                        
                        
                        
                # dans le cas où la balle monte vers la gauche    
                elif a < 0 and b < 0:
                    if (x + a) > (brick[0] - r) and (x + a) < (brick[0] + brick_width + r) and (y + b) < (brick[1] + brick_height + r) and (y + b) > (brick[1] + brick_height - r):
                        if pyxel.pget(brick[0], brick[1]) == brick_color:                            
                            bricks_list.remove(brick)
                            bricks_broken = bricks_broken + 1
                            print(bricks_broken)                        
                                
                                
                        elif pyxel.pget(brick[0], brick[1]) == brick_color_2:                            
                            brick[2] = brick_color
                                
                                
                        elif pyxel.pget(brick[0], brick[1]) == brick_color_3:
                            brick[2] = brick_color_2
                            
                        b = (- b)
                        ball_acceleration_y = (- ball_acceleration_y)
                        score += 10
                        
                        
                    elif (y + b) > (brick[1] - r) and (y + b) < (brick[1] + brick_height + r) and (x + a) < (brick[0] + brick_width + r) and (x + a) > (brick[0] + brick_width - r):
                        if pyxel.pget(brick[0], brick[1]) == brick_color:                            
                            bricks_list.remove(brick)
                            bricks_broken = bricks_broken + 1
                            print(bricks_broken)                        
                                
                                
                        elif pyxel.pget(brick[0], brick[1]) == brick_color_2:                            
                            brick[2] = brick_color
                                
                                
                        elif pyxel.pget(brick[0], brick[1]) == brick_color_3:
                            brick[2] = brick_color_2
                            
                        a = (- a)
                        ball_acceleration_x = (- ball_acceleration_x)
                        score += 10
                        
                       
                        
                # dans le cas où la balle monte vers la droite        
                elif a > 0 and b < 0:
                    if (x + a) > (brick[0] - r) and (x + a) < (brick[0] + brick_width + r) and (y + b) < (brick[1] + brick_height + r) and (y + b) > (brick[1] + brick_height - r):
                        if pyxel.pget(brick[0], brick[1]) == brick_color:                            
                            bricks_list.remove(brick)
                            bricks_broken = bricks_broken + 1
                            print(bricks_broken)                        
                                
                                
                        elif pyxel.pget(brick[0], brick[1]) == brick_color_2:                            
                            brick[2] = brick_color
                                
                                
                        elif pyxel.pget(brick[0], brick[1]) == brick_color_3:
                            brick[2] = brick_color_2
                            
                        b = (- b)
                        ball_acceleration_y = (- ball_acceleration_y)
                        score += 10
                        
                    elif (y + b) > (brick[1] - r) and (y + b) < (brick[1] + brick_height + r) and (x + a) > (brick[0] - r) and (x + a) < (brick[0] + r):
                        if pyxel.pget(brick[0], brick[1]) == brick_color:                            
                            bricks_list.remove(brick)
                            bricks_broken = bricks_broken + 1
                            print(bricks_broken)                        
                                
                                
                        elif pyxel.pget(brick[0], brick[1]) == brick_color_2:                            
                            brick[2] = brick_color
                                
                                
                        elif pyxel.pget(brick[0], brick[1]) == brick_color_3:
                            brick[2] = brick_color_2
                            
                        a = (- a)
                        ball_acceleration_x = (- ball_acceleration_x)
                        score += 10
                    
                    
                
        # rebond de la balle sur:    
        # bord droit
        if (x + r + a) >= wall_Right and a > 0: 
            a = (- a)
            ball_acceleration_x = (- ball_acceleration_x)
            
        # bord gauche
        elif (x - r + a) <= wall_Left and a < 0:
            a = (- a)
            ball_acceleration_x = (- ball_acceleration_x)
             
        # bord haut
        elif (y - r + b) <= wall_Up and b < 0:
            b = (- b)
            ball_acceleration_y = (- ball_acceleration_y)
            
        # bord bas
        elif (y + r + b) >= wall_Down and b > 0:
            ball_run = False
                
            
        # plateforme
        elif (y + b) > (platform_y - r) and (x + a) <= (platform_x + platform_width + r) and (x + a) >= (platform_x - r): 
            if b > 0:
                b = (-b)
                ball_acceleration_y = (- ball_acceleration_y)
        
        # plateforme coté gauche
        elif (y + b) > platform_y and (x + a) < platform_x and (x + a) > (platform_x - platform_sideWidth - r):
            if pyxel.pget((x + r + a), (y + r + b)) == platform_color or (y + r + b) > (platform_y + platform_height):
                if b > 0 and a > 0:
                    b = (-b)
                    a = (-a)                                                                                                       
                    ball_acceleration_y = (- ball_acceleration_y)
                    ball_acceleration_x = (- ball_acceleration_x)
                    
                elif b > 0 and a < 0:
                    b = (-b)                                                                                                      
                    ball_acceleration_y = (- ball_acceleration_y)
                    
        # plateforme coté droit
        elif (y + b) > platform_y and (x + a) < (platform_x + platform_width + platform_sideWidth + r) and (x + a) > (platform_x + platform_width):
            if pyxel.pget((x - r + a), (y + r + b)) == platform_color or (y + r + b) > (platform_y + platform_height):
                if b > 0 and a < 0:
                    b = (-b)
                    a = (-a)                                                                                                       
                    ball_acceleration_y = (- ball_acceleration_y)
                    ball_acceleration_x = (- ball_acceleration_x)
                
                elif b > 0 and a > 0:
                    b = (-b)                                                                                                      
                    ball_acceleration_y = (- ball_acceleration_y)
                
     
    # revoie les variables  
    return x, y, a, b, r, health_points, score, ball_run, ball_acceleration_x, ball_acceleration_y, level_2, level_3, bricks_broken



# fonction qui construit les briques en fonction du niveau 1, 2 ou 3
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





# Mise à jour 30 fois par seconde_____________________________________________________________________________________________________
def update():


    # appelle les variables et les listes nécessaires
    global health_points, rang, brick_level, ball_totalVelocity, platform_x, platform_y, vies, ball_x, ball_y, ball_velocity_x, ball_velocity_y, ball_radius, b_x, b_y, bricks_list, brick_start, brick_height, brick_width, score, ball_run, ball_acceleration_x, ball_acceleration_y, bricks_broken, bricks_niveau1, bricks_niveau2, level_2, level_3, acceleration
    
    
    # au lancement du jeu appuyer sur espace pour commencer le déplacement de la balle
    if pyxel.btnr(pyxel.KEY_SPACE):
        ball_run = True
        
    
    
    # si la balle n'est plus en état de se déplacer (touche bord bas)
    if ball_run == False:
        ball_x = platform_x + (platform_width /2)
        ball_y = platform_y - (ball_radius * 2) - 2
        

    # déplacement de la plateforme
    platform_x, platform_y = platform_move(platform_x, platform_y)
    
    
    
    
    # mise à jour de l'acceleration de la balle
    ball_velocity_x, ball_velocity_y, ball_acceleration_x, ball_acceleration_y, acceleration = ball_acceleration(ball_velocity_x, ball_velocity_y, ball_acceleration_x, ball_acceleration_y, acceleration)
    
    
    # déplacement de la balle
    ball_x, ball_y, ball_velocity_x, ball_velocity_y, ball_radius, health_points, score, ball_run, ball_acceleration_x, ball_acceleration_y, level_2, level_3, bricks_broken = ball_move(ball_x, ball_y, ball_velocity_x, ball_velocity_y, ball_radius, health_points, score, ball_run, ball_acceleration_x, ball_acceleration_y, level_2, level_3, bricks_broken)

    
    if bricks_broken == 21:
        ball_run = False
        level_1 = False
        level_2 = True
        bricks_creation(bricks_niveau2)
        bricks_broken = 22
        
                
    elif bricks_broken == 43:
        ball_run = False
        level_2 = False
        level_3 = True
        bricks_creation(bricks_niveau3)
        bricks_broken = 44
    
    # gestion des vies
    health_points_gestion()
    
    
    # si la construction des brique est vrai alors créer les briques 
    if brick_start :
        bricks_creation(bricks_niveau1)
        brick_start = False      
    

# affichage graphique___________________________________________________________________________________________________________________________
def draw():
    
    global level_1, level_2, level_3, game
    
    
    # effacer les éléments de l'écran
    pyxel.cls(0)


    # si les vies sont supérieures à 0
    if health_points > 0 and game == True:    


        # platform 
        pyxel.rect(platform_x, platform_y, platform_width, platform_height, platform_color)
        pyxel.tri(platform_x + platform_width, platform_y, platform_x + platform_width, platform_y + platform_height - 1, platform_x + platform_width + platform_sideWidth, platform_y + platform_height - 1, platform_color)
        pyxel.tri(platform_x, platform_y, platform_x, platform_y + platform_height - 1, platform_x - platform_sideWidth, platform_y + platform_height - 1, platform_color)
        pyxel.rect((platform_x - platform_sideWidth), (platform_y + platform_height), ((2 * platform_sideWidth) + platform_width + 1), platform_downHeight, platform_color)
        # ball
        pyxel.circ(ball_x, ball_y, ball_radius, ball_color)
        
        # dessin des briques
        for brick in bricks_list:
            pyxel.rect(brick[0], brick[1], brick_width, brick_height, brick[2])
        
        # affichage du score
        pyxel.text(10, 10,'Score: %d' % score, 7)
        
        # affichage des vies
        pyxel.text(360, 10,'vies: %d' % health_points, 7)
        
        
        # indique le niveau du jeu 
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
        
        if bricks_broken == 65:
            game = False
    
    
    
    # si le jeu est gagné
    elif game == False: 
        pyxel.text(142,150, 'BRAVO TU AS REUSSI LES 3 NIVEAUX', 7)
        
        
        
    # si les vies ne sont pas supérieures à 0  
    elif health_points <= 0:

        pyxel.text(180,150, 'GAME OVER', 7)
        
        

# lancement du jeu _____________________________________________________________________________________________________________________________
pyxel.run(update, draw)

