filter_output = lambda x, y: dict([ (i,x[i]) for i in x if i in set(y) ])
