#!/bin/bash
set -e

python3 -m pip install --user ujson umap-learn

# cd to project root directory
cd "$(dirname "$(dirname "$0")")"
cd src
python3 -m unittest test.test_app
