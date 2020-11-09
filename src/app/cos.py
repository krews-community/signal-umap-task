#!/usr/bin/env python

import sys
import numpy
import sklearn.metrics.pairwise

def cosine_similarity(m):
    padded = [ [ 0 for _ in range(len(x)) ] + x + [ 0 for _ in range(len(x)) ] for x in m ]
    m = [ x for x in m ]
    distances = [ [ 0 for _ in range(len(m)) ] for _ in range(len(m)) ]
    indexes = [ [ 0 for _ in range(len(m))] for _ in range(len(m)) ]
    for i in range(len(m)):
        if i % 1000 == 0: print("processing %d of %d" % (i, len(m)), file = sys.stderr)
        for j in range(i + 1, len(m)):
            cmin = -float('inf')
            cidx = 0
            rr = sklearn.metrics.pairwise.cosine_similarity(
                [ padded[i][k : k + len(m[j])] for k in range(len(padded[i]) - len(m[0])) ],
                [ m[j] ]
            )
            for ii, r in enumerate(rr):
                if r[0] > cmin:
                    cmin = r[0]
                    cidx = ii
            distances[i][j] = distances[j][i] = 1.0 - (cmin + 1.0) / 2.0
            indexes[i][j] = indexes[j][i] = cidx
    return distances, indexes
