#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import seaborn as sns
import math
import json
import datetime
from scipy.spatial import ConvexHull
from shapely.geometry import Point, Polygon
from descartes.patch import PolygonPatch
import warnings
warnings.filterwarnings("ignore")


# In[2]:

def adjustdisplayxy(data,x_var,y_var):
    for var in x_var+y_var:
        outdisplay = []
        for i in range(1,len(data)):
            if np.sign(data.loc[i,var])!=np.sign(data.loc[i-1,var]) and abs(data.loc[i,var]- data.loc[i-1,var])>1000:
                outdisplay.append(i)
#         print(var,outdisplay)
        if (len(outdisplay) == 1 or (len(outdisplay) == 2 and outdisplay[1] - outdisplay[0] ==1)) and np.sign(data.loc[outdisplay[0]-1,var])==1:
            max_val = data[var].max()
            data.loc[data[data[var] == max_val].index[0]:,var]=max_val 
#             print(var,"max")
        elif (len(outdisplay) == 1 or (len(outdisplay) == 2 and outdisplay[1] - outdisplay[0] ==1)) and np.sign(data.loc[outdisplay[0]-1,var])==-1:
            min_val = data[var].min()
            data.loc[data[data[var] == min_val].index[0]:,var]=min_val
#             print(var,"min")
        elif len(outdisplay) > 1 and len(outdisplay)%2 == 1:
            for k in range(0,len(outdisplay)-1):
                if k%2 == 0:
                    data.loc[outdisplay[k]:outdisplay[k+1]-1,var] = data.loc[outdisplay[k]-1,var]
            if np.sign(data.loc[outdisplay[-1],var])==1:
                max_val = data[var].max()
                data.loc[outdisplay[-1]:,var]=max_val   
            elif np.sign(data.loc[outdisplay[-1],var])==-1:
                min_val = data[var].min()
                data.loc[outdisplay[-1]:,var]=min_val
        elif len(outdisplay) > 1 and len(outdisplay)%2 == 0:
            for k in range(0,len(outdisplay)-1):
                if k%2 == 0:
                    data.loc[outdisplay[k]:outdisplay[k+1]-1,var] = data.loc[outdisplay[k]-1,var]

# In[3]:

def On_Disaplay(data,x_var,y_var,var_str,wid,hegh):
    for k in range(0,data.shape[0]):
        for i in range(0,8):
            if (data.loc[k,x_var[i]]<0 or data.loc[k,x_var[i]]>=wid) and (data.loc[k,y_var[i]]<=0 or data.loc[k,y_var[i]]>=hegh):
                data.loc[k,var_str]=False
#                 print(k,data.loc[k,var_str])
           
# In[4]:

