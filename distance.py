import math

def distance(x1, y1, x2, y2):
    distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    #distance = math.sqrt(math.pow(y1 - x1, 2) + math.pow(y2 - x2, 2))
    return distance