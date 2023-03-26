import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
fig = plt.figure()
df = pd.read_csv("sorted_data\colony_6_data_vid_2.csv")

ax = plt.axes(projection = "3d")
ax.set_axis_off()
ax.set_facecolor((173/255, 216/255, 230/255))
def create3dGraph(ant_dataset):
    for i in ant_dataset["ant"].unique():
        ax.plot(ant_dataset[ant_dataset["ant"] == i]["x"],
                ant_dataset[ant_dataset["ant"] == i]["y"],
                np.linspace(0,50,len(ant_dataset[ant_dataset["ant"] == i]["x"])))
    plt.show()      
create3dGraph(df)    
def update(frame):
    ax.view_init(elev=10., azim=frame)
    return

#ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 1), interval=50)
#ani.save('3d_animation2.mp4', writer='ffmpeg')