def On_Objects(data,Col_FT_X,Col_FT_Y,Col_LT_X,Col_LT_Y,Col_FT_sign_X,Col_FT_sign_Y,Col_LT_sign_X,Col_LT_sign_Y):
    fixation = [data['Fixation point X'],data['Fixation point Y']]
    fixation_p = Point(fixation)
    if data["FT_On_Disply"] == True:
        FT_Hull = np.concatenate((data[Col_FT_X].values.reshape((8, 1)),data[Col_FT_Y].values.reshape((8, 1))), axis=1)
        FT_Hull = ConvexHull(np.unique(FT_Hull.astype(float),axis=0))
        polygon_FT = Polygon(convex_points(FT_Hull))
        Fixation_on_FT = fixation_p.within(polygon_FT)
    else:
        Fixation_on_FT = False
    if data["LT_On_Disply"] == True:
        LT_Hull = np.concatenate((data[Col_LT_X].values.reshape((8, 1)),data[Col_LT_Y].values.reshape((8, 1))), axis=1)
        LT_Hull = ConvexHull(np.unique(LT_Hull.astype(float),axis=0))
        polygon_LT = Polygon(convex_points(LT_Hull))    
        Fixation_on_LT = fixation_p.within(polygon_LT)
    else:
        Fixation_on_LT = False
    if data["FT_sign_On_Disply"] == True:        
        FT_SIGN_Hull = np.concatenate((data[Col_FT_sign_X].values.reshape((8, 1)),data[Col_FT_sign_Y].values.reshape((8, 1))), axis=1)
        FT_SIGN_Hull = ConvexHull(np.unique(FT_SIGN_Hull.astype(float), axis=0))
        polygon_FT_SIGN = Polygon(convex_points(FT_SIGN_Hull))
        Fixation_on_FT_SIGN = fixation_p.within(polygon_FT_SIGN)  
    else:
        Fixation_on_FT_SIGN = False
    if data["LT_sign_On_Disply"] == True:   
        LT_SIGN_Hull = np.concatenate((data[Col_LT_sign_X].values.reshape((8, 1)),data[Col_LT_sign_Y].values.reshape((8, 1))), axis=1)
        LT_SIGN_Hull = ConvexHull(np.unique(LT_SIGN_Hull.astype(float), axis=0))
        polygon_LT_SIGN = Polygon(convex_points(LT_SIGN_Hull))
        Fixation_on_LT_SIGN = fixation_p.within(polygon_LT_SIGN)  
    else:
        Fixation_on_LT_SIGN = False
    
    return Fixation_on_FT,Fixation_on_LT,Fixation_on_FT_SIGN,Fixation_on_LT_SIGN

def Gaze_On_Objects(data,Col_FT_X,Col_FT_Y,Col_LT_X,Col_LT_Y,Col_FT_sign_X,Col_FT_sign_Y,Col_LT_sign_X,Col_LT_sign_Y):
    Gaze = [data['Gaze point X'],data['Gaze point Y']]
    Gaze_p = Point(Gaze)
    if data["FT_On_Disply"] == True:
        FT_Hull = np.concatenate((data[Col_FT_X].values.reshape((8, 1)),data[Col_FT_Y].values.reshape((8, 1))), axis=1)
        FT_Hull = ConvexHull(np.unique(FT_Hull.astype(float),axis=0))
        polygon_FT = Polygon(convex_points(FT_Hull))
        Fixation_on_FT = Gaze_p.within(polygon_FT)
    else:
        Fixation_on_FT = False
    if data["LT_On_Disply"] == True:
        LT_Hull = np.concatenate((data[Col_LT_X].values.reshape((8, 1)),data[Col_LT_Y].values.reshape((8, 1))), axis=1)
        LT_Hull = ConvexHull(np.unique(LT_Hull.astype(float),axis=0))
        polygon_LT = Polygon(convex_points(LT_Hull))    
        Fixation_on_LT = Gaze_p.within(polygon_LT)
    else:
        Fixation_on_LT = False
    if data["FT_sign_On_Disply"] == True:        
        FT_SIGN_Hull = np.concatenate((data[Col_FT_sign_X].values.reshape((8, 1)),data[Col_FT_sign_Y].values.reshape((8, 1))), axis=1)
        FT_SIGN_Hull = ConvexHull(np.unique(FT_SIGN_Hull.astype(float), axis=0))
        polygon_FT_SIGN = Polygon(convex_points(FT_SIGN_Hull))
        Fixation_on_FT_SIGN = Gaze_p.within(polygon_FT_SIGN)  
    else:
        Fixation_on_FT_SIGN = False
    if data["LT_sign_On_Disply"] == True:   
        LT_SIGN_Hull = np.concatenate((data[Col_LT_sign_X].values.reshape((8, 1)),data[Col_LT_sign_Y].values.reshape((8, 1))), axis=1)
        LT_SIGN_Hull = ConvexHull(np.unique(LT_SIGN_Hull.astype(float), axis=0))
        polygon_LT_SIGN = Polygon(convex_points(LT_SIGN_Hull))
        Fixation_on_LT_SIGN = Gaze_p.within(polygon_LT_SIGN)  
    else:
        Fixation_on_LT_SIGN = False
    
    return Fixation_on_FT,Fixation_on_LT,Fixation_on_FT_SIGN,Fixation_on_LT_SIGN
