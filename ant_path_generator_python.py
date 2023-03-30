import pandas as pd
import pygame
import random
import numpy as np
df = pd.read_csv("normalised_colony_6_data_vid_1.csv")
temp_df = pd.read_csv("temperature.csv")
temp = temp_df["Temp"]
ant = list(df.ant)
x = list(df.x)
y = list(df.y)
x_14 = list(df[df["ant"] == 14]["x"])
y_14 = list(df[df["ant"] == 14]["y"])

x_15 = list(df[df["ant"] == 15]["x"])
y_15 = list(df[df["ant"] == 15]["y"])

x_19 = list(df[df["ant"] == 19]["x"])
y_19 = list(df[df["ant"] == 19]["y"])

x_20 = list(df[df["ant"] == 20]["x"])
y_20 = list(df[df["ant"] == 20]["y"])

pygame.init()
screen_width = 1900
screen_height = 900
screen = pygame.display.set_mode((1900, 900))
screen_center = [screen_width // 2, screen_height // 2]

#background

background = pygame.image.load("background.jpg")

# resize the background image to fit the display surface
background = pygame.transform.scale(background, (screen_width, screen_height))

# blit the background onto the screen
screen.blit(background, (0,0))

# Draw the paths
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # User clicked the x button
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # Exit the game loop and close the window
                running = False
        current_ant = 0
        time_delay = 25 * 3 # in milliseconds
        blue = 100
        for i in range(len(x_15)-1): #x_15 has the highest length so its used
            if ant[i] != current_ant:
                current_ant = ant[i]
            
            pygame.draw.line(screen, (255,0,0), [(screen_center[0] + x_14[i])-x_14[0],(screen_center[1] - y_14[i])+y_14[0]], [(screen_center[0] + x_14[i+1])-x_14[0],(screen_center[1] - y_14[i+1])+y_14[0]], 2) # x positive y positive
            
            pygame.draw.line(screen, (255,0,0), [(screen_center[0] + x_15[i])-x_15[0],(screen_center[1] - y_15[i])+y_15[0]], [(screen_center[0] + x_15[i+1])-x_15[0],(screen_center[1] - y_15[i+1])+y_15[0]], 2) # x negative y negative
            # 
            pygame.draw.line(screen, (255,0,0), [(screen_center[0] + x_19[i])-x_19[0],(screen_center[1] - y_19[i])+y_19[0]], [(screen_center[0] + x_19[i+1])-x_19[0],(screen_center[1] - y_19[i+1])+y_19[0]], 2) # x negative y negative
            
            pygame.draw.line(screen, (255,0,0), [(screen_center[0] + x_20[i])-x_20[0],(screen_center[1] - y_20[i])+y_20[0]], [(screen_center[0] + x_20[i+1])-x_20[0],(screen_center[1] - y_20[i+1])+y_20[0]], 2) # x positive y positive
            
            
            pygame.draw.circle(screen, (0,0,blue), screen_center, 45)
            blue = blue + 2
            #print(x_15[i], y_15[i])
            
            pygame.display.update()
            pygame.time.wait(time_delay)