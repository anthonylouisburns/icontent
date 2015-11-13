#!/bin/bash

while true #run indefinitely
do
inotifywait -e modify,attrib,close_write,move,create,delete /notebooks
echo "ipython /notebooks/static/getAltered.py"
ipython /notebooks/static/getAltered.py
echo "ipython /notebooks/static/moveFiles.py"
ipython /notebooks/static/moveFiles.py
echo "finished inotifyUpdate.sh loop"
sleep 1
done

