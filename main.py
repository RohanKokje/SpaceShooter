import pgzrun,pygame,random
from pgzero.actor import Actor

WIDTH=800
HEIGHT=800
fire_speed=3
obstacle_speed=1
ship_component=Actor('ship.png',(350,650))
ship_component_clear=Actor('ship_clear.png')
fire_objects=[]
GAME_OVER=True
obstacle_objects=[]
def obstacle_create1():
    obstacle_component=Actor('obstacle.jpg')
    obstacle_component_clear=Actor('obstacle_clear.png')
    return obstacle_component , obstacle_component_clear
def obstacle_spawn():
    lenght_of_obstacle=len(obstacle_objects)
    reamining=4-lenght_of_obstacle
    for i in range(reamining):
        obstacle_create,obstacle_clear=obstacle_create1()
        obstacle_create.x=random.randint(20,WIDTH-20)
        obstacle_create.y=20
        obstacle_objects.append([obstacle_create,obstacle_clear])

def obstacle_update():
    for i in range(len(obstacle_objects)):
        obstacle_objects[i][1].x=obstacle_objects[i][0].x
        obstacle_objects[i][1].y=obstacle_objects[i][0].y
        obstacle_objects[i][1].draw()
        obstacle_objects[i][0].y=obstacle_objects[i][0].y+obstacle_speed
        obstacle_objects[i][0].draw()
        if len(obstacle_objects[i])<4:
            obstacle_objects[i][1].x=obstacle_objects[i][0].x
        obstacle_objects[i][1].y=obstacle_objects[i][0].y
        obstacle_objects[i][1].draw()
        obstacle_objects[i][0].y=obstacle_objects[i][0].y+obstacle_speed
        obstacle_objects[i][0].draw()

def obstacle_clear(index):
    print(len(obstacle_objects))
    obstacle_objects[index][1].y=obstacle_objects[index][0].y
    obstacle_objects[index][1].draw()
    del obstacle_objects[index]


def fire_create_object():
    fire_component=Actor('fire.png')
    fire_component_clear=Actor('fire_clear.png')
    return fire_component , fire_component_clear
def fire_update():
    indexes=[]
    for i in range(len(fire_objects)):
        if hit(fire_objects[i][0],i):
            indexes.append(i)
            fire_objects[i][1].y=fire_objects[i][0].y
            fire_objects[i][1].x=fire_objects[i][0].x
            fire_objects[i][1].draw()
        elif fire_objects[i][0].y<=20:
            indexes.append(i)
            fire_objects[i][1].y=fire_objects[i][0].y
            fire_objects[i][1].x=fire_objects[i][0].x
            fire_objects[i][1].draw()
        else:
            fire_objects[i][1].y=fire_objects[i][0].y
            fire_objects[i][1].x=fire_objects[i][0].x
            fire_objects[i][1].draw()
            fire_objects[i][0].y=fire_objects[i][0].y-fire_speed
            fire_objects[i][0].draw()
    fire_clear(indexes)
def fire_clear(indexes):
    for index in indexes:
        del fire_objects[index]

def hit(fire_object,i):
    index_to_delete = -1
    for i in range(len(obstacle_objects)):
        if fire_object.x>=obstacle_objects[i][0].x-25-5:
            if fire_object.x<=obstacle_objects[i][0].x+25+5: 
                if  fire_object.y>=obstacle_objects[i][0].y-25-5:
                    if fire_object.y<=obstacle_objects[i][0].y+25+5:
                        print("hit found")
                        index_to_delete=i
    if index_to_delete!=-1:
        obstacle_clear(index_to_delete)
        return True
    return False
def obstacle_miss():
    for i in range(len(obstacle_objects)):
        if obstacle_objects[i][1].y>=750:
            if len(obstacle_objects[i])<4:  
                    obstacle_clear(i)
                    obstacle_spawn()
def main_hit():
    global GAME_OVER
    for i in range(len(obstacle_objects)):
        if obstacle_objects[i][0].x>=ship_component.x-20 and obstacle_objects[i][0].x<=ship_component.x+20:
            if obstacle_objects[i][0].y>=ship_component.y-20 and obstacle_objects[i][0].y<=ship_component.y+20:
                screen.clear()
                clear_objects()
                screen.draw.text("GAME OVER",(WIDTH/2,HEIGHT/2),fontsize=40,color="red")
                
                GAME_OVER = True
def clear_objects():
    indexes = [i for i,_ in enumerate(fire_objects)]
    fire_clear(indexes)
    #indexes = [i for i, _  in enumerate(obstacle_objects)]
    #for index in indexes:
     #   obstacle_clear(index)
def draw():
    global GAME_OVER
    GAME_OVER = False
    ship_component.draw()
    
def on_mouse_down(pos):
    print(pos)
def update():
    global GAME_OVER
    ship_component_clear.x=ship_component.x
    ship_component_clear.y=ship_component.y
    ship_component_clear.draw()
    obstacle_miss()
    obstacle_update()
    obstacle_spawn()
    main_hit()
    if GAME_OVER:
        return 0

    fire_update()

    if keyboard.left:
        if ship_component.x-40>0:
            ship_component.x-=5

    elif keyboard.right:
        if ship_component.x+40<800:
            ship_component.x+=5
    elif keyboard.up:
        fire_create,fire_clear=fire_create_object()
        fire_create.y=ship_component.y-50
        fire_create.x=ship_component.x
        fire_create.draw()
        fire_objects.append([fire_create,fire_clear])
    

pgzrun.go()