# def On_Objects(index,data,Col_FT_X,Col_FT_Y,Col_LT_X,Col_LT_Y,Col_FT_sign_X,Col_FT_sign_Y,Col_LT_sign_X,Col_LT_sign_Y):
#     fixation = [data.loc[index,'Fixation point X'],data.loc[index,'Fixation point Y']]
#     data.loc[index,["FT_On_Disply","LT_On_Disply","LT_sign_On_Disply","FT_sign_On_Disply"]]
#     fixation_p = Point(fixation)
#     if data.loc[index,"FT_On_Disply"] == True:
#         FT_Hull = np.concatenate((data.loc[index,Col_FT_X].values.reshape((8, 1)),data.loc[index,Col_FT_Y].values.reshape((8, 1))), axis=1)
#         FT_Hull = ConvexHull(np.unique(FT_Hull.astype(float),axis=0))
#         polygon_FT = Polygon(convex_points(FT_Hull))
#         Fixation_on_FT = fixation_p.within(polygon_FT)
#     else:
#         Fixation_on_FT = False
#     if data.loc[index,"LT_On_Disply"] == True:
#         LT_Hull = np.concatenate((data.loc[index,Col_LT_X].values.reshape((8, 1)),data.loc[index,Col_LT_Y].values.reshape((8, 1))), axis=1)
#         LT_Hull = ConvexHull(np.unique(LT_Hull.astype(float),axis=0))
#         polygon_LT = Polygon(convex_points(LT_Hull))    
#         Fixation_on_LT = fixation_p.within(polygon_LT)
#     else:
#         Fixation_on_LT = False
#     if data.loc[index,"FT_sign_On_Disply"] == True:        
#         FT_SIGN_Hull = np.concatenate((data.loc[index,Col_FT_sign_X].values.reshape((8, 1)),data.loc[index,Col_FT_sign_Y].values.reshape((8, 1))), axis=1)
#         FT_SIGN_Hull = ConvexHull(np.unique(FT_SIGN_Hull.astype(float), axis=0))
#         Fixation_on_FT_SIGN = Polygon(convex_points(FT_SIGN_Hull))
#     else:
#         Fixation_on_FT_SIGN = False
#     if data.loc[index,"LT_sign_On_Disply"] == True:   
#         LT_SIGN_Hull = np.concatenate((data.loc[index,Col_LT_sign_X].values.reshape((8, 1)),data.loc[index,Col_LT_sign_Y].values.reshape((8, 1))), axis=1)
#         LT_SIGN_Hull = ConvexHull(np.unique(LT_SIGN_Hull.astype(float), axis=0))
#         polygon_LT_SIGN = Polygon(convex_points(LT_SIGN_Hull))
#         Fixation_on_LT_SIGN = fixation_p.within(polygon_LT_SIGN)  
#     else:
#         Fixation_on_LT_SIGN = False
    
#     return Fixation_on_FT,Fixation_on_LT,Fixation_on_FT_SIGN,Fixation_on_LT_SIGN


def to_Date(dte,dt):
    st =  dte['Recording start time']
    add = dte['Recording timestamp']
    start = datetime.datetime(int(dt[0:4]),int(dt[4:6]),int(dt[6:8]),int(st[0:2]),int(st[3:5]),int(st[6:8]),int(st[-3:]))
    return start + datetime.timedelta(seconds=add/1000000)


# In[ ]:


def to_timestampe(dte):
    return datetime.datetime(int(dte[0:4]),int(dte[4:6]),int(dte[6:8]),int(dte[9:11]),int(dte[12:14]),int(dte[15:17]),100*int(dte[-4:]))


# In[ ]:


