#!/usr/bin/env python

import json
import umap

from joblib import Parallel, delayed

def readmatrix(j):
    with open(j, 'r') as f:
        return json.load(f)

def readmatrix_j(jsonfiles):
    if len(jsonfiles) == 0: return []
    m = readmatrix(jsonfiles[0])
    l = [ 0, len(m[0]) ]
    for i in range(1, len(jsonfiles)):
        n = readmatrix(jsonfiles[i])
        m = [ m[i] + n[i] for i in range(len(n)) ]
        l.append(l[-1] + len(n[0]))
    return m, l

def signalumap_distance(jsonfiles, d, **kwargs):
    m, _ = d(readmatrix_j(jsonfiles))
    del kwargs['metric']
    u = umap.UMAP(metric = 'precomputed', **kwargs)
    return [ [ float(xxx) for xxx in xx ] for xx in u.fit_transform(m) ]

def signalumap(jsonfiles, **kwargs):
    """
    Performs UMAP on signal matrices read from the given files; returns the coordinates of the elements in the
    reduced dimension space. Each JSON file should contain a matrix with the same number of elements, corresponding
    to the matrix rows. The vectors from each file will be concatenated prior to UMAP.

    Args:
        jsonfiles (list): list of signal matrices; must have the same number of rows, one per element.

    Returns:
        A coorinate matrix, where each row corresponds to an element mapped into the lower dimensional space.
    """
    u = umap.UMAP(**kwargs)
    return [ [ float(xxx) for xxx in xx ] for xx in u.fit_transform(readmatrix_j(jsonfiles)[0]) ]
