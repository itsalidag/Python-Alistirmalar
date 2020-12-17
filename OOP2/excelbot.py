# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 18:45:00 2020

@author: alida
"""

import pandas as pd 
import numpy as np
from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt
import seaborn as sns

geolocator = Nominatim(user_agent = "world_map")
data = pd.read_csv("tr.csv")
#a = 1
#for i in data.columns:
#    print(a , "| " + i + " |" , len(data[i]) , "kayıt mevcut.")
#    a+=1
    
    
class excellbot():
    def __init__(self):
        print("welcome to excellbot. \nUse .getvars to generate new file with specified columns")
        
    def getvars(self, df, col, outname):
        df[col].to_excel(r"{}.xlsx".format(outname))
        #return df[col]
        print("Your file succesfully saved as {}".format(outname))
    
    def stats(self, df, col, outname):
#        for each column in dataframe, calculate :
#        mean, median, sum, std deviation, interquartile range, each quartile
#        try:
#
        index = ["Mean", "Median", "Sum", "Standart Deviation"]
        stat = pd.Series([df[col].mean(), df[col].median(), df[col].sum(), df[col].std()], index = index)
        new_df  = pd.DataFrame(stat, columns = [str(col)])
        
        
        new_df.to_excel(r"stats-{}2.xlsx".format(col))
        print("Your file saved as stats-{}.xlsx".format(outname))
    
    def geocode(self,data, namecol, outname): # does not working properly on turkish cities
        for i in data[namecol]:
            print(i)
            location = geolocator.geocode(i)
            lat = location.latitude
            long = location.longitude
            data["lat"] = lat
            data["long"] = long
        
        data.to_excel(r"{}-located.xlsx".format(outname))
            
    def countplot(self, data, count_data,title, xlabel, outname):  #does not working at all.
        count_data = data[str(count_data)].value_counts().sort_index()
        plt.xkcd(scale=.9,length=90,randomness=0.9)
        custom_color = sns.palplot(sns.color_palette("ch:2,r=.2,l=.6"))
        plt.figure(figsize=(12,8))
        plt.style.use("seaborn")
        sns.countplot(x = str(count_data), data = data, palette = custom_color, order = count_data.index)
        plt.title(str(title), fontsize = 16, weight = "bold")
        plt.xticks(rotation = 90, fontsize = 13)
        plt.xlabel(str(xlabel), fontsize = 14)
        plt.show()
        plt.savefig("{}-plotali.png".format(outname))
        
        


bot = excellbot()
bot.countplot(data, "nufus", "Turkiye Nüfus", "Nufüs(kişi)", "denedim")
