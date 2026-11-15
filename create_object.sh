#!/bin/bash
git init
git add .
git commit -m "hello world"
python create_object.py $1
