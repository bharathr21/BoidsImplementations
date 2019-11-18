import pygame, sys, random
pygame.init()

width=1000
height=1000
speed=25

screen=pygame.display.set_mode([width,height])
cir_col=(255,255,255)
size_of_birdies=4
n_birdies=250


food=[750,500]
pygame.draw
##initialize positions of the birdies'
position=[]
for i in range (n_birdies) :
    pos=[random.randint(size_of_birdies,width-size_of_birdies),random.randint(size_of_birdies,height-size_of_birdies)]
    position.append(pos)
    


clock=pygame.time.Clock()

done=False
while not done:
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                done = True
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.QUIT:
                done = True
                sys.exit()
            if event.type == pygame.K_ESCAPE:
                done= True
                break
    if done :
        break
    screen.fill((0,0,0))
    
    pygame.draw.circle(screen,(45,143,212),food,30,30)
    
    for i in range (n_birdies):
        pygame.draw.circle(screen,cir_col,position[i],size_of_birdies,2)
   
    ###position update 
    """       
    for pos in position:
        if pos[0] < width-speed-size_of_birdies and pos[1] < height-speed-size_of_birdies :
            if pos[0]< size_of_birdies-2 :
                 pos[0]=random.randint(pos[0],pos[0]+speed)
            if pos[1]< size_of_birdies-2 :
                 pos[1]=random.randint(pos[1],pos[1]+speed)
            pos[0]=random.randint(pos[0]-speed,pos[0]+speed)
            pos[1]=random.randint(pos[1]-speed,pos[1]+speed)
        else:
            if pos[0] < width-speed-size_of_birdies :
                pos[0]=random.randint(pos[0]-speed,pos[0])
                pos[1]=random.randint(pos[1]-speed,pos[1]+speed)
            if pos[1] < height-speed-size_of_birdies :
                pos[0]=random.randint(pos[0]-speed,pos[0])
                pos[1]=random.randint(pos[1]-speed,pos[1])
    """           
                
    ###flocking movement
    for bird in position:
        neighbours=[]
        for other_bird in position:
            if bird[0] in range(other_bird[0]-200,other_bird[0]+200):
                if bird[1] in range(other_bird[1]-200,other_bird[1]+200):
                    neighbours.append(other_bird)
        if len(neighbours)==0:
            bird[0]=random.randint(bird[0]-50,bird[0]+50)
            bird[1]=random.randint(bird[1]-50,bird[1]+50)
            break
        avg_pos=[]
        w=0
        h=0
        
        for other_bird in neighbours:
            w=w+other_bird[0]
            h=h+other_bird[1]
        avg_w=w/len(neighbours)
        avg_h=h/len(neighbours)
        avg_pos=[avg_w,avg_h]
        if bird[0]<avg_w :
            
            bird[0]=random.randint(bird[0],bird[0]+speed)
        if bird[1]<avg_h :
            
            bird[1]=random.randint(bird[1],bird[1]+speed)
        if bird[0]>avg_w :
            
            bird[0]=random.randint(bird[0]-speed,bird[0])
        if bird[1]>avg_h :
            
            bird[1]=random.randint(bird[1]-speed,bird[1])
    
  
    ###boundaries
    for bird in position :
        if bird[0] <= size_of_birdies:
            bird[0]=random.randint(bird[0],bird[0]+speed+50)
        if bird[0] > width-size_of_birdies:
            bird[0]=random.randint(bird[0]-speed-50,bird[0])
        if bird[1] <= size_of_birdies:
            bird[1]=random.randint(bird[1],bird[1]+speed+50)
        if bird[1] > height-size_of_birdies:
            bird[1]=random.randint(bird[1]-speed-50,bird[1])

    ###more speed towards food
    if bird[0] < food[0]:
            bird[0]=random.randint(bird[0]+100,bird[0]+speed+150)
    if bird[0] > food[0]:
            bird[0]=random.randint(bird[0]-speed-150,bird[0]-100)
    if bird[1] <food[1]:
            bird[1]=random.randint(bird[1]+100,bird[1]+speed+150)
    if bird[1] > food[1]:
            bird[1]=random.randint(bird[1]-speed-150,bird[1]-100)
    pygame.display.flip()
    clock.tick(10)
      
