import pygame, sys, random, time



check_errors = pygame.init()

if check_errors[1] >0:
    print('Had {0} initializing errors, exiting now...'.format(check_errors[1]))
    sys.exit(-1)
else:
    print("Pygame successfully initialized")

pygame.mixer.init()
pygame.mixer.music.load('benny.ogg')
pygame.mixer.music.play()



# play surface

play_surface = pygame.display.set_mode((720,460))
pygame.display.set_caption("Snake Game")

# colors

red = pygame.Color(255,0,0)
green = pygame.Color(43,153,93)
blue = pygame.Color(0,0,255)
black = pygame.Color(10,15,18)
white = pygame.Color(255,255,255)
brown = pygame.Color(165,42,42)
yellow = pygame.Color(247,151,39)
orange = pygame.Color(222,105,61)
redish = pygame.Color(207,56,71)
blueish = pygame.Color(35,47,69)
pink = pygame.Color(222,178,178)
darkpink = pygame.Color(110,65,70)


# FPS(frame for second) controller

fps_controller = pygame.time.Clock()

# important variable

snake_position = [100,50]
snake_body = [[100,50],[90,50],[80,50]]

food_position = [random.randrange(1,71)*10,random.randrange(1,45)*10]
food_spawn = True

direction = 'RIGHT'
changeto = direction
score = 0
speed = 15

# game function

def game_over():
    my_font = pygame.font.SysFont('monaco', 55)
    go_surf = my_font.render('GAME OVER YOU LITTLE SHIT!', True, redish)
    go_rect = go_surf.get_rect()
    go_rect.midtop = (360, 100)
    play_surface.blit(go_surf, go_rect)
    show_score(0)
    pygame.mixer.init()

    pygame.mixer.music.load('go.ogg')
    pygame.mixer.music.play()
    pygame.display.flip()

    time.sleep(3)
    pygame.quit()
    sys.exit()

def show_score(choice=1):
    score_font = pygame.font.SysFont('monaco', 30)
    score_surf = score_font.render('SCORE: {}'.format(score), True, blueish)
    score_rect = score_surf.get_rect()
    if choice ==1:
        score_rect.midtop = (80, 15)
    else:
        score_rect.midtop = (360, 150)

    play_surface.blit(score_surf, score_rect)


# main logic of the game

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT:
                changeto = 'LEFT'
            if event.key == pygame.K_UP:
                changeto = 'UP'
            if event.key == pygame.K_DOWN:
                changeto = 'DOWN'

            if event.key == pygame.K_ESCAPE:

                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # validation of direction
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction ='RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction ='UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction ='DOWN'


    if direction == "RIGHT":
        snake_position[0] += 10
    if direction == "LEFT":
        snake_position[0] -= 10
    if direction == "UP":
        snake_position[1] -= 10
    if direction == "DOWN":
        snake_position[1] += 10

    # body mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] ==food_position[1]:
        score +=1
        speed +=1
        food_spawn = False
    else:
        snake_body.pop()

    if food_spawn == False:
        food_position = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
    food_spawn = True

    play_surface.fill(pink)

    for pos in snake_body:
        pygame.draw.rect(play_surface, blueish, pygame.Rect(pos[0], pos[1], 10,10))

    pygame.draw.rect(play_surface, darkpink, pygame.Rect(food_position[0], food_position[1], 10, 10))

    if snake_position[0] > 710 or snake_position[0] < 0:
        game_over()
    if snake_position[1] > 450 or snake_position[1] < 0:
        game_over()

    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    show_score()

    pygame.display.update()  # or flip

    fps_controller.tick(speed)








