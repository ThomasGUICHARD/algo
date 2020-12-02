
import string
from time import time
matchscore   = 2
mismatchscore = 1   

def RecursiveEditDistance(machaineRef, machaineModifable,maChaineOpe):
    """Recursively calculate the edit distance between two strings, a and b.
    Returns the edit distance."""
    lcR=len(machaineRef)
    lcM=len(machaineModifable)

    if lcR==0:
        return lcM ,[] 
    if lcM==0:
        return lcR ,[]
    # Testing if the last characters of eah string are the same.
    # It's determine if there is no operations during this step.
    if(machaineRef[-1]== machaineModifable[-1]):
        mcon=[]
        costn=0
        costn,mcon=RecursiveEditDistance(machaineRef[:-1],machaineModifable[:-1],maChaineOpe)
        return costn, mcon +["no operation"]
  
    
    costd,costi,costr=0,0,0
    mcod,mcoi,mcor=[],[],[]
    costd, mcod=RecursiveEditDistance(machaineRef, machaineModifable[:-1],maChaineOpe)
    costd+=1
    costi, mcoi=RecursiveEditDistance(machaineRef[:-1], machaineModifable,maChaineOpe)
    costi+=1
    costr, mcor=RecursiveEditDistance(machaineRef[:-1],machaineModifable[:-1],maChaineOpe)
    costr+=1

    if costd == min(costd,costi,costr):
        mcod=mcod+["delet()"]
        return costd, mcod
    if costi == min(costd,costi,costr):
        mcoi=mcoi+["insert()"]
        return costi, mcoi
    if costr == min(costd,costi,costr):
        mcor= mcor + ["replace()"]
        return costr, mcor 





Insertionoperator='-'
def RecursiveSequenceAlignment (machaineRef, machaineModifable):
    
    #case where one of the two chains is null
    if len(machaineRef) == 0 or len(machaineModifable) == 0:
        while len(machaineRef) < len(machaineModifable):
            machaineRef = machaineRef + Insertionoperator
        while len(machaineModifable) < len(machaineRef):
            machaineModifable = machaineModifable + Insertionoperator
        return machaineRef, machaineModifable
    
    else:
        # no gap
        (machaineRef0, machaineModifable0) = RecursiveSequenceAlignment(machaineRef[1:], machaineModifable[1:])
        scoreWithoutGap = scoreFunction(machaineRef0, machaineModifable0,matchscore,mismatchscore)

        if machaineRef[0] == machaineModifable[0]: scoreWithoutGap += matchscore
        # Gap at machaineRef without the first character of machaineModifable
        (machaineRef1, machaineModifable1) = RecursiveSequenceAlignment(machaineRef, machaineModifable[1:])
        scoreGapmachaineRef = scoreFunction(machaineRef1, machaineModifable1,matchscore,mismatchscore) - mismatchscore
        
        # Gap at machaineModifable without the first character of machaineRef 
        (machaineRef2, machaineModifable2) = RecursiveSequenceAlignment (machaineRef[1:], machaineModifable)
        scoreGapmachaineModifable = scoreFunction(machaineRef2, machaineModifable2,matchscore,mismatchscore) - mismatchscore
        
        if scoreWithoutGap >= scoreGapmachaineRef and scoreWithoutGap >= scoreGapmachaineModifable:
            return machaineRef[0] + machaineRef0, machaineModifable[0] + machaineModifable0
        elif scoreGapmachaineRef >= scoreGapmachaineModifable:
            return Insertionoperator + machaineRef1, machaineModifable[0] + machaineModifable1
        else:
            return machaineRef[0] + machaineRef2, Insertionoperator + machaineModifable2


    
def scoreFunction(machaineRef,machaineModifable,matchscore,mismatchscore):
    score =0
    for i in range(len(machaineRef)):
        if(machaineRef[i] == machaineModifable[i]):
            score += matchscore
        else:
            score -= mismatchscore
    return score

machaineRef="testffffffffffffffffffffffffffffffffffffffffffffffff"
machaineModifable="mon"
maChaineOpe=""
editDistance=0
start_time=time()
editDistance,chop=RecursiveEditDistance(machaineRef,machaineModifable,maChaineOpe)
print(editDistance)
print(RecursiveSequenceAlignment(machaineRef,machaineModifable))
end_time=time()
print('The time taken to compute the edit distance is : %3f seconds'%(end_time-start_time))
print(chop)