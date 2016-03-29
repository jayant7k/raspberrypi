for pid in $(ps -ef | awk '/weatherk.py/ {print $2}'); do kill -9 $pid; done
