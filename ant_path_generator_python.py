import pandas as pd
import pygame
import random
import numpy as np
import cv2
df_col6_vid1 = pd.read_csv("sorted_data\colony_1_data_vid_1.csv")
df_col1_vid4 = pd.read_csv("sorted_data\colony_1_data_vid_1.csv")
# temp_df = pd.read_csv("temperature.csv")
# temp = temp_df["Temperature"]
temp = [14,14,14,14,14,14,13,13,13,13,13,13,13,14,14,14,14,14,15,15,15,15,15,15,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,17,17,17,17,17,17,17,17,17,18,18,18,18,18,17,17,17,17,17,17,16,16,16,16,16,15,15,15,15,15,14,14,14,14,14,14,13,13,13,13,13,13,13,13,14,14,14,14,14,14,15,15,15,15,15,16,16,16,16,17,17,17,17,17,17,17,17,17,16,16,16,16,16,15,15,16,16,16,16,17,17,17,17,17,17,17,17,18,18,18,18,18,17,17,17,17,17,17,16,16,16,16,16,15,15,15,15,15,14,14,14,14,14,14,13,13,13,13,13,13,13,13,14,14,14,14,14,14,15,15,15,15,15,16,16,16,16,17,17,17,17,18,18,18,18,19,19,20,20,20,21,21,22,22,23,23,23,24,24,24,24,24,24,24,24,24,24,24,24,23,23,23,23,23,22,22,22,22,21,21,21,21,20,20,20,20,19,19,19,19,18,18,18,18,17,17,17,17,16,16,16,16,15,15,15,15,14,14,14,14,14,14,14,14,14,14,15,15,15,15,15,15,15,15,15,15,15,15,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,14,14,14,15,15,15,16,16,17,18,18,19,19,20,20,21,21,22,22,23,23,24,24,24,24,24,24,24,24,23,23,22,22,21,21,20,20,19,19,18,18,17,17,16,16,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]
temp = [i for i in range(0,len(temp),2)]

x_14_col6_vid1 = list(df_col6_vid1[df_col6_vid1["ant"] == 1]["x"])
y_14_col6_vid1 = list(df_col6_vid1[df_col6_vid1["ant"] == 1]["y"])

y_14_col6_vid1_divided = list(df_col6_vid1[df_col6_vid1["ant"] == 14]["y"]*-1.542)

x_15_col6_vid1 = list(df_col6_vid1[df_col6_vid1["ant"] == 15]["x"])
y_15_col6_vid1 = list(df_col6_vid1[df_col6_vid1["ant"] == 15]["y"])

y_15_col6_vid1_divided = list(df_col6_vid1[df_col6_vid1["ant"] == 15]["y"]*5)

x_19_col6_vid1 = list(df_col6_vid1[df_col6_vid1["ant"] == 13]["x"])
y_19_col6_vid1 = list(df_col6_vid1[df_col6_vid1["ant"] == 13]["y"])

y_19_col6_vid1_divided = list(df_col6_vid1[df_col6_vid1["ant"] == 19]["y"]*-4.232)

x_20_col6_vid1 = list(df_col6_vid1[df_col6_vid1["ant"] == 23]["x"])
y_20_col6_vid1 = list(df_col6_vid1[df_col6_vid1["ant"] == 23]["y"])

x_1_col1_vid4 = list(df_col1_vid4[df_col1_vid4["ant"] == 16]["x"])
y_1_col1_vid4 = list(df_col1_vid4[df_col1_vid4["ant"] == 16]["y"])

x_2_col1_vid4 = list(df_col1_vid4[df_col1_vid4["ant"] == 2]["x"])
y_2_col1_vid4 = list(df_col1_vid4[df_col1_vid4["ant"] == 2]["y"])

x_68_col1_vid4 = list(df_col1_vid4[df_col1_vid4["ant"] == 69]["x"])
y_68_col1_vid4 = list(df_col1_vid4[df_col1_vid4["ant"] == 69]["y"])

x_93_col1_vid4 = list(df_col1_vid4[df_col1_vid4["ant"] == 93]["x"])
y_93_col1_vid4 = list(df_col1_vid4[df_col1_vid4["ant"] == 93]["y"])

