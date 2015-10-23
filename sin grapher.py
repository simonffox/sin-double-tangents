# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 11:26:47 2015

@author: sfox
"""

import numpy as np
#import matplotlib as mp
import math
import matplotlib.pyplot as plt

def sin_points(begin,end,interval):
    '''outputs list of sine values from begin to end, with intervals var'''
    
    i = begin
    x = []
    y = []
    while i < end:
        x.append(i)
        y.append(np.cos(i))
        i += interval
    
    return x, y

def tanline(begin,end,interval,tan_at_point):
    '''outputs list of sine values from begin to end, with intervals var'''
    
    i = begin
    x = []
    y = []
    while i < end:
        x.append(i)
        y.append((-np.sin(tan_at_point))*(i - tan_at_point) + np.cos(tan_at_point)) 
        i += interval
    
    return x, y
    
def grapher(values,color):
    '''graphs input tuple of two variables'''
    plt.plot(values[0],values[1],color)
    plt.ylim([-1.1,1.1])
    
    
b = 0
e = 50#math.pi*2*4
i = .01
tan_at_point0 = math.pi/2.
tan_at_point1 = 0.218979522475625
tan_at_point2 = 0.128729797036775
tan_at_point3 = 0.0914526281353765
tan_at_point4 = 0.0709730283226
tan_at_point5 = 0.058004322813094
tan_at_point6 = 0.04904928904609321
tan_at_point7 = 0.0424924032344

points = sin_points(b,e,i)
tanpoints0 = tanline(b,e,i,tan_at_point0)
tanpoints1 = tanline(b,e,i,tan_at_point1)
tanpoints2 = tanline(b,e,i,tan_at_point2)
tanpoints3 = tanline(b,e,i,tan_at_point3)
tanpoints4 = tanline(b,e,i,tan_at_point4)
tanpoints5 = tanline(b,e,i,tan_at_point5)
tanpoints6 = tanline(b,e,i,tan_at_point6)
tanpoints7 = tanline(b,e,i,tan_at_point7)
grapher(points,'b')
grapher(tanpoints0,'g')
grapher(tanpoints1,'g')
grapher(tanpoints2,'g')
grapher(tanpoints3,'g')
grapher(tanpoints4,'g')
grapher(tanpoints5,'g')
grapher(tanpoints6,'g')
grapher(tanpoints7,'g')