# -*- coding: utf-8 -*-

import os
import glob

ls = glob.glob("/home/moriya/M2/cnn_test/test/*")

for dir in ls:
    count = 0
    if os.path.isdir(dir):
        name = os.path.basename(dir)
        fl = glob.glob(dir + "/*")
        for pic in fl:
            n, ext = os.path.splitext(pic)
            os.rename(pic, name + str(count) + ext)
            count += 1
