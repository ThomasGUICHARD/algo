
import string
from time import time


def branch_and_bound(machaineRef,machaineModifable,machaineOpe,cost=0,bound=0):

    lcR=len(machaineRef)
    lcM=len(machaineModifable)

# case: the two string entries are null
    if lcR==0 and lcM==0:
        return 0, [], [], machaineOpe
# case: machaineRef is null
    if lcR == 0:
        return lcM, ["_" for i in range(lcM)], [machaineModifable[i] for i in range(lcM)], machaineOpe
   
# case: machaineModifiable is null    
    if lcM == 0:
        return lcR, [machaineRef[i] for i in range(lcR)], ["_" for i in range(lcR)], machaineOpe
   
 
    #Cost of the node
    weight1 = abs((lcR-1)-lcM)
    weight2 = abs(lcR-(lcM-1))
    weight3 = weight1+cost
    weight4 = weight2+cost
    
    #we check the cost of the nod
    weightw = abs((lcR-1)-(lcM-1))
    #we check the two last letters of both strings
    if machaineRef[-1] == machaineModifable[-1]:
        weightm = weightw + cost - 1
    else:
        weightm = weightw + cost
    ad1, ad2, ai1, ai2, ar1, ar2 = [], [], [], [], [], []
    mcod,mcoi,mcosub= [], [], []

    # branch deletion
    if bound >= weight3:
        delet,ad1,ad2,mcod  = branch_and_bound(machaineRef[:-1], machaineModifable,machaineOpe, cost + 1, bound)
        delet += 1
    else:
        delet = 1000000
    
    # branch insertion
    if bound >= weight4:
        insert,ai1,ai2,mcoi = branch_and_bound(machaineRef, machaineModifable[:-1],machaineOpe, cost + 1, bound) 
        insert += 1
    else:
        insert = 1000000

    #branch substitution
    # if the letter is the same we replace
    # else we just continue
    if bound >= weightw:
        if (machaineRef[-1] != machaineModifable[-1]):
            subst,ar1,ar2,mcosub = branch_and_bound(machaineRef[:-1], machaineModifable[:-1],machaineOpe, cost + 1, bound)
            subst += 1
        else:
            subst,ar1,ar2,mcosub = branch_and_bound(machaineRef[:-1], machaineModifable[:-1],machaineOpe, cost, bound)
    else:
        subst = 1000000

    
     #store the value of deletion, insertion and substitution
    values = [delet, insert, subst]
    minval = min(delet, insert, subst)
    if values.index(minval) == 0: 
        mcod = mcod + "delet("+machaineRef[-1]+")\n"
        ad1 = ad1 + [machaineRef[-1]]
        ad2 = ad2 + ["_"]
       
        return minval, ad1, ad2, mcod
    elif values.index(minval) == 1:
        mcoi = mcoi +"insert("+machaineModifable[-1]+")\n"
        ai1 = ai1 + ["_"]
        ai2 = ai2 +[machaineModifable[-1]]
        
        return minval, ai1, ai2, mcoi
    else:
        ar1 = ar1 + [machaineRef[-1]]
        ar2 = ar2 + [machaineModifable[-1]]
        mcosub = mcosub +"replace("+machaineRef[-1]+","+machaineModifable[-1]+")\n"
        return minval, ar1, ar2, mcosub




machaineRef="testttttt"
machaineModifable="monnn"
maChaineOpe=""




print("Branch and bound for edit distance")
print('=========================================')
start_time=time()
result, a1, a2, chope  = branch_and_bound(machaineRef,machaineModifable,maChaineOpe,0,max(len(machaineRef),len(machaineModifable)))
print('\n*******ALIGNMENT*********')
print(a1,'\n',a2)
print('\nThe edit distance is: ',result)
end_time=time()
print('The time taken to compute the edit distance is : %3f seconds'%(end_time-start_time))
print("\nOperations:")
print(chope)
print('*****************')
print('END OF PROGRAM')
print('*****************')