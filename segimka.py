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
    if keys[pygame.K_LEFT]:
        print("buh")
        if xvel > 0:
            xvel-=6
        else:
            xvel-=4
    if keys[pygame.K_RIGHT]:
        if xvel < 0:
            xvel+=6
        xvel+=4
    print(xvel)
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#0FF0F0")
    y+=yvel
    yvel-=2
    x+=xvel
    xvel *= 0.85
    if y<=0:
        y=0
        yvel=0
        onground=1
        dj = 1
    else:
        onground=0
    pygame.draw.rect(screen,col,pygame.Rect(1270-x,710-y,10,10))
    # RENDER YOUR GAME HERE
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
