import math

MAX, MIN = 1000, -1000

def minimax(curdepth,targetdepth,maxturn,nodeIndex, alpha, beta,scores):
    if curdepth == targetdepth:
        return scores[nodeIndex]

    if maxturn:
        best = MIN
        for i in range(0, 2):
            val = minimax(curdepth + 1,targetdepth,False,nodeIndex * 2 + i,alpha, beta,scores)
            best = max(best, val)
            alpha = max(alpha, best)
            print(f"alpha = {alpha} beta = {beta}")
            if beta <= alpha:
                print("rest pruned")
                break
        return best

    else:
        best = MAX
        for i in range(0, 2):
            val = minimax(curdepth + 1,targetdepth,True,nodeIndex * 2 + i,alpha, beta,scores)
            best = min(best, val)
            beta = min(beta, best)
            print(f"alpha = {alpha} beta = {beta}")
            if beta <= alpha:
                print("rest pruned")
                break
        return best


scores = [1,8,3,9,4,7,2,5]
print("The optimal value is :", minimax(0,math.log(len(scores),2),True,0,MIN,MAX,scores))