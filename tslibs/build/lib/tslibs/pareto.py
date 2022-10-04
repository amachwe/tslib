def max_max(id, x,y):
    return pareto(id, x,y,lambda a,b: a>b,lambda a,b: a>b)

def min_max(id, x,y):
    return pareto(id, x,y,lambda a,b: a<b,lambda a,b: a>b)

def max_min(id, x,y):
    return pareto(id, x,y, lambda a,b: a>b, lambda a,b: a<b)

def min_min(id, x,y):
    return pareto(id, x,y, lambda a,b: a<b, lambda a,b: a<b)

def pareto(_id, x,y, cmpx,cmpy):
    lx = len(x)
    if lx != len(y):
        print("X and Y not of same length.")
        return []
    pareto = []
    id_sol = []

    for i in range(0,lx):
 
        dom = 0
        idx = []
  
        for id, pp in enumerate(pareto):
            
            if cmpx(pp[0],x[i]) and cmpy(pp[1],y[i]):
                dom = 1
        
            if cmpx(x[i], pp[0]) and cmpy(y[i],pp[1]): 
                idx.append(id)

        for c, id in enumerate(idx):
            pareto.pop(id-c)
            id_sol.pop(id-c)
        if dom==0:
            pareto.append((x[i],y[i]))
            id_sol.append(_id[i])
        
    return pareto, id_sol