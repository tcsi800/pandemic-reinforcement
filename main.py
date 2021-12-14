import numpy as np
import pandas as pd
from typing import List, Tuple
import matplotlib.pyplot as plt
import cartopy as cy 

class Node():
    name: str
    diseases: int
    neighbours: List["Node"] = []
    loc: Tuple[float,float]
    def __init__(self, name:str, long:float, lat:float):
        self.name = name
        self.loc = (long,lat)


class Network():

    nodes: List["Node"]


    def __init__(self, filename:str):
        df = pd.read_csv(
            filename,
            header=0
        )

        self.nodes = [Node(df.name[i], df.long[i], df.lat[i]) for i in range(df.shape[0])]

        self.nodes[0].neighbours = [self.nodes[-1]]
        self.nodes[1].neighbours = [self.nodes[-2], self.nodes[3]]

    def printmap(self):
        plt.figure(2)
        ax = plt.axes(projection=cy.crs.PlateCarree())
        ax.stock_img()
        ax.coastlines()
        ax.set_title("Pandemic Map")
        
        for nd in self.nodes:
            long, lat = nd.loc
            plt.plot(long, lat, markersize = 5, marker = 'o', color = 'red')
            for nd1 in nd.neighbours:
                long1,lat1 = nd1.loc
                plt.plot([long1,long],[lat1,lat], color='blue',linewidth=1)

            
        
        plt.show()
        



if __name__=="__main__":
    n =Network("test.csv")

    
    n.printmap()
    print("woo")