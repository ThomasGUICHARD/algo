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
from pandas import read_csv


branchTab=[]
approximatedTab=[]
dpdncTab=[]
dynaTab=[]
greedyTab=[]
recursiveTab=[]


for (x, y, max_len) in producer.produce_protein():
    
    
    res=approximated_dp.approximated_dp(x, y).show(False, False,False)
    approximatedTab.append([max_len,res])
    
    res1=dpdnc.dpdnc(x, y).show(False, False,False)
    dpdncTab.append([max_len,res1])
    
    res2=dyna.dyna(x, y).show(False, False,False)
    dynaTab.append([max_len,res2])



branchTab1=[]
approximatedTab1=[]
dpdncTab1=[]
dynaTab1=[]
greedyTab1=[]
recursiveTab1=[]

for (x,y,max_len) in producer.produce_random(100, max_len_x=10):
    res=approximated_dp.approximated_dp(x, y).show(False, False,False)
    approximatedTab1.append([max_len,res])
    
    res1=dpdnc.dpdnc(x, y).show(False, False,False)
    dpdncTab1.append([max_len,res1])
    
    res2=dyna.dyna(x, y).show(False, False,False)
    dynaTab1.append([max_len,res2])
    
    maChaineOpe=""
    editDistance=0
    start_time=time()
    editDistance,chop=RecursiveEditDistance.RecursiveEditDistance(x,y,maChaineOpe)
    end_time=time()
    res3=end_time-start_time
    recursiveTab1.append([max_len,res3])
    
    
    maChaineOpe=""
    start_time=time()
    result, a1, a2, chope  = BranchAndBoundEditDistance.branch_and_bound(x,y,maChaineOpe,0,max(len(x),len(y)))
    end_time=time()
    res4=end_time-start_time
    branchTab1.append([max_len,res4])
