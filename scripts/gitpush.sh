#!/bin/bash

LINK="https://github.com/vishnumur777/Dsacodingninjas"

cd ..

git add .

git commit -m "Added .py in $(pwd)"

git remote -v add orgin $LINK 

git push orgin master
