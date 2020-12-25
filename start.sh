kill -9 $(lsof -t -i:60016)
python3 /home/pi/roaster-control/main.py
