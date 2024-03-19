'''This program is executed within the Google Cloud VM Instance.
'''
import os
import sys
import bpy
import random
import csv
from baseline_data import config

sourcepath = sys.argv[5]
blendpath = sourcepath + "/blend/"
scenepath = sourcepath + "/models/scenes/"
outpath = sys.argv[6]
dataset = sys.argv[7]
startframe = 1
endframe = sys.argv[9]
scenario_number = sys.argv[10]
camera_number = sys.argv[11]
device = sys.argv[12]


def main():
    config.load_blend_file(dataset, blendpath)
    config.render_scene(outpath, startframe, endframe, dataset)


if __name__ == "__main__":
    main()