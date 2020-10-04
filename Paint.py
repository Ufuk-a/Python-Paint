import pygame
pygame.init()

paint = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Python - Paint")

def pen():
    x = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0] == 1:
        pygame.draw.circle(paint, (0, 0, 0), x, 5)
        pygame.display.update()
        
paint.fill((255, 255, 255))
pygame.display.update()
    

painting = True
while painting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            painting = False
    
    pen()