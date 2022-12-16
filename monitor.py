#!/home/xaco/programs/miniconda3/envs/tesi/bin/python
import os
import os.path as osp
import time
import datetime

print("Job started at: ", datetime.datetime.now())
cwd = os.getcwd()
targlen = len(os.listdir(osp.join(cwd, "raw")))//2
oldlen = nowlen = len(os.listdir(osp.join(cwd, "processed"))) - 2
while nowlen < targlen:
    try:
        print(f"{nowlen}/{targlen} ({float(nowlen)/targlen:.2%}) {nowlen - oldlen} it/min \t {datetime.datetime.now()}", end="\r")
        time.sleep(60)
        oldlen = nowlen
        nowlen = len(os.listdir(osp.join(cwd, "processed"))) - 2
    except KeyboardInterrupt:
        print()
        print("User ended loop!")
        break
print("Done!")