x_77_col1_vid4 = list(df_col1_vid4[df_col1_vid4["ant"] == 67]["x"])
y_77_col1_vid4 = list(df_col1_vid4[df_col1_vid4["ant"] == 67]["y"])

x_9_col1_vid4 = list(df_col1_vid4[df_col1_vid4["ant"] == 49]["x"])
y_9_col1_vid4 = list(df_col1_vid4[df_col1_vid4["ant"] == 49]["y"])

x_17_col1_vid4 = list(df_col1_vid4[df_col1_vid4["ant"] == 17]["x"])
y_17_col1_vid4 = list(df_col1_vid4[df_col1_vid4["ant"] == 17]["y"])

pygame.init()
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
screen_center = [screen_width // 2, screen_height // 2]

#background
background = pygame.image.load("background.jpg")

# resize the background image to fit the display surface
background = pygame.transform.scale(background, (screen_width, screen_height))

# blit the background onto the screen
screen.blit(background, (0,0))

# Set up OpenCV video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (640, 480))

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
        blue = 100
        green = 0
        line_colour = (50, 205, 50)
        line_stroke = 5 # lime green
        pygame.time.wait(1000)
        for i in range(1000): #x_15 has the highest length (233) so its used
            pygame.draw.line(screen, line_colour, [(screen_center[0] + x_14_col6_vid1[i])-x_14_col6_vid1[0],(screen_center[1] - y_14_col6_vid1[i])+y_14_col6_vid1[0]], [(screen_center[0] + x_14_col6_vid1[i+1])-x_14_col6_vid1[0],(screen_center[1] - y_14_col6_vid1[i+1])+y_14_col6_vid1[0]], line_stroke) # x positive y positive

            pygame.draw.line(screen, line_colour, [(screen_center[0] + x_15_col6_vid1[i])-x_15_col6_vid1[0],(screen_center[1] - y_15_col6_vid1[i])+y_15_col6_vid1[0]], [(screen_center[0] + x_15_col6_vid1[i+1])-x_15_col6_vid1[0],(screen_center[1] - y_15_col6_vid1[i+1])+y_15_col6_vid1[0]], line_stroke) # x negative y negative
            
            pygame.draw.line(screen, line_colour, [(screen_center[0] + x_19_col6_vid1[i])-x_19_col6_vid1[0],(screen_center[1] - y_19_col6_vid1[i])+y_19_col6_vid1[0]], [(screen_center[0] + x_19_col6_vid1[i+1])-x_19_col6_vid1[0],(screen_center[1] - y_19_col6_vid1[i+1])+y_19_col6_vid1[0]], line_stroke) # x negative y negative

            pygame.draw.line(screen, line_colour, [(screen_center[0] + x_20_col6_vid1[i])-x_20_col6_vid1[0],(screen_center[1] - y_20_col6_vid1[i])+y_20_col6_vid1[0]], [(screen_center[0] + x_20_col6_vid1[i+1])-x_20_col6_vid1[0],(screen_center[1] - y_20_col6_vid1[i+1])+y_20_col6_vid1[0]], line_stroke) # x positive y positive



            #pygame.draw.line(screen, line_colour, [(screen_center[0] + x_14_col6_vid1[i])-x_14_col6_vid1[0],(screen_center[1] - y_14_col6_vid1_divided[i])+y_14_col6_vid1_divided[0]], [(screen_center[0] + x_14_col6_vid1[i+1])-x_14_col6_vid1[0],(screen_center[1] - y_14_col6_vid1_divided[i+1])+y_14_col6_vid1_divided[0]], line_stroke)
            
            pygame.draw.line(screen, line_colour, [(screen_center[0] + x_15_col6_vid1[i])-x_15_col6_vid1[0],(screen_center[1] - y_15_col6_vid1_divided[i])+y_15_col6_vid1_divided[0]], [(screen_center[0] + x_15_col6_vid1[i+1])-x_15_col6_vid1[0],(screen_center[1] - y_15_col6_vid1_divided[i+1])+y_15_col6_vid1_divided[0]], line_stroke) # x negative y negative
            
            #pygame.draw.line(screen, line_colour, [(screen_center[0] + x_19_col6_vid1[i])-x_19_col6_vid1[0],(screen_center[1] - y_19_col6_vid1_divided[i])+y_19_col6_vid1_divided[0]], [(screen_center[0] + x_19_col6_vid1[i+1])-x_19_col6_vid1[0],(screen_center[1] - y_19_col6_vid1_divided[i+1])+y_19_col6_vid1_divided[0]], line_stroke)
            
            
            
            pygame.draw.line(screen, line_colour, [(screen_center[0] + x_1_col1_vid4[i])-x_1_col1_vid4[0],(screen_center[1] - y_1_col1_vid4[i])+y_1_col1_vid4[0]], [(screen_center[0] + x_1_col1_vid4[i+1])-x_1_col1_vid4[0],(screen_center[1] - y_1_col1_vid4[i+1])+y_1_col1_vid4[0]], line_stroke) # x positive y positive
            
            pygame.draw.line(screen, line_colour, [(screen_center[0] + x_2_col1_vid4[i])-x_2_col1_vid4[0],(screen_center[1] - y_2_col1_vid4[i])+y_2_col1_vid4[0]], [(screen_center[0] + x_2_col1_vid4[i+1])-x_2_col1_vid4[0],(screen_center[1] - y_2_col1_vid4[i+1])+y_2_col1_vid4[0]], line_stroke) # x negative y negative
            # # #
            pygame.draw.line(screen, line_colour, [(screen_center[0] + x_68_col1_vid4[i])-x_68_col1_vid4[0],(screen_center[1] - y_68_col1_vid4[i])+y_68_col1_vid4[0]], [(screen_center[0] + x_68_col1_vid4[i+1])-x_68_col1_vid4[0],(screen_center[1] - y_68_col1_vid4[i+1])+y_68_col1_vid4[0]], line_stroke) # x negative y negative

            pygame.draw.line(screen, line_colour, [(screen_center[0] + x_93_col1_vid4[i])-x_93_col1_vid4[0],(screen_center[1] - y_93_col1_vid4[i])+y_93_col1_vid4[0]], [(screen_center[0] + x_93_col1_vid4[i+1])-x_93_col1_vid4[0],(screen_center[1] - y_93_col1_vid4[i+1])+y_93_col1_vid4[0]], line_stroke) # x positive y positive
            
            pygame.draw.line(screen, line_colour, [(screen_center[0] + x_77_col1_vid4[i])-x_77_col1_vid4[0],(screen_center[1] - y_77_col1_vid4[i])+y_77_col1_vid4[0]], [(screen_center[0] + x_77_col1_vid4[i+1])-x_77_col1_vid4[0],(screen_center[1] - y_77_col1_vid4[i+1])+y_77_col1_vid4[0]], line_stroke) # x negative y negative
            # #
            pygame.draw.line(screen, line_colour, [(screen_center[0] + x_9_col1_vid4[i])-x_9_col1_vid4[0],(screen_center[1] - y_9_col1_vid4[i])+y_9_col1_vid4[0]], [(screen_center[0] + x_9_col1_vid4[i+1])-x_9_col1_vid4[0],(screen_center[1] - y_9_col1_vid4[i+1])+y_9_col1_vid4[0]], line_stroke) # x negative y negative

            pygame.draw.line(screen, line_colour, [(screen_center[0] + x_17_col1_vid4[i])-x_17_col1_vid4[0],(screen_center[1] - y_17_col1_vid4[i])+y_17_col1_vid4[0]], [(screen_center[0] + x_17_col1_vid4[i+1])-x_17_col1_vid4[0],(screen_center[1] - y_17_col1_vid4[i+1])+y_17_col1_vid4[0]], line_stroke)
            
            
            pygame.draw.circle(screen, (0,green,blue), screen_center, 45)
        
            blue = blue + 2
            green = green + 2
            time_delay = temp[i]
            
            # Convert Pygame screen to OpenCV format
            frame = pygame.surfarray.array3d(screen)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            # Write frame to video file
            out.write(frame)
            out.release()
    
            pygame.display.update()
            pygame.time.wait(time_delay)