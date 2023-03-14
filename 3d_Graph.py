import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("sorted_data\colony_6_data_vid_1.csv")

ax = plt.axes(projection = "3d")
x_14 = df[df["ant"] == 14]["x"]
y_14 = df[df["ant"] == 14]["y"]

x_15 = df[df["ant"] == 15]["x"]
y_15 = df[df["ant"] == 15]["y"]

x_19 = df[df["ant"] == 19]["x"]
y_19 = df[df["ant"] == 19]["y"]

x_20 = df[df["ant"] == 20]["x"]
y_20 = df[df["ant"] == 20]["y"]
#z = np.linspace(0,50,130)
ax.plot(x_14,y_14,np.linspace(0,50,len(x_14)))
ax.plot(x_15,y_15,np.linspace(0,50,len(x_15)))
ax.plot(x_19,y_19,np.linspace(0,50,len(x_19)))
ax.plot(x_20,y_20,np.linspace(0,50,len(x_20)))

def create3dGraph(ant_dataset ):
    for i in ant_dataset["ant"].unique():
        ax.plot(ant_dataset[ant_dataset["ant"] == i]["x"],
                ant_dataset[ant_dataset["ant"] == i]["y"],
                np.linspace(0,50,len(ant_dataset[ant_dataset["ant"] == i]["x"])))
    plt.show()      
create3dGraph(df)    


