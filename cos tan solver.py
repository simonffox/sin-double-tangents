# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 13:39:53 2015

@author: sfo
"""

import numpy as np
import math
import time

def cosine_solver(n):
    '''finds points where one tan point is tan point again'''
    
    t = time.time()
    i = 0.04249240322


    while i < 0.04249240324:
        #                                                       #.123456789/123
        if abs(np.tan(i) * (math.pi*n + math.pi/2. - i) - 1) <= 0.0000000000001:
            print ("error:", abs(np.tan(i) * (math.pi*n + math.pi/2. - i)-1))           
            print (i,"is the m value for n =", n,"humps")
            i = math.pi
        else:
            i += .000000000000001
        #       #.123456789/1234567
    
    print ("time to complete in seconds:", time.time() - t)
            

def alternate_cosine_solver():
    '''same thing'''
    
    t = time.time()
    solutions = []
    interval =     0.000000000000000006

    ####           #.123456789/123
    y =            0.0424924032
    #intervalend = 0.0914526282   
    intervalend =  0.0424924033

    while y < intervalend:    
        x = (1 + y*np.tan(y)) / (math.pi * np.tan(y)) - .5
        if x.is_integer():
            solutions.append([x,y])
            y += interval
        else:
            y += interval
    
    print (solutions)
    print ("time to complete in seconds:", time.time() - t)
    
    
#cosine_solver(7)
alternate_cosine_solver()