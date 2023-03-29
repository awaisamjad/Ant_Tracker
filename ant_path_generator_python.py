import pandas as pd
import pygame
import random
df = pd.read_csv("normalised_colony_6_data_vid_1.csv")
ant = list(df.ant)
x = list(df.x)
y = list(df.y)
x_14 = list(df[df["ant"] == 14]["x_new"])
y_14 = list(df[df["ant"] == 14]["y_new"])

x_15 = list(df[df["ant"] == 15]["x_new"])
y_15 = list(df[df["ant"] == 15]["y_new"])

x_19 = list(df[df["ant"] == 19]["x_new"])
y_19 = list(df[df["ant"] == 19]["y_new"])

x_20 = list(df[df["ant"] == 20]["x_new"])
y_20 = list(df[df["ant"] == 20]["y_new"])

pygame.init()
screen_width = 1900
screen_height = 900
screen = pygame.display.set_mode((1900, 900))
screen_center = [screen_width // 2, screen_height // 2]
# Draw the paths


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # User clicked the x button
            running = False
            #sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # Exit the game loop and close the window
                running = False
        current_ant = 0
        time_delay = 100 # in milliseconds
        
        for i in range(len(x_15)-1): #x_15 has the highest length so its used
            if ant[i] != current_ant:
                current_ant = ant[i]
            #pygame.draw.line(screen, (255,0,0), (x[i], y[i]), (x[i+1], y[i+1]), 2) 
            
            pygame.draw.line(screen, (255,0,0), [(screen_center[0] + x_14[i])-x_14[0],(screen_center[1] - y_14[i])+y_14[0]], [(screen_center[0] + x_14[i+1])-x_14[0],(screen_center[1] - y_14[i+1])+y_14[0]], 2) # x positive y positive
            
            pygame.draw.line(screen, (255,0,0), [(screen_center[0] + x_15[i])-x_15[0],(screen_center[1] - y_15[i])+y_15[0]], [(screen_center[0] + x_15[i+1])-x_15[0],(screen_center[1] - y_15[i+1])+y_15[0]], 2) # x negative y negative
            
            pygame.draw.line(screen, (255,0,0), [(screen_center[0] + x_19[i])-x_19[0],(screen_center[1] - y_19[i])+y_19[0]], [(screen_center[0] + x_19[i+1])-x_19[0],(screen_center[1] - y_19[i+1])+y_19[0]], 2) # x negative y negative
            
            pygame.draw.line(screen, (255,0,0), [(screen_center[0] + x_20[i])-x_20[0],(screen_center[1] - y_20[i])+y_20[0]], [(screen_center[0] + x_20[i+1])-x_20[0],(screen_center[1] - y_20[i+1])+y_20[0]], 2) # x positive y positive
            
            #print(x_15[i], y_15[i])
            pygame.display.update()
            pygame.time.wait(time_delay)
        
        x_value = [10,20,30,40,90]
        y_value = [300,200,100,40]
           
           #DRAW IN CENTRE
        # for i in range(len(x_value)):
        #     pygame.draw.line(screen, (255,0,0),[screen_center[0] + x_value[i],screen_center[1] - y_value[i]], [screen_center[0] + x_value[i+1],screen_center[1] - y_value[i+1]], 2 ) # takes centre and adds the respective x and y value. y_value has negative as going down is positive
        #     pygame.display.update()
        #     pygame.time.wait(time_delay)