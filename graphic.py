import pygame

def draw_plane(x_axis, y_axis, scale, size, ofs, surf):
    
    col = (60, 60, 60)

    for x in range(0, size[0]):
        
        x *= scale
        scaled_x = y_axis.x + scale
        pygame.draw.line(surf, col, (x + scaled_x - size[0] / 2 * scale, 0), (x + scaled_x - size[0] / 2 * scale, size[1]))

    for y in range(0, size[0] * 2):
        
        y *= scale
        scaled_y = x_axis.y + scale
        pygame.draw.line(surf, col, (0, y + scaled_y - size[0] / 2 * scale), (size[0], y + scaled_y - size[0] / 2 * scale))
    
    pygame.draw.rect(surf, (180, 180, 180), x_axis)
    pygame.draw.rect(surf, (180, 180, 180), y_axis)
    
def loop(f, screen_w, screen_h, surf, screen):

    u_x, u_y = int(screen_w - screen_w / 2), int(screen_h - screen_h / 2)
    
    l_x, l_y = -u_x, -u_y
    
    print(str(l_x) + ' ' + str(u_x))
    print(str(l_y) + ' ' + str(u_y))
    
    x_axis = pygame.Rect(0, screen_h // 2, screen_w, 3)
    y_axis = pygame.Rect(screen_w // 2, 0, 3, screen_h)
    
    scale = 80
    
    x_ofs = 0
    y_ofs = 0
    
    dragging = False
    
    precision = 4
    
    run = True
    while(run):
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            elif event.type == pygame.KEYDOWN:
                if event.unicode == "q":
                    scale /= 2
               
                elif event.unicode == 'e':
                    scale *= 2

                elif event.unicode == "z":
                    precision -= 1
                    print(precision)
               
                elif event.unicode == 'c':
                    precision += 1
                    print(precision)

                elif event.unicode == 'r':
                    x_axis = pygame.Rect(0, screen_h // 2, screen_w, 3)
                    y_axis = pygame.Rect(screen_w // 2, 0, 3, screen_h)
                    scale = 80
                    
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

        draw_plane(x_axis, y_axis, scale, [screen_w, screen_h], [x_ofs, y_ofs], surf)

        i = 0
        for function in f:
            
            if function(0) == None:
                break
            
            for x in range(l_x * precision, u_x * precision):
                
                cols = [[255, 255, 255], [255, 0, 0], [0, 255, 0], [0, 0, 255]]
            
                next_x_pos = ((x + 1) / precision) * scale + u_x
                next_y_pos = -(function((x + 1) / precision) * scale - u_y)
        
                x /= precision
            
                x_pos = x * scale + u_x
                y_pos = -(function(x) * scale - u_y)
                
                px_ofs = y_axis.x - u_x
                py_ofs = x_axis.y - u_y    
                
                x_pos += px_ofs
                next_x_pos += px_ofs
                
                y_pos += py_ofs
                next_y_pos += py_ofs
                    
                pygame.draw.circle(surf, cols[i % len(cols)], (x_pos, y_pos), 2)
                pygame.draw.line(surf, cols[i % len(cols)], (x_pos, y_pos), (next_x_pos, next_y_pos))

            i += 1
        
        screen.update()