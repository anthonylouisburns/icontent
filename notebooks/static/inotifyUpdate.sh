#!/bin/bash

while true #run indefinitely
do
inotifywait -e modify,attrib,close_write,move,create,delete /notebooks
echo "run"
ipython /notebooks/static/getAltered.py
echo "move"
ipython /notebooks/static/moveFiles.py
sleep 1
done

