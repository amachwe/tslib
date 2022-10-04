import numpy as np

def mape(ya,yp):
    
    return np.mean(np.abs((ya-yp)/ya)*100)

def mrse(ya,yp):
    d = (ya-yp)
    return np.sqrt(np.sum(d*d))

def mae(ya, yp):

    return np.mean(np.abs(ya-yp))