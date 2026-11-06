#!/bin/sh
set -e
cd "$(dirname "$0")"
python3 build_data.py > /dev/null
python3 postprocess.py
