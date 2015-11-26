#!/bin/bash

VER=`python -c 'import sys; print("".join(map(str, sys.version_info[0:2])))';`
VER27="27"
if [[ $VER != "35" ]]; then
    pylint --disable=missing-docstring,invalid-name,fixme ./groups/*.py
fi

if [[ $VER != "36" ]]; then
    flake8 .
fi
