#!/usr/bin/env python3

import sys
import argparse

from .app import runumap

def main():
    
    parser = argparse.ArgumentParser(description = "Performs UMAP on matrices containing signal around a set of peaks.")
    parser.add_argument("--json-files", nargs = '+', type = str, help = "Path to the JSON files containing the matrices.", required = True)
    parser.add_argument("--output-file", type = str, help = "Path to write the output coordinates, in JSON format.", required = True)
    parser.add_argument("--n-neighbors", type = int, help = "UMAP hyperparameter: number of neighbors for each point. Default 15.", default = 15)
    parser.add_argument("--min-dist", type = float, help = "UMAP hyperparameter: minimum distance between points. Default 0.1.", default = 0.1)
    parser.add_argument("--metric", type = str, help = "Distance metric for UMAP to use; defaults to 'correlation'.", default = "correlation")
    parser.add_argument("--n-components", type = int, help = "Number of dimensions in the UMAP space; defaults to 2.", default = 2)

    runumap(parser.parse_args())
    return 0

if __name__ == "__main__":
    sys.exit(main())
