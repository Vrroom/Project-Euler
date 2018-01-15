
def hist(a):
    hist = {}
    for k,v in a.items():
        try:
            hist[k] = hist[k]+1
        except KeyError:
            hist[k] = 0
    return hist




