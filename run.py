import os
from pathlib import Path


os.system("chmod -R 0777 /model")

with open('/model/run.sh', 'w') as f:

    f.write('pip install /model/pyflow\n')
    
    videos = os.listdir("/dataset")

    for video in videos:
        f.write(f"python3 /model/eval.py --data_dir /dataset/{video} --output /results\n")

    f.write("chmod -R 0777 /results\n")

os.system("chmod -R 0777 /model")
os.system("/model/run.sh")
