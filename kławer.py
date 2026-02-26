import pygame
import time
# pygame setup
pygame.init()
screen = pygame.display.set_mode((550, 1000))
clock = pygame.time.Clock()
running = True
fps = 120
chartname = "chart.txt"
def ChartImport():
    temp = open("./chart.txt", 'r')
    importchart = False
    chart = []
    while True:
        line = temp.readline()
        if not importchart:
            if line.startswith("<meta>"):
                meta = line.lstrip("<meta>").rstrip("\n")
                print(meta)
                meta = meta.split(',')
                for i in range(len(meta)):
                    print(meta[i])
                    if meta[i][0] == "ime":
                        meta[i][0] = "time"
                    meta[i] = tuple(meta[i].split(':'))
                meta = dict(meta)
                continue
            if line.startswith("<start>"):
                importchart = True
        else:
            if line.startswith("<end>"):
                importchart = False
                chart = dict(chart)
                continue
            line = line.rstrip("\n")
            chart.append(line.split(":"))
            chart[-1][1] = chart[-1][1].split(",")
            chart[-1] = tuple(chart[-1])
        if line == "":
            break
    return chart,meta
chart,meta = ChartImport()
scroll_speed = 30
x=0
rects = [[],[],[],[]]
col1="cyan"
col2="cyan"
col3="cyan"
col4="cyan"
deleted = 0
print(chart)
def merge_rects(rect1,rect2):
    ymax = min(rect1[1],rect2[1])
    ymin = max(rect1[1]+rect1[3],rect2[1]+rect2[3])
    xmax = max(rect1[0]+rect1[2],rect2[0]+rect2[2])
    xmin = min(rect1[0],rect2[0])
    return [xmin,ymax,xmax-xmin,ymin-ymax]
frame = 0
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                col1 = "#007874"
            if event.key == pygame.K_w:
                col2 = "#007874"
            if event.key == pygame.K_KP8:
                col3 = "#007874"
            if event.key == pygame.K_KP9:
                col4 = "#007874"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                col1 = "cyan"
            if event.key == pygame.K_w:
                col2 = "cyan"
            if event.key == pygame.K_KP8:
                col3 = "cyan"
            if event.key == pygame.K_KP9:
                col4 = "cyan"
        

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")
    # RENDER YOUR GAME HERE
    pygame.draw.rect(screen,col1,(0,900,100,100))
    pygame.draw.rect(screen,col2,(150,900,100,100))
    pygame.draw.rect(screen,col3,(300,900,100,100))
    pygame.draw.rect(screen,col4,(450,900,100,100))
    if col1 == "#007874":
        rects[0].append([30,0,40,40])
    if col2 == "#007874":
        rects[1].append([180,0,40,40])
    if col3 == "#007874":
        rects[2].append([330,0,40,40])
    if col4 == "#007874":
        rects[3].append([480,0,40,40])
    try:
        chart[str(int(frame*60/fps))]
    except KeyError:
        0
    else:
        for i in chart[str(int(frame*60/fps))]:
            match i:
                case '1':
                    rects[0].append([30,0,40,40])   
                case '2':
                    rects[1].append([180,0,40,40])
                case '3':
                    rects[2].append([330,0,40,40])
                case '4':
                    rects[3].append([480,0,40,40])
                case _:
                    0
    for i in range(len(rects)):
        try:
            rects[i][-2]
        except IndexError:
            continue
        else:
            if rects[i][-2][1]-rects[i][-1][1]==scroll_speed*60/fps:
                rects[i][-1] = merge_rects(rects[i][-1],rects[i][-2])
                del rects[i][-2]
    for i in range(len(rects)):
        deleted = 0
        for j in range(len(rects[i])):
            rects[i][j-deleted][1] += scroll_speed*60/fps
            if rects[i][j-deleted][1] > 1000:
                del rects[i][j-deleted]
                deleted+=1
            try:
                tuple(rects[i][j-deleted])
            except IndexError:
                continue
            else:
                pygame.draw.rect(screen,"blue",tuple(rects[i][j-deleted]))
                pygame.draw.rect(screen,"black",tuple(rects[i][j-deleted]),2)
            
            
    '''for i in range(len(rects)-1,-1,-1):
        rects[i][1] -= 30
        pygame.draw.rect(screen,"blue",tuple(rects[i]))
        pygame.draw.rect(screen,"black",tuple(rects[i]),2)
    for i in range(len(rects)):
        if rects[i-deleted][1] < 0:
            del rects[i-deleted]
            deleted+=1
    deleted = 0'''
    # flip() the display to put your work on screen
    pygame.display.flip()
    frame += 1
    clock.tick(fps)  # limits FPS to fps

pygame.quit()
