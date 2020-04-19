#!/usr/bin/env python3

import ujson

from .umap import signalumap

def runumap(args):
    coordinates = signalumap(
        args.json_files, n_neighbors = args.n_neighbors, min_dist = args.min_dist,
        metric = args.metric, n_components = args.n_components
    )
    with open(args.output_file, 'w') as o:
        o.write(ujson.dumps(coordinates) + '\n')
