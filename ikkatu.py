# -*- coding: utf-8 -*-

from iota import *
from image_lib import *
from iota_lib import Iota_lib
from transaction_lib import tx_lib
import glob
import random
import sys


def iota_init():
    iota_obj = Iota_lib("http://163.225.223.50:14265", "EDCEMKUNKEBDQIFBTAXV9TL9IWXGVURHVHDNCOKVBZNUNSGLCWTERZHYNFOGKYFHXTFL9OJTCIWVGEOX")
    return iota_obj

def prepare_upload(pic_list, pic_index, iota_obj):
    tx = prepare_transaction(pic_list[pic_index], iota_obj)
    approve, index = prepare_bundle(iota_obj)
    next(approve, tx, index, iota_obj, pic_index, pic_list)

def prepare_transaction(pic, iota_obj):
    tryte = to_tryte_from_picture(pic[0])
    trytes = []
    for i in range(math.ceil(len(tryte) / 2187)):
        trytes.append(TryteString.from_string("{0:03d}_".format(i)) + tryte[0 + i * 2179 : 2179 + i * 2179])

    iota_obj.node_info()
    address = iota_obj.new_address(random.randint(0,100), len(trytes))
    if(iota_obj.check_index()):
        tx = iota_obj.set_transaction(address["addresses"], trytes, [TryteString.from_string(pic[1]) for _ in range(len(trytes))])
        iota_obj.bundle_init()
        return tx

def prepare_bundle(iota_obj):
    index = 0
    approve_image = iota_obj.get_bundle()
    return approve_image, index

def next(approve, tx, index, iota_obj, pic_index, pic_list):
    tx[index].trunk_transaction_hash = approve["approve_hash"]["trunkTransaction"]
    tx[index].branch_transaction_hash = approve["approve_hash"]["branchTransaction"]
    iota_obj.add_tx(tx[index])
    index += 1
    if index < len(tx):
        approve = iota_obj.get_bundle()
        next(approve, tx, index, iota_obj, pic_index, pic_list)
    else:
        iota_obj.send_tx(tx)
        print(pic_list[pic_index])
        pic_index += 1
        if pic_index < len(pic_list):
            prepare_upload(pic_list, pic_index, iota_obj)
        else:
            sys.exit()
def main():
    lion = glob.glob("./scraping/lion/lion*.jpeg")
    mimizuku = glob.glob("./scraping/mimizuku/mimizuku*.jpeg")
    pic_list = []
    iota_obj = iota_init()
    pic_index = 0
    tag = "lion"
    for pic in lion:
        pic_list.append([pic,tag])
    tag = "mimizuku"
    for pic in mimizuku:
        pic_list.append([pic,tag])
    prepare_upload(pic_list, pic_index, iota_obj)

if __name__ == "__main__":
    main()
