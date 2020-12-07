# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:53:06 2020

@author: rugby
"""

from time import time
import producer
import BranchAndBoundEditDistance
import approximated_dp
import dpdnc
import dyna
import greedy
import RecursiveEditDistance
import greedy



branchTab=[]
approximatedTab=[]
dpdncTab=[]
dynaTab=[]
greedyTab=[]
recursiveTab=[]
greedyTab=[]


for (x, y, xlen,ylen) in producer.produce_protein():
    
    
    res=approximated_dp.approximated_dp(x, y).show(False, False,False)
    approximatedTab.append([xlen,ylen,res])
    
    res1=dpdnc.dpdnc(x, y).show(False, False,False)
    dpdncTab.append([xlen,ylen,res1])
    
    res2=dyna.dyna(x, y).show(False, False,False)
    dynaTab.append([xlen,ylen,res2])
    
    start_time=time()
    greedy.gEdit_d(x,y)
    end_time=time()
    res3=end_time-start_time
    greedyTab.append([xlen,ylen,res3])
    
    



branchTab1=[]
approximatedTab1=[]
dpdncTab1=[]
dynaTab1=[]
greedyTab1=[]
recursiveTab1=[]
greedyTab1=[]

for (x,y,xlen,ylen) in producer.produce_random(100, max_len_x=30):
    res=approximated_dp.approximated_dp(x, y).show(False, False,False)
    approximatedTab1.append([xlen,ylen,res])
    
    res1=dpdnc.dpdnc(x, y).show(False, False,False)
    dpdncTab1.append([xlen,ylen,res1])
    
    res2=dyna.dyna(x, y).show(False, False,False)
    dynaTab1.append([xlen,ylen,res2])
    
    maChaineOpe=""
    start_time=time()
    BranchAndBoundEditDistance.branch_and_bound(x,y,"",0,max(xlen,ylen))
    end_time=time()
    res4=end_time-start_time
    branchTab1.append([xlen,ylen,res4])
    
    
    maChaineOpe=""
    start_time=time()
    RecursiveEditDistance.RecursiveEditDistance(x,y,maChaineOpe)
    RecursiveEditDistance.RecursiveSequenceAlignment(x,y)
    end_time=time()
    res3=end_time-start_time
    recursiveTab1.append([xlen,ylen,res3])
    
    
    start_time=time()
    greedy.gEdit_d(x,y)
    end_time=time()
    res5=end_time-start_time
    greedyTab1.append([xlen,ylen,res5])
