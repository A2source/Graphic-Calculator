import pygame

def draw_plane(x_axis, y_axis, x_ofs, y_ofs, surf):
    
    pygame.draw.rect(surf, (180, 180, 180), x_axis)
    pygame.draw.rect(surf, (180, 180, 180), y_axis)
    
def loop(f, screen_w, screen_h, surf, screen):

    u_x, u_y = int(screen_w - screen_w / 2), int(screen_h - screen_h / 2)
    
    l_x, l_y = -u_x, -u_y
    
    print(str(l_x) + ' ' + str(u_x))
    print(str(l_y) + ' ' + str(u_y))
    
    x_axis = pygame.Rect(0, screen_h // 2, screen_w, 3)
    y_axis = pygame.Rect(screen_w // 2, 0, 3, screen_h)
    
    scale = 1
    
    x_ofs = 0
    y_ofs = 0
    
    dragging = False
    
    run = True
    while(run):
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            elif event.type == pygame.KEYDOWN:
                if event.unicode == "+":
                    scale *= 2
                    
                elif event.unicode == '-':
                    scale /= 2
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:            
                    dragging = True
                    
                    mx, my = event.pos
                    x_ofs = y_axis.x - mx
                    y_ofs = x_axis.y - my

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:            
                    dragging = False

            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    mx, my = event.pos
                    
                    x_axis.y = my + y_ofs
                    y_axis.x = mx + x_ofs

    
        surf.fill(0)

        draw_plane(x_axis, y_axis, x_ofs, y_ofs, surf)
        
        for x in range(l_x, u_x):
        
            x_pos = x * scale + u_x
            y_pos = f(x) * scale + u_y
            
            next_x_pos = (x + 1) * scale + u_x
            next_y_pos = f(x + 1) * scale + u_y
        
            pygame.draw.circle(surf, (255, 255, 255), (x_pos, y_pos), 2)
            pygame.draw.line(surf, (255, 255, 255), (x_pos, y_pos), (next_x_pos, next_y_pos))
        
        screen.update()