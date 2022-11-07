from turtle import Screen
import pygame
import random


pygame.mixer.init()
# pygame.mixer.music.load('homepage.wav')
# pygame.mixer.music.play()
pygame.init()



# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
screen_width = 800
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

#background image
bgimg = pygame.image.load('1127551.jpg')
bgimg = pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("Snake-O-Mania")
pygame.display.update()

# Game specific variables
exit_game = False
game_over = False
snake_x = 45
snake_y = 55
velocity_x = 0
velocity_y = 0

food_x = random.randint(20, screen_width)
food_y = random.randint(20, screen_height)
score = 0
init_velocity = 5
snake_size = 10
fps = 60

clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 30)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((135,206,235))
        text_screen('Welcome to Snake-O-Mania',black,230,250)
        text_screen('Press any key to continue',black,250,300)
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:
                exit_game = True 
                
            if event.type == pygame.KEYDOWN:
                pygame.mixer.music.load('homepage.wav')
                pygame.mixer.music.play()
                game_loop()
                        
                
                
        # Hamesha screen ko update karna laazmi hoga         
        pygame.display.update()
        clock.tick(fps)
            
        
# Game Loop
def game_loop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    
    with open('hiscore.txt','r') as f:
        hiscore = f.read()
    

    food_x = random.randint(20, screen_width)
    food_y = random.randint(20, screen_height)
    score = 0
    init_velocity = 5
    snake_size = 15
    fps = 60

    clock = pygame.time.Clock()
    font = pygame.font.SysFont("arial", 18)
    
    snk_list = []
    snk_length = 1

    while not exit_game:
        if game_over:
            with open('hiscore.txt','w') as f:
                f.write (str(hiscore))
            gameWindow.fill(white)
            text_screen('Game Over , Press enter to continue',red,200,50)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                        
                    # Cheat code hai    
                    if event.key == pygame.K_q:
                        score += 5
                        
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            

            if abs(snake_x - food_x)<15 and abs(snake_y - food_y)<15:
                score +=1
                food_x = random.randint(20, screen_width )
                food_y = random.randint(20, screen_height)
                snk_length +=3
                if score > int(hiscore):
                    hiscore = score

            gameWindow.fill(white)
            #bg image add kar rahay hain
            gameWindow.blit(bgimg,(0,0))
            text_screen("Score: " + str(score) + '   Highscore: ' + str(hiscore), (27,34,228), 250, 1)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, 18, 18])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]
                
            if head in snk_list[:-1]:
                game_over = True
                
                
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over =  True

            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow, (45,71,245), snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()
game_loop()