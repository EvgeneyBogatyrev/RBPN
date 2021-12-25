pip install /model/pyflow
python3 /model/eval.py --data_dir /dataset/gauss --output /model/result
python3 /model/eval.py --data_dir /dataset/bicubic --output /model/result
chmod -R 0777 /model
