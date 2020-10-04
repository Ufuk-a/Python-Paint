import pygame
pygame.init()

paint = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Python - Paint")



def pen():
    pen_pos = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0] == 1:
        pygame.draw.circle(paint, (0, 0, 0), pen_pos, 5)
        pygame.display.update()
        
def eraser():
    esaser_pos = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[2] == 1:
        pygame.draw.circle(paint, (255, 255, 255), esaser_pos, 10)
        pygame.display.update()
        
paint.fill((255, 255, 255))
pygame.display.update()
    

painting = True
while painting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            painting = False
    
    pen()
    eraser()