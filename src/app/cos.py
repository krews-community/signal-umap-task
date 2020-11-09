#!/usr/bin/env python

import sys
import numpy
import sklearn.metrics.pairwise

def cosine_similarity(v):
    m, l = v
    m = [ [ x[l[i]:l[i + 1]] for i in range(len(l) - 1) ] for x in m ]
    padded = [ [ [ 0 for _ in range(len(x)) ] + x + [ 0 for _ in range(len(x)) ] for x in xx ] for xx in m ]
    distances = [ [ 0 for _ in range(len(m)) ] for _ in range(len(m)) ]
    indexes = [ [ 0 for _ in range(len(m))] for _ in range(len(m)) ]
    for i in range(len(m)):
        if i % 1000 == 0: print("processing %d of %d" % (i, len(m)), file = sys.stderr)
        for j in range(i + 1, len(m)):
            cmin = -float('inf')
            cidx = 0
            rr = [ sklearn.metrics.pairwise.cosine_similarity(
                [ padded[i][o][k : k + len(m[j][o])] for k in range(len(padded[i][o]) - len(m[0][o])) ],
                [ m[j][o] ]
            ) for o in range(len(padded[i])) ]
            for ii in range(len(rr[0])):
                rx = sum([ rr[xx][ii] for xx in range(len(rr)) ]) / float(len(rr))
                if rx > cmin:
                    cmin = rx
                    cidx = ii
            distances[i][j] = distances[j][i] = 1.0 - (cmin + 1.0) / 2.0
            indexes[i][j] = indexes[j][i] = cidx
    return distances, indexes
