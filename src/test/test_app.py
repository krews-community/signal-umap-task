#!/usr/bin/env python3

import os
import tempfile
import unittest
import math
import ujson

from app.app import runumap

def d(a, b):
    return math.sqrt(sum([ (a[i] - b[i]) * (a[i] - b[i]) for i in range(len(a)) ]))

class TestInput:
    
    def __init__(self, jsonfiles, n_components = 2, n_neighbors = 3, cosine_similarity = False):
        self.json_files = [ os.path.join(os.path.dirname(__file__), "resources", x) for x in jsonfiles ]
        self.n_components = n_components
        self.n_neighbors = n_neighbors
        self.min_dist = 0.1
        self.metric = 'correlation'
        self.cosine_similarity = cosine_similarity

    def __enter__(self):
        self.output = tempfile.NamedTemporaryFile()
        self.output_file = self.output.name
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            raise
        self.output.close()

class TestApp(unittest.TestCase):
        
    def test_umap(self):
        with TestInput([ "test.1.json", "test.2.json" ]) as test:
            runumap(test)
            j = ujson.load(test.output)
            self.assertLess(d(j[0], j[1]), d(j[0], j[4]))
            self.assertLess(d(j[0], j[2]), d(j[0], j[5]))
            self.assertLess(d(j[5], j[6]), d(j[0], j[3]))

    def test_umap_3(self):
        with TestInput([ "test.1.json", "test.2.json" ], n_components = 3) as test:
            runumap(test)
            j = ujson.load(test.output)
            self.assertLess(d(j[0], j[1]), d(j[0], j[4]))
            self.assertLess(d(j[0], j[2]), d(j[0], j[5]))
            self.assertLess(d(j[5], j[6]), d(j[0], j[3]))

    def test_umap_cos(self):
        with TestInput([ "test.1.json" ], n_components = 3, cosine_similarity = True) as test:
            runumap(test)
            j = ujson.load(test.output)
            self.assertLess(d(j[0], j[1]), d(j[0], j[6]))
            self.assertLess(d(j[0], j[2]), d(j[0], j[5]))
            self.assertLess(d(j[5], j[6]), d(j[0], j[3]))
