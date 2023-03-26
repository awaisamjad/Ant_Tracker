import pandas as pd
import pygame
df = pd.read_csv("sorted_data\colony_6_data_vid_1.csv")
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
screen = pygame.display.set_mode((1900, 900))

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
        time_delay = 200 # in milliseconds
        for i in range(len(x_14)-1):
            if ant[i] != current_ant:
                current_ant = ant[i]
            #pygame.draw.line(screen, (255,0,0), (x[i], y[i]), (x[i+1], y[i+1]), 2)
            pygame.draw.line(screen, (255,0,0), (x_14[i], y_14[i]), (x_14[i+1], y_14[i+1]), 2)
            pygame.draw.line(screen, (255,0,0), (x_15[i], y_15[i]), (x_15[i+1], y_15[i+1]), 2)
            pygame.draw.line(screen, (255,0,0), (x_19[i], y_19[i]), (x_19[i+1], y_19[i+1]), 2)
            pygame.draw.line(screen, (255,0,0), (x_20[i], y_20[i]), (x_20[i+1], y_20[i+1]), 2)
            
            pygame.display.update()
            pygame.time.wait(time_delay)
    pygame.display.flip()