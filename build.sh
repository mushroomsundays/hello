#!/usr/bin/bash
python setup.py sdist bdist_wheel
pip install dist/*.gz