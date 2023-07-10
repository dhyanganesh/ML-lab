import math

def minimax(curdepth,targetdepth,maxturn,nodeindex,scores):
    if curdepth == targetdepth:
        return scores[nodeindex]
    if maxturn:
        return max(minimax(curdepth+1,targetdepth,False,nodeindex*2,scores),minimax(curdepth+1,targetdepth,False,nodeindex*2+1,scores))
    else:
        return min(minimax(curdepth+1,targetdepth,True,nodeindex*2,scores),minimax(curdepth+1,targetdepth,True,nodeindex*2+1,scores))
    
scores=[2,3,5,9,0,1,7,5]
curdepth=0
targetdepth=math.log(len(scores),2)
print(minimax(curdepth,targetdepth,True,0,scores))