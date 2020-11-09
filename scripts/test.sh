#!/bin/bash
set -e

docker build -t umap-test .

# cd to project root directory
cd "$(dirname "$(dirname "$0")")"
cd src
python3 -m unittest test.test_app
