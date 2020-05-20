# -*- coding: utf-8 -*-
"""
Created on Wed May 13 14:43:40 2020

@author: Nathan Nickelson
"""

import numpy as np
import matplotlib.pyplot as plt  # To visualize
import pandas as pd  # To read data
from sklearn.linear_model import LinearRegression
from DailyCasesExtraction import new_cases



def main():

    URL1='https://www.worldometers.info/coronavirus/usa/new-york/'
    URL2 = 'https://www.worldometers.info/coronavirus/country/us/'
    URL3 = 'https://www.worldometers.info/coronavirus/usa/new-jersey/'        
    
    new_cases_NY = new_cases(URL1)
    new_cases_US = new_cases(URL2)
    new_cases_NJ = new_cases(URL3)
    
    zero_list = [0]*(len(new_cases_US)-len(new_cases_NY))
    new_cases_NY = zero_list + new_cases_NY
    
    zero_list = [0]*(len(new_cases_US)-len(new_cases_NJ))
    new_cases_NJ = zero_list + new_cases_NJ
    
    print("NY****") 
    print(new_cases_NY)
    print("NJ****")
    print(new_cases_NJ)
    print("USA****")
    print(new_cases_US)
    print('**************************************************************')
    print (len(new_cases_US))
    print('***********************************************')
    
    
    diff_cases1 = []
    diff_cases2 = []
    
    for a,b in zip(new_cases_US, new_cases_NY):
        diff_cases1.append(a-b)
    
    print(diff_cases1)
    
    for a,b,c in zip(new_cases_US, new_cases_NY, new_cases_NJ):
        diff_cases2.append(a-b-c)
    
    print(diff_cases2)
    for i in range(80):
        n = i + 14
        if (n > len(new_cases_US)):
            n = len(new_cases_US)
        plt.clf()
        y_NY = (np.array(new_cases_US))[i:n].reshape(-1,1)
        x_NY = np.array(range(0, len(y_NY))).reshape(-1,1)
        linear_regressor = LinearRegression()
        linear_regressor.fit(x_NY, y_NY)
        Y_pred = linear_regressor.predict(x_NY)
        plt.figure(dpi=300)
        plt.ylim(ymin=0, ymax=50000)
        slope = linear_regressor.coef_
        print(slope)
        plt.plot(x_NY, y_NY)
        plt.plot(x_NY, Y_pred, color='red', label=str(slope))
        plt.legend()
        plt.show()
        
    
if __name__=="__main__":
    main()
    