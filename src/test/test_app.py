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
        with tempfile.TemporaryDirectory() as dd:
            os.system(
                "docker run --volume %s:/data --volume %s:/output umap-test python3 -m app --json-files /data/test.1.json /data/test.2.json --output-file /output/test --n-neighbors 3" % (
                    os.path.join(os.path.dirname(os.path.realpath(__file__)), "resources"), dd
                )
            )
            with open(os.path.join(dd, "test"), 'r') as f:
                j = ujson.load(f)
            self.assertLess(d(j[0], j[1]), d(j[0], j[4]))
            self.assertLess(d(j[0], j[2]), d(j[0], j[5]))
            self.assertLess(d(j[5], j[6]), d(j[0], j[3]))

    def test_umap_3(self):
        with tempfile.TemporaryDirectory() as dd:
            os.system(
                "docker run --volume %s:/data --volume %s:/output umap-test python3 -m app --json-files /data/test.1.json /data/test.2.json --output-file /output/test --n-neighbors 3 --n-components 3" % (
                    os.path.join(os.path.dirname(os.path.realpath(__file__)), "resources"), dd
                )
            )
            with open(os.path.join(dd, "test"), 'r') as f:
                j = ujson.load(f)
            self.assertLess(d(j[0], j[1]), d(j[0], j[4]))
            self.assertLess(d(j[0], j[2]), d(j[0], j[5]))
            self.assertLess(d(j[5], j[6]), d(j[0], j[3]))

    def test_umap_cos(self):
        with tempfile.TemporaryDirectory() as dd:
            os.system(
                "docker run --volume %s:/data --volume %s:/output umap-test python3 -m app --json-files /data/test.1.json /data/test.2.json --output-file /output/test --n-neighbors 3 --n-components 3 --cosine-similarity" % (
                    os.path.join(os.path.dirname(os.path.realpath(__file__)), "resources"), dd
                )
            )
            with open(os.path.join(dd, "test"), 'r') as f:
                j = ujson.load(f)
            self.assertLess(d(j[0], j[1]), d(j[0], j[6]))
            self.assertLess(d(j[0], j[2]), d(j[0], j[5]))
            self.assertLess(d(j[5], j[6]), d(j[0], j[3]))
