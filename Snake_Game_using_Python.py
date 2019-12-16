import pygame
import random
from pygame import font
x = pygame.init()

white = (255, 255, 255)
red = (255,0,0)
blue = (0,0,120)
black = (0,0,0)

exit_game = False
game_over = False

speed = 5
screen_width = 1000
screen_height = 600
Snake_x = 45
Snake_y = 55
velocity_x = 0
velocity_y = 0
food_x = random.randint(0, screen_width)
food_y = random.randint(0, screen_height)

Snake_size = 15
fps = 30
score = 0
temp = 0 #used in Displaying score and the end text i.e Game Over
Clock = pygame.time.Clock()



gamewindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake Bite")
pygame.display.update()


#Rendering text in pygame
def text_screen(text,color,x,y,size):
    font = pygame.font.SysFont(None, size)
    text_on_screen = font.render(text,True,color)
    gamewindow.blit(text_on_screen,[x,y])

size_len = 1
size_list = []
#Defining the length of the SNAKE
def Display_snake(size_len,size_list,color,x,y):
    for [x,y] in size_list:
        pygame.draw.rect(gamewindow,color,[x,y,Snake_size,Snake_size])


#Creating Game Loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = speed
                velocity_y = 0
            if event.key == pygame.K_LEFT:
                velocity_x = -speed
                velocity_y = 0
            if event.key == pygame.K_UP:
                velocity_x = 0
                velocity_y = -speed
            if event.key == pygame.K_DOWN:
                velocity_x = 0
                velocity_y = speed

    #Collision handling
    if( abs(Snake_x - food_x) <= 20 and abs(Snake_y - food_y) <= 20):  #food is eaten
        food_x = random.randint(250,screen_width-250)
        food_y = random.randint(250,screen_height-250)
        score += 5
        size_len += speed

    if( Snake_x >= screen_width-12 or Snake_x < 0 or Snake_y > screen_height-12 or Snake_y < 0):#Outside of the Window limit
        temp += 1
        game_over = True




    #Drawing the snake
    Snake_x += velocity_x
    Snake_y += velocity_y

    head = []
    head.append(Snake_x)
    head.append(Snake_y)
    size_list.append(head)
    if(len(size_list)>size_len):
        del size_list[0]

    if head in size_list[:-1]: #-------------------------------------------???????
        temp += 1
        velocity_x = 0
        velocity_y = 0
        Snake_x = 0
        Snake_y = 0
        game_over = True

    # Drawing a Snake
    gamewindow.fill(white)
    if(temp == 0):
        text_screen("Score = " + str(score), blue, screen_width / 2.4, 5,40)
    else:
        gamewindow.fill(white)
        text_screen("Game Over", red, screen_width / 2.5, screen_height / 2.4, 65)
        text_screen("Score : "+str(score), red, screen_width / 2.3, screen_height / 2.0, 60)
    #pygame.draw.rect(gamewindow, black, (Snake_x, Snake_y, Snake_size, Snake_size))

    Display_snake(size_len,size_list,black,Snake_x,Snake_y)
    pygame.draw.rect(gamewindow, red, (food_x, food_y, 20, 20))
    pygame.display.update()
    Clock.tick(fps)



pygame.quit()
quit()
