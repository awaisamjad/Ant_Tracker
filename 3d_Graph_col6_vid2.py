import pandas as pd                # used to load and sort data
import matplotlib.pyplot as plt    # used to plot data 
import numpy as np                 # used to perform mathematical operations
from matplotlib import animation   # used to record animation
fig = plt.figure()
df = pd.read_csv("sorted_data\colony_6_data_vid_2.csv") # reading in data from colony 6 video 2 csv

ax = plt.axes(projection = "3d") # make projection 3D
ax.set_axis_off() # turn axis off
ax.set_facecolor((173/255, 216/255, 230/255)) # adds a light blue background
def create3dGraph(ant_dataset):
    for i in ant_dataset["ant"].unique(): # iterates through each unique ant 
        ax.plot(ant_dataset[ant_dataset["ant"] == i]["x"],  # plot the ants x value 
                ant_dataset[ant_dataset["ant"] == i]["y"], # plot the ants y value 
                np.linspace(0,50,len(ant_dataset[ant_dataset["ant"] == i]["x"]))) # as there were no z values, numpy was used to
    plt.show()                                                # generate "a" number of numbers equally spaced between       
create3dGraph(df)                                             # 0 and 5 where "a" is the length of the amount of x values    

# This part beneath creates an animation of the 3D plot created by create3dGraph(df) using the matplotlib.animation module.

# The update(frame) function is called repeatedly by animation.FuncAnimation with a frame parameter that represents the current frame number. In this case, the frame parameter is used to update the azimuthal angle of the view of the 3D plot with ax.view_init(elev=10., azim=frame).

# ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 1), interval=50) creates the animation object by calling animation.FuncAnimation, which takes several parameters:

# fig is the Figure object to animate
# update is the update function that will be called repeatedly to create the animation
# frames is an iterable of integers or a generator that defines the sequence of frames to be displayed. In this case, np.arange(0, 360, 1) generates a sequence of integers from 0 to 359 (inclusive) with a step of 1, which represents the frame numbers.
# interval is the delay between frames in milliseconds.
# Finally, ani.save('3d_animation2.mp4', writer='ffmpeg') saves the animation as an mp4 video file using the ffmpeg writer

def update(frame):
    ax.view_init(elev=10., azim=frame)
    return

ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 1), interval=50)
ani.save('3d_animation2.mp4', writer='ffmpeg')


