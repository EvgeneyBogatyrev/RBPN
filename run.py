import os
from pathlib import Path


os.system("chmod -R 0777 /model")

with open('/model/run.sh', 'w') as f:

    f.write('pip install /model/pyflow\n')
    
    Path('/model/result').mkdir(parents=True, exist_ok=True)
    
    videos = os.listdir("/dataset")

    for video in videos:
        f.write(f"python3 /model/eval.py --data_dir /dataset/{video} --output /model/result\n")

    f.write("chmod -R 0777 /model\n")

os.system("chmod -R 0777 /model")
os.system("/model/run.sh")
