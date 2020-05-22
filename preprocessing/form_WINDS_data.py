import glob
import csv
import os
import copy
import pickle
import pandas as pd
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import matplotlib.pyplot as plt
import numpy as np
import argparse


parser = argparse.ArgumentParser(description='WINDS dataset processor')
parser.add_argument('--dataset_folder_path', type=str, required=True)
parser.add_argument('--out_file', type=str, required=True)
args = parser.parse_args()

def read_folder(folder_path):
    os.chdir(folder_path)

    results = {}
    names = {}
    for file in reversed(sorted(glob.glob("*"))):
        if not file.endswith(".csv"):
            continue
        dataframe = pd.read_csv(file, skiprows=4, header=None)
        dataframe.columns = ['Year', 'Month', 'Day', 'Hour', 'Minute', 'Wind']
        with open(file, 'r') as content_file:
            content = content_file.read().split("\n")

            long, lat = float(content[1].split(',')[1]), float(content[2].split(',')[1])
        names[(long, lat)] = file
        results[(long, lat)] = dataframe
    return results, names


def save_data(folder_path, out_file):
    df_dict, names = read_folder(folder_path)

    pickle.dump([df_dict, names],open(out_file,"wb"))
	
save_data(args.dataset_folder_path, args.out_file)