# to find the convex points in sequense
def convex_points(hull):
    Uniq = np.unique(hull.simplices)
    coords = hull.points[hull.simplices[0]]
    curr_id = hull.simplices[0][1]
    Uniq = np.delete(Uniq,np.where(Uniq == hull.simplices[0][0]))
    Uniq = np.delete(Uniq,np.where(Uniq == hull.simplices[0][1]))
    i = 2
    while i < hull.simplices.shape[0]:
        search = 1
        while search < hull.simplices.shape[0]:
            if curr_id in hull.simplices[search]:
                for item in hull.simplices[search].tolist(): 
                    if item in Uniq:
                        curr_id = hull.simplices[search][abs(np.where( hull.simplices[search]==curr_id)[0][0]-1)]
                        if (hull.points[curr_id].tolist() not in coords.tolist()):
                            coords = np.vstack((coords,hull.points[curr_id]))
                            Uniq = np.delete(Uniq,np.where(Uniq == curr_id))
                            i = i+1
                            break
            search = search + 1

        if len(Uniq) == 0 :
             return coords


# In[ ]:


def draw_object_fixation(index,data,Col_FT_X,Col_FT_Y,Col_LT_X,Col_LT_Y,Col_FT_sign_X,Col_FT_sign_Y,Col_LT_sign_X,Col_LT_sign_Y,width,height):
    fixation = [data.loc[index,'Fixation point X'],data.loc[index,'Fixation point Y']]
    FT_Hull = np.concatenate((data.loc[index,Col_FT_X].values.reshape((8, 1)),data.loc[index,Col_FT_Y].values.reshape((8, 1))), axis=1)
    FT_Hull = ConvexHull(np.unique(FT_Hull.astype(float),axis=0))
    polygon_FT = Polygon(convex_points(FT_Hull))
    LT_Hull = np.concatenate((data.loc[index,Col_LT_X].values.reshape((8, 1)),data.loc[index,Col_LT_Y].values.reshape((8, 1))), axis=1)
    LT_Hull = ConvexHull(np.unique(LT_Hull.astype(float),axis=0))
    polygon_LT = Polygon(convex_points(LT_Hull))         
    FT_SIGN_Hull = np.concatenate((data.loc[index,Col_FT_sign_X].values.reshape((8, 1)),data.loc[index,Col_FT_sign_Y].values.reshape((8, 1))), axis=1)
    FT_SIGN_Hull = ConvexHull(np.unique(FT_SIGN_Hull.astype(float), axis=0))
    polygon_FT_SIGN = Polygon(convex_points(FT_SIGN_Hull))
    LT_SIGN_Hull = np.concatenate((data.loc[index,Col_LT_sign_X].values.reshape((8, 1)),data.loc[index,Col_LT_sign_Y].values.reshape((8, 1))), axis=1)
    LT_SIGN_Hull = ConvexHull(np.unique(LT_SIGN_Hull.astype(float), axis=0))
    polygon_LT_SIGN = Polygon(convex_points(LT_SIGN_Hull))
    
    fig = plt.figure(figsize=(15,5))
    ax = fig.add_subplot(121)
    patch_FT = PolygonPatch(polygon_FT,facecolor="lime", alpha=1, zorder=2)
    patch_LT = PolygonPatch(polygon_LT,facecolor="deepskyblue", alpha=1, zorder=2)
    patch_FT_SIGN = PolygonPatch(polygon_FT_SIGN,facecolor="teal", alpha=1, zorder=2)
    patch_LT_SIGN = PolygonPatch(polygon_LT_SIGN,facecolor="blue", alpha=1, zorder=2)
    ax.add_patch(patch_FT)
    ax.add_patch(patch_LT)   
    ax.add_patch(patch_FT_SIGN)
    ax.add_patch(patch_LT_SIGN)  
#     plt.plot(fixation[0],fixation[1],'*',c='r')
    plt.xlim([0,width])
    plt.ylim([height,0])
    plt.show()
    
