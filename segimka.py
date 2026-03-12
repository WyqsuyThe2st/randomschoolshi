import pygame
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
x = 0
y = 0
xvel = 0
yvel = 0
onground = 0
dj = 0
col = "purple"
level = [(0,650,100,10)]
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if onground:
                    yvel += 25
                elif dj:
                    yvel = 25
                    dj = 0
    keys=pygame.key.get_pressed()
    if keys[pygame.K_p]:
        continue
    if keys[pygame.K_LEFT]:
        if xvel > 0:
            xvel-=3
        elif xvel > -10:
            xvel-=1
    if keys[pygame.K_RIGHT]:
        if xvel < 0:
            xvel+=3
        elif xvel < 10:
            xvel+=1
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#0FF0F0")
    y+=yvel
    yvel-=2
    x+=xvel
    if y<=0:
        y=0
        yvel=0
        onground=1
        dj = 1
    else:
        onground=0
    for i in range(len(level)):
        for j in range(int(abs(yvel)/level[i][1])+1):
            if pygame.Rect(level[i]).colliderect((x,710-y+yvel-yvel/(i+1),10,10)):
                rect1walls = (level[i][0],level[i][1],level[i][0]+level[i][2],level[i][1]+level[i][3])
                print(rect1walls,x,y,x-xvel,y-yvel,yvel,xvel)
                if 710-y-yvel > level[i][1]:
                    onground = 1
                    dj = 1
                    yvel = 0
                    y = (710-rect1walls[1])+10
    
    if onground:
        xvel *= 0.85
    for i in range(len(level)):
        pygame.draw.rect(screen,"blue",level[i])
    pygame.draw.rect(screen,col,pygame.Rect(x,710-y,10,10))
    # RENDER YOUR GAME HERE
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
