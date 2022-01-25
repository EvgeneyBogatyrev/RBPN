import os
from pathlib import Path

os.system("rm -rf /model/result")

with open('/model/run.sh', 'w') as f:

    f.write('pip install /model/pyflow\n')
    
    videos = os.listdir("/dataset")

    for video in videos:
        f.write(f"python3 /model/eval.py --data_dir /dataset/{video} --output /results\n")

os.system("/model/run.sh")