def draw_object_gaze(index,data,Col_FT_X,Col_FT_Y,Col_LT_X,Col_LT_Y,Col_FT_sign_X,Col_FT_sign_Y,Col_LT_sign_X,Col_LT_sign_Y,width,height):
    gaze = [data.loc[index,'Gaze point X'],data.loc[index,'Gaze point Y']]
    FT_Hull = np.concatenate((data.loc[index,Col_FT_X].values.reshape((8, 1)),data.loc[index,Col_FT_Y].values.reshape((8, 1))), axis=1)
    FT_Hull = ConvexHull(np.unique(FT_Hull.astype(float),axis=0))
    polygon_FT = Polygon(convex_points(FT_Hull))
    LT_Hull = np.concatenate((data.loc[index,Col_LT_X].values.reshape((8, 1)),data.loc[index,Col_LT_Y].values.reshape((8, 1))), axis=1)
    LT_Hull = ConvexHull(np.unique(LT_Hull.astype(float),axis=0))
    polygon_LT = Polygon(convex_points(LT_Hull))         
    FT_SIGN_Hull = np.concatenate((data.loc[index,Col_FT_sign_X].values.reshape((8, 1)),data.loc[index,Col_FT_sign_Y].values.reshape((8, 1))), axis=1)
    FT_SIGN_Hull = ConvexHull(np.unique(FT_SIGN_Hull.astype(float), axis=0))
    polygon_FT_SIGN = Polygon(convex_points(FT_SIGN_Hull))
    LT_SIGN_Hull = np.concatenate((data.loc[index,Col_LT_sign_X].values.reshape((8, 1)),data.loc[index,Col_LT_sign_Y].values.reshape((8, 1))), axis=1)
    LT_SIGN_Hull = ConvexHull(np.unique(LT_SIGN_Hull.astype(float), axis=0))
    polygon_LT_SIGN = Polygon(convex_points(LT_SIGN_Hull))
    
    fig = plt.figure(figsize=(15,5))
    ax = fig.add_subplot(121)
    patch_FT = PolygonPatch(polygon_FT,facecolor="lime", alpha=1, zorder=2)
    patch_LT = PolygonPatch(polygon_LT,facecolor="deepskyblue", alpha=1, zorder=2)
    patch_FT_SIGN = PolygonPatch(polygon_FT_SIGN,facecolor="teal", alpha=1, zorder=2)
    patch_LT_SIGN = PolygonPatch(polygon_LT_SIGN,facecolor="blue", alpha=1, zorder=2)
    ax.add_patch(patch_FT)
    ax.add_patch(patch_LT)   
    ax.add_patch(patch_FT_SIGN)
    ax.add_patch(patch_LT_SIGN)  
    plt.plot(gaze[0],gaze[1],'*',c='r')
    plt.xlim([0,width])
    plt.ylim([height,0])
    plt.show()
# def draw_object_fixation(polygon_FT,polygon_LT,polygon_FT_SIGN,polygon_LT_SIGN,fixation,width,height):
#     fig = plt.figure(figsize=(15,5))
#     ax = fig.add_subplot(121)
#     patch_FT = PolygonPatch(polygon_FT,facecolor="lime", alpha=0.5, zorder=2)
#     patch_LT = PolygonPatch(polygon_LT,facecolor="skyblue", alpha=0.5, zorder=2)
#     patch_FT_SIGN = PolygonPatch(polygon_FT_SIGN,facecolor="c", alpha=1, zorder=2)
#     patch_LT_SIGN = PolygonPatch(polygon_LT_SIGN,facecolor="blue", alpha=1, zorder=2)
#     ax.add_patch(patch_FT)
#     ax.add_patch(patch_LT)   
#     ax.add_patch(patch_FT_SIGN)
#     ax.add_patch(patch_LT_SIGN)  
#     plt.plot(fixation[0],fixation[1],'*',c='r')
#     plt.xlim([0,width])
#     plt.ylim([height,0])
#     plt.show()

