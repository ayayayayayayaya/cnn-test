# -*- coding: utf-8 -*-

import glob

ls = glob.glob("./train_data/*")
a = []
for pic in ls:
    if "lion" in pic:
        a.append(pic + " 0\n")
    elif "mimizuku" in pic:
        a.append(pic + " 1\n")

with open("./train.txt", "w") as f:
    f.writelines(a)

ls = glob.glob("./test_data/*")
a = []
for pic in ls:
    if "lion" in pic:
        a.append(pic + " 0\n")
    elif "mimizuku" in pic:
        a.append(pic + " 1\n")

with open("./test.txt", "w") as f:
    f.writelines(a)
