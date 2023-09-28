import pgzrun,pygame
from pgzero.actor import Actor

WIDTH=800
HEIGHT=800
ship_component=Actor('ship.png',(350,650))
ship_component_clear=Actor('ship_clear.png')
fire_component=Actor('fire.png')
fire_component_clear=Actor('fire_clear.png')
def draw():
    ship_component.draw()
def on_mouse_down(pos):
    print(pos)
def update():
    ship_component_clear.x=ship_component.x
    ship_component_clear.y=ship_component.y
    ship_component_clear.draw()
    if keyboard.left:
        if ship_component.x-40>0:
            ship_component.x-=5

    
    elif keyboard.right:
        if ship_component.x+40<800:
            ship_component.x+=5
    elif keyboard.up:
        fire_component.y=ship_component.y-50
        fire_component.x=ship_component.x
        fire_component.draw()    
pgzrun.go()